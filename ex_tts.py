# text to speech  글씨 읽어주는

import os 
from pathlib import Path
from openai import OpenAI


# 이 컴퓨터의 환경변수의 키값을 읽어온다
#               환경설정에 접근 (내가정한변수이름)
openai_api_key = os.getenv("OPENAI_API_KEY")  

# 초기화      무조건 이이름 = 내마음대로 이름
client = OpenAI(api_key=openai_api_key)

text = """
Today is a wonderful day to build something people love!

"""

# speech_file_path = Path(__file__).parent / "speech.mp3"         # 경로
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",          # 사람 목소리 선택
    input=text,      # 읽게하고 싶은 문장
    response_format="mp3",      # 안해도됨 보통이거
    speed=1.0               # 속도조절
)

# response.stream_to_file(speech_file_path)

speech_file_path = "C:\\javaStudy\\workspace-python\\Ex05\\tts.mp3"

# file = open(speech_file_path, "wb") -> close 해줘야함
with open (speech_file_path, "wb") as file:
    file.write(response.content)
    # 알아서 file.close() 해줌 -> with 문법
