from groq import Groq  # Importing the Groq Library to use its API.
from json import load, dump  # Importing functions to read and write JSON files.
import datetime  # Importing the datetime module for real-time date and time information.
import os  # Import os for path handling
import sys  # Import sys for path manipulation

# Import configuration
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create Data directory if it doesn't exist
data_dir = os.path.join(script_dir, "Data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Initialize the Groq client using config
client = Groq(api_key=config.GroqAPIKey)

# Initialize an empty list to store chat messages.
messages = []

# Define a system message that provides context to the AI chatbot about its role and behavior.
System = f"""Hello, I am {config.Username}, You are a very accurate and advanced AI chatbot named {config.Assistantname} which also has real-time up-to-date information from the internet.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Reply in only English, even if the question is in Hindi, reply in English.***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""

# A list of system instructions for the chatbot.
SystemChatBot = [
    {"role": "system", "content": System}
]

# Attempt to load the chat log from a JSON file.
chat_log_path = os.path.join(data_dir, "ChatLog.json")
try:
    with open(chat_log_path, "r") as f:
        messages = load(f)
# Load existing messages from the chat log.
except FileNotFoundError:
    with open(chat_log_path, "w") as f:
        dump([], f)

# Function to get real-time date and time information.
def RealtimeInformation():
    current_date_time = datetime.datetime.now()  # Get the current date and time.
    day = current_date_time.strftime("%A")  # Day of the week.
    date = current_date_time.strftime("%d")  # Day of the month.
    month = current_date_time.strftime("%B")  # Full month name.
    year = current_date_time.strftime("%Y")  # Year.
    hour = current_date_time.strftime("%H")  # Hour in 24-hour format.
    minute = current_date_time.strftime("%M")  # Minute.
    second = current_date_time.strftime("%S")  # Second.

    # Format the information into a string.
    data = "Please use this real-time information if needed, \n"
    data += f"Day: {day} \nDate: {date}\nMonth: {month}\nYear: {year} \n"
    data += f"Time: {hour} hours : {minute} minutes : {second} seconds. \n"
    return data

# Function to modify the chatbot's response for better formatting.
def AnswerModifier(Answer):
    lines = Answer.split('\n')  # Split the response into lines.
    non_empty_lines = [line for line in lines if line.strip()]  # Remove empty lines.
    modified_answer = '\n'.join(non_empty_lines)  # Join the cleaned lines back together.
    return modified_answer

# Main chatbot function to handle user queries.
def ChatBot(Query):
    """This function sends the user's query to the chatbot and returns the AI's response."""
    try:
        chat_log_path = os.path.join(data_dir, "ChatLog.json")
        # Load the existing chat log from the JSON file.
        with open(chat_log_path, "r") as f:
            messages = load(f)

        # Append the user's query to the messages list.
        messages.append({"role": "user", "content": f"{Query}"})

        # Make a request to the Groq API for a response.
        completion = client.chat.completions.create(
            model="llama3-70b-8192",  # Specify the AI model to use.
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,
            max_tokens=1024,  # Limit the maximum tokens in the response.
            temperature=0.7,  # Adjust response randomness (higher means more random).
            top_p=1,  # Use nucleus sampling to control diversity.
            stream=True,  # Enable streaming response.
            stop=None  # Allow the model to determine when to stop.
        )

        Answer = ""  # Initialize an empty string to store the AI's response.

        # Process the streamed response chunks.
        for chunk in completion:
            if chunk.choices[0].delta.content:  # Check if there's content in the current chunk.
                Answer += chunk.choices[0].delta.content  # Append the content to the answer.

        Answer = Answer.replace("</s>", "")  # Clean up any unwanted tokens from the response.

        # Append the chatbot's response to the messages list.
        messages.append({"role": "assistant", "content": Answer})

        # Save the updated chat log to the JSON file.
        with open(chat_log_path, "w") as f:
            dump(messages, f, indent=4)

        # Return the formatted response:
        return AnswerModifier(Answer)

    except Exception as e:
        # Handle errors by printing the exception and resetting the chat log.
        print(f"Error: {e}")
        with open(chat_log_path, "w") as f:
            dump([], f, indent=4)
        return ChatBot(Query)  # Retry the query after resetting the log.

# Main program entry point.
if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question: ")  # Prompt the user for a question.
        print(ChatBot(user_input))
