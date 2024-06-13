
import pyautogui
import time
from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth
import os 
import datetime

def uploadFile(drive, filename):
    f = drive.CreateFile({'title': filename}) 
    f.SetContentFile(filename) 
    f.Upload()
    f = None
    

   
# For using listdir() 

   
  
# Below code does the authentication 
# part of the code 

if __name__ == "__main__":
    # gauth = GoogleAuth() 
    # gauth.LocalWebserverAuth()        
    # drive = GoogleDrive(gauth)

    while True:
        timeStamp = datetime.datetime.now()
        timeStamp = timeStamp.strftime("%d_%m__%H_%M_%S")
        image = pyautogui.screenshot()
        image1 = pyautogui.screenshot("output/{}.png".format(timeStamp))
        print("P1-Status| True| " + timeStamp)
        # uploadFile(drive, "image1.png")
        # break
        time.sleep(5)