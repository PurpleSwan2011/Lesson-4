import os
shutdown=input("do u wish to shutdown ur computer(y or n)")
if shutdown=='no':
 exit()
else:
    os.system("shutdown /s /t 1")