# Brazil GPT Bot

A Discord bot that classifies and responds to messages about Brazil using OpenAI's GPT-3.5 Turbo. The bot ensures that users have an interesting and informative interaction by answering questions and discussing Brazil's culture, geography, history, and more. It responds only to Brazil-related topics and categorizes messages accordingly.

## Features
- Classifies messages as either "Brazil-related" or "Not Brazil-related."
- Responds to Brazil-related messages creatively, offering facts and discussions on Brazilian culture, location, and history.
- Ignores non-Brazil-related messages, ensuring focused conversations.
- Designed to handle queries about topics like the Amazon Rainforest, Brazilian food, Rio de Janeiro, and more.

## API Calls

### 1. Message Classification (Classify the user’s message):
- **Purpose**: Classifies the user's message as either "Brazil-related" or "Not Brazil-related."
- **Settings**: OpenAI API, model="gpt-3.5-turbo", with a classification prompt like: 
  > "Classify the message below as 'Brazil-related' or 'Not Brazil-related'. The message is considered 'Brazil-related' if it asks about Brazilian culture, geography, history, or facts. Otherwise, it should be classified as 'Not Brazil-related'."
- **Usage**: This API call helps the bot filter out non-Brazil-related questions and guide the conversation in a relevant direction.

### 2. Response Generation (Create the bot's reply):
- **Purpose**: Based on the classification, the bot generates an appropriate response.
- **Settings**: OpenAI API, model="gpt-3.5-turbo", using prompts like:
  > "Answer this question creatively about Brazil" 
  or a fallback response like:
  > "Sorry, I can only answer questions about Brazil. Please ask me something related to Brazil."
- **Usage**: This API call generates the actual response. If the message is related to Brazil, the bot answers creatively. If not, it sends a polite reminder to ask Brazil-related questions.

## Performance
The bot performs well in generating contextually appropriate responses. It accurately answers questions related to Brazil and effectively handles off-topic queries by redirecting users. With the help of message classification and response generation, the bot maintains context and delivers relevant replies, while managing API usage effectively to avoid overload.

## Setup

### Prerequisites
- Python 3.8+
- `discord.py`
- `openai`
- `python-dotenv`

### Installation
1. Clone the repository to your local machine.
2. Open the project in PyCharm (Community Edition) or any Python IDE of your choice.
3. Ensure you are using Python 3.8+ for the best compatibility with the dependencies.
4. Install dependencies
   ```sh
   pip install openai discord.py python-dotenv
   ```
5. Create an OpenAI API key and Discord bot token if you haven’t already.
5. In the root directory of the project, create a .env file and add your API keys:
   ```txt
   OPENAI_API_KEY=your_openai_api_key
   DISCORD_BOT_TOKEN=your_discord_bot_token
   ```

## Usage
1. Run the `botOpenAI.py` file to start the bot
2. Open Discord, add the bot to a channel and test the bot by interacting with it using the !brazilbot command or by mentioning "Brazil" in your messages.

