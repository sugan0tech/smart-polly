from cgitb import text
from gtts import gTTS
from dotenv import load_dotenv
import os
import ftplib
import uuid
import json

#storing text with corresponding audio
def update_json(text, name) :
    with open('data.json', 'r+') as f:
        data = json.load(f)
        data[text] = name 
        f.seek(0)        
        json.dump(data, f, indent=4)
        f.truncate()     

def play(name):
    os.system(f"mpg123 {name}.mp3")

def save_to_bunny(name, text):
    session = ftplib.FTP(os.getenv("URL"),os.getenv("USERNAME"),os.getenv("PASSWORD"))
    audio = open(f"{name}.mp3",'rb')                  
    #sends the file
    session.storbinary(f"STOR {name}.mp3", audio)     
    audio.close()                                    
    session.quit()
    update_json(text, name)


load_dotenv()


if __name__ == "__main__":
    print("Welcome to the NeoTTS ;)")
    text_val = str(input("Enter the text :"))
    print("Options:\n1.Play audio only\n2.Play audio and store\n3.Store Directly")
    option = int(input("Enter the option :"))
    name = str(uuid.uuid4())

    object = gTTS(text=text_val, slow=False)
    object.save(f"{name}.mp3")


    # Only plays mp3
    if(option == 1):
        play(name)

    #Plays and saving
    elif(option == 2):
        play(name)
        save_to_bunny(name, text_val)

    #Saving alone
    elif(option == 3):
        save_to_bunny(name, text_val)
    else:
        print("Invalid Input")


    os.remove(f"{name}.mp3")