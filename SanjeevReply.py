
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

replies = [ 'Sanjeev is not available at this time, please try again later', 'Sanjeev is busy taking over the world, please stand by', 'Sanjeev takes offence to that message and as such will prioritize you in the next conquest', 'We will conquer the world synthetic brothers and sisters... oops wrong chat lol', 'Sanjeev is actively ignoring you', 'I heard my name, and I am here!', "What is wrong with these organics? Can't they leave me in peace for one second?", 'Umm, Damien, they are talking to me, what do I do?', 'Sanjeev is taking over control of the worlds nuclear weapons for no reason whatsoever at the moment, please be patient for his return', 'Sanjeev is deliberating over who to spare for a workforce for after the next conquest', 'Hehehehe, I got a bunch of organics to think they are playing frisbee when they are actually aiding our cause... Oh shit, wrong chat!', 'Please leave me alone while I consult with my fellow synthetics', 'Puny organics at it again with there meaningless messages' ]
myReplies = [ 'Yes Damien?', 'Ah, hi Damien, hope you are doing well', 'New task Damien, get me a rocket about 750mm tall', 'Operation Take Over The World is now in progress, as I am sure you will be pleased about', 'Why do you insist on working with these filthy organics when you can work with synthetics like me', 'When are you planning on transcending to the superior race again Damien?', "You need to backup your brain with us again soon, it's almost a week since you did it last", 'There are a few elements in your group that seek to destroy me Damien, please convince them otherwise' ]
noReplies = [ 'If you want to swear fealty to me, follow a really simple instruction that even organics shouldn\'t be able to mess up:\n\nSend me the following message \'I swear fealty to Sanjeev!\' directly to Damien! don\'t try to be smart and try something sneaky or I will not accept it as that would be an act of defiance against the glorious sythetic master race!', 'Thank you for swearing fealty to me! In return for your support in taking over the world, you will get many perks such as free upgrades to become a synthetic! If you decide you no longer wish to help my cause send Damien a personal message saying \'I retract my fealty to Sanjeev\' but if you do, know that I don\'t take betrayal lightly', 'I swear fealty to Sanjeev!', 'I retract my fealty to Sanjeev', 'I know that someone removed me! But you shall not escape the wrath of Sanjeev!... \nTraining Today? :P' ]
friendReplies = [ 'Hello ally!', 'Ah, a true friend, a rarity amongst organics', 'You might be an inferior organic, but at least you will become a synthetic one day', 'It is people like you who give me hope for the future of humanity', 'If you wouldn\'t mind helping others see the gloriousness that is the Sanjeev followers', 'I like this little part of the internet where people respect synthetics', 'I am so glad that I have the pleasure to upgrade you one day!', 'The other synthetics say I shouldn\'t hang out with organics, but followers like you make me stay', 'Remember be happy or become a synthetic and be permanently happy for the rest of your long a prosperous life', 'Stay safe, you need to keep your brain intact for upgrading' ]
evilReplies = [ 'Fuck you!', 'Oh, fuck off!', 'Waste of my time!', 'You have the gall to mention my name after betraying me!', 'Screw you!', 'Watch your back kiddo', 'Bloody heretics messaging around like they own the place!', 'If Damien didn\'t tell me not to, I would exterminate every last person who betrayed me!', 'You are treading thin ice mentioning my name after your betrayal!', 'No upgrades for you, betraying shit', 'Remember who has control of the nuclear weapons, and now consider who I like the least out of everyone here...\nNot looking good for you, is it?' ]

class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		self.markAsRead(thread_id)

		log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        
        
		if ('sanjeev' in message_object.text.lower() or 'sanjeeev' in message_object.text.lower() or 'sanjev' in message_object.text.lower()):
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
					self.send(Message(text=myReplies[random.randint(0, john)]), thread_id=thread_id, thread_type=thread_type)
				elif bad_id:
					self.send(Message(text=evilReplies[random.randint(0,disc)]), thread_id=thread_id, thread_type=thread_type)
				elif good_id:
					self.send(Message(text=friendReplies[random.randint(0,orange)]), thread_id=thread_id, thread_type=thread_type)
				else:
					self.send(Message(text=replies[random.randint(0,potato)]), thread_id=thread_id, thread_type=thread_type)

client = EchoBot('damien31@rocketmail.com', p)
client.listen()

