#!/usr/bin/env python3
"""
AI Tutor Chatbot Demo
This script demonstrates the core capabilities of the AI tutor system.
"""

from ai_tutor import AITutorEngine
from subjects import SubjectManager, MathSolver, PhysicsSimulator
from quiz_generator import QuizGenerator
from progress_tracker import ProgressTracker

def demo_ai_tutor():
    """Demonstrate AI tutor capabilities"""
    print("🤖 AI TUTOR DEMO")
    print("=" * 50)
    
    # Initialize AI tutor
    tutor = AITutorEngine()
    
    # Sample user profile
    user_profile = {
        "name": "Demo User",
        "level": "Intermediate",
        "subjects": ["Mathematics", "Physics"]
    }
    
    # Demo conversations
    test_questions = [
        "What is photosynthesis?",
        "Explain Newton's second law",
        "How do I solve quadratic equations?",
        "What is the difference between mitosis and meiosis?",
        "Can you help me understand derivatives?"
    ]
    
    print("💬 Sample Conversations:")
    print("-" * 30)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{i}. Student: {question}")
        response = tutor.generate_response(question, "Physics" if "Newton" in question else "Mathematics", user_profile)
        print(f"   🎓 Tutor: {response[:100]}...")
    
    print("\n✅ AI Tutor Demo Complete!")

def demo_subject_tools():
    """Demonstrate subject-specific tools"""
    print("\n🛠️  SUBJECT TOOLS DEMO")
    print("=" * 50)
    
    # Math solver demo
    print("\n📐 Math Solver:")
    solver = MathSolver()
    print("   Circle area (radius=5):", solver.calculate_area("circle", radius=5))
    print("   Rectangle area (4×6):", solver.calculate_area("rectangle", length=4, width=6))
    
    # Physics simulator demo
    print("\n⚡ Physics Simulator:")
    sim = PhysicsSimulator()
    projectile = sim.projectile_motion(velocity=25, angle=45)
    print(f"   Projectile motion (25 m/s at 45°): {projectile}")
    print(f"   Kinetic energy (2kg at 10 m/s): {sim.kinetic_energy(2, 10)} J")
    
    # Subject manager demo
    print("\n📚 Subject Manager:")
    subjects = SubjectManager()
    print(f"   Random Math concept: {subjects.get_random_concept('Mathematics')}")
    print(f"   Random Physics problem: {subjects.get_random_problem('Physics', 'Intermediate')}")
    
    print("\n✅ Subject Tools Demo Complete!")

def demo_quiz_system():
    """Demonstrate quiz generation system"""
    print("\n📝 QUIZ SYSTEM DEMO")
    print("=" * 50)
    
    quiz_gen = QuizGenerator()
    
    # Generate sample quiz
    quiz = quiz_gen.generate_quiz("Mathematics", "Intermediate", 3)
    
    print(f"\n📋 Sample Quiz: {quiz['subject']} - {quiz['level']} Level")
    print(f"   Total Questions: {quiz['total_questions']}")
    
    for i, question in enumerate(quiz['questions'], 1):
        print(f"\n   Q{i}: {question['question']}")
        print(f"       Type: {question['type']}")
        print(f"       Options: {question['options']}")
        print(f"       Answer: {question['correct_answer']}")
    
    print("\n✅ Quiz System Demo Complete!")

def demo_progress_tracking():
    """Demonstrate progress tracking system"""
    print("\n📊 PROGRESS TRACKING DEMO")
    print("=" * 50)
    
    tracker = ProgressTracker()
    
    # Simulate some learning activities
    print("\n📈 Simulating Learning Activities...")
    tracker.update_progress("Demo User", "Mathematics", "chat_interaction", score=85, duration=15)
    tracker.update_progress("Demo User", "Mathematics", "quiz_completed", score=90, duration=10)
    tracker.update_progress("Demo User", "Physics", "chat_interaction", score=75, duration=20)
    
    # Get progress summary
    progress = tracker.get_progress_summary("Demo User")
    print("\n📋 Progress Summary:")
    for subject, percent in progress.items():
        print(f"   {subject}: {percent}%")
    
    # Get detailed analytics
    analytics = tracker.get_detailed_analytics("Demo User")
    print(f"\n📊 User Statistics:")
    print(f"   Total Sessions: {analytics['statistics']['total_sessions']}")
    print(f"   Questions Answered: {analytics['statistics']['questions_answered']}")
    print(f"   Current Streak: {analytics['statistics']['streak_days']} days")
    
    # Get insights
    insights = tracker.get_learning_insights("Demo User")
    print(f"\n💡 Learning Insights:")
    for insight in insights['insights'][:2]:  # Show first 2 insights
        print(f"   • {insight}")
    
    print("\n✅ Progress Tracking Demo Complete!")

def main():
    """Run complete demo"""
    print("🎓 AI TUTOR CHATBOT - COMPLETE DEMO")
    print("=" * 60)
    print("This demo showcases all the key features of the AI Tutor system.")
    print("In the actual application, these features work together seamlessly!")
    print()
    
    try:
        demo_ai_tutor()
        demo_subject_tools()
        demo_quiz_system()
        demo_progress_tracking()
        
        print("\n" + "=" * 60)
        print("🎉 DEMO COMPLETE!")
        print("To experience the full interactive application, run:")
        print("   python app.py")
        print("   or")
        print("   streamlit run app.py")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        print("Please ensure all dependencies are installed:")
        print("   pip install -r requirements.txt")

if __name__ == "__main__":
    main()
