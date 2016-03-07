#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
# 	TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
# 	return render(request,'home.html',{'TutorialList':TutorialList})
# def home(request):
# 	info_dict = {'site':u'自强学堂','content':u'各种IT技术教程'}
# 	return render(request,'home.html',{'info_dict':info_dict})
# def home(request):
# 	List = map(str,range(100))
# 	return render(request,'home.html',{'List':List})
# def add(request,a,b):
# 	c = int(a)+int(b)
# 	return HttpResponse(str(c))
def test(request):
	return render(request,'test.html')
def sub(request):
	a = str(request.GET['a'])
	b = str(request.GET['b'])
	c = int(request.GET['c'])
	d = str(request.GET['d'])
	e = {
		'name': a,
		'sex':  b,
		'age':  c,
		'job':  d
	}
	return render(request,'test1.html',{'e':e})
