import os
import uuid
from google.cloud import texttospeech

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./key.json"

# text = str(input())
name = str(uuid.uuid4())

# # Instantiates a client
# client = texttospeech.TextToSpeechClient()

# # Set the text input to be synthesized
# synthesis_input = texttospeech.SynthesisInput(text=text)

# # Build the voice request, select the language code ("en-US") and the ssml
# # voice gender ("neutral")
# voice = texttospeech.VoiceSelectionParams(
#     language_code='en-US',
#     ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)

# # Select the type of audio file you want returned
# audio_config = texttospeech.AudioConfig(
#     pitch=0,
#     speaking_rate=1,
#     audio_encoding=texttospeech.AudioEncoding.MP3)

# # Perform the text-to-speech request on the text input with the selected
# # voice parameters and audio file type
# response = client.synthesize_speech(
#     input=synthesis_input, voice=voice, audio_config=audio_config)

# The response's audio_content is binary.


def runSpeech(synthesis_input, pitch=0, speaking_rate=1, language_code='en-US', ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL):

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
    print("Welcome to the NeoTTS ;)")
    text_val = str(input("Enter the text :"))
    synthesis_input = texttospeech.SynthesisInput(text=text_val)
    print("Options:\n1.Make with default configuration\n2.Or Custom configuration\n")
    option = int(input("Enter the option :"))
    if(option == 1):
        response = runSpeech(synthesis_input)
        pass
    elif(option == 2):
        language_code = str(input("Language :"))
        pitch = int(input("Pitch range -20 to 20 :"))
        speaking_rate = float(input("Speed range(.25 - 4.00) :"))
        response = runSpeech(synthesis_input, language_code=language_code,
                             pitch=pitch, speaking_rate=speaking_rate)
        pass
    with open(f'{name}.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f'Audio content written to file "{name}.mp3"')
