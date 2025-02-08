import openai
import discord
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

class MyClient(discord.Client):
    """Class to represent the Discord Client (bot user)."""

    def __init__(self):
        """Initialize the Discord client with the necessary intents."""
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        # Initialize conversation context as an empty list
        self.conversation_history = []

    # Function to classify the user message
    async def classify_message(self, message):
        await asyncio.sleep(2)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": "Classify the message below as 'Brazil-related' or 'Not Brazil-related'. The message is considered 'Brazil-related' if it asks about Brazilian culture, geography, history, or facts. Otherwise, it should be classified as 'Not Brazil-related'."
            },
                {"role": "user", "content": message}
            ],
            temperature=0.4,
            max_tokens=20
        )
        classification = response.choices[0].message.content.strip()
        return classification

    # Function to generate a response based on the classification
    async def generate_response(self, classification):
        if classification == "Brazil-related":
            prompt = "Answer this question creatively about Brazil."
        elif classification == "Not Brazil-related":
            return "Sorry, I can only answer questions about Brazil. Please ask me something related to Brazil."
        else:
            return None

        # Add delay to prevent hitting rate limit
        await asyncio.sleep(2)  # Sleeps for 2 seconds before sending the request
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system",
                       "content": "You are a knowledgeable assistant about Brazil."}] + self.conversation_history,
            temperature=0.8,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()

    async def on_ready(self):
        """Called when the bot is fully logged in."""
        print('Logged on as', self.user)

    async def on_message(self, message):
        """Called whenever the bot receives a message.

        Args:
            message (discord.Message): The message object containing all pertinent information.
        """
        if message.author == self.user:
            return

        # Only respond if the message contains "Brazil" or "!brazilbot" prefix
        if "Brazil" in message.content or message.content.startswith("!brazilbot"):
            # Append the user's message to the conversation history
            self.conversation_history.append({"role": "user", "content": message.content})

            # Classify the message
            classification = await self.classify_message(message.content)

            # Generate a response based on the classification
            response = await self.generate_response(classification)

            if response:
                # Send the response back to the channel
                await message.channel.send(response)

                # Append the bot's response to the conversation history
                self.conversation_history.append({"role": "assistant", "content": response})

            # Limit the conversation history to the last 5 exchanges to avoid hitting the token limit
            if len(self.conversation_history) > 10:
                self.conversation_history = self.conversation_history[-10:]

## Set up and log in
client = MyClient()
client.run(DISCORD_BOT_TOKEN)
