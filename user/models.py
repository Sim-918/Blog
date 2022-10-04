from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
class User(AbstractBaseUser):
    '''
    유저 닉네임
    유저 이메일 주소->실제 로그인할 때 사용하는 아이디
    유저 비밀번호
    '''
    # nickname=models.CharField(max_length=24,unique=True)     #닉네임
    # email=models.EmailField()            #이메일

    # class Mete:
    #     db_table="User"
