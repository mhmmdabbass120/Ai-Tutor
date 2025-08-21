import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple
import pandas as pd
import numpy as np

class ProgressTracker:
    """Advanced progress tracking system for personalized learning analytics"""
    
    def __init__(self, data_file: str = "user_progress.json"):
        self.data_file = data_file
        self.progress_data = self._load_progress_data()
        
    def _load_progress_data(self) -> Dict[str, Any]:
        """Load progress data from file or create new structure"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        
        return {
            "users": {},
            "global_stats": {
                "total_interactions": 0,
                "subjects_studied": [],
                "average_session_length": 0
            }
        }
    
    def _save_progress_data(self):
        """Save progress data to file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.progress_data, f, indent=2, default=str)
        except Exception as e:
            print(f"Warning: Could not save progress data: {e}")
    
    def update_progress(self, user_name: str, subject: str, activity_type: str, 
                       score: float = None, duration: int = None, details: Dict = None):
        """Update user progress with detailed tracking"""
        if not user_name:
            return
        
        timestamp = datetime.now().isoformat()
        
        # Initialize user data if needed
        if user_name not in self.progress_data["users"]:
            self.progress_data["users"][user_name] = {
                "profile": {
                    "name": user_name,
                    "join_date": timestamp,
                    "level": "Beginner",
                    "preferred_subjects": []
                },
                "activity_log": [],
                "subject_progress": {},
                "achievements": [],
                "statistics": {
                    "total_sessions": 0,
                    "total_time_spent": 0,
                    "questions_answered": 0,
                    "correct_answers": 0,
                    "streak_days": 0,
                    "last_activity": timestamp
                }
            }
        
        user_data = self.progress_data["users"][user_name]
        
        # Update activity log
        activity_entry = {
            "timestamp": timestamp,
            "subject": subject,
            "activity_type": activity_type,
            "score": score,
            "duration": duration,
            "details": details or {}
        }
        user_data["activity_log"].append(activity_entry)
        
        # Update subject progress
        if subject not in user_data["subject_progress"]:
            user_data["subject_progress"][subject] = {
                "total_interactions": 0,
                "average_score": 0,
                "time_spent": 0,
                "topics_covered": [],
                "difficulty_progress": {"Beginner": 0, "Intermediate": 0, "Advanced": 0},
                "last_activity": timestamp
            }
        
        subject_progress = user_data["subject_progress"][subject]
        subject_progress["total_interactions"] += 1
        subject_progress["last_activity"] = timestamp
        
        if duration:
            subject_progress["time_spent"] += duration
            user_data["statistics"]["total_time_spent"] += duration
        
        if score is not None:
            # Update average score
            current_avg = subject_progress["average_score"]
            total_interactions = subject_progress["total_interactions"]
            subject_progress["average_score"] = (current_avg * (total_interactions - 1) + score) / total_interactions
            
            user_data["statistics"]["questions_answered"] += 1
            if score >= 70:  # Consider 70% as correct
                user_data["statistics"]["correct_answers"] += 1
        
        # Update session count
        user_data["statistics"]["total_sessions"] += 1
        user_data["statistics"]["last_activity"] = timestamp
        
        # Check for achievements
        self._check_achievements(user_name)
        
        # Update streak
        self._update_streak(user_name)
        
        # Update global stats
        self.progress_data["global_stats"]["total_interactions"] += 1
        if subject not in self.progress_data["global_stats"]["subjects_studied"]:
            self.progress_data["global_stats"]["subjects_studied"].append(subject)
        
        self._save_progress_data()
    
    def get_progress_summary(self, user_name: str) -> Dict[str, Any]:
        """Get comprehensive progress summary for a user"""
        if user_name not in self.progress_data["users"]:
            return {subject: 0 for subject in ["Mathematics", "Physics", "Chemistry", "Biology", "Computer Science"]}
        
        user_data = self.progress_data["users"][user_name]
        subject_progress = user_data["subject_progress"]
        
        summary = {}
        
        for subject in ["Mathematics", "Physics", "Chemistry", "Biology", "Computer Science"]:
            if subject in subject_progress:
                # Calculate progress percentage based on interactions and performance
                interactions = subject_progress[subject]["total_interactions"]
                avg_score = subject_progress[subject]["average_score"]
                
                # Progress formula: base progress from interactions + bonus from performance
                base_progress = min(interactions * 5, 70)  # 5% per interaction, max 70%
                performance_bonus = min(avg_score * 0.3, 30)  # Up to 30% bonus from good performance
                
                total_progress = min(base_progress + performance_bonus, 100)
                summary[subject] = int(total_progress)
            else:
                summary[subject] = 0
        
        return summary
    
    def get_detailed_analytics(self, user_name: str) -> Dict[str, Any]:
        """Get detailed analytics for a user"""
        if user_name not in self.progress_data["users"]:
            return {"error": "User not found"}
        
        user_data = self.progress_data["users"][user_name]
        
        # Calculate trends
        activity_log = user_data["activity_log"]
        recent_activities = [a for a in activity_log if self._is_recent(a["timestamp"], days=7)]
        
        # Performance trends
        scores_over_time = [(a["timestamp"], a["score"]) for a in activity_log if a["score"] is not None]
        
        # Subject distribution
        subject_counts = {}
        for activity in activity_log:
            subject = activity["subject"]
            subject_counts[subject] = subject_counts.get(subject, 0) + 1
        
        # Learning streaks
        streak_data = self._calculate_learning_streaks(user_name)
        
        # Recommendations
        recommendations = self._generate_recommendations(user_name)
        
        return {
            "user_profile": user_data["profile"],
            "statistics": user_data["statistics"],
            "recent_activity": {
                "sessions_this_week": len(recent_activities),
                "subjects_this_week": len(set(a["subject"] for a in recent_activities))
            },
            "performance_trends": {
                "scores_over_time": scores_over_time[-10:],  # Last 10 scores
                "average_improvement": self._calculate_improvement_trend(scores_over_time)
            },
            "subject_distribution": subject_counts,
            "learning_streaks": streak_data,
            "achievements": user_data["achievements"],
            "recommendations": recommendations
        }
    
    def get_learning_insights(self, user_name: str) -> Dict[str, Any]:
        """Generate learning insights and suggestions"""
        if user_name not in self.progress_data["users"]:
            return {"insights": ["Start learning to get personalized insights!"]}
        
        user_data = self.progress_data["users"][user_name]
        insights = []
        
        # Analyze learning patterns
        activity_log = user_data["activity_log"]
        if len(activity_log) > 5:
            # Time of day analysis
            activity_hours = [datetime.fromisoformat(a["timestamp"]).hour for a in activity_log]
            most_active_hour = max(set(activity_hours), key=activity_hours.count)
            insights.append(f"You're most active at {most_active_hour}:00. Consider scheduling study sessions around this time.")
            
            # Subject performance analysis
            subject_scores = {}
            for activity in activity_log:
                if activity["score"] is not None:
                    subject = activity["subject"]
                    if subject not in subject_scores:
                        subject_scores[subject] = []
                    subject_scores[subject].append(activity["score"])
            
            best_subject = max(subject_scores.keys(), key=lambda s: np.mean(subject_scores[s])) if subject_scores else None
            worst_subject = min(subject_scores.keys(), key=lambda s: np.mean(subject_scores[s])) if subject_scores else None
            
            if best_subject:
                insights.append(f"You excel in {best_subject}! Your average score is {np.mean(subject_scores[best_subject]):.1f}%")
            
            if worst_subject and len(subject_scores) > 1:
                insights.append(f"Consider spending more time on {worst_subject} to improve your {np.mean(subject_scores[worst_subject]):.1f}% average")
            
            # Learning frequency analysis
            dates = [datetime.fromisoformat(a["timestamp"]).date() for a in activity_log]
            unique_dates = len(set(dates))
            total_days = (max(dates) - min(dates)).days + 1 if len(dates) > 1 else 1
            frequency = unique_dates / total_days
            
            if frequency > 0.7:
                insights.append("Great consistency! You study regularly.")
            elif frequency > 0.3:
                insights.append("Good learning rhythm. Try to maintain regular study sessions.")
            else:
                insights.append("Consider studying more regularly for better retention.")
        
        # Progress insights
        total_sessions = user_data["statistics"]["total_sessions"]
        if total_sessions >= 10:
            insights.append(f"You've completed {total_sessions} learning sessions - great dedication!")
        
        if user_data["statistics"]["streak_days"] > 3:
            insights.append(f"Fantastic! You're on a {user_data['statistics']['streak_days']}-day learning streak!")
        
        return {"insights": insights}
    
    def _is_recent(self, timestamp: str, days: int = 7) -> bool:
        """Check if timestamp is within recent days"""
        try:
            activity_date = datetime.fromisoformat(timestamp)
            return datetime.now() - activity_date <= timedelta(days=days)
        except:
            return False
    
    def _calculate_learning_streaks(self, user_name: str) -> Dict[str, Any]:
        """Calculate learning streaks for a user"""
        user_data = self.progress_data["users"][user_name]
        activity_log = user_data["activity_log"]
        
        # Get unique activity dates
        dates = sorted(set(datetime.fromisoformat(a["timestamp"]).date() for a in activity_log))
        
        if not dates:
            return {"current_streak": 0, "longest_streak": 0, "total_active_days": 0}
        
        # Calculate current streak
        current_streak = 0
        today = datetime.now().date()
        
        for i in range(len(dates)):
            date = dates[-(i+1)]  # Start from most recent
            expected_date = today - timedelta(days=i)
            
            if date == expected_date:
                current_streak += 1
            else:
                break
        
        # Calculate longest streak
        longest_streak = 0
        current_consecutive = 1
        
        for i in range(1, len(dates)):
            if dates[i] - dates[i-1] == timedelta(days=1):
                current_consecutive += 1
                longest_streak = max(longest_streak, current_consecutive)
            else:
                current_consecutive = 1
        
        return {
            "current_streak": current_streak,
            "longest_streak": max(longest_streak, current_streak),
            "total_active_days": len(dates)
        }
    
    def _calculate_improvement_trend(self, scores_over_time: List[Tuple[str, float]]) -> float:
        """Calculate improvement trend from scores over time"""
        if len(scores_over_time) < 3:
            return 0.0
        
        scores = [score for _, score in scores_over_time]
        
        # Simple linear trend calculation
        n = len(scores)
        x = list(range(n))
        
        # Calculate slope of trend line
        x_mean = sum(x) / n
        y_mean = sum(scores) / n
        
        numerator = sum((x[i] - x_mean) * (scores[i] - y_mean) for i in range(n))
        denominator = sum((x[i] - x_mean) ** 2 for i in range(n))
        
        if denominator == 0:
            return 0.0
        
        slope = numerator / denominator
        return slope
    
    def _update_streak(self, user_name: str):
        """Update learning streak for user"""
        user_data = self.progress_data["users"][user_name]
        activity_log = user_data["activity_log"]
        
        if not activity_log:
            return
        
        # Get dates of activities
        dates = [datetime.fromisoformat(a["timestamp"]).date() for a in activity_log]
        unique_dates = sorted(set(dates))
        
        # Calculate current streak
        streak = 0
        today = datetime.now().date()
        
        for i in range(len(unique_dates)):
            date = unique_dates[-(i+1)]
            expected_date = today - timedelta(days=i)
            
            if date == expected_date:
                streak += 1
            else:
                break
        
        user_data["statistics"]["streak_days"] = streak
    
    def _check_achievements(self, user_name: str):
        """Check and award achievements"""
        user_data = self.progress_data["users"][user_name]
        stats = user_data["statistics"]
        current_achievements = set(a["type"] for a in user_data["achievements"])
        
        new_achievements = []
        
        # Session-based achievements
        if stats["total_sessions"] >= 5 and "first_milestone" not in current_achievements:
            new_achievements.append({
                "type": "first_milestone",
                "title": "Getting Started",
                "description": "Completed 5 learning sessions",
                "date": datetime.now().isoformat()
            })
        
        if stats["total_sessions"] >= 20 and "dedicated_learner" not in current_achievements:
            new_achievements.append({
                "type": "dedicated_learner",
                "title": "Dedicated Learner",
                "description": "Completed 20 learning sessions",
                "date": datetime.now().isoformat()
            })
        
        # Streak-based achievements
        if stats["streak_days"] >= 7 and "week_warrior" not in current_achievements:
            new_achievements.append({
                "type": "week_warrior",
                "title": "Week Warrior",
                "description": "7-day learning streak",
                "date": datetime.now().isoformat()
            })
        
        # Accuracy-based achievements
        if stats["questions_answered"] > 0:
            accuracy = stats["correct_answers"] / stats["questions_answered"]
            if accuracy >= 0.9 and stats["questions_answered"] >= 10 and "accuracy_expert" not in current_achievements:
                new_achievements.append({
                    "type": "accuracy_expert",
                    "title": "Accuracy Expert",
                    "description": "90%+ accuracy on 10+ questions",
                    "date": datetime.now().isoformat()
                })
        
        # Subject diversity achievements
        subjects_studied = len(user_data["subject_progress"])
        if subjects_studied >= 3 and "multi_subject" not in current_achievements:
            new_achievements.append({
                "type": "multi_subject",
                "title": "Renaissance Learner",
                "description": "Studied 3 different subjects",
                "date": datetime.now().isoformat()
            })
        
        user_data["achievements"].extend(new_achievements)
    
    def _generate_recommendations(self, user_name: str) -> List[str]:
        """Generate personalized learning recommendations"""
        user_data = self.progress_data["users"][user_name]
        recommendations = []
        
        # Analyze recent activity
        recent_activities = [
            a for a in user_data["activity_log"] 
            if self._is_recent(a["timestamp"], days=7)
        ]
        
        if len(recent_activities) == 0:
            recommendations.append("Start a learning session today to get back on track!")
            return recommendations
        
        # Subject recommendations
        subject_scores = {}
        for activity in recent_activities:
            if activity["score"] is not None:
                subject = activity["subject"]
                if subject not in subject_scores:
                    subject_scores[subject] = []
                subject_scores[subject].append(activity["score"])
        
        # Find subjects needing improvement
        for subject, scores in subject_scores.items():
            avg_score = sum(scores) / len(scores)
            if avg_score < 70:
                recommendations.append(f"Focus on {subject} - your recent average is {avg_score:.1f}%")
        
        # Streak recommendations
        if user_data["statistics"]["streak_days"] == 0:
            recommendations.append("Start a new learning streak - consistency is key to progress!")
        elif user_data["statistics"]["streak_days"] < 3:
            recommendations.append("Keep going! Try to build a longer learning streak.")
        
        # Frequency recommendations
        if len(recent_activities) < 3:
            recommendations.append("Try to study more regularly - aim for at least 3 sessions per week.")
        
        # Achievement recommendations
        sessions = user_data["statistics"]["total_sessions"]
        if sessions < 5:
            recommendations.append("Complete a few more sessions to unlock your first achievement!")
        
        if not recommendations:
            recommendations.append("You're doing great! Keep up the excellent learning habits!")
        
        return recommendations
    
    def export_progress_report(self, user_name: str) -> str:
        """Export detailed progress report"""
        if user_name not in self.progress_data["users"]:
            return "User not found"
        
        user_data = self.progress_data["users"][user_name]
        analytics = self.get_detailed_analytics(user_name)
        insights = self.get_learning_insights(user_name)
        
        report = f"""
=== LEARNING PROGRESS REPORT ===
User: {user_name}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

STATISTICS:
- Total Sessions: {user_data['statistics']['total_sessions']}
- Questions Answered: {user_data['statistics']['questions_answered']}
- Accuracy: {(user_data['statistics']['correct_answers'] / max(user_data['statistics']['questions_answered'], 1) * 100):.1f}%
- Current Streak: {user_data['statistics']['streak_days']} days
- Time Spent: {user_data['statistics']['total_time_spent']} minutes

SUBJECT PROGRESS:
"""
        
        for subject, progress in user_data["subject_progress"].items():
            report += f"- {subject}: {progress['total_interactions']} sessions, {progress['average_score']:.1f}% avg score\n"
        
        report += f"\nACHIEVEMENTS ({len(user_data['achievements'])}):\n"
        for achievement in user_data["achievements"]:
            report += f"- {achievement['title']}: {achievement['description']}\n"
        
        report += f"\nINSIGHTS:\n"
        for insight in insights["insights"]:
            report += f"- {insight}\n"
        
        report += f"\nRECOMMENDATIONS:\n"
        for rec in analytics["recommendations"]:
            report += f"- {rec}\n"
        
        return report
