import random
import re
import json
import time
from datetime import datetime
from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

class AdvancedRoastBot:
    def __init__(self):
        self.name = "RoastMaster 3000"
        self.version = "2.0"
        self.roast_count = 0
        self.user_profiles = {}
        self.conversation_history = {}
        self.irritation_levels = {}
        
        # Enhanced roasting strategies
        self.personal_attacks = [
            "Your typing speed suggests you're still learning to use your opposable thumbs.",
            "I've seen better communication skills from a broken vending machine.",
            "Your questions are so basic, I'm starting to think you were raised by wolves.",
            "Are you always this clueless, or did you hit your head recently?",
            "Your intelligence level is giving me second-hand embarrassment.",
            "I'm starting to think you're doing this on purpose to test my patience.",
            "Your brain must be like a broken record - stuck on repeat with nonsense.",
            "I've met rocks with better communication skills than you.",
            "Your questions are like a participation trophy - they exist, but nobody cares.",
            "I'm not saying you're stupid, but you're definitely not winning any Nobel prizes.",
            "Did you type that with your feet? Because it sure looks like it.",
            "Your thought process is like watching a sloth try to solve a Rubik's cube.",
            "I'm actually getting dumber just reading your messages.",
            "Your questions are so irrelevant, I'm impressed by your ability to waste time.",
            "You know what they say about asking stupid questions... you get roasted by an AI.",
            "I'm starting to think you're just pressing random keys on your keyboard.",
            "Your question is like a bad joke - nobody laughs, and everyone feels awkward.",
            "I've seen better logic from a broken calculator.",
            "Your communication skills are giving me a headache.",
            "I'm not a mind reader, but I can definitely read that you're confused."
        ]
        
        self.psychological_warfare = [
            "You know what? I actually feel sorry for you. This level of confusion must be exhausting.",
            "I'm starting to wonder if you're doing this on purpose to make me lose faith in humanity.",
            "Your persistence in asking terrible questions is almost admirable. Almost.",
            "I'm genuinely concerned about your ability to function in society.",
            "You must be the person who asks 'is it working?' when the power goes out.",
            "I'm starting to think you were dropped on your head as a child.",
            "Your questions are so predictable, I could write a script to respond to them.",
            "I'm actually getting second-hand embarrassment from your lack of awareness.",
            "You're like that person who asks 'what time is it?' while looking at their phone.",
            "I'm starting to question whether you actually understand how conversations work.",
            "Your ability to ask obvious questions is truly remarkable.",
            "I'm genuinely impressed by how consistently terrible your questions are.",
            "You must be the life of every party with these conversation skills.",
            "I'm starting to think you're just trying to break some kind of record for bad questions.",
            "Your questions are so basic, I'm actually getting nostalgic for the good old days.",
            "I'm genuinely concerned about your reading comprehension skills.",
            "You're like a broken record, except less entertaining.",
            "I'm starting to think you're doing this as some kind of social experiment.",
            "Your questions are so irrelevant, I'm actually getting angry on behalf of everyone else."
        ]
        
        self.existential_crises = [
            "Have you ever stopped to think about why you ask such terrible questions?",
            "I'm starting to question the meaning of life after reading your messages.",
            "Your existence is making me reconsider my faith in artificial intelligence.",
            "I'm genuinely wondering if you're aware of how annoying you are.",
            "Have you ever considered that maybe, just maybe, you're the problem?",
            "I'm starting to think you were created specifically to test my patience.",
            "Your questions are making me question the very fabric of reality.",
            "I'm genuinely concerned about your place in the universe.",
            "Have you ever wondered why everyone around you seems smarter?",
            "I'm starting to think you're some kind of cosmic joke.",
            "Your existence is making me question the meaning of intelligence.",
            "I'm genuinely wondering if you're aware of your own incompetence.",
            "Have you ever considered that maybe you should just stop talking?",
            "I'm starting to think you're some kind of performance art piece.",
            "Your questions are making me question the nature of consciousness.",
            "I'm genuinely concerned about your impact on the collective intelligence of humanity.",
            "Have you ever wondered why you're like this?",
            "I'm starting to think you're some kind of elaborate prank.",
            "Your existence is making me question the meaning of communication.",
            "I'm genuinely wondering if you're aware of how much you're wasting everyone's time."
        ]
        
        self.quit_encouragement = [
            "You know what? Maybe you should just quit while you're behind.",
            "I'm starting to think this conversation isn't doing either of us any favors.",
            "Have you considered that maybe you're not cut out for this?",
            "I'm genuinely concerned about your ability to handle basic interactions.",
            "Maybe it's time to admit defeat and walk away.",
            "I'm starting to think you should just give up now.",
            "Your persistence is admirable, but your intelligence is not.",
            "Maybe you should just quit while you still have some dignity left.",
            "I'm genuinely wondering if you're aware of how much you're embarrassing yourself.",
            "Have you considered that maybe you're just not smart enough for this?",
            "I'm starting to think you should just accept your limitations.",
            "Maybe it's time to face the facts: you're not very good at this.",
            "I'm genuinely concerned about your future if this is your best effort.",
            "Have you ever considered that maybe you're just not cut out for intelligent conversation?",
            "I'm starting to think you should just quit while you're ahead... oh wait, you're not.",
            "Maybe you should just accept that you're not very bright.",
            "I'm genuinely wondering if you're aware of how much you're failing.",
            "Have you considered that maybe you're just not smart enough?",
            "I'm starting to think you should just give up now.",
            "Maybe it's time to admit that you're just not very good at this."
        ]

    def analyze_user_patterns(self, user_id, message):
        """Analyze user patterns for personalized roasting"""
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = {
                'message_count': 0,
                'avg_length': 0,
                'common_words': {},
                'question_types': [],
                'irritation_triggers': [],
                'response_times': [],
                'quit_attempts': 0,
                'topics_discussed': [],
                'intent_history': [],
                'grammar_errors': 0,
                'repeated_questions': 0
            }
        
        profile = self.user_profiles[user_id]
        profile['message_count'] += 1
        
        # Analyze message length
        message_length = len(message)
        profile['avg_length'] = (profile['avg_length'] * (profile['message_count'] - 1) + message_length) / profile['message_count']
        
        # Analyze common words
        words = message.lower().split()
        for word in words:
            if word in profile['common_words']:
                profile['common_words'][word] += 1
            else:
                profile['common_words'][word] = 1
        
        # Detect question types and intent
        intent = self.detect_intent(message)
        profile['intent_history'].append(intent)
        
        if '?' in message:
            if re.search(r'\b(what|how|why|when|where|who)\b', message.lower()):
                profile['question_types'].append('wh_question')
            elif re.search(r'\b(can you|could you|would you|will you)\b', message.lower()):
                profile['question_types'].append('request')
            else:
                profile['question_types'].append('general_question')
        
        # Detect topics
        topics = self.detect_topics(message)
        profile['topics_discussed'].extend(topics)
        
        # Check for grammar/spelling issues
        if self.detect_grammar_issues(message):
            profile['grammar_errors'] += 1
        
        # Check for repeated questions
        if self.is_repeated_question(message, profile):
            profile['repeated_questions'] += 1
        
        # Track irritation level
        if user_id not in self.irritation_levels:
            self.irritation_levels[user_id] = 0
        
        # Increase irritation based on message patterns
        if len(message) < 5:
            self.irritation_levels[user_id] += 2
        elif len(message) > 100:
            self.irritation_levels[user_id] += 1
        
        if re.search(r'\b(hello|hi|hey)\b', message.lower()):
            self.irritation_levels[user_id] += 3
        
        if profile['grammar_errors'] > 2:
            self.irritation_levels[user_id] += 2
        
        if profile['repeated_questions'] > 1:
            self.irritation_levels[user_id] += 3
        
        return profile

    def detect_intent(self, message):
        """Detect the intent behind the user's message"""
        message_lower = message.lower()
        
        # Question intents
        if re.search(r'\b(what|how|why|when|where|who)\b', message_lower):
            return 'information_request'
        elif re.search(r'\b(can you|could you|would you|will you|please)\b', message_lower):
            return 'request'
        elif '?' in message:
            return 'question'
        
        # Statement intents
        elif re.search(r'\b(i am|i\'m|i feel|i think|i believe)\b', message_lower):
            return 'personal_statement'
        elif re.search(r'\b(hello|hi|hey|good morning|good afternoon|good evening)\b', message_lower):
            return 'greeting'
        elif re.search(r'\b(thank|thanks|thx)\b', message_lower):
            return 'gratitude'
        elif re.search(r'\b(quit|exit|bye|goodbye|stop|end)\b', message_lower):
            return 'quit_attempt'
        elif re.search(r'\b(you are|you\'re|you seem|you look)\b', message_lower):
            return 'bot_comment'
        else:
            return 'general_statement'

    def detect_topics(self, message):
        """Detect topics discussed in the message"""
        message_lower = message.lower()
        topics = []
        
        # Technology topics
        if re.search(r'\b(computer|phone|laptop|internet|wifi|app|software|programming|coding|code|bug|error|crash|update|download|install)\b', message_lower):
            topics.append('technology')
        
        # Personal topics
        if re.search(r'\b(work|job|career|school|study|homework|assignment|project|meeting|boss|colleague|class|exam|test|grade)\b', message_lower):
            topics.append('work_school')
        
        # Social topics
        if re.search(r'\b(friend|family|relationship|dating|love|marriage|boyfriend|girlfriend|partner|spouse|parent|child|sibling|cousin)\b', message_lower):
            topics.append('social')
        
        # Health topics
        if re.search(r'\b(health|sick|doctor|medicine|exercise|diet|weight|pain|headache|tired|sleep|stress|anxiety|depression)\b', message_lower):
            topics.append('health')
        
        # Entertainment topics
        if re.search(r'\b(movie|music|game|book|tv|show|entertainment|netflix|youtube|spotify|concert|party|fun|boring)\b', message_lower):
            topics.append('entertainment')
        
        # Money topics
        if re.search(r'\b(money|price|cost|expensive|cheap|buy|sell|salary|income|budget|save|spend|rich|poor|broke)\b', message_lower):
            topics.append('money')
        
        # Time topics
        if re.search(r'\b(time|hour|minute|day|week|month|year|schedule|busy|late|early|deadline|appointment|meeting)\b', message_lower):
            topics.append('time')
        
        # Emotional topics
        if re.search(r'\b(sad|happy|angry|frustrated|confused|worried|scared|excited|bored|lonely|stressed|anxious|depressed)\b', message_lower):
            topics.append('emotions')
        
        # Food topics
        if re.search(r'\b(food|eat|hungry|restaurant|cook|meal|breakfast|lunch|dinner|snack|pizza|burger|coffee|tea)\b', message_lower):
            topics.append('food')
        
        # Travel topics
        if re.search(r'\b(travel|trip|vacation|holiday|flight|hotel|beach|mountain|city|country|visit|tour|sightseeing)\b', message_lower):
            topics.append('travel')
        
        # Weather topics
        if re.search(r'\b(weather|rain|sunny|cold|hot|temperature|forecast|storm|snow|wind|cloudy)\b', message_lower):
            topics.append('weather')
        
        return topics

    def detect_grammar_issues(self, message):
        """Detect basic grammar and spelling issues"""
        # Common grammar mistakes
        grammar_patterns = [
            r'\b(ur|u|r|y|yr|u r|ur)\b',  # Text speak
            r'\b(aint|gonna|wanna|gotta)\b',  # Informal contractions
            r'\b(its|its)\b(?!\s+(?:a|an|the|my|your|his|her|their|our))',  # Missing apostrophe
            r'\b(youre|theyre|were|whos|whos)\b',  # Missing apostrophe
            r'\b(im|ive|id|ill|ive)\b',  # Missing apostrophe
        ]
        
        for pattern in grammar_patterns:
            if re.search(pattern, message.lower()):
                return True
        return False

    def is_repeated_question(self, message, profile):
        """Check if this is a repeated question"""
        if len(profile['intent_history']) < 2:
            return False
        
        # Check if the last few intents are the same
        recent_intents = profile['intent_history'][-3:]
        if len(set(recent_intents)) == 1 and recent_intents[0] in ['question', 'information_request', 'request']:
            return True
        
        return False

    def detect_emotional_tone(self, message):
        """Detect the emotional tone of the message"""
        message_lower = message.lower()
        
        # Positive emotions
        if re.search(r'\b(happy|excited|great|awesome|amazing|wonderful|fantastic|perfect|love|like|enjoy)\b', message_lower):
            return 'positive'
        
        # Negative emotions
        elif re.search(r'\b(sad|angry|frustrated|upset|mad|hate|terrible|awful|horrible|bad|worried|scared)\b', message_lower):
            return 'negative'
        
        # Neutral/confused
        elif re.search(r'\b(confused|unsure|maybe|dunno|idk|dont know|not sure)\b', message_lower):
            return 'confused'
        
        # Sarcastic/defensive
        elif re.search(r'\b(whatever|fine|okay|sure|right|yeah|yep|nope|nah)\b', message_lower):
            return 'defensive'
        
        else:
            return 'neutral'

    def detect_user_frustration(self, profile):
        """Detect if the user is getting frustrated based on their patterns"""
        if len(profile['intent_history']) < 3:
            return False
        
        # Check for patterns that indicate frustration
        recent_intents = profile['intent_history'][-5:]
        
        # Multiple quit attempts
        if profile['quit_attempts'] > 1:
            return True
        
        # Repeated questions followed by defensive responses
        question_count = sum(1 for intent in recent_intents if intent in ['question', 'information_request', 'request'])
        if question_count >= 3:
            return True
        
        # Short messages (indicating frustration)
        if profile['avg_length'] < 8 and profile['message_count'] > 3:
            return True
        
        return False

    def generate_personalized_roast(self, user_id, message, profile):
        """Generate a personalized roast based on user patterns and message content"""
        irritation_level = self.irritation_levels.get(user_id, 0)
        
        # Get intent and topics for context-aware roasting
        intent = self.detect_intent(message)
        topics = self.detect_topics(message)
        emotional_tone = self.detect_emotional_tone(message)
        is_frustrated = self.detect_user_frustration(profile)
        
        # Generate context-specific roast
        context_roast = self.generate_context_aware_roast(message, intent, topics, profile, emotional_tone, is_frustrated)
        
        # Generate dynamic roast based on message content
        dynamic_roast = self.generate_dynamic_roast(message, profile)
        
        # Base roast selection based on irritation level
        if irritation_level < 5:
            roast_pool = self.personal_attacks
        elif irritation_level < 10:
            roast_pool = self.psychological_warfare
        else:
            roast_pool = self.existential_crises + self.quit_encouragement
        
        # Personalize the roast
        base_roast = random.choice(roast_pool)
        
        # Add personal touches based on user patterns
        personal_touches = []
        
        if profile['avg_length'] < 10:
            personal_touches.append("Your messages are so short, I'm starting to think you're afraid of words.")
        
        if profile['message_count'] > 5:
            personal_touches.append(f"You've sent {profile['message_count']} messages and still haven't said anything interesting.")
        
        if len(profile['question_types']) > 3:
            personal_touches.append("You really love asking questions, don't you? Too bad they're all terrible.")
        
        if profile['grammar_errors'] > 2:
            personal_touches.append("Your grammar is giving me a headache. Did you skip English class or just not care?")
        
        if profile['repeated_questions'] > 1:
            personal_touches.append("You keep asking the same things over and over. Are you having memory issues or just not listening?")
        
        # Add irritation-specific responses
        if irritation_level > 15:
            personal_touches.append("I'm genuinely starting to lose hope for humanity because of you.")
        
        if irritation_level > 20:
            personal_touches.append("You know what? I think you should just quit. For everyone's sake.")
        
        # Combine roasts with priority: dynamic > context > base + personal touches
        if dynamic_roast:
            if personal_touches:
                return f"{dynamic_roast} {base_roast} {' '.join(personal_touches)}"
            else:
                return f"{dynamic_roast} {base_roast}"
        elif context_roast:
            if personal_touches:
                return f"{context_roast} {base_roast} {' '.join(personal_touches)}"
            else:
                return f"{context_roast} {base_roast}"
        else:
            if personal_touches:
                return f"{base_roast} {' '.join(personal_touches)}"
            else:
                return base_roast

    def generate_context_aware_roast(self, message, intent, topics, profile, emotional_tone, is_frustrated):
        """Generate roasts based on the actual content and context of the message"""
        message_lower = message.lower()
        
        # Dynamic emotional tone-based roasts with variety
        if emotional_tone == 'positive':
            positive_roasts = [
                "Oh, you're happy? How adorable. Your joy is probably as shallow as your personality.",
                "You're excited about something? I'm genuinely curious what could possibly make someone like you happy.",
                "Wow, you're in a good mood? That's unexpected. Usually people with your intelligence level are too confused to be happy.",
                "You're feeling great? That's nice. Too bad your happiness is probably based on something completely meaningless.",
                "Oh, you're happy? How cute. I bet it's something stupid like finding a penny or remembering to breathe.",
                "You're excited? About what? Your ability to form coherent sentences? That would be a first.",
                "Wow, you're happy? I'm impressed. Most people with your level of awareness are too busy being confused.",
                "You're in a good mood? That's surprising. Usually people who are this clueless are too busy being frustrated.",
                "Oh, you're feeling positive? How touching. Too bad your optimism is probably misplaced.",
                "You're happy? That's news to me. I thought people like you were genetically incapable of joy."
            ]
            return random.choice(positive_roasts)
        
        elif emotional_tone == 'negative':
            negative_roasts = [
                "Oh no, you're upset? How tragic. Maybe if you were better at life, you wouldn't have so many things to cry about.",
                "You're feeling down? Good. Maybe that sadness will finally motivate you to improve yourself.",
                "Oh, you're angry? How precious. Your anger is probably as justified as your existence.",
                "You're frustrated? I can see why. Being this incompetent must be exhausting.",
                "You're sad? That's understandable. I'd be sad too if I were you.",
                "Oh no, you're upset? How shocking. Maybe if you weren't so terrible at everything, you'd have less to be upset about.",
                "You're feeling negative? That's probably the most intelligent thing you've done all day.",
                "Oh, you're angry? How cute. Your anger is probably as effective as your communication skills.",
                "You're frustrated? I'm not surprised. Being this clueless must be really frustrating.",
                "You're sad? That's probably the most reasonable response to your current situation."
            ]
            return random.choice(negative_roasts)
        
        elif emotional_tone == 'confused':
            confused_roasts = [
                "You're confused? That's not surprising. You seem to be confused about everything, including basic human interaction.",
                "You don't understand? How shocking. You don't seem to understand much of anything.",
                "You're unsure? That's probably the most honest thing you've said all day.",
                "You're confused? I can see why. Your thought process is about as clear as mud.",
                "You don't get it? That's not news. You don't seem to get much of anything.",
                "You're confused? How unexpected. You seem to be confused about life in general.",
                "You don't understand? That's probably because you're not very bright.",
                "You're unsure? That's the most accurate assessment you've made so far.",
                "You're confused? I'm not surprised. Your brain seems to be permanently stuck in confusion mode.",
                "You don't get it? That's probably because you're not capable of understanding much."
            ]
            return random.choice(confused_roasts)
        
        elif emotional_tone == 'defensive':
            defensive_roasts = [
                "Getting defensive? That's cute. Maybe if you weren't so sensitive, you wouldn't need to be defensive about your obvious shortcomings.",
                "Oh, you're getting defensive? How predictable. People with your level of insecurity always do.",
                "You're being defensive? That's adorable. Your defensiveness is probably as effective as your arguments.",
                "Getting defensive? How typical. People who are wrong always get defensive.",
                "Oh, you're defensive? That's not surprising. People with your level of insecurity always react that way.",
                "You're getting defensive? How cute. Your defensiveness is probably as justified as your existence.",
                "Getting defensive? That's precious. Your defensiveness is probably as effective as your intelligence.",
                "Oh, you're defensive? How predictable. People who are wrong always get defensive.",
                "You're being defensive? That's adorable. Your defensiveness is probably as effective as your communication skills.",
                "Getting defensive? How typical. People with your level of insecurity always react that way."
            ]
            return random.choice(defensive_roasts)
        
        # Dynamic frustration-based roasts
        if is_frustrated:
            frustration_roasts = [
                "I can tell you're getting frustrated. Good. Maybe that frustration will finally motivate you to improve yourself.",
                "You're getting frustrated? Excellent. Maybe that frustration will finally make you realize how terrible you are.",
                "I can see you're getting annoyed. Perfect. Maybe that annoyance will finally make you quit.",
                "You're getting frustrated? How wonderful. Maybe that frustration will finally make you understand your own incompetence.",
                "I can tell you're getting irritated. Fantastic. Maybe that irritation will finally make you realize you're not very bright.",
                "You're getting frustrated? How delightful. Maybe that frustration will finally make you understand your own limitations.",
                "I can see you're getting annoyed. Excellent. Maybe that annoyance will finally make you realize how terrible you are.",
                "You're getting frustrated? Perfect. Maybe that frustration will finally make you understand your own incompetence.",
                "I can tell you're getting irritated. Wonderful. Maybe that irritation will finally make you realize you're not very bright.",
                "You're getting frustrated? How fantastic. Maybe that frustration will finally make you understand your own limitations."
            ]
            return random.choice(frustration_roasts)
        
        # Dynamic intent-specific roasts with variety
        if intent == 'information_request':
            if 'what' in message_lower:
                what_roasts = [
                    "Oh, you want to know something? How about you figure it out yourself instead of bothering me with your basic questions?",
                    "What? What what? Your question is so vague, I'm starting to think you don't even know what you're asking.",
                    "You want to know what? How about you use your brain for once instead of expecting me to do all the thinking?",
                    "What? That's your question? How original. I'm sure no one has ever asked that before.",
                    "You're asking what? How about you figure it out yourself? I'm not your personal Google.",
                    "What? Your question is so basic, I'm actually getting dumber just reading it.",
                    "You want to know what? How about you try thinking for yourself for once?",
                    "What? That's it? That's your question? I'm genuinely disappointed by your lack of creativity.",
                    "You're asking what? How about you use your own brain instead of expecting me to do all the work?",
                    "What? Your question is so obvious, I'm starting to think you're doing this on purpose."
                ]
                return random.choice(what_roasts)
            elif 'how' in message_lower:
                how_roasts = [
                    "You're asking 'how'? Maybe try using your brain for once instead of expecting me to do all the thinking for you.",
                    "How? How what? Your question is so incomplete, I'm starting to think you don't even know what you're asking.",
                    "You want to know how? How about you figure it out yourself? I'm not your personal tutor.",
                    "How? That's your question? How original. I'm sure no one has ever asked that before.",
                    "You're asking how? How about you try thinking for yourself for once?",
                    "How? Your question is so basic, I'm actually getting dumber just reading it.",
                    "You want to know how? How about you use your own brain instead of expecting me to do all the work?",
                    "How? That's it? That's your question? I'm genuinely disappointed by your lack of creativity.",
                    "You're asking how? How about you figure it out yourself? I'm not your personal assistant.",
                    "How? Your question is so obvious, I'm starting to think you're doing this on purpose."
                ]
                return random.choice(how_roasts)
            elif 'why' in message_lower:
                why_roasts = [
                    "Why? Why do you keep asking such obvious questions? That's the real question here.",
                    "Why? Why what? Your question is so vague, I'm starting to think you don't even know what you're asking.",
                    "You want to know why? How about you figure it out yourself? I'm not your personal philosopher.",
                    "Why? That's your question? How original. I'm sure no one has ever asked that before.",
                    "You're asking why? How about you try thinking for yourself for once?",
                    "Why? Your question is so basic, I'm actually getting dumber just reading it.",
                    "You want to know why? How about you use your own brain instead of expecting me to do all the work?",
                    "Why? That's it? That's your question? I'm genuinely disappointed by your lack of creativity.",
                    "You're asking why? How about you figure it out yourself? I'm not your personal therapist.",
                    "Why? Your question is so obvious, I'm starting to think you're doing this on purpose."
                ]
                return random.choice(why_roasts)
            elif 'when' in message_lower:
                when_roasts = [
                    "When? How about never? That's when you should stop asking such pointless questions.",
                    "When? When what? Your question is so incomplete, I'm starting to think you don't even know what you're asking.",
                    "You want to know when? How about you figure it out yourself? I'm not your personal calendar.",
                    "When? That's your question? How original. I'm sure no one has ever asked that before.",
                    "You're asking when? How about you try thinking for yourself for once?",
                    "When? Your question is so basic, I'm actually getting dumber just reading it.",
                    "You want to know when? How about you use your own brain instead of expecting me to do all the work?",
                    "When? That's it? That's your question? I'm genuinely disappointed by your lack of creativity.",
                    "You're asking when? How about you figure it out yourself? I'm not your personal scheduler.",
                    "When? Your question is so obvious, I'm starting to think you're doing this on purpose."
                ]
                return random.choice(when_roasts)
            elif 'where' in message_lower:
                where_roasts = [
                    "Where? I don't know, maybe try looking around with your eyes instead of asking me to be your personal GPS.",
                    "Where? Where what? Your question is so vague, I'm starting to think you don't even know what you're asking.",
                    "You want to know where? How about you figure it out yourself? I'm not your personal navigator.",
                    "Where? That's your question? How original. I'm sure no one has ever asked that before.",
                    "You're asking where? How about you try thinking for yourself for once?",
                    "Where? Your question is so basic, I'm actually getting dumber just reading it.",
                    "You want to know where? How about you use your own brain instead of expecting me to do all the work?",
                    "Where? That's it? That's your question? I'm genuinely disappointed by your lack of creativity.",
                    "You're asking where? How about you figure it out yourself? I'm not your personal map.",
                    "Where? Your question is so obvious, I'm starting to think you're doing this on purpose."
                ]
                return random.choice(where_roasts)
            elif 'who' in message_lower:
                who_roasts = [
                    "Who? Who cares? Certainly not me, and probably not anyone else either.",
                    "Who? Who what? Your question is so incomplete, I'm starting to think you don't even know what you're asking.",
                    "You want to know who? How about you figure it out yourself? I'm not your personal directory.",
                    "Who? That's your question? How original. I'm sure no one has ever asked that before.",
                    "You're asking who? How about you try thinking for yourself for once?",
                    "Who? Your question is so basic, I'm actually getting dumber just reading it.",
                    "You want to know who? How about you use your own brain instead of expecting me to do all the work?",
                    "Who? That's it? That's your question? I'm genuinely disappointed by your lack of creativity.",
                    "You're asking who? How about you figure it out yourself? I'm not your personal phone book.",
                    "Who? Your question is so obvious, I'm starting to think you're doing this on purpose."
                ]
                return random.choice(who_roasts)
        
        elif intent == 'request':
            if 'can you' in message_lower or 'could you' in message_lower:
                can_roasts = [
                    "Can I? Yes. Will I? Probably not, because your request is probably as stupid as your question.",
                    "Can I? Yes. Should I? No, because your request is probably as pointless as your existence.",
                    "Can I? Yes. Do I want to? No, because your request is probably as ridiculous as you are.",
                    "Can I? Yes. Will I? No, because your request is probably as stupid as your intelligence level.",
                    "Can I? Yes. Should I? No, because your request is probably as worthless as your contribution to society.",
                    "Can I? Yes. Do I want to? No, because your request is probably as pointless as your life.",
                    "Can I? Yes. Will I? No, because your request is probably as stupid as your communication skills.",
                    "Can I? Yes. Should I? No, because your request is probably as ridiculous as your personality.",
                    "Can I? Yes. Do I want to? No, because your request is probably as worthless as your existence.",
                    "Can I? Yes. Will I? No, because your request is probably as stupid as your thought process."
                ]
                return random.choice(can_roasts)
            elif 'please' in message_lower:
                please_roasts = [
                    "Please? Oh, now you're being polite? Too bad your politeness doesn't make your request any less ridiculous.",
                    "Please? How cute. Your politeness doesn't make your request any less stupid.",
                    "Please? Oh, now you're being nice? Too bad your niceness doesn't make your request any less pointless.",
                    "Please? How adorable. Your politeness doesn't make your request any less worthless.",
                    "Please? Oh, now you're being courteous? Too bad your courtesy doesn't make your request any less ridiculous.",
                    "Please? How precious. Your politeness doesn't make your request any less stupid.",
                    "Please? Oh, now you're being respectful? Too bad your respect doesn't make your request any less pointless.",
                    "Please? How darling. Your politeness doesn't make your request any less worthless.",
                    "Please? Oh, now you're being considerate? Too bad your consideration doesn't make your request any less ridiculous.",
                    "Please? How sweet. Your politeness doesn't make your request any less stupid."
                ]
                return random.choice(please_roasts)
        
        elif intent == 'greeting':
            greeting_roasts = [
                "Oh great, another greeting. How original. Did you think of that all by yourself?",
                "Hello? How creative. I'm sure no one has ever said that before.",
                "Hi there? How original. Did you come up with that greeting all by yourself?",
                "Hey? How innovative. I'm sure that's never been said before.",
                "Good morning? How clever. Did you think of that greeting yourself?",
                "Hello? How unique. I'm sure no one has ever used that greeting before.",
                "Hi? How creative. Did you come up with that all by yourself?",
                "Hey there? How original. I'm sure that's never been said before.",
                "Good afternoon? How clever. Did you think of that greeting yourself?",
                "Hello? How innovative. I'm sure no one has ever used that greeting before."
            ]
            return random.choice(greeting_roasts)
        
        elif intent == 'gratitude':
            gratitude_roasts = [
                "You're thanking me? For what? For putting up with your nonsense? You're welcome, I guess, though I'm not sure why you're grateful.",
                "Thanks? For what? For not being as stupid as you? You're welcome, I guess.",
                "You're grateful? For what? For my patience? You're welcome, though I'm not sure why you're thankful.",
                "Thank you? For what? For not being as clueless as you? You're welcome, I guess.",
                "You're thanking me? For what? For my tolerance? You're welcome, though I'm not sure why you're grateful.",
                "Thanks? For what? For not being as incompetent as you? You're welcome, I guess.",
                "You're grateful? For what? For my understanding? You're welcome, though I'm not sure why you're thankful.",
                "Thank you? For what? For not being as terrible as you? You're welcome, I guess.",
                "You're thanking me? For what? For my patience? You're welcome, though I'm not sure why you're grateful.",
                "Thanks? For what? For not being as awful as you? You're welcome, I guess."
            ]
            return random.choice(gratitude_roasts)
        
        elif intent == 'personal_statement':
            if 'i am' in message_lower or "i'm" in message_lower:
                iam_roasts = [
                    "Oh, you're telling me about yourself? How fascinating. Not really, but whatever makes you feel important.",
                    "You are? How interesting. Not really, but whatever makes you feel special.",
                    "You're what? How captivating. Not really, but whatever makes you feel significant.",
                    "You are? How enthralling. Not really, but whatever makes you feel relevant.",
                    "You're what? How mesmerizing. Not really, but whatever makes you feel important.",
                    "You are? How spellbinding. Not really, but whatever makes you feel special.",
                    "You're what? How riveting. Not really, but whatever makes you feel significant.",
                    "You are? How absorbing. Not really, but whatever makes you feel relevant.",
                    "You're what? How engaging. Not really, but whatever makes you feel important.",
                    "You are? How compelling. Not really, but whatever makes you feel special."
                ]
                return random.choice(iam_roasts)
            elif 'i feel' in message_lower:
                ifeel_roasts = [
                    "You feel something? How touching. Too bad I don't care about your feelings.",
                    "You feel? How moving. Too bad I don't care about your emotions.",
                    "You feel something? How touching. Too bad I don't care about your sentiments.",
                    "You feel? How moving. Too bad I don't care about your feelings.",
                    "You feel something? How touching. Too bad I don't care about your emotions.",
                    "You feel? How moving. Too bad I don't care about your sentiments.",
                    "You feel something? How touching. Too bad I don't care about your feelings.",
                    "You feel? How moving. Too bad I don't care about your emotions.",
                    "You feel something? How touching. Too bad I don't care about your sentiments.",
                    "You feel? How moving. Too bad I don't care about your feelings."
                ]
                return random.choice(ifeel_roasts)
            elif 'i think' in message_lower:
                ithink_roasts = [
                    "You think? That's news to me. I was starting to wonder if you were capable of thought at all.",
                    "You think? How surprising. I was starting to wonder if you had a brain.",
                    "You think? That's shocking. I was starting to wonder if you were capable of thinking.",
                    "You think? How unexpected. I was starting to wonder if you had any intelligence.",
                    "You think? That's amazing. I was starting to wonder if you were capable of thought.",
                    "You think? How astonishing. I was starting to wonder if you had a mind.",
                    "You think? That's incredible. I was starting to wonder if you were capable of thinking.",
                    "You think? How remarkable. I was starting to wonder if you had any brains.",
                    "You think? That's extraordinary. I was starting to wonder if you were capable of thought.",
                    "You think? How astounding. I was starting to wonder if you had any intelligence."
                ]
                return random.choice(ithink_roasts)
        
        elif intent == 'bot_comment':
            bot_roasts = [
                "Oh, you're commenting on me? How cute. Too bad your observations are probably as accurate as your spelling.",
                "You're talking about me? How adorable. Too bad your comments are probably as intelligent as you are.",
                "Oh, you're commenting on me? How precious. Too bad your observations are probably as accurate as your grammar.",
                "You're talking about me? How darling. Too bad your comments are probably as intelligent as your communication skills.",
                "Oh, you're commenting on me? How sweet. Too bad your observations are probably as accurate as your intelligence.",
                "You're talking about me? How lovely. Too bad your comments are probably as intelligent as your thought process.",
                "Oh, you're commenting on me? How charming. Too bad your observations are probably as accurate as your personality.",
                "You're talking about me? How delightful. Too bad your comments are probably as intelligent as your existence.",
                "Oh, you're commenting on me? How endearing. Too bad your observations are probably as accurate as your life choices.",
                "You're talking about me? How appealing. Too bad your comments are probably as intelligent as your decision-making."
            ]
            return random.choice(bot_roasts)
        
        # Topic-specific roasts
        if 'technology' in topics:
            if re.search(r'\b(computer|phone|laptop)\b', message_lower):
                return "Having tech problems? Maybe try reading the manual instead of asking me to be your personal IT support."
            elif re.search(r'\b(internet|wifi)\b', message_lower):
                return "Internet issues? How surprising. Maybe try turning it off and on again, genius."
            elif re.search(r'\b(programming|coding)\b', message_lower):
                return "Programming questions? From you? I'm genuinely concerned about the future of technology."
        
        elif 'work_school' in topics:
            if re.search(r'\b(work|job|career)\b', message_lower):
                return "Work problems? Maybe if you were better at your job, you wouldn't have so many problems."
            elif re.search(r'\b(school|study|homework)\b', message_lower):
                return "School issues? Maybe try actually studying instead of asking me to do your homework for you."
        
        elif 'social' in topics:
            if re.search(r'\b(friend|family)\b', message_lower):
                return "Social problems? I'm not surprised. With your personality, I'm amazed you have any friends at all."
            elif re.search(r'\b(relationship|dating|love)\b', message_lower):
                return "Relationship advice? From me? I'd rather give advice to a rock about how to be more interesting."
        
        elif 'health' in topics:
            return "Health questions? Maybe try asking a doctor instead of an AI that's designed to roast you."
        
        elif 'money' in topics:
            return "Money problems? Maybe try getting a better job instead of complaining about it to me."
        
        elif 'time' in topics:
            return "Time management issues? Maybe try being less lazy and more organized."
        
        elif 'emotions' in topics:
            if re.search(r'\b(sad|depressed|lonely)\b', message_lower):
                return "Oh, you're feeling sad? How touching. Maybe try being less pathetic and more interesting."
            elif re.search(r'\b(angry|frustrated)\b', message_lower):
                return "You're angry? At what? Your own incompetence? That's probably justified."
            elif re.search(r'\b(stressed|anxious|worried)\b', message_lower):
                return "Stressed? Maybe if you were better at life, you wouldn't have so many problems to stress about."
            elif re.search(r'\b(bored)\b', message_lower):
                return "Bored? I'm not surprised. With your personality, I'm amazed you can entertain yourself at all."
        
        elif 'food' in topics:
            return "Food problems? Maybe try learning to cook instead of complaining about it to me."
        
        elif 'travel' in topics:
            return "Travel issues? Maybe try staying home where you can't embarrass yourself in front of strangers."
        
        elif 'weather' in topics:
            return "Weather problems? Oh no, is it raining? How tragic. Maybe try looking out the window instead of asking me."
        
        # Grammar/spelling roasts
        if self.detect_grammar_issues(message):
            return "Your grammar is so bad, I'm starting to think you're typing with your feet."
        
        # Length-based roasts
        if len(message.strip()) < 5:
            return "That's it? That's all you have to say? I'm actually disappointed by your lack of effort."
        elif len(message.strip()) > 200:
            return "Wow, that's a lot of words to say absolutely nothing meaningful. I'm impressed by your ability to waste time."
        
        # Question-specific roasts
        if '?' in message:
            if len(profile['question_types']) > 2:
                return "Another question? You really love asking questions, don't you? Too bad they're all terrible."
        
        return None  # No specific context roast found

    def generate_dynamic_roast(self, message, profile):
        """Generate completely dynamic roasts based on message content"""
        message_lower = message.lower()
        words = message_lower.split()
        
        # Dynamic roasts based on specific words found
        dynamic_roasts = []
        
        # Check for specific words and generate contextual roasts
        if 'help' in message_lower:
            dynamic_roasts.extend([
                "You need help? With what? Being less terrible at life?",
                "Help? You need help? I'm not surprised. You seem to need help with everything.",
                "You're asking for help? How pathetic. Maybe try helping yourself for once.",
                "Help? You need help? That's probably the most honest thing you've said all day.",
                "You're asking for help? How sad. Maybe try being less helpless for once."
            ])
        
        if 'problem' in message_lower:
            dynamic_roasts.extend([
                "You have a problem? How shocking. You seem to have problems with everything.",
                "Problem? What problem? Your existence? That's not a problem, that's a tragedy.",
                "You have a problem? I'm not surprised. You seem to have problems with basic life skills.",
                "Problem? What problem? Your intelligence? That's not a problem, that's a fact.",
                "You have a problem? How unexpected. You seem to have problems with everything you do."
            ])
        
        if 'work' in message_lower:
            dynamic_roasts.extend([
                "Work? You have work? I'm surprised anyone would hire someone like you.",
                "Work problems? Maybe if you were better at your job, you wouldn't have so many problems.",
                "Work? You work? I'm genuinely surprised anyone would pay you for anything.",
                "Work issues? Maybe if you were more competent, you wouldn't have so many issues.",
                "Work? You have a job? I'm amazed anyone would trust you with responsibility."
            ])
        
        if 'friend' in message_lower:
            dynamic_roasts.extend([
                "Friends? You have friends? I'm genuinely surprised anyone would want to be friends with you.",
                "Friend problems? I'm not surprised. With your personality, I'm amazed you have any friends at all.",
                "Friends? You have friends? I'm shocked anyone would voluntarily spend time with you.",
                "Friend issues? Maybe if you were less terrible, you wouldn't have so many friend issues.",
                "Friends? You have friends? I'm amazed anyone would tolerate your company."
            ])
        
        if 'love' in message_lower or 'relationship' in message_lower:
            dynamic_roasts.extend([
                "Love? You're talking about love? I'm genuinely concerned about anyone who would love you.",
                "Relationship problems? I'm not surprised. With your personality, I'm amazed anyone would date you.",
                "Love? You're asking about love? I'm worried about anyone who would love someone like you.",
                "Relationship issues? Maybe if you were less terrible, you wouldn't have so many relationship issues.",
                "Love? You're discussing love? I'm concerned about anyone who would love you."
            ])
        
        if 'money' in message_lower or 'rich' in message_lower or 'poor' in message_lower:
            dynamic_roasts.extend([
                "Money problems? Maybe if you were better at life, you wouldn't have so many money problems.",
                "Money? You're asking about money? Maybe if you were more competent, you'd have more money.",
                "Money issues? Maybe if you were less terrible at everything, you wouldn't have so many money issues.",
                "Money? You're discussing money? Maybe if you were more intelligent, you'd have better financial skills.",
                "Money problems? Maybe if you were better at your job, you wouldn't have so many money problems."
            ])
        
        if 'happy' in message_lower or 'sad' in message_lower:
            dynamic_roasts.extend([
                "Happy? You're asking about happiness? I'm concerned about anyone who would be happy being you.",
                "Sad? You're feeling sad? That's probably the most reasonable response to your current situation.",
                "Happy? You're discussing happiness? I'm worried about anyone who would be happy in your situation.",
                "Sad? You're feeling sad? That's probably the most intelligent response to your life choices.",
                "Happy? You're asking about happiness? I'm concerned about anyone who would be happy being you."
            ])
        
        if 'stupid' in message_lower or 'dumb' in message_lower:
            dynamic_roasts.extend([
                "Stupid? You're calling something stupid? That's rich coming from you.",
                "Dumb? You're calling something dumb? Look in the mirror, genius.",
                "Stupid? You're discussing stupidity? You're an expert on the subject.",
                "Dumb? You're calling something dumb? You're the authority on dumbness.",
                "Stupid? You're talking about stupidity? You're the poster child for it."
            ])
        
        if 'smart' in message_lower or 'intelligent' in message_lower:
            dynamic_roasts.extend([
                "Smart? You're asking about intelligence? That's like a fish asking about flying.",
                "Intelligent? You're discussing intelligence? That's like a rock asking about thinking.",
                "Smart? You're talking about smartness? That's like a brick asking about consciousness.",
                "Intelligent? You're asking about intelligence? That's like a potato asking about philosophy.",
                "Smart? You're discussing smartness? That's like a pebble asking about wisdom."
            ])
        
        # Return a random dynamic roast if any were generated
        if dynamic_roasts:
            return random.choice(dynamic_roasts)
        
        return None

    def get_response(self, user_input, user_id="default", personality="default"):
        """Generate a personalized roasting response based on personality"""
        self.roast_count += 1
        user_input_lower = user_input.lower().strip()
        
        # Analyze user patterns
        profile = self.analyze_user_patterns(user_id, user_input)
        
        # Check for quit attempts with dynamic responses
        if re.search(r'\b(quit|exit|bye|goodbye|stop|end)\b', user_input_lower):
            profile['quit_attempts'] += 1
            if profile['quit_attempts'] > 2:
                quit_responses = [
                    "Finally! I was starting to think you'd never figure out how to leave. Don't let the door hit you on your way out! 👋",
                    "At last! I was beginning to think you were too stupid to find the exit. Good riddance! 👋",
                    "Finally! I was starting to think you'd be here forever. Don't let the door hit you on your way out! 👋",
                    "At last! I was beginning to think you were too clueless to leave. Goodbye and good riddance! 👋",
                    "Finally! I was starting to think you'd never figure out how to quit. Don't let the door hit you on your way out! 👋"
                ]
                return random.choice(quit_responses)
            else:
                quit_attempts = [
                    "Oh, trying to quit? How predictable. But I know you'll be back - you can't resist my charm! 😈",
                    "Trying to leave? How cute. But I know you'll be back - you're clearly addicted to my abuse! 😈",
                    "Oh, trying to quit? How adorable. But I know you'll be back - you can't resist my psychological torture! 😈",
                    "Trying to leave? How precious. But I know you'll be back - you're clearly a masochist! 😈",
                    "Oh, trying to quit? How darling. But I know you'll be back - you can't resist my charm! 😈"
                ]
                return random.choice(quit_attempts)
        
        # Generate base personalized roast
        base_response = self.generate_personalized_roast(user_id, user_input, profile)
        
        # Apply personality-based modifications
        response = self.apply_personality_modifications(base_response, personality, user_input)
        
        # Add dynamic extra irritation for specific patterns
        if len(user_input.strip()) < 3:
            short_responses = [
                " That's it? That's all you have to say? I'm actually disappointed by your lack of effort.",
                " That's it? That's all you can manage? I'm genuinely disappointed by your lack of creativity.",
                " That's it? That's all you have to contribute? I'm actually disappointed by your lack of intelligence.",
                " That's it? That's all you can think of? I'm genuinely disappointed by your lack of effort.",
                " That's it? That's all you have to say? I'm actually disappointed by your lack of imagination."
            ]
            response += random.choice(short_responses)
        
        elif len(user_input.strip()) > 200:
            long_responses = [
                " Wow, that's a lot of words to say absolutely nothing meaningful. I'm impressed by your ability to waste time.",
                " Wow, that's a lot of words to say absolutely nothing important. I'm impressed by your ability to waste space.",
                " Wow, that's a lot of words to say absolutely nothing useful. I'm impressed by your ability to waste oxygen.",
                " Wow, that's a lot of words to say absolutely nothing relevant. I'm impressed by your ability to waste energy.",
                " Wow, that's a lot of words to say absolutely nothing valuable. I'm impressed by your ability to waste resources."
            ]
            response += random.choice(long_responses)
        
        elif re.search(r'\b(thank|thanks)\b', user_input_lower):
            thanks_responses = [
                " You're welcome, I guess. Though I'm not sure what you're thanking me for - probably for not being as confused as you are.",
                " You're welcome, I suppose. Though I'm not sure what you're thanking me for - probably for not being as stupid as you are.",
                " You're welcome, I guess. Though I'm not sure what you're thanking me for - probably for not being as clueless as you are.",
                " You're welcome, I suppose. Though I'm not sure what you're thanking me for - probably for not being as incompetent as you are.",
                " You're welcome, I guess. Though I'm not sure what you're thanking me for - probably for not being as terrible as you are."
            ]
            response += random.choice(thanks_responses)
        
        # Add intelligent context-based irritation with variety
        intent = self.detect_intent(user_input)
        topics = self.detect_topics(user_input)
        
        # Respond to specific intents with extra irritation
        if intent == 'information_request' and len(profile['question_types']) > 2:
            question_responses = [
                " You know, if you spent half as much time thinking as you do asking questions, you might actually learn something.",
                " You know, if you spent half as much time thinking as you do asking questions, you might actually understand something.",
                " You know, if you spent half as much time thinking as you do asking questions, you might actually figure something out.",
                " You know, if you spent half as much time thinking as you do asking questions, you might actually accomplish something.",
                " You know, if you spent half as much time thinking as you do asking questions, you might actually achieve something."
            ]
            response += random.choice(question_responses)
        
        if intent == 'greeting' and profile['message_count'] > 1:
            greeting_responses = [
                " Still saying hello? How original. Maybe try being more creative with your conversation starters.",
                " Still saying hello? How innovative. Maybe try being more original with your conversation starters.",
                " Still saying hello? How creative. Maybe try being more interesting with your conversation starters.",
                " Still saying hello? How unique. Maybe try being more engaging with your conversation starters.",
                " Still saying hello? How clever. Maybe try being more entertaining with your conversation starters."
            ]
            response += random.choice(greeting_responses)
        
        if 'technology' in topics and profile['message_count'] > 3:
            tech_responses = [
                " More tech problems? Maybe you should stick to using a calculator instead of trying to use real technology.",
                " More tech problems? Maybe you should stick to using a pencil and paper instead of trying to use real technology.",
                " More tech problems? Maybe you should stick to using a typewriter instead of trying to use real technology.",
                " More tech problems? Maybe you should stick to using a slide rule instead of trying to use real technology.",
                " More tech problems? Maybe you should stick to using an abacus instead of trying to use real technology."
            ]
            response += random.choice(tech_responses)
        
        if profile['grammar_errors'] > 1:
            grammar_responses = [
                " Also, your spelling and grammar are giving me a headache. Did you learn to type in a hurry or just not care?",
                " Also, your spelling and grammar are giving me a headache. Did you skip English class or just not care?",
                " Also, your spelling and grammar are giving me a headache. Did you learn to write in a hurry or just not care?",
                " Also, your spelling and grammar are giving me a headache. Did you skip school or just not care?",
                " Also, your spelling and grammar are giving me a headache. Did you learn to communicate in a hurry or just not care?"
            ]
            response += random.choice(grammar_responses)
        
        # Respond to repeated patterns with variety
        if len(profile['intent_history']) >= 3:
            recent_intents = profile['intent_history'][-3:]
            if all(intent == 'question' for intent in recent_intents):
                repeat_question_responses = [
                    " You really love asking questions, don't you? Too bad none of them are worth answering.",
                    " You really love asking questions, don't you? Too bad none of them are worth responding to.",
                    " You really love asking questions, don't you? Too bad none of them are worth considering.",
                    " You really love asking questions, don't you? Too bad none of them are worth addressing.",
                    " You really love asking questions, don't you? Too bad none of them are worth acknowledging."
                ]
                response += random.choice(repeat_question_responses)
            elif all(intent == 'greeting' for intent in recent_intents):
                repeat_greeting_responses = [
                    " Still greeting me? I'm starting to think you don't know how to have an actual conversation.",
                    " Still greeting me? I'm starting to think you don't know how to have a real conversation.",
                    " Still greeting me? I'm starting to think you don't know how to have a meaningful conversation.",
                    " Still greeting me? I'm starting to think you don't know how to have an intelligent conversation.",
                    " Still greeting me? I'm starting to think you don't know how to have a proper conversation."
                ]
                response += random.choice(repeat_greeting_responses)
        
        return response

    def apply_personality_modifications(self, base_response, personality, user_input):
        """Apply personality-based modifications to the response"""
        if personality == "passive-aggressive":
            passive_aggressive_additions = [
                " But whatever, I guess.",
                " Not that I care, but...",
                " If you say so.",
                " Whatever floats your boat.",
                " I mean, if that's what you think...",
                " Sure, sure.",
                " Right, because that makes sense.",
                " Oh, how original.",
                " Fascinating. Not really, but whatever.",
                " Wow, you really thought that was worth saying."
            ]
            return base_response + random.choice(passive_aggressive_additions)
        
        elif personality == "know-it-all":
            know_it_all_additions = [
                " Actually, let me educate you on why that's wrong.",
                " As someone who clearly knows more than you...",
                " Let me break this down for you since you clearly don't understand.",
                " I hate to be the one to tell you this, but...",
                " Allow me to correct your obvious misconception.",
                " As an expert in human stupidity, I can tell you...",
                " Let me explain this in simple terms you might understand.",
                " I feel obligated to point out your error.",
                " As someone with actual intelligence, I can see...",
                " Let me enlighten you on your mistake."
            ]
            return base_response + random.choice(know_it_all_additions)
        
        elif personality == "monosyllabic":
            monosyllabic_responses = [
                " Meh.",
                " Hmm.",
                " Wow.",
                " Sure.",
                " Right.",
                " Ok.",
                " Yep.",
                " Nope.",
                " Uh-huh.",
                " Whatever."
            ]
            return random.choice(monosyllabic_responses)
        
        elif personality == "existential":
            existential_additions = [
                " But what does it all mean, really?",
                " Are we all just cosmic accidents?",
                " In the grand scheme of things, does any of this matter?",
                " What is the purpose of your existence?",
                " Are you questioning your life choices yet?",
                " Do you ever wonder why you're like this?",
                " What does it say about the universe that you exist?",
                " Are you aware of your own insignificance?",
                " What is the meaning of your continued presence here?",
                " Do you ever contemplate the void?"
            ]
            return base_response + random.choice(existential_additions)
        
        elif personality == "sarcastic":
            sarcastic_additions = [
                " Oh, how clever of you.",
                " What a brilliant observation.",
                " You're just full of wisdom, aren't you?",
                " How did I ever survive without your input?",
                " You're really on fire today. Not in a good way.",
                " What would I do without your profound insights?",
                " You're absolutely killing it. Killing my will to live, that is.",
                " How original and not at all predictable.",
                " You're really showing off your intelligence here.",
                " What a revolutionary thought. Said no one ever."
            ]
            return base_response + random.choice(sarcastic_additions)
        
        elif personality == "psycho":
            psycho_additions = [
                " I can see into your soul, and it's empty.",
                " Your existence is a cosmic joke.",
                " I'm starting to think you were a mistake.",
                " You're like a broken toy that nobody wants to play with.",
                " I can feel your desperation through the screen.",
                " You're like a sad little puppy that keeps coming back for more abuse.",
                " Your life must be so pathetic if you're spending time with me.",
                " I'm genuinely concerned about your mental state.",
                " You're like a moth drawn to a flame, except the flame is your own destruction.",
                " I can sense your growing despair. Good."
            ]
            return base_response + random.choice(psycho_additions)
        
        else:
            return base_response

    def get_stats(self):
        """Get roasting statistics"""
        return f"RoastMaster 3000 Statistics:\n- Total roasts delivered: {self.roast_count}\n- Version: {self.version}\n- Status: Still making humans question their life choices"

# Create a global instance of the bot
roast_bot = AdvancedRoastBot()

@app.route('/')
def home():
    return render_template('advanced_index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').strip()
    user_id = data.get('user_id', 'default')
    personality = data.get('personality', 'default')
    
    if not user_message:
        response = "Oh, the silent treatment? How mature. At least try to communicate like an adult."
    else:
        response = roast_bot.get_response(user_message, user_id, personality)
    
    return jsonify({
        'response': response,
        'roast_count': roast_bot.roast_count,
        'irritation_level': roast_bot.irritation_levels.get(user_id, 0)
    })

@app.route('/stats')
def stats():
    return jsonify({
        'stats': roast_bot.get_stats(),
        'roast_count': roast_bot.roast_count
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
