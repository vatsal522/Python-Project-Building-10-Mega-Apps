import time
import os
from datetime import datetime as dt
while True:
    if os.path.exists('C:/Windows/System32/drivers/etc/hosts'):
        hosts_temp='hosts'
        hosts_path='C:/Windows/System32/drivers/etc/hosts'
        redirect='127.0.0.1'
        websitelist=['https://www.facebook.com','www.facebook.com','facebook.com']
        print("Path exists")
        if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,21):
            print('WORKING HOURS, CHECK LATER')
            with open(hosts_path,'r+') as file:
                content=file.read()
                print(content)
                for x in websitelist:
                    if x in content:
                        pass
                    else:
                        file.write("\n" +redirect+" "+x)




        else:
            with open(hosts_path,'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websitelist):
                        file.write(line)
                file.truncate() # delete everything after the cursor point
                
                
    
    time.sleep(5)
    
    
    
    
else:
    print("Please recheck the path")
