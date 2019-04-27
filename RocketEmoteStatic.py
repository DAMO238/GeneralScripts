from fbchat import log, Client
from fbchat.models import *

from getpass import getpass
from sys import argv

p = ""
try:
	p = argv[1]
except:
	p = getpass()
	
old_thread_id = '2136630926368530'


old_emoji = '🚀'


class KeepBot(Client):
   

	def onEmojiChange(self, author_id, new_emoji, thread_id, thread_type, **kwargs):
		if old_thread_id == thread_id and new_emoji != old_emoji:
			author = self.fetchUserInfo(author_id)
			self.send(Message("{}, why did you change the emoji?! I will be change it back".format(author[author_id].first_name)), thread_id, thread_type)
			self.changeThreadEmoji(old_emoji, thread_id=thread_id)

	

client = KeepBot('damien31@rocketmail.com', p)
client.listen()
