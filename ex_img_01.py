

import os           # os 모듈을 사용해서 환경변수에 접근 (키값 사용)
from openai import OpenAI


# 이 컴퓨터의 환경변수의 키값을 읽어온다
#               환경설정에 접근 (내가정한변수이름)
openai_api_key = os.getenv("OPENAI_API_KEY")  

# 초기화      무조건 이이름 = 내마음대로 이름
client = OpenAI(api_key=openai_api_key)

prompt_txt = """
A moody beach scene at sunset, 
with dramatic clouds reflecting vibrant colors in the sky. 
Gentle waves lap at the shore, and silhouettes of seagulls fly overhead. 
The atmosphere is tranquil yet mysterious.
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
