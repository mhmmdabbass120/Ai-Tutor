"""
Advanced Text Processing Engine
Handles summarization, paraphrasing, code explanation, and intelligent text analysis
"""

import streamlit as st
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Any, Optional
import re
import json
from datetime import datetime
from collections import Counter
import random

try:
    from textblob import TextBlob
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.tag import pos_tag
    from nltk.chunk import ne_chunk
    from nltk.stem import WordNetLemmatizer
except ImportError:
    st.warning("NLTK not fully available. Some text processing features may be limited.")

class AdvancedTextProcessor:
    """Advanced text processing with summarization, paraphrasing, and analysis"""
    
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer() if 'WordNetLemmatizer' in globals() else None
        self.stop_words = set(stopwords.words('english')) if 'stopwords' in globals() else set()
        
        # Programming language patterns
        self.code_patterns = {
            'python': [r'def\s+\w+', r'import\s+\w+', r'class\s+\w+', r'print\s*\(', r'if\s+__name__'],
            'java': [r'public\s+class', r'public\s+static\s+void\s+main', r'System\.out\.print', r'import\s+java'],
            'javascript': [r'function\s+\w+', r'var\s+\w+', r'let\s+\w+', r'const\s+\w+', r'console\.log'],
            'c++': [r'#include\s*<', r'int\s+main\s*\(', r'std::', r'cout\s*<<', r'using\s+namespace'],
            'html': [r'<html>', r'<div', r'<p>', r'<script>', r'</\w+>'],
            'css': [r'\w+\s*:\s*\w+;', r'\.\w+\s*{', r'#\w+\s*{', r'@media'],
            'sql': [r'SELECT\s+', r'FROM\s+\w+', r'WHERE\s+', r'INSERT\s+INTO', r'CREATE\s+TABLE']
        }
        
        # Subject-specific keywords
        self.subject_keywords = {
            'mathematics': ['equation', 'formula', 'theorem', 'proof', 'calculate', 'solve', 'derivative', 'integral', 'matrix', 'algebra'],
            'physics': ['force', 'energy', 'momentum', 'quantum', 'relativity', 'particle', 'wave', 'field', 'mass', 'velocity'],
            'chemistry': ['molecule', 'atom', 'reaction', 'compound', 'element', 'bond', 'catalyst', 'oxidation', 'ph', 'molar'],
            'biology': ['cell', 'dna', 'protein', 'organism', 'species', 'evolution', 'gene', 'enzyme', 'membrane', 'tissue'],
            'computer_science': ['algorithm', 'data structure', 'complexity', 'programming', 'software', 'database', 'network', 'security']
        }
    
    def detect_content_type(self, text: str) -> str:
        """Detect if text is code, academic content, or general text"""
        # Check for code patterns
        for language, patterns in self.code_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    return f"code_{language}"
        
        # Check for academic subjects
        text_lower = text.lower()
        subject_scores = {}
        
        for subject, keywords in self.subject_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            if score > 0:
                subject_scores[subject] = score
        
        if subject_scores:
            top_subject = max(subject_scores, key=subject_scores.get)
            return f"academic_{top_subject}"
        
        return "general"
    
    def extract_key_concepts(self, text: str) -> List[str]:
        """Extract key concepts and main ideas from text"""
        try:
            blob = TextBlob(text)
            
            # Get words and filter
            words = [word.lower() for word in blob.words if len(word) > 3]
            
            # Remove stop words
            meaningful_words = [word for word in words if word not in self.stop_words]
            
            # Get word frequency
            word_freq = Counter(meaningful_words)
            
            # Get top concepts
            key_concepts = [word for word, freq in word_freq.most_common(10)]
            
            # Add noun phrases
            noun_phrases = [str(phrase).lower() for phrase in blob.noun_phrases if len(phrase) > 3]
            key_concepts.extend(noun_phrases[:5])
            
            return list(set(key_concepts))[:15]
            
        except Exception as e:
            # Fallback: simple word frequency
            words = re.findall(r'\b\w{4,}\b', text.lower())
            word_freq = Counter(words)
            return [word for word, freq in word_freq.most_common(10)]
    
    def summarize_text(self, text: str, summary_type: str = "extractive", length: str = "medium") -> Dict[str, Any]:
        """Advanced text summarization with multiple approaches"""
        
        if len(text.strip()) < 50:
            return {"error": "Text too short to summarize effectively"}
        
        content_type = self.detect_content_type(text)
        key_concepts = self.extract_key_concepts(text)
        
        # Determine summary length
        length_ratios = {"short": 0.2, "medium": 0.4, "long": 0.6}
        target_ratio = length_ratios.get(length, 0.4)
        
        result = {
            "original_length": len(text),
            "content_type": content_type,
            "key_concepts": key_concepts,
            "summaries": {},
            "analysis": {}
        }
        
        # Generate different types of summaries
        if summary_type in ["extractive", "all"]:
            result["summaries"]["extractive"] = self._extractive_summary(text, target_ratio)
        
        if summary_type in ["abstractive", "all"]:
            result["summaries"]["abstractive"] = self._abstractive_summary(text, key_concepts)
        
        if summary_type in ["bullet_points", "all"]:
            result["summaries"]["bullet_points"] = self._bullet_point_summary(text, key_concepts)
        
        # Add specialized summaries based on content type
        if content_type.startswith("code_"):
            result["summaries"]["code_explanation"] = self._explain_code(text, content_type)
        elif content_type.startswith("academic_"):
            result["summaries"]["academic_summary"] = self._academic_summary(text, content_type)
        
        # Text analysis
        result["analysis"] = self._analyze_text_structure(text)
        
        return result
    
    def _extractive_summary(self, text: str, ratio: float) -> str:
        """Extract the most important sentences"""
        try:
            sentences = sent_tokenize(text)
            if len(sentences) <= 2:
                return text
            
            # Score sentences based on key word frequency
            sentence_scores = {}
            word_freq = Counter(re.findall(r'\b\w+\b', text.lower()))
            
            for sentence in sentences:
                words = re.findall(r'\b\w+\b', sentence.lower())
                score = sum(word_freq.get(word, 0) for word in words if word not in self.stop_words)
                sentence_scores[sentence] = score / max(len(words), 1)
            
            # Select top sentences
            num_sentences = max(1, int(len(sentences) * ratio))
            top_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]
            
            # Maintain original order
            summary_sentences = []
            for sentence in sentences:
                if any(sentence == sent[0] for sent in top_sentences):
                    summary_sentences.append(sentence)
            
            return " ".join(summary_sentences)
            
        except Exception:
            # Fallback: return first few sentences
            sentences = text.split('. ')
            num_sentences = max(1, int(len(sentences) * ratio))
            return '. '.join(sentences[:num_sentences]) + '.'
    
    def _abstractive_summary(self, text: str, key_concepts: List[str]) -> str:
        """Generate an abstractive summary using key concepts"""
        
        # Analyze text structure
        sentences = sent_tokenize(text) if 'sent_tokenize' in globals() else text.split('.')
        
        # Create concept-based summary
        summary_parts = []
        
        # Introduction
        if key_concepts:
            main_topics = ', '.join(key_concepts[:3])
            summary_parts.append(f"This text discusses {main_topics}")
        
        # Main content analysis
        if len(sentences) > 3:
            # Find sentences with most key concepts
            concept_sentences = []
            for sentence in sentences[:5]:  # Check first 5 sentences
                concept_count = sum(1 for concept in key_concepts if concept.lower() in sentence.lower())
                if concept_count > 0:
                    concept_sentences.append((sentence, concept_count))
            
            if concept_sentences:
                # Get the sentence with most concepts
                best_sentence = max(concept_sentences, key=lambda x: x[1])[0]
                summary_parts.append(f"Key insight: {best_sentence.strip()}")
        
        # Conclusion based on concepts
        if len(key_concepts) > 3:
            other_concepts = ', '.join(key_concepts[3:6])
            summary_parts.append(f"The text also covers {other_concepts}")
        
        return ". ".join(summary_parts) + "."
    
    def _bullet_point_summary(self, text: str, key_concepts: List[str]) -> List[str]:
        """Create bullet point summary"""
        
        sentences = sent_tokenize(text) if 'sent_tokenize' in globals() else text.split('.')
        bullet_points = []
        
        # Group concepts by importance
        high_priority_concepts = key_concepts[:5]
        
        for concept in high_priority_concepts:
            # Find sentences related to this concept
            related_sentences = [s for s in sentences if concept.lower() in s.lower()]
            if related_sentences:
                # Take the first relevant sentence and simplify
                sentence = related_sentences[0].strip()
                if len(sentence) > 100:
                    sentence = sentence[:97] + "..."
                bullet_points.append(f"• {concept.title()}: {sentence}")
        
        # Add general bullet points if we don't have enough
        while len(bullet_points) < 3 and len(sentences) > len(bullet_points):
            sentence = sentences[len(bullet_points)].strip()
            if len(sentence) > 20:
                if len(sentence) > 80:
                    sentence = sentence[:77] + "..."
                bullet_points.append(f"• {sentence}")
        
        return bullet_points[:5]  # Max 5 bullet points
    
    def _explain_code(self, code: str, content_type: str) -> str:
        """Explain code functionality"""
        
        language = content_type.split('_')[1] if '_' in content_type else 'unknown'
        
        explanation = [f"**{language.title()} Code Explanation:**\n"]
        
        lines = code.split('\n')
        
        # Analyze code structure
        functions = re.findall(r'def\s+(\w+)|function\s+(\w+)|public\s+\w+\s+(\w+)\s*\(', code)
        classes = re.findall(r'class\s+(\w+)', code)
        imports = re.findall(r'import\s+(\w+)|#include\s*<(\w+)>', code)
        
        if imports:
            explanation.append(f"**Imports/Includes:** {', '.join([imp for group in imports for imp in group if imp])}")
        
        if classes:
            explanation.append(f"**Classes defined:** {', '.join([cls for cls in classes])}")
        
        if functions:
            explanation.append(f"**Functions defined:** {', '.join([func for group in functions for func in group if func])}")
        
        # Add line-by-line explanation for short code
        if len(lines) <= 10:
            explanation.append("\n**Line-by-line breakdown:**")
            for i, line in enumerate(lines, 1):
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('//'):
                    explanation.append(f"Line {i}: {line}")
                    explanation.append(f"  → {self._explain_code_line(line, language)}")
        
        # Overall purpose
        explanation.append(f"\n**Overall Purpose:** This {language} code appears to implement functionality related to the imported modules and defined functions/classes.")
        
        return "\n".join(explanation)
    
    def _explain_code_line(self, line: str, language: str) -> str:
        """Explain a single line of code"""
        
        line_lower = line.lower()
        
        # Common patterns
        if 'print' in line_lower or 'cout' in line_lower or 'console.log' in line_lower:
            return "Outputs information to the console/screen"
        elif 'input' in line_lower or 'cin' in line_lower:
            return "Gets input from the user"
        elif 'if' in line_lower:
            return "Conditional statement - executes code if condition is true"
        elif 'for' in line_lower or 'while' in line_lower:
            return "Loop statement - repeats code multiple times"
        elif 'def' in line_lower or 'function' in line_lower:
            return "Defines a new function/method"
        elif 'class' in line_lower:
            return "Defines a new class (blueprint for objects)"
        elif 'import' in line_lower or 'include' in line_lower:
            return "Imports external libraries or modules"
        elif '=' in line and not '==' in line:
            return "Assigns a value to a variable"
        elif 'return' in line_lower:
            return "Returns a value from the function"
        else:
            return "Executes a specific operation or computation"
    
    def _academic_summary(self, text: str, content_type: str) -> str:
        """Create academic-focused summary"""
        
        subject = content_type.split('_')[1] if '_' in content_type else 'general'
        
        summary_parts = [f"**Academic Summary ({subject.title()}):**\n"]
        
        # Look for key academic elements
        definitions = re.findall(r'(\w+)\s+is\s+defined\s+as\s+([^.]+)', text, re.IGNORECASE)
        theorems = re.findall(r'theorem\s*:?\s*([^.]+)', text, re.IGNORECASE)
        formulas = re.findall(r'formula\s*:?\s*([^.]+)', text, re.IGNORECASE)
        
        if definitions:
            summary_parts.append("**Key Definitions:**")
            for term, definition in definitions[:3]:
                summary_parts.append(f"• {term}: {definition}")
        
        if theorems:
            summary_parts.append("**Theorems/Principles:**")
            for theorem in theorems[:2]:
                summary_parts.append(f"• {theorem}")
        
        if formulas:
            summary_parts.append("**Important Formulas:**")
            for formula in formulas[:2]:
                summary_parts.append(f"• {formula}")
        
        # Add subject-specific analysis
        key_concepts = self.extract_key_concepts(text)
        subject_concepts = [concept for concept in key_concepts 
                          if concept in self.subject_keywords.get(subject, [])]
        
        if subject_concepts:
            summary_parts.append(f"**Key {subject.title()} Concepts:** {', '.join(subject_concepts[:5])}")
        
        return "\n".join(summary_parts)
    
    def _analyze_text_structure(self, text: str) -> Dict[str, Any]:
        """Analyze text structure and provide insights"""
        
        analysis = {}
        
        # Basic statistics
        words = text.split()
        sentences = text.split('.')
        paragraphs = text.split('\n\n')
        
        analysis['statistics'] = {
            'word_count': len(words),
            'sentence_count': len(sentences),
            'paragraph_count': len(paragraphs),
            'avg_words_per_sentence': len(words) / max(len(sentences), 1),
            'reading_time_minutes': len(words) / 200  # Average reading speed
        }
        
        # Complexity analysis
        long_words = [word for word in words if len(word) > 6]
        analysis['complexity'] = {
            'long_words_percentage': len(long_words) / max(len(words), 1) * 100,
            'avg_word_length': sum(len(word) for word in words) / max(len(words), 1),
            'complexity_level': self._determine_complexity_level(text)
        }
        
        # Content type insights
        content_type = self.detect_content_type(text)
        analysis['content_insights'] = {
            'detected_type': content_type,
            'academic_indicators': self._count_academic_indicators(text),
            'technical_indicators': self._count_technical_indicators(text)
        }
        
        return analysis
    
    def _determine_complexity_level(self, text: str) -> str:
        """Determine text complexity level"""
        words = text.split()
        
        # Simple heuristics
        avg_word_length = sum(len(word) for word in words) / max(len(words), 1)
        long_sentences = len([s for s in text.split('.') if len(s.split()) > 20])
        total_sentences = len(text.split('.'))
        
        if avg_word_length > 6 and long_sentences / max(total_sentences, 1) > 0.3:
            return "Advanced"
        elif avg_word_length > 5:
            return "Intermediate"
        else:
            return "Beginner"
    
    def _count_academic_indicators(self, text: str) -> int:
        """Count academic writing indicators"""
        indicators = [
            'research', 'study', 'analysis', 'hypothesis', 'methodology',
            'conclusion', 'evidence', 'data', 'results', 'findings',
            'theory', 'concept', 'principle', 'framework', 'model'
        ]
        
        text_lower = text.lower()
        return sum(1 for indicator in indicators if indicator in text_lower)
    
    def _count_technical_indicators(self, text: str) -> int:
        """Count technical writing indicators"""
        indicators = [
            'algorithm', 'implementation', 'system', 'process', 'method',
            'technique', 'approach', 'solution', 'optimization', 'performance',
            'efficiency', 'architecture', 'design', 'specification', 'protocol'
        ]
        
        text_lower = text.lower()
        return sum(1 for indicator in indicators if indicator in text_lower)
    
    def paraphrase_text(self, text: str, style: str = "formal") -> Dict[str, Any]:
        """Paraphrase text in different styles"""
        
        if len(text.strip()) < 20:
            return {"error": "Text too short to paraphrase effectively"}
        
        key_concepts = self.extract_key_concepts(text)
        content_type = self.detect_content_type(text)
        
        result = {
            "original": text,
            "content_type": content_type,
            "key_concepts": key_concepts,
            "paraphrases": {}
        }
        
        # Generate different style paraphrases
        styles = ["formal", "simple", "academic", "conversational"] if style == "all" else [style]
        
        for paraphrase_style in styles:
            result["paraphrases"][paraphrase_style] = self._generate_paraphrase(text, paraphrase_style, key_concepts)
        
        return result
    
    def _generate_paraphrase(self, text: str, style: str, key_concepts: List[str]) -> str:
        """Generate paraphrase in specific style"""
        
        sentences = sent_tokenize(text) if 'sent_tokenize' in globals() else text.split('.')
        paraphrased_sentences = []
        
        for sentence in sentences:
            if len(sentence.strip()) < 10:
                continue
                
            paraphrased = self._paraphrase_sentence(sentence, style, key_concepts)
            paraphrased_sentences.append(paraphrased)
        
        return " ".join(paraphrased_sentences)
    
    def _paraphrase_sentence(self, sentence: str, style: str, key_concepts: List[str]) -> str:
        """Paraphrase a single sentence"""
        
        # Simple paraphrasing strategies
        sentence = sentence.strip()
        
        if style == "simple":
            # Simplify complex words and structures
            replacements = {
                'utilize': 'use', 'demonstrate': 'show', 'facilitate': 'help',
                'consequently': 'so', 'furthermore': 'also', 'therefore': 'so',
                'however': 'but', 'nevertheless': 'but', 'moreover': 'also'
            }
            
            for complex_word, simple_word in replacements.items():
                sentence = re.sub(r'\b' + complex_word + r'\b', simple_word, sentence, flags=re.IGNORECASE)
        
        elif style == "formal":
            # Make more formal
            replacements = {
                'use': 'utilize', 'show': 'demonstrate', 'help': 'facilitate',
                'so': 'therefore', 'also': 'furthermore', 'but': 'however',
                'get': 'obtain', 'make': 'create', 'find': 'discover'
            }
            
            for informal, formal in replacements.items():
                sentence = re.sub(r'\b' + informal + r'\b', formal, sentence, flags=re.IGNORECASE)
        
        elif style == "academic":
            # Add academic phrases
            if sentence.startswith("This"):
                sentence = "The present analysis indicates that " + sentence[4:].lower()
            elif not any(phrase in sentence.lower() for phrase in ["research", "study", "analysis"]):
                sentence = "Research suggests that " + sentence.lower()
        
        elif style == "conversational":
            # Make more conversational
            if not sentence.endswith('?') and not sentence.endswith('!'):
                if random.choice([True, False]):
                    sentence += ", right?"
            
            # Add conversational starters
            starters = ["You know,", "Actually,", "Basically,", "So,"]
            if random.choice([True, False]):
                sentence = random.choice(starters) + " " + sentence.lower()
        
        return sentence
