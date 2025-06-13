from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import os
from dreams.models import DreamRecord
# import google.generativeai as genai
from django.http import JsonResponse
from .api import get_gemini_response
from urllib.parse import unquote

from .models import Interpret


# Create your views here.
## 꿈 해몽 출력
@login_required
def interpretation_view(request, content):
        # print(content)
        # url로 받은 문자열 디코딩
        decodedContent = unquote(content)
        dream = DreamRecord.objects.filter(context=decodedContent).first()

        if not decodedContent:
            interpret = None
            interpret.result = "꿈을 기록해 주세요."
        else:
            if dream:
                interpret = Interpret(dreamRecord=dream)
                extra_text = ' 이 꿈 내용이 무엇을 암시하는지 해몽해 줘.'
                full_prompt = decodedContent + extra_text
                interpret.result = get_gemini_response(full_prompt)
                interpret.save()
            else:
                interpret = Interpret()
                interpret.result = "해당 꿈 기록이 없습니다."
                interpret.save()

        return render(request, 'interpretation.html', {
            'interpret': interpret,
        })


@login_required
def interpretation_save(request, interpret_id):
    interpret = get_object_or_404(Interpret, id=interpret_id)
    print("interpret:", interpret)
    print("interpret.id:", getattr(interpret, 'id', None))
    # if request.method == 'POST':
    #     content = request.POST.get('content')
    dreams = DreamRecord.objects.filter(user=request.user).order_by('-id')  # 최신순 정렬


    return render(request, 'dreams/dream_list.html', {'dreams': dreams})

# @login_required
# def interpretation_save(request, dream_id):
#     dream = get_object_or_404(DreamRecord, id=dream_id)
#     return redirect
