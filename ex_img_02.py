

import os           # os 모듈을 사용해서 환경변수에 접근 (키값 사용)
from openai import OpenAI
import uuid
import requests     # pip install requests

# 이 컴퓨터의 환경변수의 키값을 읽어온다
#               환경설정에 접근 (내가정한변수이름)
openai_api_key = os.getenv("OPENAI_API_KEY")  

# 초기화      무조건 이이름 = 내마음대로 이름
client = OpenAI(api_key=openai_api_key)

prompt_txt = """
A bright beach scene on a sunny day, 
with clear blue skies and sparkling turquoise water.
"""

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt_txt ,
    size="1024x1024",
    quality="standard",
    n=1,
)

# 그림을 못주니까 url로 주소로 줌
image_url = response.data[0].url
print(image_url)


# 다운로드 받을 경로
download_path = "C:\\javaStudy\\upload_py"

# 파일 이름 생성
file_name = str(uuid.uuid4())+".png"

# 이미지 다운로드
response = requests.get(image_url)
if response.status_code == 200:
        file_path = os.path.join(download_path, file_name)      
        with open(file_path, "wb") as file:        # wb 쓰는데 바이너리 사진
            file.write(response.content)
        
        print("다운로드 완료")
else:
    print("url 오류")

