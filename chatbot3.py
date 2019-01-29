from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

trainer.train([
	"hello",
	"hi",
	"Hi",
	"Hello",
	"Greetings!",
	"Hello",
	"Hello",
	"Greetings!",
	"Hi, How is it going?",
	"Good",
	"Hi, How is it going?",
	"Fine",
	"Hi, How is it going?",
	"Okay",
	"Hi, How is it going?",
	"Great",
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

# Get a response to the input text 'I would like to book a flight.'
#response = chatbot.get_response('I would like to book a flight.')
#print(response)
while True:
	request = input('You: ')
	response = chatbot.get_response(request)
	
	print('Bot: ', response)
