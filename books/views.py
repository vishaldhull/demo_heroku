from django.shortcuts import render
import datetime

def first_page(request):
    now = datetime.datetime.now()
    return render(request, 'index.html', {'first_page': now})
