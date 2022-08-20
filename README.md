
# Project Neo

Simple python script to convert any language text to speech via Google's gTTS api.
and Stores speect as MP3 files directly into AWS s3 bucket.




## Features

#### you can create speech required

- pitch
- rate
- gender
- db
#### gTTS api reference [here](https://cloud.google.com/text-to-speech/docs/reference/rest/v1/text/synthesize).
#### All files are stored in a given S3 bucket done via [boto3](https://pypi.org/project/boto3/) (AWS SDK for python)






## Installation

Fist install [google-cloud](https://pypi.org/project/google-cloud/) and [AWS boto3](https://pypi.org/project/boto3/) python library
```bash
pip install google-cloud-texttospeech boto3
```

Authenticate your google-cloud account 
reference [here](https://codelabs.developers.google.com/codelabs/cloud-text-speech-python3#0)\
Authenticate you boto3
reference [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html)
## Running the Script


```bash
  python main.py
```


## Authors

- [@sugavanesh](https://www.github.com/sugan0tech)

