import os
  
shutdown = input("Do you wish to shutdown your computer ? No or Yes ")
  
if shutdown == 'No' or 'no':
    print("Halted shutdown")
    exit()
else:
    os.system("shutdown /s /t 1")