from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def set_session(request):
    """设置session"""
    request.session['username'] = 'admin'
    request.session['age'] = 18
    return HttpResponse('ok')


def get_session(request):
    """读取session"""
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username + ':' + str(age))
