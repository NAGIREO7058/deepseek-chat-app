# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
 
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")
 
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你叫骏东，是一个人工智能助手"},
        {"role": "user", "content": "你好，你叫什么名字"},
    ],
    stream=False
)
 
print(response.choices[0].message.content)