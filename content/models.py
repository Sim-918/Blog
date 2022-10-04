from operator import mod
from django.db import models

# Create your models here.
# 1.사진들(최대 4개까지)
# 2. 글 내용
# 3. 작성자
# 4. 제목
class Feed(models.Model):
    #content=models.TextField()      #글내용
    image=models.TextField()       #4개의 이미지 중 첫 번째 이미지
    user_id=models.TextField()      #글쓴이
    title=models.TextField()        #제목

# class UploadFeed(models.Model):
#     #1.제목
#     #2.사진(4개)
#     #3.본문
