
"""
1. 최소버전 + 토큰값
---
2. 이전 내용 기억하기

"""



import os           # os 모듈을 사용해서 환경변수에 접근 (키값 사용)
from openai import OpenAI

#               환경설정에 접근 (내가정한변수이름)
openai_api_key = os.getenv("OPENAI_API_KEY")        # 이 컴퓨터의 환경변수의 키값을 읽어온다

# 초기화      무조건 이이름 = 내마음대로 이름
client = OpenAI(api_key=openai_api_key)

# system 프롬프트 
prompt_txt = """
    context: 50글자 이내로 답해주세요
    tone: 친절한 말투로 답변해주세요
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",          
    messages=[              
        {"role":"system", "content":prompt_txt},                        # 환경, 배경
        {"role":"user", "content":"대한민국의 수도는?"},                    # 사용자 나
        {"role":"assistant", "content":"대한민국의 수도는 서울입니다."},    # 지피티의 대답 이렇게 기억시킬수있음
        {"role":"user", "content":"그곳의 인구수는?"}                       # 사용자 나  
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
#print(response.choices[0])

