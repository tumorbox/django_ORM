from django.shortcuts import render, redirect
import requests

#모델 가져오기 
from articles.models import Article

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title': title,
        'content': content
    }
    return render(request, 'articles/create.html', context)

def introduce(request):
    return render(request, 'articles/introduce.html')


    # 1. /introduce/ 경로
    # 2. h1 태그로 이뤄진 메고
    # 2-1 각각의 p 태그에 이름과 나이 작석
    # 3. back 링크로  index로 돌아갈 수 있는 링크 하나
    # 4. index에서 introduce로 이동할 수 있는 링크 하나
    # 5. base.html 상속받아서 block body 안에 작성


    # 0616 오후 수업 14시~
    # edit
    # 1. 특정 글 삭제를 위한 경로 작성
    # 1-1. /articles/1/delete/
    # 2. 글 삭제 처리를 해주는 view 작성
    # 3. 글 삭제 후 , index page로 redirect
    # 4. 글 삭제를 위한 링크 detail에 작성
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    artcile.delete()
    return redirect('/articles:index')

    # update
    # 1. 특정 글 수정을 위한 경로 생성
    # 1-1. /articles/1/edit/
    # 2. 글 수정 template을 render하는 edit view 작성
    # 2-1. 해당 template에 from tag 작성
    # 2-2. 각 input tag 내부에 기존 내용이 들어 있어야함.
    # 2-3. value 속성을 확용 
    # 3. edit 보낸 데이터 처리를 위한 경로 생성
    # 3-1. /articles/1/update/
    # 4. 글 수정 처리를 하는 update view 작성
    # 5. 해당 글 상세 페이지로 redirect
    # 6. 글 수정을 위한 edit 링크 해당 글 상세 페이지에 생성
    # 6-1. {% url 'articles:edit' article.pk %}


