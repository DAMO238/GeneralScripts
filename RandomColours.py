
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

colours = [ ThreadColor.BILOBA_FLOWER, ThreadColor.BRILLIANT_ROSE, ThreadColor.CAMEO, ThreadColor.DEEP_SKY_BLUE, ThreadColor.FERN, ThreadColor.FREE_SPEECH_GREEN, ThreadColor.GOLDEN_POPPY, ThreadColor.LIGHT_CORAL, ThreadColor.MEDIUM_SLATE_BLUE, ThreadColor.MESSENGER_BLUE, ThreadColor.PICTON_BLUE, ThreadColor.PUMPKIN, ThreadColor.RADICAL_RED, ThreadColor.SHOCKING, ThreadColor.VIKING]

class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		self.markAsRead(thread_id)

		log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        
		data = {}
		with load('stopGroups', 'r') as stopGroups:
			data = json.load(stopGroups)
        
		if thread_type == ThreadType.GROUP and random.randint(0,100) < 10 and not thread_id in data:
			self.changeThreadColor(colours[random.randint(0,13)], thread_id)

client = EchoBot('damien31@rocketmail.com', p)
client.listen()

