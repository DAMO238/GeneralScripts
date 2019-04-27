# -*- coding: UTF-8 -*-



from fbchat import Client
from fbchat.models import *


from datetime import datetime
from threading import Timer

from getpass import getpass
from sys import argv

p = ""
try:
	p = argv[1]
except:
	p = getpass()

client = Client('damien31@rocketmail.com', p)
group = client.fetchGroupInfo('2136630926368530')
client.logout()
user_ids = group['2136630926368530'].participants

x=datetime.today()
try:
	y=x.replace(day=x.day+1, hour=0, minute=0, second=0, microsecond=0)
except ValueError:
	y=x.replace(month=x.month+1, day=1, hour=0, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
	x = datetime.today()
	if (x.weekday() == 3):
		client = Client('damien31@rocketmail.com', p)
		
		print('Own id: {}'.format(client.uid))
		
		try:
			client.send(Message(text='Attention all puny organics: There is a meeting today in John\'s JCR at 7pm.'), thread_id='2136630926368530', thread_type=ThreadType.GROUP)
		except:
			for user_id in user_ids:
				client.send(Message(text='I know that someone removed me! But you shall not escape the wrath of Sanjeev!... \nMeeting, 7pm, John\'s JCR, Be there or else!'), thread_id=user_id, thread_type=ThreadType.USER)
		
		client.logout()
	
	x=datetime.today()
	try:
		y=x.replace(day=x.day+1, hour=0, minute=0, second=0, microsecond=0)
	except ValueError:
		y=x.replace(month=x.month+1, day=1, hour=0, minute=0, second=0, microsecond=0)
	delta_t=y-x
	
	secs=delta_t.seconds+1
	
	t = Timer(secs, hello_world)
	t.start()

t = Timer(secs, hello_world)
t.start()


