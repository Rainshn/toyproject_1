from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import os
from dreams.models import DreamRecord
# import google.generativeai as genai
from django.http import JsonResponse
from .api import get_gemini_response
from urllib.parse import unquote


# Create your views here.
## 꿈 해몽 출력
@login_required
def interpretation_view(request, content):
        # print(content)
        # url로 받은 문자열 디코딩
        decodedContent = unquote(content)
        dream = DreamRecord.objects.filter(context=decodedContent).first()

        if not decodedContent:
            result = "꿈을 기록해 주세요."
        else:
            extra_text = ' 이 꿈 내용이 무엇을 암시하는지 해몽해 줘.'
            full_prompt = decodedContent + extra_text
            result = get_gemini_response(full_prompt)

        return render(request, 'interpretation.html', {
            'prompt': decodedContent,
            'result': result,
        })


