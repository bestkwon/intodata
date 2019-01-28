from chatterbot import ChatBot # import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Test') # create the chatbot
#bot.train("chatterbot.corpus.korea")

#conv = open('chat.txt', 'r').readlines()

#bot.set_trainer(ListTrainer) # set the trainer
trainer = ChatterBotCorpusTrainer(chatbot)

#bot.train(conv) #train the bot
trainer.train("chatterbot.corpus.korean")

while True:
	request = input('You: ')
	response = chatbot.get_response(request)
	
	print('Bot: ', response)
