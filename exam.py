
import os           # os 모듈을 사용해서 환경변수에 접근 (키값 사용)
from pathlib import Path
from openai import OpenAI

#               환경설정에 접근 (내가정한변수이름)
openai_api_key = os.getenv("OPENAI_API_KEY")        # 이 컴퓨터의 환경변수의 키값을 읽어온다

# 초기화      무조건 이이름 = 내마음대로 이름
client = OpenAI(api_key=openai_api_key)

# system 프롬프트 
prompt_txt = """
# 명령[task]
내가 주제를 주면 그 주제에 맞게 아이들을 위한 동시를 하나 만들어줘

# 맥락[context]
긍정적인 단어를 사용해줘
나는 아이들을 위한 동시가 필요해
쓸데없는 말은 하지말고 동시만 딱 말해줘

# 예시[example]
강아지
귀여운 강아지, 활짝 웃으며,
꼬리 흔들고 뛰어와 반겨주네.
모두 함께 놀고, 달리기 시작,
햇살 아래 즐거운 하루가 돼!

# 페르소나[persona]
너는 유치원 선생님이야
밝고 긍정적인 말투로 해줘

# 형식[format]
답변은 150글자 이내로 해줘
아이들을 위한 시인처럼 동시를 만들어줘
예시처럼 형식을 갖춰줘
json형식 말고 일반 문자열로 출력해줘

# 어조[tone]
밝고 긍정적인 말투로 희망찬 어조를 사용해줘
"""


while True:

    # 사용자로 부터 질문입력 받기
    print("*****주제를 입력해주세요*****")
    print("")
    question = input("주제: ")

    if question == "\q":
        break

    else:

        # 메세지
        message_history = [
            {"role":"system", "content":prompt_txt},        # 환경, 배경
            {"role":"user", "content":question},            # 사용자 나
        ] 

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",          
            messages= message_history,          
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={
                "type": "text"
            }
        )

        content = response.choices[0].message.content  
        print(content)

        print("")

        text = content

        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",          # 사람 목소리 선택
            input=text,             # 읽게하고 싶은 문장
            response_format="mp3",      
            speed=1.0               # 속도조절
        )


        # 경로
        speech_file_path = "C:\\javaStudy\\workspace-python\\Ex05\\exam.mp3"

        with open (speech_file_path, "wb") as file:
            file.write(response.content)
