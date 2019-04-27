from fbchat import Client
from fbchat.models import *

client = Client('damien31@rocketmail.com', 'utBw735x4%@R')
threads = client.fetchThreadList()
while True:
    
    for thread in threads:
        print("Thread: {}".format(thread))
        client.send(Message(text="Merry Christmas!"), thread_id = thread.uid, thread_type = thread.type)
    lastTimeStamp = int(threads[-1].last_message_timestamp)
    threads = client.fetchThreadList(before = lastTimeStamp - 1)
    
