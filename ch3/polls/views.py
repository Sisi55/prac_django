from django.shortcuts import render
from polls.models import Question #Question 테이블에 접근하기 위해 import

# Create your views here.

def index(request): #request 객체는 뷰 함수의 필수 인자
    # lastest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'lastest_question_list': ''}
    return render(request, 'polls/index.html', context) #단순히 페이지 render만 한다
    #render 디폴트 .html 파일 위치가 polls-앱/template 폴더인가보다
    #HttpResponse 객체를 반환합니다


