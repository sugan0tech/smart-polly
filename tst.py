import os
from gtts import gTTS

va = input("Enter the text :")

object = gTTS(text=va,slow=False)

object.save("1.mp3")
os.system("mpg123 1.mp3")
