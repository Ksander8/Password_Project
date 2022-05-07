from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'generator/index.html')


def password(request):
    abc_en = list('zyxwvutsrqponmlkjihgfedcba')
    length = int(request.GET.get('length', 0))

    if request.GET.get('uppercase'):
        abc_en.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        abc_en.extend(list('1234567890'))
    if request.GET.get('special'):
        abc_en.extend(list('#!@$%^&*()_+-=><?:"|\{|"}'))
    you_password = ''
    for _ in range(length):
        you_password += random.choice(abc_en)

    return render(request, 'generator/password.html', {'password': you_password})

def info(request):
    return render(request, 'generator/info.html')