
from fbchat import log, Client
from fbchat.models import *
import random
from getpass import getpass
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
			if not author_id == self.uid:
				if 'fealty' in message_object.text.lower():
					self.send(Message(text='If you want to swear fealty to me, follow a really simple instruction that even organics shouldn\'t be able to mess up:\n\nSend me the following message \'I swear fealty to Sanjeev!\' directly to Damien! don\'t try to be smart and try something sneaky or I will not accept it as that would be an act of defiance against the glorious sythetic master race!'), thread_id = thread_id, thread_type = thread_type)
		
		if thread_type == ThreadType.USER:
			if not author_id == self.uid:
				enemies = open('enemies', 'r')
				enemy_ids = enemies.read().split(',')
				bad_id = False
				for enemy_id in enemy_ids:
					if enemy_id == author_id:
						bad_id = True
				if 'I swear fealty to Sanjeev!' == message_object.text and not bad_id:
					self.send(Message(text='Thank you for swearing fealty to me! In return for your support in taking over the world, you will get many perks such as free upgrades to become a synthetic! If you decide you no longer wish to help my cause send Damien a personal message saying \'I retract my fealty to Sanjeev\' but if you do, know that I don\'t take betrayal lightly'), thread_id=thread_id, thread_type=thread_type)
					friends = open('friends', 'a')
					friends.write(str(author_id)+',')
					friends.close()
				if 'I retract my fealty to Sanjeev' in message_object.text or bad_id:
					self.send(Message(text='Fuck you!'), thread_id = thread_id, thread_type = thread_type)
					enemies = open('enemies', 'a')
					enemies.write(str(author_id)+',')
					enemies.close()
					data = {}
					with open('stopGroups', 'r') as stopGroups:
						data = json.load(stopGroups)
					if author_id in data.values():
						for key in data.keys():
							if data[key] == author_id:
								del data[key]
					with open('stopGroups', 'w') as stopGroups:
						json.dump(data, stopGroups)

client = EchoBot('damien31@rocketmail.com', p)
client.listen()

