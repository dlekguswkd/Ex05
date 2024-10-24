
"""
1. 최소버전 + 토큰값
---
2. 이전 내용 기억하기
---
3. 사용자 질문입력하기
---
4. 반복해서 질문입력하기, 종료가능  * 대화내용이 누적되지않음
---
5. 대화내용 누적 -> 토큰(비용)이 많이 사용해야한다
---
6. 배경(1)+ 질문+답변(5*2) ==> 총 11개만 보관  --> 우리의 사이트의 정보가 없다
---
7. system에 사이트 정보 추가
---
8. 사이트정보 함수로 호출하기
"""



import os           # os 모듈을 사용해서 환경변수에 접근 (키값 사용)
from openai import OpenAI
import chat_dao

# 메세지 갯수
n = 7

#               환경설정에 접근 (내가정한변수이름)
openai_api_key = os.getenv("OPENAI_API_KEY")        # 이 컴퓨터의 환경변수의 키값을 읽어온다

# 초기화      무조건 이이름 = 내마음대로 이름
client = OpenAI(api_key=openai_api_key)

# system 프롬프트 
prompt_txt = chat_dao.get_data()

# 내용 누적
message_history = [
    {"role":"system", "content":prompt_txt},    
]

# 사용자로 부터 질문입력 받기
print("**************************************")
print("***반갑습니다. 질문을 입력해 주세요***")
print("**************************************")

while True:

    question = input("(사용자)")

    if question == "\q":
        break

    else:

        # 질문 추가
        message_history.append({"role":"user", "content":question}) # 사용자의 질문 추가

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


        #print(response.choices[0].message.content)      # 답변의 메세지만 딱 옴
        print(f"[챗_GPT]{response.choices[0].message.content}")
        message_history.append({"role":"assistant", "content":response.choices[0].message.content})    # 지피티의 대답 추가
    
        # 총 5개의 데이터만 유지
        if len(message_history) > n :
            message_history = [message_history[0]]+message_history[-(n-1):]
            print(message_history)

    # / else

print("**********************************")
print("*** 이용해 주셔서 감사합니다. ***")
print("**********************************")