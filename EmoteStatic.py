from fbchat import log, Client
from fbchat.models import *

from getpass import getpass
from sys import argv

p = ""
try:
	p = argv[1]
except:
	p = getpass()
	
old_thread_id = '339661942891632'


old_emoji = '🔨'
old_title = 'ST JOHN\'S RAMS (WE\'LL RAM YE with 2 hands)'


class KeepBot(Client):

	ids = [0]

	def getUserIDs(self):
		group = self.fetchGroupInfo(old_thread_id)
		ids = group[old_thread_id].participants

	def onEmojiChange(self, author_id, new_emoji, thread_id, thread_type, **kwargs):
		print("detected")
		if old_thread_id == thread_id and new_emoji != old_emoji:
			print("detected")
			author = self.fetchUserInfo(author_id)
			try:
				self.send(Message("{}, why did you change the emoji?! I will change it back".format(author[author_id].first_name)), thread_id, thread_type)
				self.changeThreadEmoji(old_emoji, thread_id=thread_id)
			except:
				print("Error in sending request")

	def onPeopleAdded(self, added_ids, author_id, thread_id, **kwargs):
		for added_id in added_ids:
			if old_thread_id == thread_id and added_id == self.uid:
				self.send(Message("Haha, I am back!"), thread_id, ThreadType.GROUP)
				self.changeThreadEmoji(old_emoji, thread_id=thread_id)
				self.changeThreadTitle(old_title, thread_id=thread_id, thread_type=thread_type)
				
	def onTitleChange(self, author_id, new_title, thread_id, thread_type, **kwargs):
		if old_thread_id == thread_id and new_title != old_title:
			author = self.fetchUserInfo(author_id)
			try:
				self.send(Message(text="I know you changed the title to {}, {}! Don't do it again!".format(new_title, author[author_id].first_name)), thread_id, thread_type)
				self.changeThreadTitle(old_title, thread_id=thread_id, thread_type=thread_type)
			except:
				pass

client = KeepBot('damien31@rocketmail.com', p)
client.getUserIDs()
client.listen()
