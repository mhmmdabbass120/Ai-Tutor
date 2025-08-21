"""
Comprehensive Educational Resource Database
Real learning resources from trusted sources including YouTube, online courses, PDFs, and more
"""

import streamlit as st
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Any, Optional
import random
from datetime import datetime
import json

class EducationalResourceDatabase:
    """Comprehensive database of educational resources from trusted sources"""
    
    def __init__(self):
        self.resources = self._initialize_resource_database()
        self.platforms = {
            "YouTube": "🎥",
            "Khan Academy": "🎓",
            "Coursera": "📚",
            "edX": "🏛️",
            "MIT OpenCourseWare": "🔬",
            "Stanford Online": "🌟",
            "Udemy": "💻",
            "FreeCodeCamp": "⚡",
            "Brilliant": "💡",
            "Archive.org": "📖",
            "ArXiv": "📄",
            "Google Scholar": "🔍"
        }
    
    def _initialize_resource_database(self) -> Dict[str, Dict[str, List[Dict]]]:
        """Initialize the comprehensive resource database"""
        return {
            "Mathematics": {
                "Beginner": [
                    {
                        "title": "Basic Math - Khan Academy",
                        "platform": "Khan Academy",
                        "type": "Course",
                        "url": "https://www.khanacademy.org/math/basic-geo",
                        "description": "Comprehensive basic mathematics covering arithmetic, algebra basics, and geometry",
                        "duration": "40 hours",
                        "rating": 4.9,
                        "prerequisites": "None"
                    },
                    {
                        "title": "Algebra Basics - Professor Leonard",
                        "platform": "YouTube",
                        "type": "Video Series",
                        "url": "https://youtube.com/playlist?list=PLC292123722B1B450",
                        "description": "Complete algebra course from basic concepts to advanced topics",
                        "duration": "50+ videos",
                        "rating": 4.8,
                        "prerequisites": "Basic arithmetic"
                    },
                    {
                        "title": "Elementary Mathematics - MIT OpenCourseWare",
                        "platform": "MIT OpenCourseWare",
                        "type": "Course Materials",
                        "url": "https://ocw.mit.edu/courses/mathematics/",
                        "description": "Free course materials from MIT mathematics courses",
                        "duration": "Self-paced",
                        "rating": 4.9,
                        "prerequisites": "High school math"
                    }
                ],
                "Intermediate": [
                    {
                        "title": "Calculus - 3Blue1Brown",
                        "platform": "YouTube",
                        "type": "Video Series",
                        "url": "https://youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr",
                        "description": "Essence of Calculus - intuitive explanations of calculus concepts",
                        "duration": "20 videos",
                        "rating": 4.9,
                        "prerequisites": "Algebra, trigonometry"
                    },
                    {
                        "title": "Linear Algebra - Khan Academy",
                        "platform": "Khan Academy",
                        "type": "Course",
                        "url": "https://www.khanacademy.org/math/linear-algebra",
                        "description": "Complete linear algebra course with interactive exercises",
                        "duration": "35 hours",
                        "rating": 4.7,
                        "prerequisites": "Algebra II"
                    },
                    {
                        "title": "Introduction to Mathematical Thinking - Stanford",
                        "platform": "Coursera",
                        "type": "Course",
                        "url": "https://www.coursera.org/learn/mathematical-thinking",
                        "description": "Learn to think mathematically and develop problem-solving skills",
                        "duration": "10 weeks",
                        "rating": 4.6,
                        "prerequisites": "High school algebra"
                    }
                ],
                "Advanced": [
                    {
                        "title": "Real Analysis - Harvard Extension",
                        "platform": "YouTube",
                        "type": "Lecture Series",
                        "url": "https://youtube.com/playlist?list=PL0E754696F72137EC",
                        "description": "Complete real analysis course covering limits, continuity, derivatives",
                        "duration": "40+ lectures",
                        "rating": 4.8,
                        "prerequisites": "Calculus I-III, proof techniques"
                    },
                    {
                        "title": "Abstract Algebra - MIT OpenCourseWare",
                        "platform": "MIT OpenCourseWare",
                        "type": "Course",
                        "url": "https://ocw.mit.edu/courses/18-703-modern-algebra-spring-2013/",
                        "description": "Groups, rings, fields, and Galois theory",
                        "duration": "1 semester",
                        "rating": 4.7,
                        "prerequisites": "Linear algebra, proof techniques"
                    }
                ]
            },
            "Physics": {
                "Beginner": [
                    {
                        "title": "Physics - Khan Academy",
                        "platform": "Khan Academy",
                        "type": "Course",
                        "url": "https://www.khanacademy.org/science/physics",
                        "description": "Comprehensive physics covering mechanics, waves, thermodynamics",
                        "duration": "60 hours",
                        "rating": 4.8,
                        "prerequisites": "Basic algebra"
                    },
                    {
                        "title": "Physics for Scientists and Engineers - Walter Lewin",
                        "platform": "YouTube",
                        "type": "Lecture Series",
                        "url": "https://youtube.com/playlist?list=PLyQSN7X0ro203puVhQsmCj9qhlFQ-As8e",
                        "description": "Complete physics course with engaging demonstrations",
                        "duration": "35+ lectures",
                        "rating": 4.9,
                        "prerequisites": "Calculus recommended"
                    },
                    {
                        "title": "Conceptual Physics - Paul Hewitt",
                        "platform": "Archive.org",
                        "type": "Textbook PDF",
                        "url": "https://archive.org/details/ConceptualPhysics_201907",
                        "description": "Free PDF of the classic conceptual physics textbook",
                        "duration": "Self-paced",
                        "rating": 4.6,
                        "prerequisites": "Basic math"
                    }
                ],
                "Intermediate": [
                    {
                        "title": "Classical Mechanics - MIT 8.01x",
                        "platform": "edX",
                        "type": "Course",
                        "url": "https://www.edx.org/course/introduction-to-mechanics",
                        "description": "Rigorous introduction to Newtonian mechanics",
                        "duration": "13 weeks",
                        "rating": 4.7,
                        "prerequisites": "Calculus I"
                    },
                    {
                        "title": "Electromagnetism - MIT OpenCourseWare",
                        "platform": "MIT OpenCourseWare",
                        "type": "Course",
                        "url": "https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/",
                        "description": "Complete E&M course with problem sets and solutions",
                        "duration": "1 semester",
                        "rating": 4.8,
                        "prerequisites": "Classical mechanics, vector calculus"
                    }
                ],
                "Advanced": [
                    {
                        "title": "Quantum Mechanics - MIT 8.04",
                        "platform": "MIT OpenCourseWare",
                        "type": "Course",
                        "url": "https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/",
                        "description": "Introduction to quantum mechanics with Schrödinger equation",
                        "duration": "1 semester",
                        "rating": 4.9,
                        "prerequisites": "Classical mechanics, linear algebra"
                    },
                    {
                        "title": "Relativity - Stanford",
                        "platform": "YouTube",
                        "type": "Lecture Series",
                        "url": "https://youtube.com/playlist?list=PLoaVOjvkzQtyjhV55wZcdicAz5KexgKvm",
                        "description": "Special and general relativity by Leonard Susskind",
                        "duration": "12+ lectures",
                        "rating": 4.8,
                        "prerequisites": "Classical mechanics, calculus"
                    }
                ]
            },
            "Computer Science": {
                "Beginner": [
                    {
                        "title": "CS50: Introduction to Computer Science - Harvard",
                        "platform": "edX",
                        "type": "Course",
                        "url": "https://www.edx.org/course/introduction-computer-science-harvardx-cs50x",
                        "description": "World-famous introduction to computer science and programming",
                        "duration": "12 weeks",
                        "rating": 4.9,
                        "prerequisites": "None"
                    },
                    {
                        "title": "Python Programming - FreeCodeCamp",
                        "platform": "YouTube",
                        "type": "Course",
                        "url": "https://youtube.com/watch?v=rfscVS0vtbw",
                        "description": "Complete Python course for beginners (4+ hours)",
                        "duration": "4.5 hours",
                        "rating": 4.8,
                        "prerequisites": "None"
                    },
                    {
                        "title": "The Structure and Interpretation of Computer Programs",
                        "platform": "Archive.org",
                        "type": "Textbook PDF",
                        "url": "https://archive.org/details/structureandinterpretationofcomputerprograms",
                        "description": "Classic CS textbook (SICP) available as free PDF",
                        "duration": "Self-paced",
                        "rating": 4.7,
                        "prerequisites": "Basic programming"
                    }
                ],
                "Intermediate": [
                    {
                        "title": "Data Structures and Algorithms - MIT 6.006",
                        "platform": "MIT OpenCourseWare",
                        "type": "Course",
                        "url": "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/",
                        "description": "Complete algorithms course with video lectures",
                        "duration": "1 semester",
                        "rating": 4.8,
                        "prerequisites": "Programming experience"
                    },
                    {
                        "title": "Machine Learning - Andrew Ng",
                        "platform": "Coursera",
                        "type": "Course",
                        "url": "https://www.coursera.org/learn/machine-learning",
                        "description": "Most popular machine learning course online",
                        "duration": "11 weeks",
                        "rating": 4.9,
                        "prerequisites": "Linear algebra, programming"
                    }
                ],
                "Advanced": [
                    {
                        "title": "Deep Learning Specialization - Andrew Ng",
                        "platform": "Coursera",
                        "type": "Specialization",
                        "url": "https://www.coursera.org/specializations/deep-learning",
                        "description": "5-course specialization on deep learning and neural networks",
                        "duration": "4 months",
                        "rating": 4.8,
                        "prerequisites": "Machine learning basics"
                    },
                    {
                        "title": "Algorithms: Design and Analysis - Stanford",
                        "platform": "Coursera",
                        "type": "Course",
                        "url": "https://www.coursera.org/learn/algorithms-divide-conquer",
                        "description": "Advanced algorithms with mathematical analysis",
                        "duration": "4 weeks",
                        "rating": 4.7,
                        "prerequisites": "Data structures, discrete math"
                    }
                ]
            },
            "Biology": {
                "Beginner": [
                    {
                        "title": "Biology - Khan Academy",
                        "platform": "Khan Academy",
                        "type": "Course",
                        "url": "https://www.khanacademy.org/science/biology",
                        "description": "Complete biology course from cells to ecosystems",
                        "duration": "50 hours",
                        "rating": 4.8,
                        "prerequisites": "Basic chemistry"
                    },
                    {
                        "title": "Campbell Biology - OpenStax",
                        "platform": "Archive.org",
                        "type": "Textbook PDF",
                        "url": "https://archive.org/details/Campbell_Biology_11th_Edition",
                        "description": "Free access to comprehensive biology textbook",
                        "duration": "Self-paced",
                        "rating": 4.7,
                        "prerequisites": "High school chemistry"
                    }
                ],
                "Intermediate": [
                    {
                        "title": "Molecular Biology - MIT 7.28",
                        "platform": "MIT OpenCourseWare",
                        "type": "Course",
                        "url": "https://ocw.mit.edu/courses/7-28-molecular-biology-spring-2005/",
                        "description": "Advanced molecular biology with current research",
                        "duration": "1 semester",
                        "rating": 4.8,
                        "prerequisites": "General biology, organic chemistry"
                    },
                    {
                        "title": "Genetics - University of British Columbia",
                        "platform": "YouTube",
                        "type": "Lecture Series",
                        "url": "https://youtube.com/playlist?list=PLM8wYQRetTxBkdvBtz-gw8b9lcVkdXQKV",
                        "description": "Complete genetics course with modern techniques",
                        "duration": "30+ lectures",
                        "rating": 4.6,
                        "prerequisites": "General biology"
                    }
                ],
                "Advanced": [
                    {
                        "title": "Biochemistry - Harvard Extension",
                        "platform": "YouTube",
                        "type": "Lecture Series",
                        "url": "https://youtube.com/playlist?list=PL0o_zxa4K1BWziAvOKdqsMFSB_MyyLAqS",
                        "description": "Advanced biochemistry covering protein structure and function",
                        "duration": "20+ lectures",
                        "rating": 4.9,
                        "prerequisites": "Organic chemistry, cell biology"
                    }
                ]
            },
            "Chemistry": {
                "Beginner": [
                    {
                        "title": "General Chemistry - Khan Academy",
                        "platform": "Khan Academy",
                        "type": "Course",
                        "url": "https://www.khanacademy.org/science/chemistry",
                        "description": "Complete general chemistry course with practice problems",
                        "duration": "45 hours",
                        "rating": 4.7,
                        "prerequisites": "Basic math"
                    },
                    {
                        "title": "Chemistry: A Molecular Approach - Tro",
                        "platform": "Archive.org",
                        "type": "Textbook PDF",
                        "url": "https://archive.org/details/chemistry-molecular-approach-tro",
                        "description": "Comprehensive general chemistry textbook",
                        "duration": "Self-paced",
                        "rating": 4.6,
                        "prerequisites": "High school math"
                    }
                ],
                "Intermediate": [
                    {
                        "title": "Organic Chemistry - Yale",
                        "platform": "YouTube",
                        "type": "Lecture Series",
                        "url": "https://youtube.com/playlist?list=PL0o_zxa4K1BXP7PeWOz5m1d0PgMgYp3Ky",
                        "description": "Complete organic chemistry course by Professor McBride",
                        "duration": "36 lectures",
                        "rating": 4.8,
                        "prerequisites": "General chemistry"
                    }
                ],
                "Advanced": [
                    {
                        "title": "Physical Chemistry - MIT OpenCourseWare",
                        "platform": "MIT OpenCourseWare",
                        "type": "Course",
                        "url": "https://ocw.mit.edu/courses/5-61-physical-chemistry-fall-2007/",
                        "description": "Thermodynamics and kinetics for chemistry",
                        "duration": "1 semester",
                        "rating": 4.7,
                        "prerequisites": "Calculus, general chemistry"
                    }
                ]
            }
        }
    
    def get_resources_by_subject_level(self, subject: str, level: str) -> List[Dict]:
        """Get resources for a specific subject and level"""
        return self.resources.get(subject, {}).get(level, [])
    
    def get_all_subjects(self) -> List[str]:
        """Get list of all available subjects"""
        return list(self.resources.keys())
    
    def search_resources(self, query: str, subject: str = None, level: str = None) -> List[Dict]:
        """Search resources by query"""
        results = []
        search_subjects = [subject] if subject else self.resources.keys()
        
        for subj in search_subjects:
            search_levels = [level] if level else self.resources[subj].keys()
            for lvl in search_levels:
                for resource in self.resources[subj][lvl]:
                    if (query.lower() in resource['title'].lower() or 
                        query.lower() in resource['description'].lower()):
                        resource['subject'] = subj
                        resource['level'] = lvl
                        results.append(resource)
        
        return results
    
    def get_platform_icon(self, platform: str) -> str:
        """Get icon for platform"""
        return self.platforms.get(platform, "🔗")
    
    def get_recommended_resources(self, subject: str, level: str, num_resources: int = 3) -> List[Dict]:
        """Get top recommended resources for subject and level"""
        resources = self.get_resources_by_subject_level(subject, level)
        # Sort by rating and return top N
        sorted_resources = sorted(resources, key=lambda x: x.get('rating', 0), reverse=True)
        return sorted_resources[:num_resources]

