import os
import ftplib
from dotenv import load_dotenv
load_dotenv()

session = ftplib.FTP(os.getenv("URL"),os.getenv("USERNAME"),os.getenv("PASSWORD"))
file = open('test.mp3','rb')                  # file to send
session.storbinary('STOR test.mp3', file)     # send the file
file.close()                                    # close file and FTP
session.quit()