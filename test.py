import datetime
now_time = datetime.datetime.now()
future_time = now_time+datetime.timedelta(seconds=10)

while True:
    if datetime.datetime.now() > future_time:
        print('10secs has passed')
        break;
        
        
