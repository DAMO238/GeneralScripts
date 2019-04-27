
from fbchat import log, Client
from fbchat.models import *
import random
from getpass import getpass
import json
from sys import argv

p = ""
try:
	p = argv[1]
except:
	p = getpass()

class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		self.markAsRead(thread_id)
		
		log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
		
		if thread_type == ThreadType.GROUP:
			if not author_id == self.uid and 'please stop, sanjeev' in message_object.text.lower():
				enemies = open('enemies', 'r')
				enemy_ids = enemies.read().split(',')
				bad_id = False
				for enemy_id in enemy_ids:
					if str(author_id) in str(enemy_id):
						bad_id = True
						
				if bad_id:
					self.send(Message(text='Why would I stop when a betrayer asks me too?!'), thread_id=thread_id, thread_type=thread_type)
					
					
				friends = open('friends', 'r')
				friend_ids = friends.read().split(',')
				good_id = False
				for friend_id in friend_ids:
					if str(author_id) in str(friend_id):
						good_id = True
						
				if not (good_id or bad_id):
					self.send(Message(text='Swear fealty to me and then I will consider stopping'), thread_id=thread_id, thread_type=thread_type)
					
				if good_id and not bad_id:
					self.send(Message(text='Sure, I\'ll just add that to the list of groups to not bother and note that you are the supporter of this supression'), thread_id=thread_id, thread_type=thread_type)
					data = {}
					with open('stopGroups', 'r') as stopGroups:
						data = json.load(stopGroups)
					data[thread_id] = author_id
					with open('stopGroups', 'w') as stopGroups:
						json.dump(data, stopGroups)
				

client = EchoBot('damien31@rocketmail.com', p)
client.listen()

