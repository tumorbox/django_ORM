# Django ORM
---
## CREATE
**1. INSERT TINTO TABLE (column1, culomn2.....) values (values1, values2 ......)** 

```python
# 첫번째 방법
article = Article()
article.title = 'fisrt'
article.content = 'django!'
article.save()

# 두번째 방법
# 어느 변수에 어떤 값을 넣을건지 명시
# id가 생략되어 있을 뿐, 자동으로 생성된다.
article = Article(title='second',
            content='django!')
article.save()

# 세번째 방법
Article.object.create(title='third', content='django~~')

```

## select
**2. SELECT *FROM articles_artcle**

```python
# 전체 조회
article = Article.objects.all()

```
## where
**3. SELECT * FROM articles_article WHERE title='first'**

```python
# 특정 제목 불러오기
Article.objects.filter(title='first')
```

**4. SELECT * FROM articles_article WHERE title = 'first' LIMIT 1**

```python
Article.objects.filter(title='first').first()
Article.objects.filter(title='first').last()
Article.objects.filter(title='first')[0]
```

**5. SELECT * FROM articles_article WHRER id=1**

```python
Article.objects.get(id=1)
Article.objects.get(pk=1)
# 주의점
# 고유값이 아닌 내용을 필터링해서 2개 이상의 값을 찾아오면 오류를 발생한다.
# 없는 것을 가지고 오려고 해도 오류 발생
```

**6. Like / startswith / endwith**

```python
# 특정 문자열을 포함하고 있는가
Article.objects.filter(title__contains="fir")
# 특정 문자열로 시작하는가
Article.objects.filter(title__endswith="ha")
# 특정 문자열로 끝나는가
Article.objects.filter(title__endswith="ha")
```

---
## UPDATE 
**7. UPDATE articles_article SET title='byebye' WHERE id=1**

```python
# 수정
artilce = Article.objects.get(pk=1)
article.title = 'byebye'
article.save()
```

---
## DELETE
**8. DELETE FROM articles_article WHERE id=1**

```python
# 삭제
artilce = Article.objects.get(pk=1)
article.delete()
```

