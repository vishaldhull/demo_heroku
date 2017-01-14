#from django.http import HttpResponse

#
#from django.http import Http404, HttpResponse
#import datetime

#def hello(request):
#   return HttpResponse("Hello world")

#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><body>It is now %s</body></html>" % now
#    return HttpResponse(html)

#def hours_ahead(request, offset):
#    try:
#        offset = int(offset)
#    except ValueError:
#        raise Http404()

#    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    assert False
#    html = "In %s hour(s), it will be  %s." % (offset, dt)
#    return HttpResponse(html)
#

#from django.template.loader import get_template
#from django.template import Context
#from django.http import HttpResponse
#import datetime

#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = get_template('hello.html')
#    html = t.render(Context({'current_date': now}))
#   return HttpResponse(html)

from django.shortcuts import render
import datetime

def current(request):
    now = datetime.datetime.now()
    return render(request, 'mypage.html', {'current_date': now})

def mynewview(request):
    now = datetime.datetime.now()
    somethingVariable = "<h2>"+str(now)+"</h2>"
    return render(request, 'mypage.html',{'something':somethingVariable})







