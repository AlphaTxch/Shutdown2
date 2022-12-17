import os
import time
  
shutdown = input("Do you wish to shutdown your computer ? No or Yes ")
  
if shutdown == 'no':
    print("Halted shutdown.")
    exit()
else:
    print("Shutting down pc")
    time.sleep(6)
    print("doing it rn")

    os.system("shutdown /s /t 1")