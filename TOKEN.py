import os, sys, platform,time
 
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    os.system('chmod 777 DUMP64')
    os.system('./DUMP64')
    
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    os.system('chmod 777 DUMP32')
    os.system('./DUMP32')
