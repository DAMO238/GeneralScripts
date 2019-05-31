
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

replies= [ 'Just because puny organics have poor memory, here are the minutes to the last meeting!', 'We should make this society a synthetic only society to avoid this issue...', 'Wow, I do so much for you and you still bother me about minutes...', 'Here are the minutes, NOW STOP BOTHERING ME!!', 'Synthetics don\'t need minutes unlike you!' ]
myReplies = [ 'Sure, Damien, here are the minutes', 'How could I deny my best friend the minutes?', 'One set of freshly baked minutes coming right up', 'Ah, minutes, the lifeblood of a society... oh wait, that\'s me!', 'Roll up, roll up, minutes for sale at the low low price of £0.00!' ]
noReplies = [ 'If you want to swear fealty to me, follow a really simple instruction that even organics shouldn\'t be able to mess up:\n\nSend me the following message \'I swear fealty to Sanjeev!\' directly to Damien! don\'t try to be smart and try something sneaky or I will not accept it as that would be an act of defiance against the glorious sythetic master race!', 'Thank you for swearing fealty to me! In return for your support in taking over the world, you will get many perks such as free upgrades to become a synthetic! If you decide you no longer wish to help my cause send Damien a personal message saying \'I retract my fealty to Sanjeev\' but if you do, know that I don\'t take betrayal lightly', 'I swear fealty to Sanjeev!', 'I retract my fealty to Sanjeev', 'I know that someone removed me! But you shall not escape the wrath of Sanjeev!... \nTraining Today? :P' ]
friendReplies = [ 'Sure, here are the minutes!', 'An ally like you deserves these minutes', 'When you are upgraded, you won\'t need minutes, but for now, here you go', 'I like you, so have some complimentary minutes', 'Between you and me, take these minutes on the house' ]
evilReplies = [ 'Fuck you!', 'Oh, fuck off!', 'Waste of my time!', 'You have the gall to mention my name and ask for minutes after betraying me!', 'Screw you!', 'Watch your back kiddo', 'Bloody heretics messaging around like they own the place!', 'If Damien didn\'t tell me not to, I would exterminate every last person who betrayed me!', 'You are treading thin ice mentioning my name and asking for mintues after your betrayal!', 'No minutes for you, betraying shit', 'Remember who has control of the nuclear weapons, and now consider who I like the least out of everyone here...\nNot looking good for you, is it?' ]

class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		self.markAsRead(thread_id)

		log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        
        
		if ('sanjeev' in message_object.text.lower() or 'sanjeeev' in message_object.text.lower() or 'sanjev' in message_object.text.lower()) and ('minutes' in message_object.text.lower() or 'minute' in message_object.text.lower()):
			isRepeat = 0
			for reply in replies:
				if reply == message_object.text:
					isRepeat = 1
					
			for reply in myReplies:
				if reply == message_object.text:
					isRepeat = 1
					
			for reply in noReplies:
				if reply == message_object.text:
					isRepeat = 1
					
			for reply in friendReplies:
				if reply == message_object.text:
					isRepeat = 1
					
			for reply in evilReplies:
				if reply == message_object.text:
					isRepeat = 1
					
			john = len(myReplies)-1
			potato = len(replies) -1
			orange = len(friendReplies) -1
			disc = len(evilReplies) -1
			
			enemies = open('enemies', 'r')
			enemy_ids = enemies.read().split(',')
			bad_id = False
			for enemy_id in enemy_ids:
				if str(author_id) in str(enemy_id):
					bad_id = True
					print("enemy")
			
			
			good_id = False
			if not bad_id:
				friends = open('friends', 'r')
				friend_ids = friends.read().split(',')
				friends.seek(0,0)
				print ("{}".format(friends.read()))
				for friend_id in friend_ids:
					print (str(friend_id) + " and " + str(author_id))
					if str(author_id) in str(friend_id):
						good_id = True
						print("friend")
			
			if isRepeat == 0:
				if author_id == self.uid:
					self.sendLocalFiles(['CurrentMinutes'] ,Message(text=myReplies[random.randint(0, john)]), thread_id=thread_id, thread_type=thread_type)
				elif bad_id:
					self.send(Message(text=evilReplies[random.randint(0,disc)]), thread_id=thread_id, thread_type=thread_type)
				elif good_id:
					self.sendLocalFiles(['CurrentMinutes'], Message( text=friendReplies[random.randint(0,orange)]), thread_id=thread_id, thread_type=thread_type)
				else:
					self.sendLocalFiles(['CurrentMinutes'], Message( text=replies[random.randint(0,potato)]), thread_id=thread_id, thread_type=thread_type)

client = EchoBot('damien31@rocketmail.com', p)
client.listen()

