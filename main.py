import os
import ftplib
import uuid
from gtts import gTTS
from dotenv import load_dotenv
load_dotenv()

va = input("Enter the text :")

name = uuid.uuid4()
object = gTTS(text=va,slow=True)

object.save(f"{name}.mp3")

# os.system("mpg123 1.mp3")

session = ftplib.FTP(os.getenv("URL"),os.getenv("USERNAME"),os.getenv("PASSWORD"))
file = open(f"{name}.mp3",'rb')                  # file to send
session.storbinary(f"STOR {name}.mp3", file)     # send the file
file.close()                                    # close file and FTP
session.quit()
os.remove(f"{name}.mp3")