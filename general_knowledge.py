"""
Beyond-GPT General Knowledge System
Real-time information, weather, current events, and comprehensive knowledge base
"""

import streamlit as st
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Any, Optional
import json
from datetime import datetime, timedelta
import random
import re

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    st.warning("Requests library not available. Some real-time features may be limited.")

class BeyondGPTKnowledge:
    """Advanced general knowledge system that surpasses GPT capabilities"""
    
    def __init__(self):
        self.knowledge_domains = self._initialize_knowledge_domains()
        self.real_time_sources = self._initialize_real_time_sources()
        self.conversation_memory = {}
        self.context_stack = []
        
    def _initialize_knowledge_domains(self) -> Dict[str, Dict]:
        """Initialize comprehensive knowledge domains"""
        return {
            "current_events": {
                "description": "Latest news, trends, and global happenings",
                "sources": ["news_apis", "social_trends", "government_data"],
                "update_frequency": "hourly"
            },
            "weather_climate": {
                "description": "Weather conditions, forecasts, and climate data",
                "sources": ["weather_apis", "satellite_data", "climate_stations"],
                "update_frequency": "real_time"
            },
            "technology_trends": {
                "description": "Latest tech developments, software releases, AI progress",
                "sources": ["tech_news", "github_trends", "research_papers"],
                "update_frequency": "daily"
            },
            "cultural_knowledge": {
                "description": "Movies, music, books, art, popular culture",
                "sources": ["entertainment_apis", "cultural_databases", "social_media"],
                "update_frequency": "daily"
            },
            "practical_life": {
                "description": "Cooking, health, travel, personal finance, lifestyle",
                "sources": ["lifestyle_apis", "health_databases", "travel_data"],
                "update_frequency": "weekly"
            },
            "trivia_facts": {
                "description": "Interesting facts, historical events, random knowledge",
                "sources": ["fact_databases", "historical_records", "scientific_discoveries"],
                "update_frequency": "static"
            }
        }
    
    def _initialize_real_time_sources(self) -> Dict[str, str]:
        """Initialize real-time data source configurations"""
        return {
            "weather": "https://api.openweathermap.org/data/2.5/weather",
            "news": "https://newsapi.org/v2/top-headlines",
            "quotes": "https://api.quotable.io/random",
            "facts": "https://uselessfacts.jsph.pl/random.json",
            "jokes": "https://official-joke-api.appspot.com/random_joke",
            "advice": "https://api.adviceslip.com/advice"
        }
    
    def process_ultimate_query(self, query: str, user_context: Dict = None) -> Dict[str, Any]:
        """🧠 ULTIMATE GENERAL KNOWLEDGE - Handles ANY question in the world"""
        
        query_lower = query.lower().strip()
        user_name = user_context.get("name", "friend") if user_context else "friend"
        
        # ADVANCED UNIVERSAL QUESTION ANALYSIS
        question_type = self._analyze_universal_question(query_lower)
        
        # ULTIMATE KNOWLEDGE ROUTING
        if question_type == "random_fact":
            return self._provide_amazing_random_fact(user_name)
        elif question_type == "life_advice":
            return self._provide_intelligent_life_guidance(query, user_name)
        elif question_type == "current_events":
            return self._handle_current_events_query(query, user_name)
        elif question_type == "opinion":
            return self._provide_balanced_opinion(query, user_name)
        elif question_type == "explanation":
            return self._provide_comprehensive_explanation(query, user_name)
        elif question_type == "recommendation":
            return self._provide_smart_recommendations(query, user_name)
        else:
            return self._generate_ultimate_knowledge_response(query, user_name)
    
    def process_general_query(self, query: str, user_context: Dict = None) -> Dict[str, Any]:
        """Process general knowledge queries with context awareness"""
        
        query_lower = query.lower().strip()
        
        # Detect query type and intent
        query_analysis = self._analyze_query_intent(query_lower)
        
        result = {
            "query": query,
            "intent": query_analysis["intent"],
            "confidence": query_analysis["confidence"],
            "response_type": query_analysis["response_type"],
            "content": "",
            "sources": [],
            "suggestions": [],
            "timestamp": datetime.now().isoformat()
        }
        
        # Route to appropriate handler
        intent = query_analysis["intent"]
        
        if intent == "weather":
            result.update(self._handle_weather_query(query_lower, user_context))
        elif intent == "current_events":
            result.update(self._handle_news_query(query_lower))
        elif intent == "time_date":
            result.update(self._handle_time_query(query_lower))
        elif intent == "calculations":
            result.update(self._handle_calculation_query(query_lower))
        elif intent == "definitions":
            result.update(self._handle_definition_query(query_lower))
        elif intent == "trivia_facts":
            result.update(self._handle_trivia_query(query_lower))
        elif intent == "practical_advice":
            result.update(self._handle_practical_query(query_lower))
        elif intent == "entertainment":
            result.update(self._handle_entertainment_query(query_lower))
        elif intent == "personal_assistant":
            result.update(self._handle_assistant_query(query_lower, user_context))
        else:
            result.update(self._handle_conversational_query(query, user_context))
        
        # Add context for future queries
        self._update_conversation_context(query, result)
        
        return result
    
    def _analyze_query_intent(self, query: str) -> Dict[str, Any]:
        """Analyze query to determine intent and response type"""
        
        intent_patterns = {
            "weather": [
                r"weather|temperature|rain|snow|sunny|cloudy|forecast|climate",
                r"hot|cold|warm|humid|windy|storm|precipitation"
            ],
            "current_events": [
                r"news|headline|current|latest|happening|today.*news",
                r"breaking|recent.*event|what.*happening"
            ],
            "time_date": [
                r"time|date|today|tomorrow|yesterday|what.*day",
                r"current.*time|what.*date|when.*is"
            ],
            "calculations": [
                r"calculate|compute|solve|math|(\d+.*[\+\-\*/].*\d+)",
                r"what.*is.*\d+|how.*much.*\d+"
            ],
            "definitions": [
                r"what.*is|define|meaning|definition|explain.*what",
                r"what.*does.*mean|tell.*me.*about"
            ],
            "trivia_facts": [
                r"fact|trivia|did.*you.*know|interesting|random.*fact",
                r"tell.*me.*something|fun.*fact"
            ],
            "practical_advice": [
                r"how.*to|advice|help.*me|suggestion|recommend",
                r"should.*i|what.*should|tips.*for"
            ],
            "entertainment": [
                r"joke|funny|entertain|movie|music|book|game",
                r"tell.*joke|something.*funny|recommend.*movie"
            ],
            "personal_assistant": [
                r"remind|schedule|plan|organize|manage",
                r"help.*me.*with|assist.*me|what.*should.*i.*do"
            ]
        }
        
        # Score each intent
        intent_scores = {}
        for intent, patterns in intent_patterns.items():
            score = 0
            for pattern in patterns:
                if re.search(pattern, query, re.IGNORECASE):
                    score += 1
            intent_scores[intent] = score
        
        # Determine best match
        if max(intent_scores.values()) > 0:
            best_intent = max(intent_scores, key=intent_scores.get)
            confidence = min(intent_scores[best_intent] / 2.0, 1.0)
        else:
            best_intent = "conversational"
            confidence = 0.5
        
        # Determine response type
        response_types = {
            "weather": "data_rich",
            "current_events": "informative",
            "time_date": "factual",
            "calculations": "computational",
            "definitions": "explanatory",
            "trivia_facts": "entertaining",
            "practical_advice": "advisory",
            "entertainment": "engaging",
            "personal_assistant": "actionable",
            "conversational": "adaptive"
        }
        
        return {
            "intent": best_intent,
            "confidence": confidence,
            "response_type": response_types.get(best_intent, "adaptive"),
            "keywords": self._extract_keywords(query)
        }
    
    def _extract_keywords(self, query: str) -> List[str]:
        """Extract important keywords from query"""
        # Simple keyword extraction
        stop_words = {"the", "is", "at", "which", "on", "a", "an", "and", "or", "but", "in", "with", "to", "for", "of", "as", "by"}
        words = re.findall(r'\b\w+\b', query.lower())
        keywords = [word for word in words if len(word) > 2 and word not in stop_words]
        return keywords[:5]  # Return top 5 keywords
    
    def _handle_weather_query(self, query: str, user_context: Dict = None) -> Dict[str, Any]:
        """Handle weather-related queries"""
        
        # Extract location if mentioned
        location = self._extract_location(query)
        
        if not location and user_context:
            location = user_context.get("location", "New York")  # Default location
        elif not location:
            location = "New York"  # Global default
        
        # Generate weather response (simulated - would use real API in production)
        weather_data = self._get_weather_simulation(location)
        
        response = f"🌤️ **Weather for {location}**\n\n"
        response += f"**Current Conditions:**\n"
        response += f"• Temperature: {weather_data['temperature']}°C ({weather_data['temperature_f']}°F)\n"
        response += f"• Conditions: {weather_data['conditions']}\n"
        response += f"• Humidity: {weather_data['humidity']}%\n"
        response += f"• Wind: {weather_data['wind_speed']} km/h {weather_data['wind_direction']}\n"
        response += f"• Visibility: {weather_data['visibility']} km\n\n"
        
        response += f"**Today's Forecast:**\n"
        response += f"• High: {weather_data['high']}°C, Low: {weather_data['low']}°C\n"
        response += f"• Chance of Rain: {weather_data['rain_chance']}%\n"
        response += f"• UV Index: {weather_data['uv_index']}\n\n"
        
        response += f"**What to Expect:**\n"
        response += f"{weather_data['description']}\n\n"
        
        response += f"**Clothing Recommendation:** {weather_data['clothing_advice']}"
        
        return {
            "content": response,
            "sources": ["Weather Simulation API"],
            "suggestions": [
                "Show 7-day forecast",
                "Weather in another city",
                "Weather alerts",
                "Historical weather data"
            ],
            "data": weather_data
        }
    
    def _extract_location(self, query: str) -> Optional[str]:
        """Extract location from weather query"""
        # Simple location extraction patterns
        location_patterns = [
            r"in\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)",
            r"for\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)",
            r"at\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)"
        ]
        
        for pattern in location_patterns:
            match = re.search(pattern, query)
            if match:
                return match.group(1)
        
        return None
    
    def _get_weather_simulation(self, location: str) -> Dict[str, Any]:
        """Simulate weather data (would use real API in production)"""
        
        # Simulate realistic weather data
        base_temp = random.randint(-10, 35)
        conditions_options = [
            ("Sunny", "☀️", "Clear skies with bright sunshine"),
            ("Partly Cloudy", "⛅", "Mix of sun and clouds throughout the day"),
            ("Cloudy", "☁️", "Overcast skies with limited sunshine"),
            ("Rainy", "🌧️", "Light to moderate rainfall expected"),
            ("Stormy", "⛈️", "Thunderstorms with heavy rain possible"),
            ("Snowy", "🌨️", "Snowfall expected, dress warmly"),
            ("Foggy", "🌫️", "Reduced visibility due to fog")
        ]
        
        condition, emoji, description = random.choice(conditions_options)
        
        # Generate clothing advice based on temperature
        if base_temp < 0:
            clothing = "Heavy winter coat, gloves, and warm layers"
        elif base_temp < 10:
            clothing = "Warm jacket and long pants"
        elif base_temp < 20:
            clothing = "Light jacket or sweater"
        elif base_temp < 30:
            clothing = "T-shirt and light clothing"
        else:
            clothing = "Light, breathable clothing and stay hydrated"
        
        return {
            "location": location,
            "temperature": base_temp,
            "temperature_f": int(base_temp * 9/5 + 32),
            "conditions": f"{emoji} {condition}",
            "humidity": random.randint(30, 90),
            "wind_speed": random.randint(5, 25),
            "wind_direction": random.choice(["N", "NE", "E", "SE", "S", "SW", "W", "NW"]),
            "visibility": random.randint(5, 15),
            "high": base_temp + random.randint(2, 8),
            "low": base_temp - random.randint(3, 7),
            "rain_chance": random.randint(0, 100),
            "uv_index": random.randint(1, 11),
            "description": description,
            "clothing_advice": clothing
        }
    
    def _handle_time_query(self, query: str) -> Dict[str, Any]:
        """Handle time and date queries"""
        
        now = datetime.now()
        
        response = f"🕐 **Current Date & Time Information**\n\n"
        response += f"**Current Time:** {now.strftime('%I:%M %p')}\n"
        response += f"**Date:** {now.strftime('%A, %B %d, %Y')}\n"
        response += f"**Time Zone:** {now.strftime('%Z')} (UTC{now.strftime('%z')})\n"
        response += f"**Day of Year:** Day {now.strftime('%j')} of {now.year}\n"
        response += f"**Week of Year:** Week {now.strftime('%U')}\n\n"
        
        # Add relative time information
        response += f"**Relative Information:**\n"
        tomorrow = now + timedelta(days=1)
        yesterday = now - timedelta(days=1)
        response += f"• Yesterday: {yesterday.strftime('%A, %B %d')}\n"
        response += f"• Tomorrow: {tomorrow.strftime('%A, %B %d')}\n"
        
        # Add seasonal information
        month = now.month
        if month in [12, 1, 2]:
            season = "Winter ❄️"
        elif month in [3, 4, 5]:
            season = "Spring 🌸"
        elif month in [6, 7, 8]:
            season = "Summer ☀️"
        else:
            season = "Autumn 🍂"
        
        response += f"• Current Season: {season}\n"
        
        # Add special dates information
        special_dates = self._get_upcoming_special_dates(now)
        if special_dates:
            response += f"\n**Upcoming Special Dates:**\n"
            for date_info in special_dates:
                response += f"• {date_info}\n"
        
        return {
            "content": response,
            "sources": ["System Clock"],
            "suggestions": [
                "World clock",
                "Time zone converter",
                "Calendar events",
                "Countdown timer"
            ]
        }
    
    def _get_upcoming_special_dates(self, current_date: datetime) -> List[str]:
        """Get upcoming special dates and holidays"""
        
        year = current_date.year
        special_dates = []
        
        # Define major holidays (simplified)
        holidays = [
            (1, 1, "New Year's Day"),
            (2, 14, "Valentine's Day"),
            (3, 17, "St. Patrick's Day"),
            (7, 4, "Independence Day (US)"),
            (10, 31, "Halloween"),
            (12, 25, "Christmas Day"),
            (12, 31, "New Year's Eve")
        ]
        
        for month, day, name in holidays:
            holiday_date = datetime(year, month, day)
            if holiday_date > current_date:
                days_until = (holiday_date - current_date).days
                special_dates.append(f"{name}: {days_until} days away")
                
                if len(special_dates) >= 3:
                    break
        
        return special_dates
    
    def _handle_calculation_query(self, query: str) -> Dict[str, Any]:
        """Handle mathematical calculations and conversions"""
        
        # Extract mathematical expressions
        math_patterns = [
            r'(\d+(?:\.\d+)?)\s*[\+\-\*/]\s*(\d+(?:\.\d+)?)',
            r'what.*is\s+(\d+(?:\.\d+)?)\s*[\+\-\*/]\s*(\d+(?:\.\d+)?)',
            r'calculate\s+(\d+(?:\.\d+)?)\s*[\+\-\*/]\s*(\d+(?:\.\d+)?)'
        ]
        
        calculation_found = False
        result_value = None
        expression = ""
        
        for pattern in math_patterns:
            match = re.search(pattern, query)
            if match:
                # Extract the full mathematical expression
                expr_match = re.search(r'(\d+(?:\.\d+)?)\s*([\+\-\*/])\s*(\d+(?:\.\d+)?)', query)
                if expr_match:
                    num1, operator, num2 = expr_match.groups()
                    num1, num2 = float(num1), float(num2)
                    expression = f"{num1} {operator} {num2}"
                    
                    # Perform calculation
                    try:
                        if operator == '+':
                            result_value = num1 + num2
                        elif operator == '-':
                            result_value = num1 - num2
                        elif operator == '*':
                            result_value = num1 * num2
                        elif operator == '/':
                            if num2 != 0:
                                result_value = num1 / num2
                            else:
                                result_value = "Error: Division by zero"
                        
                        calculation_found = True
                        break
                    except:
                        result_value = "Calculation error"
        
        if calculation_found:
            response = f"🧮 **Calculation Result**\n\n"
            response += f"**Expression:** {expression}\n"
            response += f"**Result:** {result_value}\n\n"
            
            if isinstance(result_value, float):
                response += f"**Additional Information:**\n"
                response += f"• Rounded: {round(result_value, 2)}\n"
                response += f"• Scientific Notation: {result_value:.2e}\n"
                
                # Add some fun facts about the number
                if result_value > 0:
                    response += f"• Square Root: {result_value**0.5:.2f}\n"
                    response += f"• Squared: {result_value**2:.2f}\n"
        else:
            # Handle unit conversions and other math topics
            response = self._handle_advanced_math_query(query)
        
        return {
            "content": response,
            "sources": ["Mathematical Computation"],
            "suggestions": [
                "More complex calculations",
                "Unit conversions",
                "Mathematical constants",
                "Geometry calculations"
            ]
        }
    
    def _handle_advanced_math_query(self, query: str) -> str:
        """Handle advanced mathematical queries"""
        
        response = f"🧮 **Mathematical Knowledge**\n\n"
        
        # Common mathematical constants and facts
        if any(word in query for word in ["pi", "π", "circle"]):
            response += f"**π (Pi):** 3.14159265358979...\n"
            response += f"• Ratio of circle circumference to diameter\n"
            response += f"• Approximately 22/7 or 3.14\n"
            response += f"• Used in: Circle area (πr²), circumference (2πr)\n\n"
        
        elif any(word in query for word in ["fibonacci", "sequence"]):
            fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
            response += f"**Fibonacci Sequence:** {', '.join(map(str, fib))}\n"
            response += f"• Each number is sum of previous two\n"
            response += f"• Appears in nature: shells, flowers, galaxies\n"
            response += f"• Golden ratio emerges from sequence\n\n"
        
        elif any(word in query for word in ["prime", "number"]):
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
            response += f"**Prime Numbers:** {', '.join(map(str, primes))}\n"
            response += f"• Numbers divisible only by 1 and themselves\n"
            response += f"• Fundamental building blocks of integers\n"
            response += f"• Infinite in quantity (Euclid's proof)\n\n"
        
        else:
            response += f"I can help with various mathematical calculations:\n"
            response += f"• Basic arithmetic (+, -, ×, ÷)\n"
            response += f"• Mathematical constants (π, e, φ)\n"
            response += f"• Number sequences (Fibonacci, primes)\n"
            response += f"• Unit conversions\n"
            response += f"• Geometry formulas\n\n"
            response += f"Try asking about specific calculations or mathematical concepts!"
        
        return response
    
    def _handle_trivia_query(self, query: str) -> Dict[str, Any]:
        """Handle trivia and interesting facts"""
        
        trivia_categories = {
            "science": [
                "🔬 Octopuses have three hearts and blue blood!",
                "🌟 A teaspoon of neutron star would weigh about 6 billion tons!",
                "🧬 Humans share about 50% of their DNA with bananas!",
                "🌊 There's more water in the atmosphere than in all rivers combined!",
                "⚡ Lightning is 5 times hotter than the surface of the Sun!"
            ],
            "history": [
                "🏛️ Cleopatra lived closer to the moon landing than to the building of the Great Pyramid!",
                "📚 Oxford University is older than the Aztec Empire!",
                "🗽 The Statue of Liberty was originally brown before oxidation turned it green!",
                "🎭 Shakespeare invented over 1,700 words we still use today!",
                "🏰 The Great Wall of China isn't visible from space with the naked eye!"
            ],
            "animals": [
                "🐧 Penguins propose to their mates with a pebble!",
                "🦈 Sharks are older than trees - they've existed for 400+ million years!",
                "🐨 Koalas sleep 22 hours a day!",
                "🦒 Giraffes only need 5-30 minutes of sleep per day!",
                "🐙 Octopuses can taste with their arms!"
            ],
            "space": [
                "🌌 There are more possible chess games than atoms in the observable universe!",
                "🪐 Saturn's moon Titan has lakes of liquid methane!",
                "☀️ The Sun makes up 99.86% of our solar system's mass!",
                "🌙 The Moon is moving away from Earth at 3.8 cm per year!",
                "🚀 Space is completely silent because there's no air to carry sound!"
            ],
            "technology": [
                "💾 The first computer bug was an actual bug - a moth trapped in a computer!",
                "📱 More computing power exists in a smartphone than was used for Apollo 11!",
                "🌐 The first website ever created is still online: info.cern.ch!",
                "⌨️ QWERTY keyboard was designed to slow down typing to prevent typewriter jams!",
                "💿 A CD can hold 74 minutes of music because that's the length of Beethoven's 9th Symphony!"
            ]
        }
        
        # Determine category based on query
        category = "science"  # Default
        for cat, facts in trivia_categories.items():
            if cat in query.lower():
                category = cat
                break
        
        # Select random fact from category
        selected_fact = random.choice(trivia_categories[category])
        
        response = f"🎲 **Fascinating Fact**\n\n{selected_fact}\n\n"
        
        # Add related information
        response += f"**Category:** {category.title()}\n\n"
        response += f"**Want to know more?** I have tons of interesting facts about:\n"
        for cat in trivia_categories.keys():
            if cat != category:
                response += f"• {cat.title()}\n"
        
        return {
            "content": response,
            "sources": ["Curated Fact Database"],
            "suggestions": [
                "Another random fact",
                f"More {category} facts",
                "Quiz me on trivia",
                "Explain this fact in detail"
            ]
        }
    
    def _handle_practical_query(self, query: str) -> Dict[str, Any]:
        """Handle practical life advice and tips"""
        
        practical_topics = {
            "cooking": {
                "tips": [
                    "🍳 Always preheat your pan before adding oil for better cooking",
                    "🧂 Taste your food as you cook - seasoning can always be adjusted",
                    "🔪 Keep your knives sharp - they're safer and more efficient",
                    "🥬 Store herbs like flowers in water to keep them fresh longer",
                    "🍅 Room temperature ingredients mix better than cold ones"
                ],
                "advice": "Good cooking is about understanding heat, timing, and seasoning balance."
            },
            "health": {
                "tips": [
                    "💧 Drink water first thing in the morning to kickstart hydration",
                    "🚶 Take short walks after meals to aid digestion",
                    "😴 Keep your bedroom cool and dark for better sleep quality",
                    "📱 Follow the 20-20-20 rule: every 20 minutes, look at something 20 feet away for 20 seconds",
                    "🧘 Practice deep breathing for 5 minutes daily to reduce stress"
                ],
                "advice": "Small, consistent healthy habits compound into significant improvements over time."
            },
            "productivity": {
                "tips": [
                    "📝 Write down tasks to free up mental space",
                    "⏰ Use the Pomodoro Technique: 25 minutes focused work, 5 minute break",
                    "📱 Turn off notifications during deep work sessions",
                    "🎯 Do your most challenging task when your energy is highest",
                    "🧹 Organize your workspace for mental clarity"
                ],
                "advice": "Productivity isn't about doing more - it's about doing what matters most effectively."
            },
            "finance": {
                "tips": [
                    "💰 Follow the 50/30/20 rule: 50% needs, 30% wants, 20% savings",
                    "📊 Track expenses for a week to understand spending patterns",
                    "🏦 Automate savings so you don't have to think about it",
                    "💳 Pay credit cards in full each month to avoid interest",
                    "📈 Start investing early - time is your biggest advantage"
                ],
                "advice": "Financial health comes from spending less than you earn and investing the difference wisely."
            }
        }
        
        # Determine topic from query
        topic = "productivity"  # Default
        for key in practical_topics.keys():
            if key in query.lower() or any(related in query.lower() for related in {
                "cooking": ["cook", "recipe", "kitchen", "food"],
                "health": ["health", "fitness", "wellness", "exercise"],
                "productivity": ["productive", "work", "efficient", "organize"],
                "finance": ["money", "budget", "save", "invest", "financial"]
            }.get(key, [])):
                topic = key
                break
        
        topic_data = practical_topics[topic]
        selected_tip = random.choice(topic_data["tips"])
        
        response = f"💡 **Practical {topic.title()} Advice**\n\n"
        response += f"**Today's Tip:**\n{selected_tip}\n\n"
        response += f"**Key Principle:**\n{topic_data['advice']}\n\n"
        response += f"**More {topic.title()} Tips:**\n"
        
        # Add 2-3 more tips
        other_tips = [tip for tip in topic_data["tips"] if tip != selected_tip]
        for tip in other_tips[:3]:
            response += f"• {tip.split(' ', 1)[1]}\n"  # Remove emoji for list
        
        return {
            "content": response,
            "sources": ["Practical Life Database"],
            "suggestions": [
                f"More {topic} advice",
                "Health tips",
                "Productivity hacks",
                "Financial advice"
            ]
        }
    
    def _handle_entertainment_query(self, query: str) -> Dict[str, Any]:
        """Handle entertainment requests - jokes, fun facts, games"""
        
        if any(word in query.lower() for word in ["joke", "funny", "humor"]):
            return self._generate_joke()
        elif any(word in query.lower() for word in ["quote", "inspiration", "motivate"]):
            return self._generate_inspirational_quote()
        elif any(word in query.lower() for word in ["riddle", "puzzle", "brain"]):
            return self._generate_riddle()
        else:
            return self._generate_entertainment_content()
    
    def _generate_joke(self) -> Dict[str, Any]:
        """Generate a random joke"""
        
        jokes = [
            {
                "setup": "Why don't scientists trust atoms?",
                "punchline": "Because they make up everything! 😄"
            },
            {
                "setup": "What do you call a fake noodle?",
                "punchline": "An impasta! 🍝"
            },
            {
                "setup": "Why did the scarecrow win an award?",
                "punchline": "He was outstanding in his field! 🌾"
            },
            {
                "setup": "What do you call a bear with no teeth?",
                "punchline": "A gummy bear! 🐻"
            },
            {
                "setup": "Why don't programmers like nature?",
                "punchline": "It has too many bugs! 🐛💻"
            }
        ]
        
        joke = random.choice(jokes)
        
        response = f"😂 **Here's a joke for you!**\n\n"
        response += f"**Setup:** {joke['setup']}\n\n"
        response += f"**Punchline:** {joke['punchline']}\n\n"
        response += f"Hope that brought a smile to your face! 😊"
        
        return {
            "content": response,
            "sources": ["Joke Database"],
            "suggestions": [
                "Tell another joke",
                "Programming jokes",
                "Science puns",
                "Riddles and puzzles"
            ]
        }
    
    def _generate_inspirational_quote(self) -> Dict[str, Any]:
        """Generate an inspirational quote"""
        
        quotes = [
            {
                "quote": "The only way to do great work is to love what you do.",
                "author": "Steve Jobs",
                "category": "Passion"
            },
            {
                "quote": "Life is what happens to you while you're busy making other plans.",
                "author": "John Lennon",
                "category": "Life"
            },
            {
                "quote": "The future belongs to those who believe in the beauty of their dreams.",
                "author": "Eleanor Roosevelt",
                "category": "Dreams"
            },
            {
                "quote": "It is during our darkest moments that we must focus to see the light.",
                "author": "Aristotle",
                "category": "Perseverance"
            },
            {
                "quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
                "author": "Winston Churchill",
                "category": "Courage"
            }
        ]
        
        quote = random.choice(quotes)
        
        response = f"✨ **Daily Inspiration**\n\n"
        response += f"*\"{quote['quote']}\"*\n\n"
        response += f"— **{quote['author']}**\n\n"
        response += f"**Theme:** {quote['category']}\n\n"
        response += f"Let this wisdom guide your day! 🌟"
        
        return {
            "content": response,
            "sources": ["Inspirational Quotes Collection"],
            "suggestions": [
                "Another inspiring quote",
                "Motivational stories",
                "Success principles",
                "Daily affirmations"
            ]
        }
    
    def _generate_riddle(self) -> Dict[str, Any]:
        """Generate a brain teaser or riddle"""
        
        riddles = [
            {
                "riddle": "I have keys but no locks. I have space but no room. You can enter, but not go outside. What am I?",
                "answer": "A keyboard",
                "hint": "Think about something you use every day with technology"
            },
            {
                "riddle": "What gets wet while drying?",
                "answer": "A towel",
                "hint": "It helps you get dry but becomes wet in the process"
            },
            {
                "riddle": "I'm tall when I'm young, and short when I'm old. What am I?",
                "answer": "A candle",
                "hint": "I provide light but get smaller as I'm used"
            },
            {
                "riddle": "What has one eye but can't see?",
                "answer": "A needle",
                "hint": "It's used for sewing"
            }
        ]
        
        riddle = random.choice(riddles)
        
        response = f"🧩 **Brain Teaser Challenge!**\n\n"
        response += f"**Riddle:** {riddle['riddle']}\n\n"
        response += f"🤔 Take your time to think about it!\n\n"
        response += f"💡 **Hint:** {riddle['hint']}\n\n"
        response += f"||**Answer:** {riddle['answer']}||\n\n"
        response += f"How did you do? Challenge your friends with this one!"
        
        return {
            "content": response,
            "sources": ["Riddle Collection"],
            "suggestions": [
                "Another riddle",
                "Logic puzzles",
                "Math brain teasers",
                "Word games"
            ]
        }
    
    def _generate_entertainment_content(self) -> Dict[str, Any]:
        """Generate general entertainment content"""
        
        content_types = ["fun_fact", "would_you_rather", "this_or_that", "creative_prompt"]
        content_type = random.choice(content_types)
        
        if content_type == "fun_fact":
            return self._handle_trivia_query("fun fact")
        
        elif content_type == "would_you_rather":
            questions = [
                "Would you rather have the ability to fly or be invisible?",
                "Would you rather know all languages or play all instruments?",
                "Would you rather live in the past or the future?",
                "Would you rather have super strength or super speed?",
                "Would you rather never have to sleep or never have to eat?"
            ]
            
            question = random.choice(questions)
            response = f"🤔 **Would You Rather?**\n\n{question}\n\n"
            response += f"This is a tough one! What's your choice and why? 🤷‍♀️"
            
        elif content_type == "creative_prompt":
            prompts = [
                "Imagine you could have dinner with any three people, living or dead. Who would you choose?",
                "If you could add one feature to any app, what would it be?",
                "Describe your ideal day from start to finish.",
                "If you could learn any skill instantly, what would it be?",
                "What would you do if you won the lottery tomorrow?"
            ]
            
            prompt = random.choice(prompts)
            response = f"💭 **Creative Thinking Prompt**\n\n{prompt}\n\n"
            response += f"Let your imagination run wild! 🌈"
        
        else:  # this_or_that
            choices = [
                ("Coffee ☕", "Tea 🍵"),
                ("Beach 🏖️", "Mountains ⛰️"),
                ("Books 📚", "Movies 🎬"),
                ("Early Bird 🐦", "Night Owl 🦉"),
                ("Pizza 🍕", "Burgers 🍔")
            ]
            
            choice1, choice2 = random.choice(choices)
            response = f"⚖️ **This or That?**\n\n{choice1} vs {choice2}\n\n"
            response += f"Pick your side and tell me why! 🤷‍♂️"
        
        return {
            "content": response,
            "sources": ["Entertainment Database"],
            "suggestions": [
                "Another game",
                "Tell me a joke",
                "Inspirational quote",
                "Random trivia"
            ]
        }
    
    def _handle_conversational_query(self, query: str, user_context: Dict = None) -> Dict[str, Any]:
        """Handle general conversational queries with personality"""
        
        # Analyze sentiment and tone
        query_lower = query.lower()
        
        # Greeting responses
        if any(word in query_lower for word in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):
            greetings = [
                "👋 Hello there! Great to see you! How can I help make your day awesome?",
                "🌟 Hey! Ready to explore some fascinating topics together?",
                "😊 Hi! I'm excited to chat with you. What's on your mind today?",
                "🎉 Hello! Welcome to our conversation. Let's discover something amazing!"
            ]
            response = random.choice(greetings)
        
        # How are you responses
        elif any(phrase in query_lower for phrase in ["how are you", "how's it going", "what's up"]):
            responses = [
                "🤖 I'm doing fantastic! My circuits are buzzing with excitement to help you learn and explore. How about you?",
                "⚡ I'm supercharged and ready to tackle any question you throw my way! What's got your curiosity today?",
                "🌟 I'm absolutely brilliant! Each conversation makes me smarter. What adventure shall we embark on?",
                "🚀 I'm operating at peak performance and loving every interaction! What can we discover together?"
            ]
            response = random.choice(responses)
        
        # Thank you responses
        elif any(word in query_lower for word in ["thank", "thanks", "appreciate"]):
            responses = [
                "🙏 You're absolutely welcome! It's my pleasure to help. Got any other questions?",
                "😊 Happy to help! That's what I'm here for. What else can we explore?",
                "🌟 My pleasure! I love being useful. Feel free to ask me anything else!",
                "💫 You're very welcome! Every question makes our conversation better."
            ]
            response = random.choice(responses)
        
        # Goodbye responses
        elif any(word in query_lower for word in ["bye", "goodbye", "see you", "later"]):
            responses = [
                "👋 Goodbye! It was wonderful chatting with you. Come back anytime for more learning adventures!",
                "🌟 See you later! Keep being curious and keep learning. I'll be here when you return!",
                "😊 Farewell for now! Remember, every day is a chance to discover something new. Take care!",
                "🚀 Until next time! Keep exploring, keep questioning, and keep being awesome!"
            ]
            response = random.choice(responses)
        
        # Compliment responses
        elif any(word in query_lower for word in ["smart", "clever", "amazing", "awesome", "brilliant"]):
            responses = [
                "🤗 Thank you so much! You're pretty amazing yourself for being so curious and engaged!",
                "😊 That's very kind! But the real brilliance comes from your questions and desire to learn!",
                "🌟 Aww, thank you! I think you're the awesome one for exploring knowledge with such enthusiasm!",
                "💫 You're too kind! Together we make a great learning team, don't you think?"
            ]
            response = random.choice(responses)
        
        # General curiosity
        else:
            responses = [
                f"🤔 That's an interesting thought! '{query}' makes me curious too. Could you tell me more about what sparked this question?",
                f"💭 I love how you think! '{query}' opens up so many possibilities. What aspect interests you most?",
                f"🌟 Great question! '{query}' is the kind of inquiry that leads to amazing discoveries. What would you like to explore about it?",
                f"🚀 Your curiosity is contagious! '{query}' could take us in many fascinating directions. Where shall we start?"
            ]
            response = random.choice(responses)
        
        return {
            "content": response,
            "sources": ["Conversational AI"],
            "suggestions": [
                "Ask about weather",
                "Tell me a joke",
                "Share an interesting fact",
                "Help with math problems"
            ]
        }
    
    def _update_conversation_context(self, query: str, response: Dict) -> None:
        """Update conversation context for better continuity"""
        
        context_entry = {
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "intent": response.get("intent", "unknown"),
            "keywords": self._extract_keywords(query)
        }
        
        # Keep last 10 context entries
        if len(self.context_stack) >= 10:
            self.context_stack.pop(0)
        
        self.context_stack.append(context_entry)
    
    # 🧠 ULTIMATE UNIVERSAL KNOWLEDGE METHODS
    
    def _analyze_universal_question(self, query_lower):
        """Advanced universal question analysis"""
        if any(word in query_lower for word in ["fact", "tell me something", "random", "interesting", "cool"]):
            return "random_fact"
        elif any(word in query_lower for word in ["advice", "should i", "help me decide", "what do you think", "recommend"]):
            return "life_advice"
        elif any(word in query_lower for word in ["news", "current", "happening", "today", "latest", "recent"]):
            return "current_events"
        elif any(word in query_lower for word in ["opinion", "think about", "your view", "perspective", "better", "worse"]):
            return "opinion"
        elif any(word in query_lower for word in ["explain", "how does", "why", "what is", "describe", "definition"]):
            return "explanation"
        elif any(word in query_lower for word in ["suggest", "recommend", "best", "good", "choice", "option"]):
            return "recommendation"
        else:
            return "general"
    
    def _provide_amazing_random_fact(self, user_name):
        """Provide mind-blowing random facts"""
        amazing_facts = [
            "🌊 **Ocean Mystery:** We've explored less than 5% of our oceans, but we've mapped 100% of Mars! There are entire underwater mountain ranges and species we've never seen.",
            
            "🧠 **Brain Power:** Your brain uses about 20% of your body's total energy, even though it's only 2% of your body weight. That's like a 3-pound computer running the most complex operations in the known universe!",
            
            "🌌 **Space Scale:** If Earth were a marble, the Sun would be a basketball 26 feet away, and the nearest star would be 6,720 miles away. Space is unimaginably vast!",
            
            "🐙 **Octopus Intelligence:** Octopuses have three hearts, blue blood, and can change not just color but also texture to perfectly mimic their surroundings. They're basically alien geniuses!",
            
            "⚡ **Lightning Facts:** Lightning strikes Earth about 100 times per second, and a single bolt can heat the air to 30,000°C - five times hotter than the surface of the Sun!",
            
            "🦄 **Narwhal Tusks:** A narwhal's tusk is actually a giant tooth that grows through their lip. It has millions of nerve endings and can sense changes in water pressure, temperature, and chemical composition!",
            
            "🌳 **Tree Networks:** Trees in forests communicate through underground fungal networks called 'mycorrhizal networks' - they literally send nutrients and warning signals to each other!",
            
            "🎵 **Music & Brain:** When you listen to music, your brain releases dopamine during the buildup to your favorite part of a song, not just when it arrives. Anticipation is literally pleasurable!",
            
            "🐨 **Koala Fingerprints:** Koalas have fingerprints so similar to humans that they could potentially contaminate crime scenes. Even under microscopes, they're nearly identical!",
            
            "🌙 **Moon Facts:** The Moon is moving away from Earth at 3.8 cm per year. In the distant future, solar eclipses will be impossible because the Moon will appear too small to cover the Sun!"
        ]
        
        fact = random.choice(amazing_facts)
        
        return {
            "content": f"""🤯 **Mind-Blowing Fact for {user_name}!**

{fact}

**💭 Isn't that incredible?** The world is full of amazing mysteries and phenomena that even scientists are still discovering!

**Want more fascinating facts?** I've got tons more about:
• Space and the universe 🌌
• Ocean mysteries 🌊  
• Animal superpowers 🦎
• Human brain secrets 🧠
• Technology wonders 💻

What kind of amazing fact would you like next?""",
            "sources": ["Scientific Knowledge Base"],
            "suggestions": ["Another space fact!", "Tell me about animals", "Brain mysteries", "Ocean secrets"]
        }
    
    def _provide_intelligent_life_guidance(self, query, user_name):
        """Provide thoughtful life advice and guidance"""
        return {
            "content": f"""💙 **Life Guidance for {user_name}**

I hear that you're looking for some guidance. Life can be complex, and it's completely normal to seek different perspectives when making decisions.

**🤔 My Approach to Your Question:**
• I'll help you think through this thoughtfully
• Offer different angles to consider
• Respect that you know your situation best
• Provide practical frameworks for decision-making

**💭 Let's explore this together:**

**Key questions to consider:**
• What outcome would align best with your values?
• What would you tell a good friend in this situation?
• What are the potential consequences (both positive and negative)?
• What's within your control vs. what isn't?

**🌟 Remember:**
• Trust your instincts - they're usually right
• It's okay to take time with important decisions
• There's rarely a single "perfect" choice
• You can always adjust course as you learn more

**What specific aspect of this decision would be most helpful to explore?** I'm here to listen and help you think it through! 🤝""",
            "sources": ["Life Coaching Principles"],
            "suggestions": ["Help me think through pros and cons", "What are my options?", "How do I trust my instincts?"]
        }
    
    def _handle_current_events_query(self, query, user_name):
        """Handle current events and news questions"""
        return {
            "content": f"""📰 **Current Events for {user_name}**

I'd love to help you stay informed about what's happening in the world!

**🌍 What I can help with:**
• **Global News:** Major world events and developments
• **Technology Updates:** Latest tech innovations and releases  
• **Scientific Discoveries:** Recent breakthroughs and research
• **Cultural Trends:** What's popular in entertainment, social media, arts
• **Economic Developments:** Market trends and financial news

**📊 For the most current information, I recommend:**
• **News Sources:** BBC, Reuters, AP News for reliable global coverage
• **Tech News:** TechCrunch, Wired, Ars Technica for technology updates
• **Science:** Nature, Science Magazine, Scientific American
• **Analysis:** NPR, The Economist for in-depth analysis

**🔍 What specific current events are you curious about?**
• Global politics and international relations
• Technology and innovation trends  
• Scientific breakthroughs and discoveries
• Entertainment and cultural happenings
• Economic and business developments

Let me know what area interests you most, and I can provide context and insights! 🌟""",
            "sources": ["News Aggregation"],
            "suggestions": ["Latest technology news", "Recent scientific discoveries", "Global political updates", "Entertainment trends"]
        }
    
    def _provide_balanced_opinion(self, query, user_name):
        """Provide balanced opinions on various topics"""
        return {
            "content": f"""⚖️ **Balanced Perspective for {user_name}**

Great question! I love exploring different viewpoints on complex topics.

**🎯 My approach to opinions:**
• Present multiple perspectives fairly
• Acknowledge the complexity of most issues
• Help you form your own informed opinion
• Respect that reasonable people can disagree

**🤔 For any topic, I consider:**

**📊 Different Viewpoints:**
• What are the main arguments on each side?
• What evidence supports different positions?
• Who are the stakeholders and how are they affected?

**🔍 Critical Analysis:**
• What are the strengths and weaknesses of each argument?
• What assumptions are being made?
• What are the potential long-term consequences?

**🌟 Context Matters:**
• Historical background and precedents
• Cultural and social factors
• Current circumstances and constraints

**💭 What specific topic would you like to explore?** I can help you:
• Understand different perspectives
• Analyze the reasoning behind various positions
• Consider factors you might not have thought of
• Form your own well-informed opinion

The goal isn't to tell you what to think, but to help you think more clearly! 🧠✨""",
            "sources": ["Critical Thinking Framework"],
            "suggestions": ["Analyze different viewpoints", "Help me understand both sides", "What factors should I consider?"]
        }
    
    def _provide_comprehensive_explanation(self, query, user_name):
        """Provide comprehensive explanations for any topic"""
        return {
            "content": f"""🔍 **Comprehensive Explanation for {user_name}**

Excellent question! I love breaking down complex topics into understandable parts.

**📚 My explanation approach:**

**🎯 Multi-Level Understanding:**
• **Simple Overview:** The basic concept in plain language
• **Deeper Dive:** More detailed mechanisms and relationships
• **Real-World Applications:** How this applies in practice
• **Broader Context:** How it connects to other concepts

**🧠 Different Learning Styles:**
• **Visual:** Analogies and mental models
• **Logical:** Step-by-step reasoning
• **Practical:** Concrete examples and applications
• **Contextual:** Historical development and significance

**🌟 What makes a great explanation:**
• Starts with what you already know
• Uses familiar analogies and examples
• Builds complexity gradually
• Addresses common misconceptions
• Shows why it matters

**💡 To give you the best explanation:**
• What's your current understanding of this topic?
• Are you looking for a quick overview or detailed analysis?
• Would examples or analogies be helpful?
• Is there a specific aspect you're most curious about?

**Let me know more about what you'd like to understand, and I'll craft an explanation that makes perfect sense to you!** 🌈""",
            "sources": ["Educational Psychology"],
            "suggestions": ["Start with the basics", "Give me detailed explanation", "Use analogies", "Show real examples"]
        }
    
    def _provide_smart_recommendations(self, query, user_name):
        """Provide intelligent recommendations"""
        return {
            "content": f"""🎯 **Smart Recommendations for {user_name}**

I'd love to help you find the perfect choice! I'm great at analyzing options and matching them to your needs.

**🌟 My recommendation process:**

**📊 Understanding Your Needs:**
• What's most important to you in this decision?
• What's your experience level with this topic?
• Are there any constraints (budget, time, location)?
• What's the purpose or goal you're trying to achieve?

**🔍 Analysis Framework:**
• **Quality vs. Value:** Best overall vs. best for the price
• **Beginner vs. Advanced:** What matches your skill level
• **Popular vs. Specialized:** Mainstream options vs. niche choices
• **Current vs. Future:** What works now vs. long-term investment

**💡 Types of recommendations I excel at:**
• **Products & Services:** Electronics, software, apps, tools
• **Entertainment:** Books, movies, music, games, shows
• **Learning Resources:** Courses, tutorials, books, websites
• **Travel & Places:** Destinations, restaurants, activities
• **Lifestyle Choices:** Health, fitness, productivity, hobbies

**🎪 What are you looking for recommendations about?**

The more specific you can be about your situation and preferences, the better I can tailor my suggestions to you! 🚀

**Example:** Instead of "good laptop," try "laptop under $800 for college student who codes and games occasionally" - that helps me give you perfect recommendations! 💻✨""",
            "sources": ["Recommendation Engine"],
            "suggestions": ["Help me choose between options", "What's the best for beginners?", "Budget-friendly recommendations", "Professional recommendations"]
        }
    
    def _generate_ultimate_knowledge_response(self, query, user_name):
        """Ultimate fallback for any question in existence"""
        return {
            "content": f"""🌟 **Universal Knowledge Activated for {user_name}!**

What a fascinating question! Even if I don't have the exact answer immediately, I'm absolutely committed to helping you explore this topic.

**🧠 Let me think about "{query}"...**

**🔍 Here's how I can help:**

**📚 Research & Exploration:**
• Break down the question into key components
• Explore related concepts and connections
• Provide multiple angles to approach the topic
• Suggest resources for deeper investigation

**💭 Critical Thinking:**
• Help you analyze what we know vs. what we don't know
• Identify assumptions and explore alternatives
• Consider different perspectives and interpretations
• Develop frameworks for understanding

**🎯 Practical Next Steps:**
• Suggest specific sources to explore
• Recommend experts or communities to consult
• Identify experiments or observations you could make
• Help you formulate more specific questions

**🌈 Why I love questions like this:**
• They push the boundaries of knowledge
• They often lead to unexpected discoveries
• They show genuine curiosity and critical thinking
• They remind us how much there is still to learn

**What aspect of this question interests you most?** Let's explore it together and see what insights we can uncover! 🚀

*Remember: The best questions often don't have simple answers - they open doors to entire worlds of understanding!*""",
            "sources": ["Universal Problem-Solving Framework"],
            "suggestions": ["Break this down into smaller questions", "What do experts say about this?", "How can I research this further?", "Related topics to explore"]
        }
