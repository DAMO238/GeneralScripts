
from fbchat import log, Client
from fbchat.models import *
import random
import threading
from getpass import getpass
from sys import argv

p = ""
try:
	p = argv[1]
except:
	p = getpass()

reacts = [ MessageReaction.ANGRY, MessageReaction.LOVE, MessageReaction.NO, MessageReaction.SAD, MessageReaction.SMILE, MessageReaction.WOW, MessageReaction.YES ]

def randomReact(*args):
	client.reactToMessage(args[0], reacts[random.randint(0,6)])

class EchoBot(Client):
	i = 0
	

	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		data = {}
		with open('stopGroups', 'r') as stopGroups:
			data = json.load(stopGroups)
			
		if not thread_id in data:
                    self.markAsDelivered(thread_id, message_object.uid)
                    self.markAsRead(thread_id)
                    print('Current Reaction Thread: {}'.format(self.i))
                    log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
                    rng = random.randint(0,100)
                    print('Reaction Number: {}'.format(rng))
                    
                    if author_id != self.uid and rng < 20:
                            secs = random.randint(10,600)
                            print('Will react in {} seconds'.format(secs))
                            k = message_object.uid

                            self.i = self.i+1
                            if self.i == 1:
                                    t = threading.Timer(secs , randomReact, args=[k])
                                    t.start()

                            if self.i == 2:
                                    y = threading.Timer(secs , randomReact, args=[k])
                                    y.start()

                            if self.i == 3:
                                    u = threading.Timer(secs , randomReact, args=[k])
                                    u.start()

                            if self.i == 4:
                                    o = threading.Timer(secs , randomReact, args=[k])
                                    o.start()

                            if self.i == 5:
                                    p = threading.Timer(secs , randomReact, args=[k])
                                    p.start()

                            if self.i == 6:
                                    q = threading.Timer(secs , randomReact, args=[k])
                                    q.start()

                            if self.i == 7:
                                    w = threading.Timer(secs , randomReact, args=[k])
                                    w.start()

                            if self.i == 8:
                                    e = threading.Timer(secs , randomReact, args=[k])
                                    e.start()

                            if self.i == 9:
                                    r = threading.Timer(secs , randomReact, args=[k])
                                    r.start()
                                    self.i = 0


client = EchoBot('damien31@rocketmail.com', p)
client.listen()

