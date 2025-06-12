# api.py
import google.generativeai as genai
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일에서 환경변수를 읽어옴

GEMINI_KEY = os.getenv("GEMINI_KEY")

def get_gemini_response(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_KEY}"  # API 엔드포인트 URL

    headers = {
        "Content-Type": "application/json"  # 요청 본문이 JSON 형식임을 명시
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ],
    }
    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()
    text = response_json['candidates'][0]['content']['parts'][0]['text']

    #텍스트 보기 좋게 변환
    cleaned_text = text.replace('**', '')  # 볼드 제거
    cleaned_text = text.replace('*', '')
    cleaned_text = cleaned_text.replace('\n', '<br>')  # 줄바꿈 처리
    return cleaned_text
