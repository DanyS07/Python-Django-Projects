from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team




def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
#def addition(request):
 #   x= int (request.GET['num1'])
  #  y= int (request.GET['num2'])
   # sum1=x+y
   # diff=x-y
   # prod=x*y
   # quo=x/y
   # return render(request, 'result.html',{'result1':sum1,'result2':diff, 'result3':prod, 'result4':quo})