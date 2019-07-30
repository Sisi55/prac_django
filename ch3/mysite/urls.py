"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls import views # polls 폴더 안에 views.py 파일 있다

urlpatterns = [
    path('/admin/', admin.site.urls),

# path(url패턴 문자열,  호출되는 뷰 함수, 추가인자, name=url패턴이름지정)
    path('/polls/', views.index, name='index'), #url 패턴 매칭은 위-아래로 진행되므로, 정의 순서에 유의한다
    # path('polls/<int:question_id>/', views.detail, name='detail'), #뷰 함수에 인자가 전달된다
    # path('polls/<int:question_id>/results/', views.results, name='results'),
    # path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]
