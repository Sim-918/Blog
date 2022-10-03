from django.shortcuts import render
from rest_framework.views import APIView

class Sub(APIView):
    def get(self,request):
        print("get호출")
        return render(request,"Simpleblog/main.html")
    def post(self,request):
        print("post호출")
        return render(request,"Simpleblog/main.html")
