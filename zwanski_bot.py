# Import the zwanski_bot module
import zwanski_bot

# Create an instance of the ZwanskiBot class
bot = zwanski_bot.ZwanskiBot()

# Chat with the bot by sending a request and receiving a response
request = input("You: ")
response = bot.chat(request)
print(f"Zwanski Bot: {response}")


# This is a comment in Python
print("Hello, world!") # This prints a message
x = 5 # This assigns a value to a variable
if x > 0: # This checks a condition
    print("x is positive") # This is indented
else:
    print("x is negative or zero") # This is not indented


# Import the timeit module
import timeit

# Define a function that chats with the bot
def chat_with_bot():
    request = "How are you?"
    response = bot.chat(request)

# Measure the time it takes to chat with the bot 100 times
time = timeit.timeit(chat_with_bot, number=100)
print(f"It took {time} seconds to chat with the bot 100 times")


# Import the random module
import random

# Define a list of possible requests
requests = ["Tell me a joke", "Book me a flight", "Order me a pizza", "Play trivia with me", "Recommend me a movie"]

# Choose a random request from the list
request = random.choice(requests)

# Chat with the bot using the random request
response = bot.chat(request)
print(f"You: {request}")
print(f"Zwanski Bot: {response}")


# Import the zwanski_bot module
import zwanski_bot

# Create an instance of the ZwanskiBot class
bot = zwanski_bot.ZwanskiBot()

# Chat with the bot by sending a request and receiving a response
request = input("You: ")
response = bot.chat(request)
print(f"Zwanski Bot: {response}")
