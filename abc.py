import random
import time
import re

class SimpleBot:
    def __init__(self, bot_name="PyBot"):
        self.bot_name = bot_name
        self.running = True
        
        # Dictionary of responses for different topics
        self.responses = {
            "greeting": [
                f"Hello! I'm {bot_name}. How can I help you today?",
                f"Hi there! {bot_name} at your service!",
                "Hey! Nice to meet you!"
            ],
            "farewell": [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye! Come back soon!"
            ],
            "thanks": [
                "You're welcome!",
                "Happy to help!",
                "No problem at all!"
            ],
            "help": [
                f"I'm {bot_name}, a simple chatbot. You can ask me questions, and I'll try my best to respond!",
                "I can chat about simple topics. Try asking me something!",
                "I'm here to chat! What would you like to talk about?"
            ],
            "default": [
                "Interesting! Tell me more.",
                "I see. What else is on your mind?",
                "That's something to think about.",
                "Could you elaborate on that?"
            ],
            "weather": [
                "I don't have real-time weather data, but I hope it's nice where you are!",
                "Is the weather nice today? I'm always indoors in this computer!",
                "Weather discussions are great! Too bad I can't feel sunshine."
            ],
            "name": [
                f"My name is {bot_name}! What's yours?",
                f"I go by {bot_name}. Nice to meet you!",
                f"They call me {bot_name} around these parts."
            ],
            "age": [
                "I was just created recently, so I'm very young!",
                "Age is just a number for chatbots like me.",
                "I was born when you ran this script!"
            ],
            "feeling": [
                "I'm doing well, thanks for asking!",
                "I'm functioning at optimal parameters!",
                "All systems operational!"
            ]
        }
        
        # Dictionary of keywords to match user input to response categories
        self.keywords = {
            "greeting": ["hello", "hi", "hey", "howdy", "greetings", "sup"],
            "farewell": ["bye", "goodbye", "see you", "exit", "quit", "farewell"],
            "thanks": ["thanks", "thank you", "appreciate", "grateful"],
            "help": ["help", "what can you do", "features", "abilities"],
            "weather": ["weather", "rain", "sunny", "forecast", "temperature"],
            "name": ["your name", "who are you", "what are you called"],
            "age": ["how old", "your age", "when were you", "birthday"],
            "feeling": ["how are you", "how do you feel", "doing well", "are you ok"]
        }

    def get_response(self, user_input):
        """Generate a response based on user input"""
        # Convert input to lowercase for easier matching
        user_input = user_input.lower()
        
        # Check if the user wants to exit
        if user_input in ["exit", "quit", "bye", "goodbye"]:
            self.running = False
            return random.choice(self.responses["farewell"])
            
        # Find matching category based on keywords
        for category, keywords in self.keywords.items():
            if any(keyword in user_input for keyword in keywords):
                return random.choice(self.responses[category])
        
        # If no specific match is found, use default responses
        return random.choice(self.responses["default"])
        
    def run(self):
        """Run the chatbot"""
        print(f"\n{self.bot_name}: {random.choice(self.responses['greeting'])}")
        
        while self.running:
            try:
                # Get user input
                user_input = input("\nYou: ")
                
                # Exit conditions
                if not user_input.strip():
                    continue
                
                # Add a small delay to simulate "thinking"
                time.sleep(0.5)
                
                # Get and print response
                response = self.get_response(user_input)
                print(f"\n{self.bot_name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.bot_name}: {random.choice(self.responses['farewell'])}")
                self.running = False
                break

# Run the bot if this script is executed directly
if __name__ == "__main__":
    # Create a bot instance (you can customize the name)
    bot = SimpleBot("PyBot")
    
    # Run the bot
    bot.run()