from django.db import models

# Create your models here.
class Article(models.Model) :                   # articles_article로 생성된다.
    title = models.CharField(max_length=150)    # 글자수를 제한하고 싶을 때 사용 CharField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # False가 default값
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title} : {self.content}'


