"""
🔥💀 GPT KILLER INTERFACE - LOOKS SIMPLE, HIDES REVOLUTIONARY POWER! 💀🔥
Single chat interface that secretly contains ALL our advanced features!
"""

import streamlit as st
import re
from typing import Dict, List, Any, Optional
import base64
from io import BytesIO
import pandas as pd

class IntelligentFeatureDetector:
    """🧠 SECRETLY DETECTS WHAT FEATURES TO ACTIVATE FROM USER INPUT! 🧠"""
    
    def __init__(self):
        self.feature_patterns = {
            "file_processing": [
                r"upload", r"file", r"document", r"pdf", r"image", r"analyze this",
                r"process this", r"read this", r"extract from", r"ocr"
            ],
            "quiz_generation": [
                r"quiz", r"test", r"questions", r"practice", r"exam", r"assessment",
                r"check my knowledge", r"test me on", r"create questions"
            ],
            "summarization": [
                r"summarize", r"summary", r"tldr", r"main points", r"key points",
                r"brief", r"overview", r"condensed", r"short version"
            ],
            "problem_solving": [
                r"solve", r"how to", r"help me with", r"calculate", r"find the",
                r"what is the solution", r"step by step", r"work through"
            ],
            "code_help": [
                r"code", r"programming", r"debug", r"error", r"function", r"algorithm",
                r"python", r"javascript", r"java", r"c\+\+", r"html", r"css"
            ],
            "motivation_needed": [
                r"struggling", r"difficult", r"hard", r"can't understand", r"confused",
                r"frustrated", r"give up", r"discouraged", r"tired"
            ],
            "roadmap_request": [
                r"roadmap", r"learning path", r"where to start", r"how to learn",
                r"study plan", r"curriculum", r"what should i study"
            ],
            "cybersecurity": [
                r"cybersecurity", r"hacking", r"security", r"penetration", r"vulnerability",
                r"exploit", r"malware", r"encryption", r"firewall"
            ]
        }
    
    def detect_features(self, text: str) -> List[str]:
        """🔍 Intelligently detect which features to activate"""
        text_lower = text.lower()
        activated_features = []
        
        for feature, patterns in self.feature_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    activated_features.append(feature)
                    break
        
        return activated_features
    
    def get_smart_routing(self, text: str, uploaded_files: List = None) -> Dict[str, Any]:
        """🧠 Smart routing based on input and context"""
        features = self.detect_features(text)
        
        # If files are uploaded, always include file processing
        if uploaded_files:
            if "file_processing" not in features:
                features.append("file_processing")
        
        # Smart context detection
        context = {
            "features_to_activate": features,
            "needs_motivation": "motivation_needed" in features,
            "is_complex_problem": any(word in text.lower() for word in ["complex", "advanced", "difficult", "challenging"]),
            "wants_visual_feedback": any(word in text.lower() for word in ["show", "visualize", "graph", "chart"]),
            "needs_step_by_step": any(word in text.lower() for word in ["step", "explain", "how", "tutorial"])
        }
        
        return context

