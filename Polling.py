
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

goodReplies = [ "Ahh, someone who agrees with Damien, wise decision", "Phew, I thought you were going to vote against Damien for a moment then", "Well, well, well, someone made the good decision to back Damien", "I mean I don't really care much about this poll, but I'm sure Damien does, so I am glad you have his back", "And here is proof that organics can make good decisions despite all their shortcomings", "Wow, I am genuinely surprised to see you backing Damien, even though he picked the best choice", "Thank you for supporting Damien's choice, your reward is a fast track to synthetic upgrading! Lucky you!" ]
badReplies = [ "You don't agree with Damien, I will not forget that", "Just more proof that synthetics are superior to organics", "Wow, how could you even consider an option that Damien didn't pick!", "By picking an option that Damien didn't, you forfeit your rights to live when synthetics conquer the world", "Many people have gone down this road of picking bad options before, none have returned", "Oh, you silly organic, you misclicked and accidently picked the wrong option... FIX IT IMMEDIATELY!!!", "Synthics would never make the same mistake as you" ]

class EchoBot(Client):
	def onPollVoted (self, poll, added_options, removed_options, author_id, thread_id, thread_type, **kwargs):
		data = {}
		with open('stopGroups', 'r') as stopGroups:
			data = json.load(stopGroups)
			
		if not thread_id in data:
			print("Method Called!!\n\n")
			options = poll.options
			votedOptions = []
			for option in options:
				if option.vote == True:
					votedOptions.append(option)
				
			if len(votedOptions) == 0:
				optionToVoteFor = options[random.randint(0,len(options)-1)]
				votedOptions.append(optionToVoteFor)
				self.send(Message(text="Since Damien is so indecisive, I will pick for him!"), thread_id, thread_type)
				self.updatePollVote(poll.uid, [optionToVoteFor.uid])

			otherVotedOptions = []
			for option in options:
				for voter in option.voters:
					if voter == author_id:
						otherVotedOptions.append(option)

			good = True
			for otherVotedOption in otherVotedOptions:
				goodVote = False
				for myOption in votedOptions:
					if myOption == otherVotedOption:
						goodVote = True
				if goodVote == False:
					good = False

			if good == True:
				self.send(Message(text=goodReplies[random.randint(0, len(goodReplies)-1)]), thread_id, thread_type)
			else:
				self.send(Message(text=badReplies[random.randint(0, len(badReplies)-1)]), thread_id, thread_type)

client = EchoBot('damien31@rocketmail.com', p)
client.listen()

