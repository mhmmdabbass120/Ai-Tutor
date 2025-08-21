import random
import json
from typing import Dict, List, Any, Tuple

class QuizGenerator:
    """Advanced quiz generator with adaptive difficulty and multiple question types"""
    
    def __init__(self):
        self.question_bank = self._initialize_question_bank()
        self.difficulty_weights = {
            "Beginner": {"easy": 0.7, "medium": 0.3, "hard": 0.0},
            "Intermediate": {"easy": 0.2, "medium": 0.6, "hard": 0.2},
            "Advanced": {"easy": 0.1, "medium": 0.3, "hard": 0.6}
        }
    
    def _initialize_question_bank(self) -> Dict[str, Any]:
        """Initialize comprehensive question bank for all subjects"""
        return {
            "Mathematics": {
                "easy": [
                    {
                        "question": "What is 5 + 7?",
                        "type": "multiple_choice",
                        "options": ["10", "12", "13", "15"],
                        "correct_answer": "12",
                        "explanation": "5 + 7 = 12. This is basic addition."
                    },
                    {
                        "question": "Solve for x: x + 3 = 8",
                        "type": "multiple_choice",
                        "options": ["3", "5", "8", "11"],
                        "correct_answer": "5",
                        "explanation": "x = 8 - 3 = 5. Subtract 3 from both sides."
                    },
                    {
                        "question": "What is the area of a square with side length 4?",
                        "type": "multiple_choice",
                        "options": ["12", "16", "20", "24"],
                        "correct_answer": "16",
                        "explanation": "Area = side × side = 4 × 4 = 16 square units."
                    },
                    {
                        "question": "Is 15 divisible by 3?",
                        "type": "true_false",
                        "options": ["True", "False"],
                        "correct_answer": "True",
                        "explanation": "15 ÷ 3 = 5, so yes, 15 is divisible by 3."
                    }
                ],
                "medium": [
                    {
                        "question": "Solve the quadratic equation: x² - 5x + 6 = 0",
                        "type": "multiple_choice",
                        "options": ["x = 2, 3", "x = 1, 6", "x = -2, -3", "x = 0, 5"],
                        "correct_answer": "x = 2, 3",
                        "explanation": "Factor: (x-2)(x-3) = 0, so x = 2 or x = 3."
                    },
                    {
                        "question": "What is the derivative of f(x) = x²?",
                        "type": "multiple_choice",
                        "options": ["x", "2x", "x²", "2"],
                        "correct_answer": "2x",
                        "explanation": "Using power rule: d/dx(x²) = 2x¹ = 2x."
                    },
                    {
                        "question": "The sum of angles in any triangle is 180°.",
                        "type": "true_false",
                        "options": ["True", "False"],
                        "correct_answer": "True",
                        "explanation": "This is a fundamental property of triangles in Euclidean geometry."
                    }
                ],
                "hard": [
                    {
                        "question": "What is the limit of (sin x)/x as x approaches 0?",
                        "type": "multiple_choice",
                        "options": ["0", "1", "∞", "undefined"],
                        "correct_answer": "1",
                        "explanation": "This is a standard limit: lim(x→0) sin(x)/x = 1."
                    },
                    {
                        "question": "The eigenvalues of a 2×2 matrix can be complex numbers.",
                        "type": "true_false",
                        "options": ["True", "False"],
                        "correct_answer": "True",
                        "explanation": "Eigenvalues can be complex, especially for rotation matrices."
                    }
                ]
            },
            "Physics": {
                "easy": [
                    {
                        "question": "What is the unit of force?",
                        "type": "multiple_choice",
                        "options": ["Joule", "Newton", "Watt", "Pascal"],
                        "correct_answer": "Newton",
                        "explanation": "The SI unit of force is the Newton (N)."
                    },
                    {
                        "question": "Objects fall faster on the Moon than on Earth.",
                        "type": "true_false",
                        "options": ["True", "False"],
                        "correct_answer": "False",
                        "explanation": "Objects fall slower on the Moon due to weaker gravity (1.6 m/s² vs 9.8 m/s²)."
                    },
                    {
                        "question": "What is the speed of light in vacuum?",
                        "type": "multiple_choice",
                        "options": ["3×10⁶ m/s", "3×10⁸ m/s", "3×10¹⁰ m/s", "3×10¹² m/s"],
                        "correct_answer": "3×10⁸ m/s",
                        "explanation": "The speed of light in vacuum is approximately 3×10⁸ m/s."
                    }
                ],
                "medium": [
                    {
                        "question": "A 2 kg object accelerates at 5 m/s². What force is applied?",
                        "type": "multiple_choice",
                        "options": ["7 N", "10 N", "3 N", "2.5 N"],
                        "correct_answer": "10 N",
                        "explanation": "F = ma = 2 kg × 5 m/s² = 10 N."
                    },
                    {
                        "question": "Energy can be created or destroyed.",
                        "type": "true_false",
                        "options": ["True", "False"],
                        "correct_answer": "False",
                        "explanation": "Energy is conserved - it can only be converted from one form to another."
                    }
                ],
                "hard": [
                    {
                        "question": "According to special relativity, what happens to time as velocity approaches the speed of light?",
                        "type": "multiple_choice",
                        "options": ["Time speeds up", "Time slows down", "Time stops", "Time reverses"],
                        "correct_answer": "Time slows down",
                        "explanation": "Time dilation occurs: time slows down for the moving observer."
                    }
                ]
            },
            "Chemistry": {
                "easy": [
                    {
                        "question": "What is the chemical symbol for water?",
                        "type": "multiple_choice",
                        "options": ["H₂O", "CO₂", "NaCl", "O₂"],
                        "correct_answer": "H₂O",
                        "explanation": "Water consists of 2 hydrogen atoms and 1 oxygen atom: H₂O."
                    },
                    {
                        "question": "Acids have a pH less than 7.",
                        "type": "true_false",
                        "options": ["True", "False"],
                        "correct_answer": "True",
                        "explanation": "The pH scale: acids < 7, neutral = 7, bases > 7."
                    },
                    {
                        "question": "How many protons does carbon have?",
                        "type": "multiple_choice",
                        "options": ["4", "6", "8", "12"],
                        "correct_answer": "6",
                        "explanation": "Carbon has atomic number 6, meaning 6 protons."
                    }
                ],
                "medium": [
                    {
                        "question": "What is the pH of a 0.01 M HCl solution?",
                        "type": "multiple_choice",
                        "options": ["1", "2", "12", "13"],
                        "correct_answer": "2",
                        "explanation": "pH = -log[H⁺] = -log(0.01) = -log(10⁻²) = 2."
                    },
                    {
                        "question": "Catalysts are consumed in chemical reactions.",
                        "type": "true_false",
                        "options": ["True", "False"],
                        "correct_answer": "False",
                        "explanation": "Catalysts speed up reactions but are not consumed in the process."
                    }
                ],
                "hard": [
                    {
                        "question": "What is the hybridization of carbon in methane (CH₄)?",
                        "type": "multiple_choice",
                        "options": ["sp", "sp²", "sp³", "sp³d"],
                        "correct_answer": "sp³",
                        "explanation": "Carbon in methane has tetrahedral geometry with sp³ hybridization."
                    }
                ]
            },
            "Biology": {
                "easy": [
                    {
                        "question": "What is the powerhouse of the cell?",
                        "type": "multiple_choice",
                        "options": ["Nucleus", "Mitochondria", "Ribosome", "Golgi apparatus"],
                        "correct_answer": "Mitochondria",
                        "explanation": "Mitochondria produce ATP, the cell's energy currency."
                    },
                    {
                        "question": "Plants produce oxygen during photosynthesis.",
                        "type": "true_false",
                        "options": ["True", "False"],
                        "correct_answer": "True",
                        "explanation": "Photosynthesis: 6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂."
                    },
                    {
                        "question": "How many chromosomes do humans normally have?",
                        "type": "multiple_choice",
                        "options": ["23", "46", "48", "92"],
                        "correct_answer": "46",
                        "explanation": "Humans have 23 pairs of chromosomes, totaling 46."
                    }
                ],
                "medium": [
                    {
                        "question": "What is the difference between mitosis and meiosis?",
                        "type": "multiple_choice",
                        "options": ["Mitosis produces gametes", "Meiosis produces somatic cells", "Mitosis produces diploid cells", "They are the same process"],
                        "correct_answer": "Mitosis produces diploid cells",
                        "explanation": "Mitosis produces identical diploid cells; meiosis produces genetically different haploid gametes."
                    },
                    {
                        "question": "DNA is found only in the nucleus.",
                        "type": "true_false",
                        "options": ["True", "False"],
                        "correct_answer": "False",
                        "explanation": "DNA is also found in mitochondria and chloroplasts."
                    }
                ],
                "hard": [
                    {
                        "question": "What enzyme is responsible for unwinding DNA during replication?",
                        "type": "multiple_choice",
                        "options": ["DNA polymerase", "Helicase", "Ligase", "Primase"],
                        "correct_answer": "Helicase",
                        "explanation": "Helicase unwinds the DNA double helix during replication."
                    }
                ]
            },
            "Computer Science": {
                "easy": [
                    {
                        "question": "What does 'HTML' stand for?",
                        "type": "multiple_choice",
                        "options": ["HyperText Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlink Text Management Language"],
                        "correct_answer": "HyperText Markup Language",
                        "explanation": "HTML stands for HyperText Markup Language, used for creating web pages."
                    },
                    {
                        "question": "Python is a compiled programming language.",
                        "type": "true_false",
                        "options": ["True", "False"],
                        "correct_answer": "False",
                        "explanation": "Python is an interpreted language, not compiled."
                    }
                ],
                "medium": [
                    {
                        "question": "What is the time complexity of binary search?",
                        "type": "multiple_choice",
                        "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
                        "correct_answer": "O(log n)",
                        "explanation": "Binary search eliminates half the search space each iteration, giving O(log n) complexity."
                    },
                    {
                        "question": "A stack follows LIFO (Last In, First Out) principle.",
                        "type": "true_false",
                        "options": ["True", "False"],
                        "correct_answer": "True",
                        "explanation": "Stacks are LIFO data structures - the last item added is the first one removed."
                    }
                ],
                "hard": [
                    {
                        "question": "What is the worst-case time complexity of quicksort?",
                        "type": "multiple_choice",
                        "options": ["O(n log n)", "O(n²)", "O(log n)", "O(n)"],
                        "correct_answer": "O(n²)",
                        "explanation": "Quicksort's worst case is O(n²) when the pivot is always the smallest or largest element."
                    }
                ]
            }
        }
    
    def generate_quiz(self, subject: str, level: str, num_questions: int = 5) -> Dict[str, Any]:
        """Generate a customized quiz based on subject and difficulty level"""
        if subject not in self.question_bank:
            return self._generate_generic_quiz(subject, level, num_questions)
        
        # Get difficulty distribution based on level
        difficulty_dist = self.difficulty_weights[level]
        
        # Calculate number of questions for each difficulty
        easy_count = int(num_questions * difficulty_dist["easy"])
        medium_count = int(num_questions * difficulty_dist["medium"])
        hard_count = num_questions - easy_count - medium_count
        
        questions = []
        
        # Add questions from each difficulty level
        subject_questions = self.question_bank[subject]
        
        # Easy questions
        if easy_count > 0 and "easy" in subject_questions:
            easy_q = random.sample(subject_questions["easy"], 
                                 min(easy_count, len(subject_questions["easy"])))
            questions.extend(easy_q)
        
        # Medium questions
        if medium_count > 0 and "medium" in subject_questions:
            medium_q = random.sample(subject_questions["medium"], 
                                   min(medium_count, len(subject_questions["medium"])))
            questions.extend(medium_q)
        
        # Hard questions
        if hard_count > 0 and "hard" in subject_questions:
            hard_q = random.sample(subject_questions["hard"], 
                                 min(hard_count, len(subject_questions["hard"])))
            questions.extend(hard_q)
        
        # Fill remaining slots if needed
        while len(questions) < num_questions:
            all_questions = []
            for difficulty in subject_questions.values():
                all_questions.extend(difficulty)
            
            remaining = [q for q in all_questions if q not in questions]
            if remaining:
                questions.append(random.choice(remaining))
            else:
                break
        
        # Shuffle questions
        random.shuffle(questions)
        
        return {
            "subject": subject,
            "level": level,
            "total_questions": len(questions),
            "questions": questions,
            "quiz_id": f"{subject}_{level}_{random.randint(1000, 9999)}"
        }
    
    def _generate_generic_quiz(self, subject: str, level: str, num_questions: int) -> Dict[str, Any]:
        """Generate a generic quiz for subjects not in the question bank"""
        generic_questions = [
            {
                "question": f"What is a fundamental concept in {subject}?",
                "type": "multiple_choice",
                "options": ["Concept A", "Concept B", "Concept C", "All of the above"],
                "correct_answer": "All of the above",
                "explanation": f"All these concepts are important in {subject}."
            },
            {
                "question": f"Is {subject} an important field of study?",
                "type": "true_false",
                "options": ["True", "False"],
                "correct_answer": "True",
                "explanation": f"{subject} has many practical applications and is worth studying."
            }
        ]
        
        # Repeat questions to reach desired number
        questions = []
        for i in range(num_questions):
            question = generic_questions[i % len(generic_questions)].copy()
            question["question"] = f"Question {i+1}: {question['question']}"
            questions.append(question)
        
        return {
            "subject": subject,
            "level": level,
            "total_questions": num_questions,
            "questions": questions,
            "quiz_id": f"{subject}_{level}_{random.randint(1000, 9999)}"
        }
    
    def generate_adaptive_quiz(self, subject: str, initial_level: str, performance_history: List[float] = None) -> Dict[str, Any]:
        """Generate an adaptive quiz that adjusts difficulty based on performance"""
        if performance_history is None:
            performance_history = []
        
        # Adjust level based on recent performance
        current_level = initial_level
        
        if len(performance_history) >= 3:
            avg_score = sum(performance_history[-3:]) / 3
            
            if avg_score >= 85 and current_level == "Beginner":
                current_level = "Intermediate"
            elif avg_score >= 85 and current_level == "Intermediate":
                current_level = "Advanced"
            elif avg_score < 60 and current_level == "Advanced":
                current_level = "Intermediate"
            elif avg_score < 60 and current_level == "Intermediate":
                current_level = "Beginner"
        
        quiz = self.generate_quiz(subject, current_level)
        quiz["adapted_from"] = initial_level
        quiz["adapted_to"] = current_level
        
        return quiz
    
    def generate_mixed_subject_quiz(self, subjects: List[str], level: str, questions_per_subject: int = 2) -> Dict[str, Any]:
        """Generate a quiz with questions from multiple subjects"""
        all_questions = []
        
        for subject in subjects:
            if subject in self.question_bank:
                subject_quiz = self.generate_quiz(subject, level, questions_per_subject)
                for question in subject_quiz["questions"]:
                    question["subject"] = subject  # Tag with subject
                    all_questions.append(question)
        
        random.shuffle(all_questions)
        
        return {
            "subjects": subjects,
            "level": level,
            "total_questions": len(all_questions),
            "questions": all_questions,
            "quiz_id": f"mixed_{level}_{random.randint(1000, 9999)}"
        }
    
    def create_custom_question(self, question_text: str, question_type: str, 
                             options: List[str], correct_answer: str, 
                             explanation: str = "") -> Dict[str, Any]:
        """Create a custom question"""
        return {
            "question": question_text,
            "type": question_type,
            "options": options,
            "correct_answer": correct_answer,
            "explanation": explanation or "Custom question - explanation not provided.",
            "custom": True
        }
    
    def add_question_to_bank(self, subject: str, difficulty: str, question: Dict[str, Any]):
        """Add a new question to the question bank"""
        if subject not in self.question_bank:
            self.question_bank[subject] = {"easy": [], "medium": [], "hard": []}
        
        if difficulty not in self.question_bank[subject]:
            self.question_bank[subject][difficulty] = []
        
        self.question_bank[subject][difficulty].append(question)
    
    def get_quiz_statistics(self, quiz_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate statistics from quiz results"""
        if not quiz_results:
            return {"message": "No quiz results available"}
        
        total_quizzes = len(quiz_results)
        total_questions = sum(len(result.get("answers", [])) for result in quiz_results)
        correct_answers = sum(result.get("score", 0) for result in quiz_results)
        
        subject_performance = {}
        difficulty_performance = {}
        
        for result in quiz_results:
            subject = result.get("subject", "Unknown")
            level = result.get("level", "Unknown")
            score = result.get("score", 0)
            
            if subject not in subject_performance:
                subject_performance[subject] = []
            subject_performance[subject].append(score)
            
            if level not in difficulty_performance:
                difficulty_performance[level] = []
            difficulty_performance[level].append(score)
        
        # Calculate averages
        avg_subject_performance = {
            subject: sum(scores) / len(scores) 
            for subject, scores in subject_performance.items()
        }
        
        avg_difficulty_performance = {
            level: sum(scores) / len(scores) 
            for level, scores in difficulty_performance.items()
        }
        
        return {
            "total_quizzes": total_quizzes,
            "total_questions": total_questions,
            "overall_accuracy": (correct_answers / total_questions * 100) if total_questions > 0 else 0,
            "subject_performance": avg_subject_performance,
            "difficulty_performance": avg_difficulty_performance,
            "improvement_suggestions": self._generate_improvement_suggestions(avg_subject_performance, avg_difficulty_performance)
        }
    
    def _generate_improvement_suggestions(self, subject_perf: Dict[str, float], 
                                        difficulty_perf: Dict[str, float]) -> List[str]:
        """Generate suggestions for improvement based on performance"""
        suggestions = []
        
        # Subject-based suggestions
        for subject, score in subject_perf.items():
            if score < 70:
                suggestions.append(f"Focus more on {subject} fundamentals - current average: {score:.1f}%")
            elif score > 90:
                suggestions.append(f"Great job in {subject}! Consider advancing to harder topics.")
        
        # Difficulty-based suggestions
        for level, score in difficulty_perf.items():
            if score < 60:
                suggestions.append(f"Review {level} level concepts more thoroughly")
            elif score > 85:
                suggestions.append(f"Ready to advance from {level} level!")
        
        if not suggestions:
            suggestions.append("Keep up the excellent work! Continue practicing regularly.")
        
        return suggestions

class QuizAnalyzer:
    """Analyze quiz performance and provide insights"""
    
    @staticmethod
    def analyze_wrong_answers(quiz_result: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze patterns in wrong answers"""
        wrong_answers = []
        question_types_missed = {}
        subjects_missed = {}
        
        for i, question in enumerate(quiz_result.get("questions", [])):
            user_answer = quiz_result.get("user_answers", {}).get(str(i))
            correct_answer = question.get("correct_answer")
            
            if user_answer != correct_answer:
                wrong_answers.append({
                    "question": question.get("question"),
                    "user_answer": user_answer,
                    "correct_answer": correct_answer,
                    "explanation": question.get("explanation"),
                    "type": question.get("type"),
                    "subject": question.get("subject", quiz_result.get("subject"))
                })
                
                # Track question type patterns
                q_type = question.get("type", "unknown")
                question_types_missed[q_type] = question_types_missed.get(q_type, 0) + 1
                
                # Track subject patterns
                subject = question.get("subject", quiz_result.get("subject", "unknown"))
                subjects_missed[subject] = subjects_missed.get(subject, 0) + 1
        
        return {
            "wrong_answers": wrong_answers,
            "patterns": {
                "question_types": question_types_missed,
                "subjects": subjects_missed
            },
            "recommendations": QuizAnalyzer._generate_recommendations(wrong_answers, question_types_missed, subjects_missed)
        }
    
    @staticmethod
    def _generate_recommendations(wrong_answers: List[Dict], type_patterns: Dict, subject_patterns: Dict) -> List[str]:
        """Generate personalized recommendations based on analysis"""
        recommendations = []
        
        if len(wrong_answers) == 0:
            return ["Perfect score! Keep up the excellent work!"]
        
        # Question type recommendations
        if "multiple_choice" in type_patterns and type_patterns["multiple_choice"] > 2:
            recommendations.append("Practice multiple choice strategy: eliminate obviously wrong answers first")
        
        if "true_false" in type_patterns and type_patterns["true_false"] > 1:
            recommendations.append("For true/false questions, look for absolute words like 'always' or 'never' - they're often false")
        
        # Subject recommendations
        for subject, count in subject_patterns.items():
            if count > 1:
                recommendations.append(f"Review {subject} concepts - you missed {count} questions in this area")
        
        # General recommendations
        if len(wrong_answers) > len(type_patterns):
            recommendations.append("Read questions more carefully - some errors might be due to misreading")
        
        return recommendations
