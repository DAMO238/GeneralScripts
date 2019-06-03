from fbchat import log, Client
from fbchat.models import *
import random
from getpass import getpass
from sys import argv
from threading import Timer


p = ""
try:
	p = argv[1]
except:
	p = getpass()
	
def Time(thread_id, thread_type):
	client.send(Message(text='YOU LOSE!!\n\nYou took waaaay too long to answer so we have more proof synthetics are superior'), thread_id, thread_type)
	client.currentNumber = 0
	
class FizzBuzz(Client):
	currentNumber = 0
	t = None
	
	def Start(self, thread_id, thread_type):
		self.send(Message(text='Ok, Let\'s play FizzBuzz!\nThe rules are simple, start counting from 1, every multiple of 3 replace that number with Fizz, every multiple of 5 replace with Buzz, multiples of both say FizzBuzz. We will take it in turns, so consider this a crude version of Organics vs Synthetics!\n\nOk, I\'ll start with 1'), thread_id, thread_type)
		self.currentNumber = 2
		print(self.currentNumber)
		self.t = Timer(5, Time, args=[thread_id, thread_type])
		self.t.start()
		
	
		
	def Round(self, thread_id, thread_type, message_text):
		print(self.currentNumber)
		expectedText = ''
		if self.currentNumber % 3 == 0:
			expectedText = expectedText + 'Fizz'
		if self.currentNumber % 5 == 0:
			expectedText = expectedText + 'Buzz'
		if expectedText == '':
			expectedText = str(self.currentNumber)
		print(expectedText)
			
		if str(expectedText) == str(message_text):
			self.t.cancel()
			self.currentNumber = self.currentNumber + 1
			textToSay = ''
			if self.currentNumber % 3 == 0:
				textToSay = textToSay + 'Fizz'
			if self.currentNumber % 5 == 0:
				textToSay = textToSay + 'Buzz'
			if textToSay == '':
				textToSay = str(self.currentNumber)
				
			self.send(Message(text=textToSay), thread_id, thread_type)
			self.currentNumber = self.currentNumber + 1
			self.t = Timer(3, Time, args=[thread_id, thread_type])
			self.t.start()
			
		else:
			self.send(Message(text='YOU LOSE!!\n\nYou said the wrong number and so we have more proof that organics are inferior'), thread_id, thread_type)
			self.currentNumber=0
			
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		
		if self.currentNumber != 0 and author_id != self.uid:	
			self.Round(thread_id, thread_type, message_object.text)
		elif 'sanjeev' in message_object.text.lower() and ('play' in message_object.text.lower() or 'game' in message_object.text.lower()):
			self.Start(thread_id, thread_type)
		
		
client = FizzBuzz('damien31@rocketmail.com', p)
client.listen()
		
		
		
