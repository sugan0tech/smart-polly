import os
from dotenv import load_dotenv
load_dotenv()

import ftplib
session = ftplib.FTP(os.getenv("URL"),os.getenv("USERNAME"),os.getenv("PASSWORD"))
file = open('kitten.jpeg','rb')                  # file to send
session.storbinary('STOR kitten.jpeg', file)     # send the file
file.close()                                    # close file and FTP
session.quit()