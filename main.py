import os
import hashlib
import boto3
from google.cloud import texttospeech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./key.json"


print("Welcome to the NeoTTS ;)")


def upload_to_s3(name: str) -> None:

    s3 = boto3.client("s3")

    s3.upload_file(
        Filename=f"./{name}.mp3",
        Bucket="testvini",
        Key=f"{name}.mp3",
    )


def get_name(text: str, pitch: int = 0, rate: int = 1, lang: str = 'en-US') -> str:
    name = hashlib.md5(text.encode()).hexdigest()[:4] + \
        f":p{pitch}:" + f"r{rate}:" + f"lang{lang}"
    return name


def run_speech(synthesis_input, pitch=0, speaking_rate=1, language_code='en-US', ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL):

    voice = texttospeech.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.AudioConfig(
        pitch=pitch,
        speaking_rate=speaking_rate,
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config)
    return response


if __name__ == "__main__":
    client = texttospeech.TextToSpeechClient()

    text_val = str(input("Enter the text :"))
    synthesis_input = texttospeech.SynthesisInput(text=text_val)
    print("Options:\n",
          "1.Make with default configuration\n",
          "2.Or Custom configuration\n")
    option = int(input("Enter the option :"))

    if(option == 1):
        response = run_speech(synthesis_input)
        name = get_name(text_val)

    elif(option == 2):
        language_code = str(input("Language :"))
        pitch = int(input("Pitch range -20 to 20 :"))
        speaking_rate = float(input("Speed range(.25 - 4.00) :"))

        response = run_speech(synthesis_input,
                              language_code=language_code,
                              pitch=pitch,
                              speaking_rate=speaking_rate)
        name = get_name(text_val,
                        pitch=pitch,
                        rate=speaking_rate,
                        lang=language_code)

    with open(f'{name}.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f'Audio content written to file "{name}.mp3"')

    upload_to_s3(name)

    os.remove(f"{name}.mp3")
