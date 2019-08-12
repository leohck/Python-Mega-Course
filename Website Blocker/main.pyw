#  Copyright (c)  9/8/2019
#  Developed by: Leonardo Black | 21 years old | Computer Engineer


import time
from datetime import datetime as dt

hosts_temp_path = "hosts.txt"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_black_list = ["www.facebook.com", "facebook.com", "terra.com", "www.terra.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 12) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        print("working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_black_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+'\n')
    else:
        print("Fun hours...")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_black_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)
