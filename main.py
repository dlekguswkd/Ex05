
"""
웹사이트용

"""



import os           # os 모듈을 사용해서 환경변수에 접근 (키값 사용)
import sys
from openai import OpenAI
import chat_dao

sys.stdout.reconfigure(encoding="utf-8")        # 한글로 나오게하기

# [자기파일이름, "영업시간은?"]  필요한건 [1]방
if len(sys.argv) > 1:           # argv 정해진이름 
    question = sys.argv[1]          # 실행


    #               환경설정에 접근 (내가정한변수이름)
    openai_api_key = os.getenv("OPENAI_API_KEY")        # 이 컴퓨터의 환경변수의 키값을 읽어온다

    # 초기화      무조건 이이름 = 내마음대로 이름
    client = OpenAI(api_key=openai_api_key)

    # system 프롬프트 
    prompt_txt = chat_dao.get_data()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",          
        messages=[              
            {"role":"system", "content":prompt_txt},                # 환경, 배경
            {"role":"user", "content":question},            # 사용자 나
        ],          
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )


    print(response.choices[0].message.content)      # 답변의 메세지만 딱 옴