class LearningPathGenerator:
    """Generate comprehensive learning paths with real resources"""
    
    def __init__(self, resource_db: EducationalResourceDatabase):
        self.resource_db = resource_db
        self.learning_paths = self._initialize_learning_paths()
    
    def _initialize_learning_paths(self) -> Dict[str, Dict]:
        """Initialize comprehensive learning path templates"""
        return {
            "Mathematics": {
                "Complete Mathematics Journey": {
                    "description": "From basic arithmetic to advanced mathematics",
                    "duration": "2-3 years",
                    "phases": [
                        {
                            "phase": "Foundation (Months 1-6)",
                            "topics": [
                                "Basic Arithmetic & Number Theory",
                                "Pre-Algebra & Algebraic Thinking",
                                "Geometry Fundamentals",
                                "Basic Statistics & Probability"
                            ],
                            "level": "Beginner",
                            "skills": ["Problem-solving", "Logical reasoning", "Pattern recognition"],
                            "assessments": ["Weekly practice problems", "Monthly progress tests"]
                        },
                        {
                            "phase": "Intermediate (Months 7-18)",
                            "topics": [
                                "Algebra I & II",
                                "Trigonometry",
                                "Precalculus",
                                "Introduction to Calculus"
                            ],
                            "level": "Intermediate",
                            "skills": ["Abstract thinking", "Function analysis", "Graphical interpretation"],
                            "assessments": ["Project-based assignments", "Peer problem-solving"]
                        },
                        {
                            "phase": "Advanced (Months 19-36)",
                            "topics": [
                                "Calculus I, II, III",
                                "Linear Algebra",
                                "Differential Equations",
                                "Real Analysis or Abstract Algebra"
                            ],
                            "level": "Advanced",
                            "skills": ["Proof techniques", "Mathematical rigor", "Research methods"],
                            "assessments": ["Research projects", "Proof writing", "Independent study"]
                        }
                    ]
                }
            },
            "Computer Science": {
                "Software Developer Path": {
                    "description": "From programming basics to software engineering",
                    "duration": "12-18 months",
                    "phases": [
                        {
                            "phase": "Programming Fundamentals (Months 1-4)",
                            "topics": [
                                "Programming Basics (Python/Java)",
                                "Data Types & Control Structures",
                                "Functions & Object-Oriented Programming",
                                "Basic Data Structures"
                            ],
                            "level": "Beginner",
                            "skills": ["Problem decomposition", "Code debugging", "Algorithm design"],
                            "assessments": ["Coding exercises", "Small projects", "Code reviews"]
                        },
                        {
                            "phase": "Core CS Concepts (Months 5-10)",
                            "topics": [
                                "Advanced Data Structures",
                                "Algorithm Analysis",
                                "Database Fundamentals",
                                "Software Engineering Principles"
                            ],
                            "level": "Intermediate",
                            "skills": ["System design", "Database modeling", "Testing strategies"],
                            "assessments": ["Medium-scale projects", "Technical interviews", "System design"]
                        },
                        {
                            "phase": "Specialization (Months 11-18)",
                            "topics": [
                                "Web Development/Mobile/AI (choose one)",
                                "Advanced Algorithms",
                                "Distributed Systems",
                                "Industry Best Practices"
                            ],
                            "level": "Advanced",
                            "skills": ["Full-stack development", "Code optimization", "Project leadership"],
                            "assessments": ["Capstone project", "Open source contributions", "Portfolio development"]
                        }
                    ]
                }
            },
            "Physics": {
                "Physics Mastery Path": {
                    "description": "Comprehensive physics education from basics to advanced topics",
                    "duration": "2-4 years",
                    "phases": [
                        {
                            "phase": "Classical Physics (Year 1)",
                            "topics": [
                                "Mechanics & Motion",
                                "Forces & Energy",
                                "Waves & Sound",
                                "Basic Thermodynamics"
                            ],
                            "level": "Beginner",
                            "skills": ["Mathematical modeling", "Experimental design", "Data analysis"],
                            "assessments": ["Lab reports", "Problem sets", "Conceptual understanding tests"]
                        },
                        {
                            "phase": "Modern Physics (Year 2)",
                            "topics": [
                                "Electromagnetism",
                                "Optics",
                                "Special Relativity",
                                "Introduction to Quantum Mechanics"
                            ],
                            "level": "Intermediate",
                            "skills": ["Vector calculus", "Complex analysis", "Computational physics"],
                            "assessments": ["Research presentations", "Simulation projects", "Peer teaching"]
                        },
                        {
                            "phase": "Advanced Topics (Years 3-4)",
                            "topics": [
                                "Quantum Mechanics",
                                "Statistical Mechanics",
                                "Solid State Physics",
                                "Particle Physics or Astrophysics"
                            ],
                            "level": "Advanced",
                            "skills": ["Advanced mathematics", "Research methodology", "Scientific writing"],
                            "assessments": ["Independent research", "Conference presentations", "Thesis project"]
                        }
                    ]
                }
            }
        }
    
    def generate_personalized_path(self, subject: str, current_level: str, 
                                 goal_level: str, available_time_hours: int = 10, 
                                 learning_style: str = "balanced") -> Dict[str, Any]:
        """Generate a personalized learning path with resources"""
        
        # Get base path template
        base_paths = self.learning_paths.get(subject, {})
        if not base_paths:
            return {"error": f"No learning paths available for {subject}"}
        
        # Use the first available path as template
        path_name = list(base_paths.keys())[0]
        template = base_paths[path_name]
        
        # Customize based on user parameters
        customized_path = {
            "subject": subject,
            "path_name": f"Personalized {path_name}",
            "description": template["description"],
            "current_level": current_level,
            "goal_level": goal_level,
            "weekly_hours": available_time_hours,
            "learning_style": learning_style,
            "estimated_duration": self._calculate_duration(template, current_level, goal_level, available_time_hours),
            "phases": [],
            "resources": [],
            "generated_at": datetime.now().isoformat()
        }
        
        # Filter phases based on current and goal levels
        relevant_phases = self._filter_phases_by_level(template["phases"], current_level, goal_level)
        
        for phase in relevant_phases:
            phase_resources = []
            
            # Get resources for each topic in the phase
            for topic in phase["topics"]:
                topic_resources = self.resource_db.get_recommended_resources(
                    subject, phase["level"], num_resources=2
                )
                phase_resources.extend(topic_resources)
            
            customized_phase = {
                **phase,
                "resources": phase_resources,
                "weekly_schedule": self._generate_weekly_schedule(phase, available_time_hours, learning_style)
            }
            
            customized_path["phases"].append(customized_phase)
        
        # Add overall resource recommendations
        all_levels = ["Beginner", "Intermediate", "Advanced"]
        for level in all_levels:
            if level in [current_level, goal_level] or self._is_level_between(level, current_level, goal_level):
                level_resources = self.resource_db.get_recommended_resources(subject, level, num_resources=3)
                customized_path["resources"].extend(level_resources)
        
        return customized_path
    
    def _calculate_duration(self, template: Dict, current_level: str, goal_level: str, weekly_hours: int) -> str:
        """Calculate estimated duration based on parameters"""
        base_weeks = 52  # Base assumption: 1 year
        
        level_multipliers = {"Beginner": 1.0, "Intermediate": 1.5, "Advanced": 2.0}
        complexity = level_multipliers.get(goal_level, 1.5)
        
        # Adjust based on weekly time commitment
        time_factor = 10 / max(weekly_hours, 1)  # Normalize to 10 hours baseline
        
        estimated_weeks = int(base_weeks * complexity * time_factor)
        
        if estimated_weeks < 12:
            return f"{estimated_weeks} weeks"
        else:
            return f"{estimated_weeks // 4} months"
    
    def _filter_phases_by_level(self, phases: List[Dict], current_level: str, goal_level: str) -> List[Dict]:
        """Filter phases based on current and goal levels"""
        level_order = ["Beginner", "Intermediate", "Advanced"]
        
        try:
            start_idx = level_order.index(current_level)
            end_idx = level_order.index(goal_level)
        except ValueError:
            return phases  # Return all if levels not found
        
        relevant_phases = []
        for phase in phases:
            phase_level = phase.get("level", "Intermediate")
            if phase_level in level_order:
                phase_idx = level_order.index(phase_level)
                if start_idx <= phase_idx <= end_idx:
                    relevant_phases.append(phase)
        
        return relevant_phases
    
    def _is_level_between(self, level: str, start: str, end: str) -> bool:
        """Check if level is between start and end levels"""
        level_order = ["Beginner", "Intermediate", "Advanced"]
        try:
            level_idx = level_order.index(level)
            start_idx = level_order.index(start)
            end_idx = level_order.index(end)
            return start_idx <= level_idx <= end_idx
        except ValueError:
            return False
    
    def _generate_weekly_schedule(self, phase: Dict, weekly_hours: int, learning_style: str) -> Dict[str, Any]:
        """Generate a weekly study schedule for the phase"""
        
        schedule = {
            "total_weekly_hours": weekly_hours,
            "learning_style": learning_style,
            "daily_breakdown": {},
            "study_tips": []
        }
        
        # Distribute hours across the week
        if weekly_hours <= 5:
            # Intensive weekend study
            schedule["daily_breakdown"] = {
                "Monday": {"hours": 0, "activities": ["Review previous week"]},
                "Tuesday": {"hours": 0, "activities": ["Light reading"]},
                "Wednesday": {"hours": 1, "activities": ["Video lectures"]},
                "Thursday": {"hours": 0, "activities": ["Practice problems"]},
                "Friday": {"hours": 1, "activities": ["Concept review"]},
                "Saturday": {"hours": weekly_hours // 2, "activities": ["Main study session", "Projects"]},
                "Sunday": {"hours": weekly_hours - (weekly_hours // 2) - 2, "activities": ["Practice", "Assessment"]}
            }
        else:
            # Distributed daily study
            daily_hours = weekly_hours / 7
            for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                schedule["daily_breakdown"][day] = {
                    "hours": round(daily_hours, 1),
                    "activities": ["Study session", "Practice problems"]
                }
        
        # Add learning style specific tips
        if learning_style == "visual":
            schedule["study_tips"] = [
                "Use diagrams and visual aids",
                "Create mind maps for concepts",
                "Watch video lectures with good visuals"
            ]
        elif learning_style == "hands-on":
            schedule["study_tips"] = [
                "Focus on practical exercises",
                "Build projects while learning",
                "Use interactive simulations"
            ]
        else:  # balanced
            schedule["study_tips"] = [
                "Mix theory with practice",
                "Use multiple resource types",
                "Regular self-assessment"
            ]
        
        return schedule
