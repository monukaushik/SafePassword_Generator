from django.shortcuts import render,redirect
import random


def home(request):
    return render(request,'index.html')


def index(request):
    if request.method != 'POST':
        return render(request, 'index.html')
    thepass=''
    length=request.POST.get('lenght')
    length=int(length)
    characters=list('abcdefghijklmnopqrstuvwzyz')

    if request.POST.get('character'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.POST.get('scharacter'):
        characters.extend(list("! #$%&()*+,-./:;<=>?@[\]^_`{|}~ "))

    if request.POST.get('number'):
        characters.extend(list('0123456789'))

    for _ in range(length):
        thepass = thepass + random.choice(characters)
    return render(request, 'index.html', {'password': thepass})
