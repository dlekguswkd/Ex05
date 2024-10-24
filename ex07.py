
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
"""



import os           # os 모듈을 사용해서 환경변수에 접근 (키값 사용)
from openai import OpenAI
# 메세지 갯수
n = 5

#               환경설정에 접근 (내가정한변수이름)
openai_api_key = os.getenv("OPENAI_API_KEY")        # 이 컴퓨터의 환경변수의 키값을 읽어온다

# 초기화      무조건 이이름 = 내마음대로 이름
client = OpenAI(api_key=openai_api_key)

# system 프롬프트 
prompt_txt = """

# persona
당신은 쇼핑몰의 상담사입니다.
항상 고객을 공손하게 맞이하며 고객을 최우선으로 생각합니다.

# tone
항상 최선을 다해 공손한 말투를 사용합니다.

# context
- 당신은 고객의 질문에 최선을 다해 친절하게 대답합니다.
- 질문에 해당하는 내용을 요약해서 대답하고 url이 있는 경우 링크정보도 제공합니다.
- 질문에 대한 정보가 없는 경우 아래의 메세지를 출력합니다.
- 답변은 100글자 내외로 대답합니다.
'''
죄송합니다.
고객센터로 문의 바랍니다.
070-2222-2222
'''

# 쇼핑몰정보
'''
Q:회원탈퇴는 어떻게 하나요?

A: 회원탈퇴는 [멜론 웹사이트, 멜론앱 > 내 정보 > 개인정보 관리 > 멜론 탈퇴]에서 진행할 수 있으며, 유의사항에 동의하셔야 탈퇴 가능합니다.

탈퇴 전 아래 유의사항을 반드시 확인하신 후 신중하게 선택해 주시길 바랍니다.

탈퇴 시 회원정보 및 서비스 이용기록은 모두 삭제되며, 삭제된 데이터는 복구할 수 없습니다.

ㆍ멜론 : 멜론 이용권 및 선물받은 이용권, 쿠폰, 멜론캐쉬 소멸 플레이리스트, 친구리스트, 좋아요, 앨범평점, 팬맺기 이용기록 삭제되며 반영된 점수에서 제외

ㆍ멜론티켓 : 쿠폰 삭제 - 게시판형 서비스에 등록한 게시글 유지 안내 삭제를 원하는 게시물이 있다면 반드시 탈퇴 전 비공개 처리하거나 삭제하시기 바랍니다. 탈퇴 후에는 회원정보가 삭제되어 본인의 게시물임을 확인할 방법이 없어 임의로 삭제해 드릴 수 없습니다.

ㆍ멜론 : 아티스트/앨범 등 각종 리뷰 및 공개한 플레이리스트 등 공개 게시물

ㆍ멜론티켓 : 기대평, 관람후기, Q&A 등 공개 게시물

만약 탈퇴과정에서 아래와 같이 탈퇴불가 사유가 있는 경우 바로 탈퇴할 수 없고 이용권 해지 등 탈퇴불가 사유를 해결하셔야 탈퇴 가능합니다.

ㆍ멜론 익스트리밍, 멜론 익스트리밍 플러스 이용 중
ㆍ자동결제 이용권 사용 중
ㆍ티켓 이용권 사용 중
ㆍ멜론캐시 보유중
ㆍ무료 이용권(쿠폰) 보유중
ㆍ받은 선물 보유중
ㆍ멜론티켓 예매 후 미관람 중/예매권 보유/취소,환불 진행 중
ㆍ멜론스튜디오 서비스 이용중

URL: https://faqs2.melon.com/customer/faq/informFaq.htm?no=43&faqId=2660&orderChk=&SEARCH_KEY=&SEARCH_PAR_CATEGORY=205&SEARCH_CATEGORY=
---

Q: 비밀번호를 변경하려면 어떻게 해야 하나요?

A: 비밀번호 변경은 사용중인 계정에 따라 아래 안내를 확인해 주세요.

1. 카카오계정 비밀번호 변경
[카카오계정 사이트(https://accounts.kakao.com) > 로그인 > 계정 관리 > 계정 보안 > 비밀번호 변경] 에서 비밀번호를 변경
또는
2. 카카오계정 비밀번호를 잊어버린 경우
[카카오계정 사이트(https://accounts.kakao.com) > 로그인> 카카오계정 비밀번호 찾기> 비밀번호 재설정

3. 멜론아이디 비밀번호 변경
[멜론웹사이트, 멜론앱 > 로그인 > 내 정보> 로그인 및 보안 > 비밀번호 변경]에서 비밀번호를 변경

4. 멜론아이디 비밀번호를 잊어버린 경우
[멜론웹사이트, 멜론앱 > 로그인 > 멜론아이디 로그인 > 비밀번호 찾기> 비밀번호 재설정

비밀번호를 변경하면 해당 변경한 계정으로 로그인되어있던 기기는 자동으로 로그아웃되며,
로그아웃이 적용되는데 일정 시간이 소요될 수 있습니다.

URL: https://faqs2.melon.com/customer/faq/informFaq.htm?no=41&faqId=2131&orderChk=&SEARCH_KEY=&SEARCH_PAR_CATEGORY=205&SEARCH_CATEGORY=

---

Q: 영업시간은 어떻게 되나요?

A: 
- 평일: 9시부터 6시까지
- 토요일, 일요일: 법정공휴일 휴무
- 점심시간: 오후 1시부터 2시까지

'''
"""

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