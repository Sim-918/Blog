from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get(self,request):
        feed_list=Feed.objects.all()        #Feed의 데이터를 feed_list에 넣음
    
        return render(request,"Simpleblog/main.html",context=dict(feeds=feed_list))
    