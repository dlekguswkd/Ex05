# speech to text 말을 글자로

import os 
from openai import OpenAI

# 이 컴퓨터의 환경변수의 키값을 읽어온다
#               환경설정에 접근 (내가정한변수이름)
openai_api_key = os.getenv("OPENAI_API_KEY")  

# 초기화      무조건 이이름 = 내마음대로 이름
client = OpenAI(api_key=openai_api_key)


audio_file= open("C:\\javaStudy\\workspace-python\\Ex05\\tts.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)
print(transcription.text)