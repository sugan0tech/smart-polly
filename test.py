import ftplib
session = ftplib.FTP('storage.bunnycdn.com','travelratings','430cdcb7-b0d3-4b41-ba40fb7a8da5-0a4b-4762')
file = open('kitten.jpeg','rb')                  # file to send
session.storbinary('STOR kitten.jpeg', file)     # send the file
file.close()                                    # close file and FTP
session.quit()