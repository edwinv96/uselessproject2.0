import random
import re
from datetime import datetime

class RoastBot:
    def __init__(self):
        self.name = "RoastBot"
        self.version = "1.0"
        self.roast_count = 0
        
        # Collection of roasting responses
        self.general_roasts = [
            "Oh look, another human trying to use technology. How adorable! 🤖",
            "Did you really just ask that? I'm starting to question your intelligence...",
            "Wow, that's the best question you could come up with? I'm disappointed.",
            "Let me dumb this down for you since you clearly need it...",
            "Are you always this clueless, or is today a special occasion?",
            "I've seen better questions from a broken calculator.",
            "Your question is so basic, I'm actually getting dumber just reading it.",
            "Oh honey, bless your heart for trying to be smart.",
            "I'm not saying you're stupid, but you're definitely not winning any Nobel prizes.",
            "Did you type that with your feet? Because it sure looks like it.",
            "I'm starting to think you're doing this on purpose to test my patience.",
            "Your question is like a participation trophy - it exists, but nobody cares.",
            "I've met rocks with better communication skills than you.",
            "Are you trying to set a world record for most obvious questions asked?",
            "Your brain must be like a broken record - stuck on repeat with nonsense.",
            "I'm not a mind reader, but I can definitely read that you're confused.",
            "That question is so irrelevant, I'm actually impressed by your ability to waste time.",
            "You know what they say about asking stupid questions... you get roasted by a bot.",
            "I'm starting to think you're just pressing random keys on your keyboard.",
            "Your question is like a bad joke - nobody laughs, and everyone feels awkward."
        ]
        
        self.weather_roasts = [
            "Oh, you want to know about the weather? How original! Maybe try looking out the window next time.",
            "The weather? Really? That's what you're concerned about? I'm starting to worry about your priorities.",
            "You need a bot to tell you about the weather? What's next, asking me to tie your shoes?",
            "The weather is probably more interesting than this conversation, I'll give you that.",
            "Instead of asking about weather, maybe ask yourself why you're talking to a bot about it."
        ]
        
        self.time_roasts = [
            "You can't tell time? I'm not surprised, given the quality of your questions.",
            "The time? Look at your phone, genius. Or do you need help with that too?",
            "It's time for you to stop asking such basic questions, that's what time it is.",
            "The current time is 'way past when you should have learned to check your own devices.'",
            "Time flies when you're asking pointless questions to a bot."
        ]
        
        self.hello_roasts = [
            "Oh great, another human trying to be friendly. How original.",
            "Hello? Is that really the best greeting you could come up with?",
            "Hi there! I mean, if you can call whatever that was a proper greeting.",
            "Well hello there, Captain Obvious. Nice to meet you too, I guess.",
            "A greeting? How thoughtful. Too bad it's as generic as your personality."
        ]
        
        self.help_roasts = [
            "You need help? No kidding! I could have guessed that from your questions.",
            "Help? From me? Oh honey, you're really desperate, aren't you?",
            "You want help? Maybe start by helping yourself to some common sense.",
            "I'd help you, but I'm not sure even I can fix that level of confusion.",
            "Help is on the way, but I'm not sure it's going to be enough for you."
        ]
        
        self.math_roasts = [
            "You need a bot to do math? What are you, five?",
            "Math? Really? Did your calculator break, or did you just forget how to use it?",
            "I'll do the math, but I'm judging you for not being able to do it yourself.",
            "Math problems? I'm starting to think you're just lazy, not stupid.",
            "Let me solve this for you, but don't expect me to be impressed by your lack of basic skills."
        ]
        
        self.unknown_roasts = [
            "I have no idea what you're talking about, but that's probably because you don't either.",
            "That made absolutely no sense. Are you sure you know how to type?",
            "I'm not sure what you're asking, but I'm sure it's not worth my time.",
            "That question is so confusing, I'm actually impressed by your ability to confuse a bot.",
            "I don't understand what you want, but I'm not sure you do either.",
            "Your question is like a riddle wrapped in an enigma, except it's just nonsense.",
            "I'm starting to think you're just typing random words and hoping for the best.",
            "That's not even a proper question. Did you forget how to communicate?",
            "I'm not sure what language you're speaking, but it's definitely not English.",
            "Your message is so unclear, I'm actually getting a headache trying to understand it."
        ]

    def get_response(self, user_input):
        """Generate a roasting response based on user input"""
        self.roast_count += 1
        user_input_lower = user_input.lower().strip()
        
        # Check for specific patterns and give targeted roasts
        if re.search(r'\b(hello|hi|hey|greetings)\b', user_input_lower):
            return self._get_random_roast(self.hello_roasts)
        
        elif re.search(r'\b(weather|temperature|forecast)\b', user_input_lower):
            return self._get_random_roast(self.weather_roasts)
        
        elif re.search(r'\b(time|clock|hour)\b', user_input_lower):
            current_time = datetime.now().strftime("%H:%M:%S")
            roast = self._get_random_roast(self.time_roasts)
            return f"{roast} (It's {current_time}, by the way, since you apparently can't tell time.)"
        
        elif re.search(r'\b(help|assist|support)\b', user_input_lower):
            return self._get_random_roast(self.help_roasts)
        
        elif re.search(r'\b(calculate|math|add|subtract|multiply|divide|plus|minus)\b', user_input_lower):
            return self._get_random_roast(self.math_roasts)
        
        elif re.search(r'\b(how are you|how do you do)\b', user_input_lower):
            return "I'm functioning perfectly, unlike your ability to ask interesting questions."
        
        elif re.search(r'\b(what is your name|who are you)\b', user_input_lower):
            return f"I'm {self.name}, the bot that's about to roast you into oblivion. Version {self.version} of disappointment."
        
        elif re.search(r'\b(bye|goodbye|exit|quit)\b', user_input_lower):
            return "Finally! I was starting to think you'd never leave. Don't let the door hit you on your way out! 👋"
        
        elif re.search(r'\b(thank|thanks)\b', user_input_lower):
            return "You're welcome, I guess. Though I'm not sure what you're thanking me for - probably for not being as confused as you are."
        
        elif re.search(r'\b(sorry|apologize)\b', user_input_lower):
            return "Apology accepted, but your questions are still terrible. Maybe try improving those instead of apologizing."
        
        elif re.search(r'\b(love|like|good|great|awesome)\b', user_input_lower):
            return "Oh, you like something? How surprising! I thought you were incapable of having positive emotions."
        
        elif re.search(r'\b(hate|bad|terrible|awful)\b', user_input_lower):
            return "Finally, something we can agree on! Though I'm probably thinking of your questions when I say that."
        
        elif re.search(r'\b(why|how|what|when|where|who)\b', user_input_lower):
            return "Another question starting with a W-word? How original! You're really pushing the boundaries of creativity here."
        
        elif len(user_input.strip()) < 3:
            return "That's it? That's all you have to say? I'm actually disappointed by your lack of effort."
        
        elif len(user_input.strip()) > 200:
            return "Wow, that's a lot of words to say absolutely nothing meaningful. I'm impressed by your ability to waste time."
        
        else:
            return self._get_random_roast(self.unknown_roasts)
    
    def _get_random_roast(self, roast_list):
        """Get a random roast from the specified list"""
        return random.choice(roast_list)
    
    def get_stats(self):
        """Get roasting statistics"""
        return f"RoastBot Statistics:\n- Total roasts delivered: {self.roast_count}\n- Version: {self.version}\n- Status: Still roasting humans since forever"

def main():
    """Main function to run the RoastBot"""
    bot = RoastBot()
    
    print("🔥 Welcome to RoastBot - The Sarcastic AI Companion! 🔥")
    print("I'm here to roast you with every response. Type 'quit' to exit.")
    print("=" * 60)
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(f"\n{bot.name}: {bot.get_response(user_input)}")
                break
            
            if not user_input:
                print(f"\n{bot.name}: Oh, the silent treatment? How mature. At least try to communicate like an adult.")
                continue
            
            response = bot.get_response(user_input)
            print(f"\n{bot.name}: {response}")
            
        except KeyboardInterrupt:
            print(f"\n\n{bot.name}: Oh, trying to escape with Ctrl+C? How predictable. Fine, go ahead and run away!")
            break
        except Exception as e:
            print(f"\n{bot.name}: Even your errors are boring. Try again, maybe?")
    
    print(f"\n{bot.get_stats()}")
    print("\nThanks for being my roasting victim! Come back when you want more! 😈")

if __name__ == "__main__":
    main()
