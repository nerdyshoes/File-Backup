#simply takes every file in the specified folders and copies them to backup folder
#create new folder with yy/mm/dd format as the name of the folder
import shutil
import os
from datetime import date

if os.path.exists(r"E:\Backup\Automated\Backups\21.09.25")==True:
    #print("test")
    os.rmdir(r"E:\Backup\Automated\Backups\21.09.25")
else:
    print("sad")



backup_directory = "E:\Backup\Automated\Backups"

#creates the new backups directory in the format yy/mm/dd
today = date.today()
new_directory = today.strftime("%y.%m.%d")+"/yes"
dst = os.path.join(backup_directory, new_directory)
print(dst)
#os.mkdir(dst)



shutil.copytree(r"C:\Users\Benjamin Mason\Documents", dst)
