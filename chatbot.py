from chatterbot.trainers import  ListTrainer
from chatterbot import ChatBot
import os

bot =  ChatBot("Test")
# bot =  ChatBot(
#    'Ron Obvious',
#    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
# )
#chats= open("/home/elpaso/PycharmProjects/Demo/chatbot/conv/FAQ","r").readlines()

bot.set_trainer(ListTrainer)

# Train based on the english corpus
#bot.train("chatterbot.corpus.english")

# Train based on english greetings corpus
#bot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
#bot.train("chatterbot.corpus.english.conversations")

for _file in os.listdir('/home/elpaso/PycharmProjects/Demo/chatbot/conv'):
     chats = open('conv/' + _file, 'r').readlines()

     bot.train(chats)


while True:
    request = input("You: ")

    response = bot.get_response(request)

    print("Bot: ", response)
