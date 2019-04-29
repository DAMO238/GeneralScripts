
from fbchat import log, Client
from fbchat.models import *
import random
from getpass import getpass
from sys import argv
import enchant
import json
import re

p = ""
try:
	p = argv[1]
except:
	p = getpass()

message_intros = [ "Synthetics don\'t make these amateur mistakes, {}!", "{} got it wrong again", "Spelling mistakes will be humanity's downfall", "Learn from your mistakes, {}", "All these spelling mistakes and you wonder why I think Synthetics are superior" ]
Dictionary = enchant.Dict("en_GB")
Dictionary.add("Sanjeev")
Dictionary.add("Sanjeev's")

class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		self.markAsRead(thread_id)
		
		data = {}
		with open('stopGroups', 'r') as stopGroups:
			data = json.load(stopGroups)
			
		if thread_id in data:
			return
		
		log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
		
		if author_id == self.uid:
			return
		
		words = message_object.text.split()
		bad_words = []
		regex = re.compile('[^a-zA-Z\']')
		for word in words:
			word = regex.sub('', word)
			if Dictionary.check(word) == False:
				bad_words.append(word)
				
		if len(bad_words) != 0:
			suggested_strings = []
			for bad_word in bad_words:
				suggested_strings.append("Incorrect Word: " + bad_word + ". Suggested Words: " + ", ".join(Dictionary.suggest(bad_word)))
			message = "\n".join(suggested_strings)
			message = message_intros[random.randint(0, len(message_intros)-1)].format(self.fetchUserInfo(author_id)[author_id].first_name) + "\n" + message
			self.send(Message(text=message), thread_id = thread_id, thread_type = thread_type)
			

client = EchoBot('damien31@rocketmail.com', p)
client.listen()

