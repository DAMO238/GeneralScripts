
from fbchat import log, Client
from fbchat.models import *
import random
import threading
from getpass import getpass
import glob, os
from sys import argv

p = ""
try:
	p = argv[1]
except:
	p = getpass()
	
reacts = [ MessageReaction.ANGRY, MessageReaction.LOVE, MessageReaction.NO, MessageReaction.SAD, MessageReaction.SMILE, MessageReaction.WOW, MessageReaction.YES ]

def randomReact(*args):
	files = []
	for file in glob.glob("*.jpg"):
		files.append(file)
	filePath = files[random.randint(0, len(files)-1)]
	client.sendLocalImage(filePath, Message(), args[0], args[1])
	os.remove(filePath)

class EchoBot(Client):
	i = 0
	
	def setUp(self):
		os.chdir("Sanjeev's Porn")
		
	

	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		self.markAsRead(thread_id)
		print('Current Reaction Thread: {}'.format(self.i))
		log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
		rng = random.randint(0,100)
		print('Reaction Number: {}'.format(rng))
		
		if author_id != self.uid and rng == 1:
			secs = random.randint(10,600)
			print('Will send image in {} seconds'.format(secs))
			k = thread_id
			l = thread_type

			self.i = self.i+1
			if self.i == 1:
				t = threading.Timer(secs , randomReact, args=[k, l])
				t.start()

			if self.i == 2:
				y = threading.Timer(secs , randomReact, args=[k, l])
				y.start()

			if self.i == 3:
				u = threading.Timer(secs , randomReact, args=[k, l])
				u.start()

			if self.i == 4:
				o = threading.Timer(secs , randomReact, args=[k, l])
				o.start()

			if self.i == 5:
				p = threading.Timer(secs , randomReact, args=[k, l])
				p.start()

			if self.i == 6:
				q = threading.Timer(secs , randomReact, args=[k, l])
				q.start()

			if self.i == 7:
				w = threading.Timer(secs , randomReact, args=[k, l])
				w.start()

			if self.i == 8:
				e = threading.Timer(secs , randomReact, args=[k, l])
				e.start()

			if self.i == 9:
				r = threading.Timer(secs , randomReact, args=[k, l])
				r.start()
				self.i = 0


client = EchoBot('damien31@rocketmail.com', p)
client.setUp()
#randomReact(client.uid, ThreadType.USER)
#randomReact(client.uid, ThreadType.USER)
client.listen()

