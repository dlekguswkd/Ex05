
"""
1. 최소버전 + 토큰값
"""



import os           # os 모듈을 사용해서 환경변수에 접근 (키값 사용)
from openai import OpenAI

#               환경설정에 접근 (내가정한변수이름)
openai_api_key = os.getenv("OPENAI_API_KEY")        # 이 컴퓨터의 환경변수의 키값을 읽어온다

            #   무조건 이이름 = 내마음대로 이름
client = OpenAI(api_key=openai_api_key)

#                                   함수  (파라미터 (변수=값))
response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",          # 꼭있어야함
    messages=[              # 리스트안에 딕션어리 (딕션어리로 여러개 들어갈수있다는뜻)
        {"role":"system", "content":"너는 일반적인 문장을 시로 표현을 잘하는 재능을 가진 유명한 시인이야"},
        {"role":"user", "content":"강남역을 100자내로 설명해줘"}    # 꼭있어야함
    ],      
    temperature=1,              # 엉뚱한 단어
    max_tokens=2048,            
    top_p=1,                    # 다양한 문장형식 1~5형식
    frequency_penalty=0,        # 중복단어 제한
    presence_penalty=0,         # 다른 주제까지 확장
    response_format={
        "type": "text"
    }
)


print(response.choices[0].message.content)      # 답변의 메세지만 딱 옴


# 토큰수 확인
q_token = response.usage.prompt_tokens         # 질문토큰수
a_token = response.usage.completion_tokens     # 응답토큰수
t_token = response.usage.total_tokens             # 전체토큰수
print(f"질문:{q_token}+응답:{a_token}=합계:{t_token}")