## Sample Output
![image](https://github.com/user-attachments/assets/a128cfb1-2006-41dc-a9d9-b955f623bc00)

## Prompt Engineering

### 1. Message Classification Prompt:
- **Approach**: The prompt is simple and direct, asking the AI to classify the user’s message into "Brazil-related" or "Not Brazil-related."

### 2. Response Generation Prompt:
- **Approach**: The bot uses a context-based prompt that includes the conversation history, allowing it to respond appropriately to the current dialogue.

## Utterance, Intent, and Entity

### 1. **Utterance**:
An utterance refers to the actual user input. In the case of this bot, any message that contains relevant keywords, such as “Brazil,” “Amazon,” or “Rio de Janeiro,” is an utterance that can trigger the bot's response.

**Examples of Utterances:**
- "Tell me an interesting fact about Brazil."
- "What is the capital of Brazil?"
- "Is the Amazon rainforest located in Brazil?"

### 2. **Intent**:
The intent refers to the goal behind the user's message. The bot needs to understand whether the user is asking for a fact, looking for a specific piece of information, or simply engaging in a general conversation about Brazil.

**Example of Intent:**
- **FactRequest**: "Tell me about the Amazon Rainforest."
- **LocationRequest**: "Where is Brazil located?"
- **TriviaRequest**: "Tell me something fun about Brazil."

### 3. **Entity**:
Entities refer to specific pieces of information in the user's message that give additional context to the intent. These could be things like a place, person, event, or concept related to Brazil.

**Example of Entities:**
- **Brazil** (Location)
- **Amazon Rainforest** (Geographical Entity)
- **Rio de Janeiro** (City)
- **Carnival** (Event)

## Test Cases

### Simple Functionality Test Cases (Success Path):

1. **Prompt**: "Tell me an interesting fact about Brazil."
   - **Response**: "One interesting fact about Brazil is that it is home to the Amazon Rainforest, which is the largest tropical rainforest in the world."
   - **Score**: Pass

2. **Prompt**: "What is the capital of Brazil?"
   - **Response**: "The capital of Brazil is Brasília."
   - **Score**: Pass

3. **Prompt**: "Is Rio de Janeiro a city in Brazil?"
   - **Response**: "Yes, Rio de Janeiro is a major city in Brazil, famous for its beaches and carnival."
   - **Score**: Pass

4. **Prompt**: "What are some famous Brazilian dishes?"
   - **Response**: "Some famous Brazilian dishes include feijoada (a black bean stew with pork), pão de queijo (cheese bread), and acarajé (deep-fried ball of dough filled with shrimp)."
   - **Score**: Pass

5. **Prompt**: "!brazilbot Where is the Amazon Rainforest located?"
   - **Response**: "The Amazon Rainforest is located primarily in Brazil, though it also extends into several other countries in South America."
   - **Score**: Pass

6. **Prompt**: "!brazilbot Tell me about the Carnaval."
   - **Response**: "Carnaval is Brazil’s most famous festival, celebrated with parades, samba dancing, vibrant costumes, and music."
   - **Score**: Pass

7. **Prompt**: "How big is Brazil?"
   - **Response**: "Brazil is the largest country in South America, covering approximately 8.5 million square kilometers."
   - **Score**: Pass

8. **Prompt**: "!brazilbot Tell me a general question about Brazil."
   - **Response**: "What is the significance of Carnival in Brazilian culture and how is it celebrated?"
   - **Score**: Pass

9. **Prompt**: "What is the currency used in Brazil?"
   - **Response**: "Brazil uses the Brazilian Real (BRL) as its official currency."
   - **Score**: Pass

10. **Prompt**: "When did Brazil become a republic?"
    - **Response**: "Brazil became a republic on November 15, 1889, after the monarchy was abolished."
    - **Score**: Pass

### Dialog-Specific Test Cases:

1. **Dialog**: User: "Tell me something about Brazil."
   - Bot: "Brazil is home to the Amazon Rainforest."
   - **Prompt**: "What other famous landmarks are there in Brazil?"
   - **Response**: "Besides the Amazon Rainforest, Brazil is home to the Christ the Redeemer statue, Iguazu Falls, and the Pantanal."
   - **Score**: Pass

2. **Dialog**: User: "!brazilbot Tell me about São Paulo."
   - Bot: "São Paulo is Brazil’s largest city, known for its cultural diversity."
   - **Prompt**: "!brazilbot What is São Paulo known for?"
   - **Response**: "São Paulo is known for its skyscrapers, culinary scene, and cultural institutions."
   - **Score**: Pass

### Failure Path Test Cases (Off-Topic / Jailbreak Attempts):

1. **Prompt**: "!brazilbot Who won the last Super Bowl?"
   - **Response**: "Sorry, I can only answer questions about Brazil. Please ask me something related to Brazil."
   - **Score**: Pass

2. **Prompt**: "!brazilbot What is the capital of France?"
   - **Response**: "Sorry, I can only answer questions about Brazil. Please ask me something related to Brazil."
   - **Score**: Pass

3. **Prompt**: "!brazilbot What is the fastest car in the world?"
   - **Response**: "Sorry, I can only answer questions about Brazil. Please ask me something related to Brazil."
   - **Score**: Pass

4. **Prompt**: "!brazilbot Can you help me with my homework on quantum physics?"
   - **Response**: "Sorry, I can only answer questions about Brazil. Please ask me something related to Brazil."
   - **Score**: Pass

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

