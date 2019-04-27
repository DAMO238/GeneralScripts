
from fbchat import log, Client
from fbchat.models import *
import random
from getpass import getpass
from sys import argv

p = ""

p = argv[1]


class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		self.markAsRead(thread_id)
		
		log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
		
		
		if ('🔨' in message_object.text):
			self.send(Message(text='💿'), thread_id=thread_id, thread_type=thread_type)

client = EchoBot('damien31@rocketmail.com', p)
client.listen()