class SeamlessInterfaceManager:
    """🎭 MANAGES THE SEAMLESS CHATGPT-STYLE INTERFACE! 🎭"""
    
    def __init__(self):
        self.detector = IntelligentFeatureDetector()
        self.conversation_history = []
    
    def create_file_upload_section(self):
        """📎 Create ChatGPT-style file upload section (FIXED for forms!)"""
        
        # Create horizontal layout like ChatGPT
        col1, col2, col3, col4 = st.columns([1, 1, 1, 3])
        
        with col1:
            uploaded_docs = st.file_uploader(
                "📄",
                type=['pdf', 'docx', 'txt'],
                help="📄 Upload documents (PDF, Word, Text)",
                key="docs_upload",
                label_visibility="collapsed"
            )
        
        with col2:
            uploaded_images = st.file_uploader(
                "🖼️", 
                type=['png', 'jpg', 'jpeg'],
                help="🖼️ Upload images for analysis",
                key="images_upload",
                label_visibility="collapsed"
            )
        
        with col3:
            uploaded_data = st.file_uploader(
                "📊",
                type=['csv', 'xlsx'],
                help="📊 Upload data files (CSV, Excel)",
                key="data_upload",
                label_visibility="collapsed"
            )
        
        with col4:
            # Show upload status
            upload_status = []
            if uploaded_docs:
                upload_status.append(f"📄 {uploaded_docs.name}")
            if uploaded_images:
                upload_status.append(f"🖼️ {uploaded_images.name}")
            if uploaded_data:
                upload_status.append(f"📊 {uploaded_data.name}")
            
            if upload_status:
                st.markdown(f"**Attached:** {' | '.join(upload_status)}")
        
        return {
            "documents": uploaded_docs,
            "images": uploaded_images, 
            "data": uploaded_data
        }
    
    def create_smart_suggestions(self, context: Dict[str, Any]):
        """💡 Show smart suggestions based on context"""
        suggestions = []
        
        if context.get("needs_motivation"):
            suggestions.append("🔥 Need motivation? I can provide personalized encouragement!")
        
        if context.get("is_complex_problem"):
            suggestions.append("🧠 Complex problem? I'll break it down step-by-step!")
        
        if "code_help" in context.get("features_to_activate", []):
            suggestions.append("💻 Code issue? I can debug and explain any programming language!")
        
        if "cybersecurity" in context.get("features_to_activate", []):
            suggestions.append("🛡️ Cybersecurity question? I have expert-level knowledge!")
        
        if suggestions:
            st.markdown("💡 **Smart Suggestions:**")
            for suggestion in suggestions:
                st.info(suggestion)
    
    def process_user_input(self, user_input: str, uploaded_files: Dict, session_state) -> str:
        """🚀 PROCESS INPUT WITH ALL HIDDEN FEATURES!"""
        
        # Get smart routing context
        context = self.detector.get_smart_routing(user_input, uploaded_files)
        
        response = ""
        features_used = []
        
        # FILE PROCESSING (if files uploaded)
        if uploaded_files.get("documents") or uploaded_files.get("images") or uploaded_files.get("data"):
            try:
                if uploaded_files.get("documents"):
                    file_result = session_state.file_processor.process_uploaded_file(uploaded_files["documents"])
                    response += f"📄 **Document Analysis:**\n{file_result.get('content', '')}\n\n"
                    features_used.append("File Processing")
                
                if uploaded_files.get("images"):
                    # OCR processing
                    response += f"🖼️ **Image Text Extraction:** Processing image with OCR...\n\n"
                    features_used.append("OCR Technology")
                
                if uploaded_files.get("data"):
                    # Data analysis
                    response += f"📊 **Data Analysis:** Analyzing uploaded data...\n\n"
                    features_used.append("Data Analytics")
            except Exception as e:
                response += f"⚡ **Processing Files:** {str(e)}\n\n"
        
        # INTELLIGENT FEATURE ACTIVATION
        activated_features = context["features_to_activate"]
        
        # PROBLEM SOLVING
        if "problem_solving" in activated_features:
            solver_result = session_state.universal_solver.solve_universal_problem(user_input)
            response += solver_result.get("response", "")
            features_used.append("Universal Problem Solver")
        
        # SUMMARIZATION
        elif "summarization" in activated_features:
            summary_result = session_state.text_processor.summarize_text(user_input)
            response += f"📝 **Ultra-Advanced Summary:**\n{summary_result}\n\n"
            features_used.append("Advanced Summarization")
        
        # CODE HELP
        elif "code_help" in activated_features:
            code_result = session_state.text_processor.explain_code(user_input)
            response += f"💻 **Code Analysis:**\n{code_result}\n\n"
            features_used.append("Code Intelligence")
        
        # CYBERSECURITY
        elif "cybersecurity" in activated_features:
            cyber_result = session_state.cybersecurity_destroyer.get_cybersecurity_response(user_input, "comprehensive", "expert")
            response += cyber_result.get("response", "")
            features_used.append("Cybersecurity Mastery")
        
        # QUIZ GENERATION
        elif "quiz_generation" in activated_features:
            # Extract subject from input
            subject = "General"
            if any(subj in user_input.lower() for subj in ["math", "physics", "chemistry", "biology", "computer"]):
                for subj in ["Mathematics", "Physics", "Chemistry", "Biology", "Computer Science"]:
                    if subj.lower() in user_input.lower():
                        subject = subj
                        break
            
            quiz = session_state.quiz_generator.generate_quiz(subject, "intermediate", 5)
            response += f"🎯 **Interactive Quiz Generated:**\n\n"
            for i, q in enumerate(quiz["questions"], 1):
                response += f"**Q{i}:** {q['question']}\n"
                if q.get("options"):
                    for opt in q["options"]:
                        response += f"  • {opt}\n"
                response += f"**Answer:** {q['correct_answer']}\n\n"
            features_used.append("Quiz Generation")
        
        # ROADMAP REQUEST
        elif "roadmap_request" in activated_features:
            roadmap = session_state.roadmap_generator.generate_roadmap("General Learning", "beginner")
            response += f"🗺️ **Personalized Learning Roadmap:**\n{roadmap.get('content', '')}\n\n"
            features_used.append("Learning Roadmap")
        
        # DEFAULT AI TUTOR
        else:
            # Use general knowledge or AI tutor
            if session_state.current_subject == "General":
                response_data = session_state.general_knowledge.process_general_query(user_input, session_state.user_profile)
                response += response_data.get("content", "")
            else:
                response += session_state.ai_tutor.generate_response(user_input, session_state.current_subject, session_state.user_profile)
            features_used.append("AI Intelligence")
        
        # ADD MOTIVATION if needed
        if context.get("needs_motivation") and session_state.user_profile.get("name"):
            user_stats = session_state.gamification.get_user_stats(session_state.user_profile["name"])
            motivation = session_state.motivational_engine.generate_dynamic_motivation(user_stats, "encouragement")
            response += f"\n\n{motivation['response']}"
            features_used.append("Motivational Engine")
        
        # ADD ANIMATIONS for achievements
        if features_used and session_state.user_profile.get("name"):
            animation = session_state.animation_engine.create_quiz_animation("feature_used")
            response += f"\n\n✨ **Features Activated:** {', '.join(features_used)} {animation['animation_text']}"
        
        # UPDATE GAMIFICATION
        if session_state.user_profile.get("name"):
            session_state.gamification.update_user_activity(
                session_state.user_profile["name"],
                "advanced_query",
                {"features_used": features_used, "query_complexity": len(activated_features)}
            )
        
        return response
    
    def create_seamless_interface(self, session_state):
        """🎭 CREATE THE ULTIMATE GPT-KILLER INTERFACE!"""
        
        # Apply ChatGPT-like dark styling
        st.markdown("""
        <style>
        .stApp {
            background-color: #212121;
            color: #ffffff;
        }
        .stApp > header {
            background-color: transparent;
        }
        .stApp > .main > .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 100%;
        }
        .main-title {
            color: #ffffff;
            text-align: center;
            font-size: 2.5rem;
            font-weight: 400;
            margin-bottom: 3rem;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .chat-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 0 2rem;
        }
        .user-message-box {
            background-color: #2f2f2f;
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
            margin-left: 3rem;
            border-left: 3px solid #10a37f;
        }
        .ai-message-box {
            background-color: #444444;
            border-radius: 8px;
            padding: 1rem;
            margin: 1rem 0;
            margin-right: 3rem;
            border-left: 3px solid #ff6b6b;
        }
        .input-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #212121;
            padding: 1rem 2rem 2rem 2rem;
            border-top: 1px solid #444444;
        }
        .stTextArea > div > div > textarea {
            background-color: #2f2f2f;
            border: 1px solid #444444;
            border-radius: 8px;
            color: #ffffff;
            font-size: 1rem;
        }
        .stTextArea > div > div > textarea:focus {
            border-color: #10a37f;
            box-shadow: 0 0 0 1px #10a37f;
        }
        .stButton > button {
            background-color: #10a37f;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 0.5rem 1rem;
            font-weight: 500;
        }
        .stButton > button:hover {
            background-color: #0d8f6f;
        }
        .file-upload-section {
            background-color: #2f2f2f;
            border-radius: 8px;
            padding: 0.5rem;
            margin-bottom: 1rem;
            border: 1px solid #444444;
        }
        .sidebar .element-container {
            background-color: #1a1a1a;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # ChatGPT-style centered header with suggestions
        if not session_state.chat_history:
            st.markdown("""
            <div class="main-title">
                What can I help you learn today?
            </div>
            """, unsafe_allow_html=True)
            
            # Add suggestion cards like ChatGPT
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("🧮 Solve complex math problems", use_container_width=True, help="Get step-by-step solutions"):
                    session_state.chat_history.append({
                        "role": "user", 
                        "content": "Solve this calculus problem: ∫(x² + 3x + 2)dx"
                    })
                    st.rerun()
            
            with col2:
                if st.button("📚 Explain any concept", use_container_width=True, help="Deep explanations with examples"):
                    session_state.chat_history.append({
                        "role": "user", 
                        "content": "Explain quantum entanglement in simple terms with real-world analogies"
                    })
                    st.rerun()
            
            with col3:
                if st.button("🎯 Generate practice quizzes", use_container_width=True, help="Instant assessments"):
                    session_state.chat_history.append({
                        "role": "user", 
                        "content": "Create a quiz on machine learning fundamentals"
                    })
                    st.rerun()
            
            # Second row of suggestions
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("💻 Debug and explain code", use_container_width=True, help="Any programming language"):
                    session_state.chat_history.append({
                        "role": "user", 
                        "content": "Debug this Python code and explain what's wrong: for i in range(10) print(i)"
                    })
                    st.rerun()
            
            with col2:
                if st.button("🌍 General knowledge questions", use_container_width=True, help="Beyond academics"):
                    session_state.chat_history.append({
                        "role": "user", 
                        "content": "What are the latest developments in renewable energy technology?"
                    })
                    st.rerun()
            
            with col3:
                if st.button("🚀 Learning roadmaps", use_container_width=True, help="Structured learning paths"):
                    session_state.chat_history.append({
                        "role": "user", 
                        "content": "Create a learning roadmap for becoming a cybersecurity expert"
                    })
                    st.rerun()
        else:
            # Show compact header when chat exists
            st.markdown("""
            <div style="text-align: center; margin-bottom: 1rem;">
                <h3 style="color: #ffffff; margin: 0; font-weight: 400;">🧠 AI Learning Assistant</h3>
            </div>
            """, unsafe_allow_html=True)
        
        # Chat history display with ChatGPT styling
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        for message in session_state.chat_history:
            if message["role"] == "user":
                st.markdown(f"""
                <div class="user-message-box">
                    <strong style="color: #10a37f;">You:</strong> {message["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="ai-message-box">
                    <strong style="color: #ff6b6b;">🧠 AI Assistant:</strong><br>{message["content"]}
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # ChatGPT-style input area at bottom
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        
        with st.form(key="chat_form", clear_on_submit=True):
            # File upload section with ChatGPT styling
            st.markdown('<div class="file-upload-section">', unsafe_allow_html=True)
            uploaded_files = self.create_file_upload_section()
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Main text input with ChatGPT-style placeholder
            user_input = st.text_area(
                "",
                placeholder="Ask anything...",
                height=60,
                key="main_input",
                help="💡 I can analyze files, solve problems, create quizzes, and much more!"
            )
            
            # ChatGPT-style button layout
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
            with col2:
                submitted = st.form_submit_button("Send", use_container_width=True)
            with col3:
                generate_quiz = st.form_submit_button("Quiz", use_container_width=True, help="Generate quiz")
            with col4:
                clear_chat = st.form_submit_button("Clear", use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Handle different form submissions
        if clear_chat:
            session_state.chat_history = []
            st.rerun()
        
        if generate_quiz:
            # Generate a quick quiz
            quiz = session_state.quiz_generator.generate_quiz("General", "intermediate", 3)
            quiz_text = "🎯 **Quick Quiz Generated:**\n\n"
            for i, q in enumerate(quiz["questions"], 1):
                quiz_text += f"**Q{i}:** {q['question']}\n"
                if q.get("options"):
                    for opt in q["options"]:
                        quiz_text += f"  • {opt}\n"
                quiz_text += f"**Answer:** {q['correct_answer']}\n\n"
            
            session_state.chat_history.append({"role": "assistant", "content": quiz_text})
            st.rerun()
        
        if submitted and user_input:
            # Add user message to history
            session_state.chat_history.append({"role": "user", "content": user_input})
            
            # Get smart routing context for suggestions
            context = self.detector.get_smart_routing(user_input, uploaded_files)
            
            # Show smart suggestions
            self.create_smart_suggestions(context)
            
            # Process with ALL hidden features
            with st.spinner("🧠 AI thinking..."):
                response = self.process_user_input(user_input, uploaded_files, session_state)
            
            # Add AI response to history
            session_state.chat_history.append({"role": "assistant", "content": response})
            
            # Auto-scroll to bottom (rerun to show new messages)
            st.rerun()
        
        # Subtle feature hints in sidebar
        with st.sidebar:
            st.markdown("### 🔥 **Hidden Superpowers**")
            st.info("🧠 **This AI is more advanced than it looks!**")
            
            with st.expander("💫 Secret Capabilities"):
                st.markdown("""
                🔹 **Universal Problem Solver** - Any domain, any complexity  
                🔹 **File Processing Master** - PDFs, images, documents  
                🔹 **Quiz Generator** - Instant assessments  
                🔹 **Code Intelligence** - Any programming language  
                🔹 **Motivational Engine** - Personalized encouragement  
                🔹 **Learning Analytics** - Progress tracking  
                🔹 **Cybersecurity Expert** - Professional-level knowledge  
                🔹 **Advanced Summarization** - Ultra-intelligent analysis  
                
                💀 **GPT can't do half of this!**
                """)
            
            st.markdown("---")
            st.markdown("### ⚡ **Quick Actions**")
            
            # Use separate forms for sidebar buttons
            with st.form("quick_quiz_form"):
                if st.form_submit_button("🎯 Generate Random Quiz", use_container_width=True):
                    # Generate quick quiz
                    quiz = session_state.quiz_generator.generate_quiz("General", "intermediate", 3)
                    quiz_text = "🎯 **Quick Quiz:**\n\n"
                    for i, q in enumerate(quiz["questions"], 1):
                        quiz_text += f"**Q{i}:** {q['question']}\n"
                        if q.get("options"):
                            for opt in q["options"]:
                                quiz_text += f"  • {opt}\n"
                        quiz_text += f"**Answer:** {q['correct_answer']}\n\n"
                    
                    session_state.chat_history.append({"role": "assistant", "content": quiz_text})
                    st.rerun()
            
            with st.form("motivation_form"):
                if st.form_submit_button("💪 Get Motivation", use_container_width=True):
                    if session_state.user_profile.get("name"):
                        user_stats = session_state.gamification.get_user_stats(session_state.user_profile["name"])
                        motivation = session_state.motivational_engine.generate_dynamic_motivation(user_stats, "general")
                        session_state.chat_history.append({"role": "assistant", "content": motivation["response"]})
                        st.rerun()
            
            with st.form("progress_form"):
                if st.form_submit_button("🌟 Show My Progress", use_container_width=True):
                    if session_state.user_profile.get("name"):
                        stats = session_state.gamification.get_user_stats(session_state.user_profile["name"])
                        progress_text = f"""
                        📊 **Your Learning Progress:**
                        
                        🎖️ **Level:** {stats.get('level', 1)}
                        ⚡ **XP:** {stats.get('xp', 0)}
                        🔥 **Streak:** {stats.get('streaks', {}).get('daily_login', 0)} days
                        🏆 **Achievements:** {len(stats.get('achievements', []))}
                        📝 **Questions Asked:** {stats.get('statistics', {}).get('questions_asked', 0)}
                        
                        🚀 **Keep going! You're building expertise!**
                        """
                        session_state.chat_history.append({"role": "assistant", "content": progress_text})
                        st.rerun()

def create_gpt_killer_interface(session_state):
    """🔥💀 CREATE THE ULTIMATE GPT-KILLING INTERFACE! 💀🔥"""
    manager = SeamlessInterfaceManager()
    manager.create_seamless_interface(session_state)
