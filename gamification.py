"""
Advanced Gamification System
Fire streaks, achievements, rewards, and engaging features to surpass GPT
"""

import streamlit as st
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Any, Optional
import json
from datetime import datetime, timedelta
import random

class GamificationEngine:
    """Advanced gamification system with streaks, achievements, and rewards"""
    
    def __init__(self):
        self.achievements = self._initialize_achievements()
        self.streak_types = ["daily_login", "consecutive_questions", "study_sessions", "perfect_scores"]
        self.xp_rewards = {
            "question_answered": 10,
            "quiz_completed": 50,
            "perfect_quiz": 100,
            "streak_milestone": 25,
            "achievement_unlocked": 75,
            "daily_login": 15,
            "study_session": 20,
            "code_explained": 30,
            "text_summarized": 20,
            "roadmap_completed": 200
        }
        self.level_thresholds = [0, 100, 300, 600, 1000, 1500, 2200, 3000, 4000, 5500, 7500, 10000]
    
    def _initialize_achievements(self) -> Dict[str, Dict]:
        """Initialize achievement system"""
        return {
            # Learning Achievements
            "first_question": {
                "name": "🌟 First Steps",
                "description": "Ask your first question",
                "category": "Beginner",
                "xp_reward": 25,
                "rarity": "Common"
            },
            "hundred_questions": {
                "name": "🎯 Curious Mind",
                "description": "Ask 100 questions",
                "category": "Learning",
                "xp_reward": 150,
                "rarity": "Rare"
            },
            "quiz_master": {
                "name": "🏆 Quiz Master",
                "description": "Complete 10 quizzes with 80%+ score",
                "category": "Assessment",
                "xp_reward": 200,
                "rarity": "Epic"
            },
            "perfect_week": {
                "name": "💎 Perfect Week",
                "description": "Maintain 7-day streak",
                "category": "Consistency",
                "xp_reward": 300,
                "rarity": "Legendary"
            },
            
            # Streak Achievements
            "fire_starter": {
                "name": "🔥 Fire Starter",
                "description": "Start your first streak",
                "category": "Streaks",
                "xp_reward": 50,
                "rarity": "Common"
            },
            "streak_warrior": {
                "name": "⚔️ Streak Warrior",
                "description": "Maintain 30-day streak",
                "category": "Streaks",
                "xp_reward": 500,
                "rarity": "Legendary"
            },
            "unstoppable": {
                "name": "🚀 Unstoppable",
                "description": "Maintain 100-day streak",
                "category": "Streaks",
                "xp_reward": 1000,
                "rarity": "Mythical"
            },
            
            # Subject Mastery
            "math_wizard": {
                "name": "🧙‍♂️ Math Wizard",
                "description": "Answer 50 math questions correctly",
                "category": "Subject Mastery",
                "xp_reward": 250,
                "rarity": "Epic"
            },
            "code_ninja": {
                "name": "🥷 Code Ninja",
                "description": "Explain 25 code snippets",
                "category": "Programming",
                "xp_reward": 250,
                "rarity": "Epic"
            },
            "science_explorer": {
                "name": "🔬 Science Explorer",
                "description": "Study 3 different science subjects",
                "category": "Exploration",
                "xp_reward": 200,
                "rarity": "Rare"
            },
            
            # Special Achievements
            "night_owl": {
                "name": "🦉 Night Owl",
                "description": "Study after 10 PM",
                "category": "Special",
                "xp_reward": 75,
                "rarity": "Uncommon"
            },
            "early_bird": {
                "name": "🐦 Early Bird",
                "description": "Study before 6 AM",
                "category": "Special",
                "xp_reward": 75,
                "rarity": "Uncommon"
            },
            "weekend_warrior": {
                "name": "⚡ Weekend Warrior",
                "description": "Study 5+ hours on weekend",
                "category": "Dedication",
                "xp_reward": 150,
                "rarity": "Rare"
            },
            
            # Advanced Achievements
            "ai_whisperer": {
                "name": "🤖 AI Whisperer",
                "description": "Use all AI features (chat, summarize, code, quiz)",
                "category": "Feature Explorer",
                "xp_reward": 300,
                "rarity": "Epic"
            },
            "knowledge_seeker": {
                "name": "📚 Knowledge Seeker",
                "description": "Explore 10 different topics",
                "category": "Exploration",
                "xp_reward": 200,
                "rarity": "Rare"
            },
            "tutor_champion": {
                "name": "👑 Tutor Champion",
                "description": "Reach level 10",
                "category": "Progression",
                "xp_reward": 500,
                "rarity": "Legendary"
            }
        }
    
    def get_user_stats(self, user_name: str) -> Dict[str, Any]:
        """Get comprehensive user statistics"""
        if not user_name:
            return {"error": "No user name provided"}
        
        # Initialize or load user data
        if 'user_stats' not in st.session_state:
            st.session_state.user_stats = {}
        
        if user_name not in st.session_state.user_stats:
            st.session_state.user_stats[user_name] = self._create_new_user_profile(user_name)
        
        return st.session_state.user_stats[user_name]
    
    def _create_new_user_profile(self, user_name: str) -> Dict[str, Any]:
        """Create new user profile with gamification data"""
        return {
            "name": user_name,
            "created_at": datetime.now().isoformat(),
            "last_active": datetime.now().isoformat(),
            "level": 1,
            "xp": 0,
            "total_xp": 0,
            "streaks": {
                "daily_login": 0,
                "consecutive_questions": 0,
                "study_sessions": 0,
                "perfect_scores": 0,
                "max_daily_login": 0,
                "max_consecutive_questions": 0,
                "max_study_sessions": 0,
                "max_perfect_scores": 0
            },
            "achievements": [],
            "statistics": {
                "questions_asked": 0,
                "quizzes_completed": 0,
                "perfect_quizzes": 0,
                "study_time_minutes": 0,
                "code_explanations": 0,
                "text_summaries": 0,
                "subjects_explored": [],
                "login_days": [],
                "favorite_subject": "General"
            },
            "badges": [],
            "rewards": [],
            "preferences": {
                "show_achievements": True,
                "show_streaks": True,
                "difficulty_preference": "Intermediate"
            }
        }
    
    def update_user_activity(self, user_name: str, activity_type: str, activity_data: Dict = None) -> Dict[str, Any]:
        """Update user activity and calculate rewards"""
        user_stats = self.get_user_stats(user_name)
        
        if "error" in user_stats:
            return user_stats
        
        rewards = {
            "xp_gained": 0,
            "achievements_unlocked": [],
            "streaks_updated": [],
            "level_up": False,
            "special_rewards": []
        }
        
        # Update statistics based on activity
        if activity_type == "question_answered":
            user_stats["statistics"]["questions_asked"] += 1
            rewards["xp_gained"] += self.xp_rewards["question_answered"]
            
            # Update consecutive questions streak
            user_stats["streaks"]["consecutive_questions"] += 1
            user_stats["streaks"]["max_consecutive_questions"] = max(
                user_stats["streaks"]["max_consecutive_questions"],
                user_stats["streaks"]["consecutive_questions"]
            )
            
        elif activity_type == "quiz_completed":
            user_stats["statistics"]["quizzes_completed"] += 1
            score = activity_data.get("score", 0) if activity_data else 0
            
            if score >= 100:
                user_stats["statistics"]["perfect_quizzes"] += 1
                user_stats["streaks"]["perfect_scores"] += 1
                rewards["xp_gained"] += self.xp_rewards["perfect_quiz"]
            else:
                user_stats["streaks"]["perfect_scores"] = 0  # Reset perfect score streak
                rewards["xp_gained"] += self.xp_rewards["quiz_completed"]
            
        elif activity_type == "daily_login":
            today = datetime.now().date().isoformat()
            if today not in user_stats["statistics"]["login_days"]:
                user_stats["statistics"]["login_days"].append(today)
                user_stats["streaks"]["daily_login"] += 1
                user_stats["streaks"]["max_daily_login"] = max(
                    user_stats["streaks"]["max_daily_login"],
                    user_stats["streaks"]["daily_login"]
                )
                rewards["xp_gained"] += self.xp_rewards["daily_login"]
        
        elif activity_type == "code_explained":
            user_stats["statistics"]["code_explanations"] += 1
            rewards["xp_gained"] += self.xp_rewards["code_explained"]
        
        elif activity_type == "text_summarized":
            user_stats["statistics"]["text_summaries"] += 1
            rewards["xp_gained"] += self.xp_rewards["text_summarized"]
        
        elif activity_type == "subject_explored":
            subject = activity_data.get("subject", "") if activity_data else ""
            if subject and subject not in user_stats["statistics"]["subjects_explored"]:
                user_stats["statistics"]["subjects_explored"].append(subject)
        
        # Check for achievements
        new_achievements = self._check_achievements(user_stats)
        for achievement in new_achievements:
            if achievement not in user_stats["achievements"]:
                user_stats["achievements"].append(achievement)
                rewards["achievements_unlocked"].append(achievement)
                rewards["xp_gained"] += self.achievements[achievement]["xp_reward"]
        
        # Update XP and level
        user_stats["xp"] += rewards["xp_gained"]
        user_stats["total_xp"] += rewards["xp_gained"]
        
        # Check for level up
        old_level = user_stats["level"]
        new_level = self._calculate_level(user_stats["total_xp"])
        
        if new_level > old_level:
            user_stats["level"] = new_level
            rewards["level_up"] = True
            rewards["special_rewards"].append(f"🎉 Level {new_level} Reached!")
        
        # Update last active
        user_stats["last_active"] = datetime.now().isoformat()
        
        # Check for streak milestones
        rewards["streaks_updated"] = self._check_streak_milestones(user_stats)
        
        # Save updated stats
        st.session_state.user_stats[user_name] = user_stats
        
        return rewards
    
    def _check_achievements(self, user_stats: Dict) -> List[str]:
        """Check for newly unlocked achievements"""
        new_achievements = []
        stats = user_stats["statistics"]
        streaks = user_stats["streaks"]
        
        # First question
        if stats["questions_asked"] >= 1 and "first_question" not in user_stats["achievements"]:
            new_achievements.append("first_question")
        
        # Hundred questions
        if stats["questions_asked"] >= 100 and "hundred_questions" not in user_stats["achievements"]:
            new_achievements.append("hundred_questions")
        
        # Quiz master
        if stats["perfect_quizzes"] >= 10 and "quiz_master" not in user_stats["achievements"]:
            new_achievements.append("quiz_master")
        
        # Fire starter
        if max(streaks.values()) >= 1 and "fire_starter" not in user_stats["achievements"]:
            new_achievements.append("fire_starter")
        
        # Perfect week
        if streaks["daily_login"] >= 7 and "perfect_week" not in user_stats["achievements"]:
            new_achievements.append("perfect_week")
        
        # Streak warrior
        if streaks["daily_login"] >= 30 and "streak_warrior" not in user_stats["achievements"]:
            new_achievements.append("streak_warrior")
        
        # Unstoppable
        if streaks["daily_login"] >= 100 and "unstoppable" not in user_stats["achievements"]:
            new_achievements.append("unstoppable")
        
        # Subject specific achievements
        if stats["questions_asked"] >= 50:  # Simplified check for math wizard
            if "math_wizard" not in user_stats["achievements"]:
                new_achievements.append("math_wizard")
        
        if stats["code_explanations"] >= 25 and "code_ninja" not in user_stats["achievements"]:
            new_achievements.append("code_ninja")
        
        if len(stats["subjects_explored"]) >= 3 and "science_explorer" not in user_stats["achievements"]:
            new_achievements.append("science_explorer")
        
        # Time-based achievements
        current_hour = datetime.now().hour
        if current_hour >= 22 or current_hour <= 2:
            if "night_owl" not in user_stats["achievements"]:
                new_achievements.append("night_owl")
        
        if current_hour <= 6:
            if "early_bird" not in user_stats["achievements"]:
                new_achievements.append("early_bird")
        
        # Advanced achievements
        features_used = sum([
            1 if stats["questions_asked"] > 0 else 0,
            1 if stats["text_summaries"] > 0 else 0,
            1 if stats["code_explanations"] > 0 else 0,
            1 if stats["quizzes_completed"] > 0 else 0
        ])
        
        if features_used >= 4 and "ai_whisperer" not in user_stats["achievements"]:
            new_achievements.append("ai_whisperer")
        
        if len(stats["subjects_explored"]) >= 10 and "knowledge_seeker" not in user_stats["achievements"]:
            new_achievements.append("knowledge_seeker")
        
        if user_stats["level"] >= 10 and "tutor_champion" not in user_stats["achievements"]:
            new_achievements.append("tutor_champion")
        
        return new_achievements
    
    def _calculate_level(self, total_xp: int) -> int:
        """Calculate user level based on total XP"""
        level = 1
        for threshold in self.level_thresholds:
            if total_xp >= threshold:
                level += 1
            else:
                break
        return min(level - 1, len(self.level_thresholds) - 1)
    
    def _check_streak_milestones(self, user_stats: Dict) -> List[str]:
        """Check for streak milestones"""
        milestones = []
        streaks = user_stats["streaks"]
        
        # Daily login milestones
        daily_streak = streaks["daily_login"]
        if daily_streak in [7, 14, 30, 50, 100]:
            milestones.append(f"🔥 {daily_streak}-day login streak!")
        
        # Consecutive questions milestones
        question_streak = streaks["consecutive_questions"]
        if question_streak in [10, 25, 50, 100]:
            milestones.append(f"🎯 {question_streak} questions in a row!")
        
        # Perfect scores milestones
        perfect_streak = streaks["perfect_scores"]
        if perfect_streak in [3, 5, 10]:
            milestones.append(f"💯 {perfect_streak} perfect scores in a row!")
        
        return milestones
    
    def get_leaderboard(self, category: str = "total_xp", limit: int = 10) -> List[Dict]:
        """Get leaderboard for different categories"""
        if 'user_stats' not in st.session_state:
            return []
        
        users = list(st.session_state.user_stats.values())
        
        if category == "total_xp":
            sorted_users = sorted(users, key=lambda x: x.get("total_xp", 0), reverse=True)
        elif category == "level":
            sorted_users = sorted(users, key=lambda x: x.get("level", 1), reverse=True)
        elif category == "streak":
            sorted_users = sorted(users, key=lambda x: x.get("streaks", {}).get("daily_login", 0), reverse=True)
        elif category == "achievements":
            sorted_users = sorted(users, key=lambda x: len(x.get("achievements", [])), reverse=True)
        else:
            sorted_users = users
        
        leaderboard = []
        for i, user in enumerate(sorted_users[:limit], 1):
            entry = {
                "rank": i,
                "name": user["name"],
                "level": user["level"],
                "total_xp": user["total_xp"],
                "achievements": len(user["achievements"]),
                "max_streak": max(user["streaks"].values()) if user["streaks"] else 0
            }
            leaderboard.append(entry)
        
        return leaderboard
    
    def generate_daily_challenge(self, user_stats: Dict) -> Dict[str, Any]:
        """Generate personalized daily challenge"""
        user_level = user_stats.get("level", 1)
        subjects_explored = user_stats.get("statistics", {}).get("subjects_explored", [])
        
        challenges = [
            {
                "title": "🎯 Question Marathon",
                "description": "Answer 5 questions in different subjects",
                "goal": 5,
                "type": "questions",
                "xp_reward": 100,
                "difficulty": "Medium"
            },
            {
                "title": "🧠 Code Explorer",
                "description": "Explain 3 different code snippets",
                "goal": 3,
                "type": "code_explanations",
                "xp_reward": 150,
                "difficulty": "Medium"
            },
            {
                "title": "📝 Summary Master",
                "description": "Summarize 2 long texts",
                "goal": 2,
                "type": "summaries",
                "xp_reward": 80,
                "difficulty": "Easy"
            },
            {
                "title": "🎓 Quiz Champion",
                "description": "Complete a quiz with 90%+ score",
                "goal": 1,
                "type": "perfect_quiz",
                "xp_reward": 200,
                "difficulty": "Hard"
            },
            {
                "title": "🌟 New Horizons",
                "description": "Explore a new subject area",
                "goal": 1,
                "type": "new_subject",
                "xp_reward": 120,
                "difficulty": "Medium"
            }
        ]
        
        # Select challenge based on user level and history
        available_challenges = challenges.copy()
        
        # Adjust difficulty based on user level
        if user_level < 3:
            available_challenges = [c for c in challenges if c["difficulty"] in ["Easy", "Medium"]]
        elif user_level > 7:
            # Add harder challenges for advanced users
            available_challenges.extend([
                {
                    "title": "🚀 AI Master",
                    "description": "Use all 4 AI features today",
                    "goal": 4,
                    "type": "feature_usage",
                    "xp_reward": 300,
                    "difficulty": "Expert"
                }
            ])
        
        # Select random challenge
        challenge = random.choice(available_challenges)
        challenge["expires_at"] = (datetime.now() + timedelta(days=1)).isoformat()
        challenge["progress"] = 0
        
        return challenge
    
    def get_motivational_message(self, user_stats: Dict, context: str = "general") -> str:
        """Generate motivational messages based on user progress"""
        level = user_stats.get("level", 1)
        streaks = user_stats.get("streaks", {})
        achievements = len(user_stats.get("achievements", []))
        
        messages = {
            "welcome": [
                "🎉 Welcome back, knowledge seeker! Ready to level up?",
                "🚀 Your learning journey continues! What will you discover today?",
                "💡 Every question brings you closer to mastery!",
                "🌟 Time to unlock new achievements and expand your mind!"
            ],
            "streak": [
                f"🔥 Amazing! You're on a {streaks.get('daily_login', 0)}-day streak!",
                "💪 Consistency is key to success - keep it up!",
                "⚡ Your dedication is inspiring! Don't break the chain!",
                "🎯 Every day you study, you're building unstoppable momentum!"
            ],
            "achievement": [
                f"🏆 Incredible! You've unlocked {achievements} achievements!",
                "👑 You're becoming a true learning champion!",
                "🌟 Your progress is outstanding - keep reaching for the stars!",
                "💎 Each achievement proves your dedication to growth!"
            ],
            "encouragement": [
                "🌱 Remember: every expert was once a beginner!",
                "💫 Challenges are opportunities in disguise!",
                "🚀 Your potential is limitless - keep exploring!",
                "🧠 Every question you ask makes you smarter!"
            ]
        }
        
        # Select appropriate message category
        if context == "login" and streaks.get("daily_login", 0) > 0:
            category = "streak"
        elif context == "achievement" or achievements > 5:
            category = "achievement"
        elif level > 5:
            category = "welcome"
        else:
            category = "encouragement"
        
        return random.choice(messages[category])
    
    def get_progress_insights(self, user_stats: Dict) -> Dict[str, Any]:
        """Generate personalized progress insights"""
        stats = user_stats.get("statistics", {})
        streaks = user_stats.get("streaks", {})
        level = user_stats.get("level", 1)
        
        insights = {
            "summary": "",
            "strengths": [],
            "areas_for_improvement": [],
            "recommendations": [],
            "next_milestone": ""
        }
        
        # Generate summary
        total_questions = stats.get("questions_asked", 0)
        total_achievements = len(user_stats.get("achievements", []))
        
        insights["summary"] = f"Level {level} learner with {total_questions} questions asked and {total_achievements} achievements unlocked!"
        
        # Identify strengths
        if streaks.get("daily_login", 0) >= 7:
            insights["strengths"].append("🔥 Excellent consistency with daily learning")
        
        if stats.get("perfect_quizzes", 0) > stats.get("quizzes_completed", 1) * 0.8:
            insights["strengths"].append("🎯 High quiz performance")
        
        if len(stats.get("subjects_explored", [])) >= 3:
            insights["strengths"].append("🌍 Great subject diversity")
        
        if stats.get("code_explanations", 0) > 10:
            insights["strengths"].append("💻 Strong programming focus")
        
        # Areas for improvement
        if streaks.get("daily_login", 0) < 3:
            insights["areas_for_improvement"].append("📅 Building consistent study habits")
        
        if stats.get("quizzes_completed", 0) < stats.get("questions_asked", 0) * 0.1:
            insights["areas_for_improvement"].append("📝 Taking more assessments")
        
        if len(stats.get("subjects_explored", [])) < 2:
            insights["areas_for_improvement"].append("🔍 Exploring different subjects")
        
        # Recommendations
        if level < 5:
            insights["recommendations"].append("🎯 Focus on daily engagement to reach Level 5")
        
        if stats.get("text_summaries", 0) < 5:
            insights["recommendations"].append("📄 Try the text summarization feature")
        
        if not stats.get("subjects_explored"):
            insights["recommendations"].append("🌟 Explore different subject areas")
        
        # Next milestone
        next_level_xp = self.level_thresholds[min(level, len(self.level_thresholds) - 1)]
        current_xp = user_stats.get("total_xp", 0)
        xp_needed = next_level_xp - current_xp
        
        if xp_needed > 0:
            insights["next_milestone"] = f"🎯 {xp_needed} XP needed for Level {level + 1}"
        else:
            insights["next_milestone"] = "🏆 Maximum level achieved!"
        
        return insights
