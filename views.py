from django.shortcuts import render
from django.template import RequestContext, Template, loader
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Answer
from django.http import HttpResponse

def get_today(request):
    import datetime
    today = datetime.date.today()
    all_today = Answer.objects.filter(date = today, user = request.user)
    today_response = None

    if len(all_today) > 0:
        today_response = all_today.last()
    return today_response

@login_required
def index(request):
    if request.method == 'POST':
        is_better = request.POST['is_better']
        response = Answer(user = request.user)

        if type(is_better) not in (str, unicode):
            print("WTF: %s, %s" % (is_better, type(is_better)))
            return HttpResponseRedirect(".")

        if is_better.upper() == "YES":
            response.result = True
        else:
            response.result = False
        response.save() 
        return HttpResponseRedirect(".")
    else:
        c = RequestContext(request, {'name': 'Jared'})
        answer = get_today(request) 
        
        template = 'twenty14/index.html'
        if answer != None:
            template = 'twenty14/thanks.html'
            c['response'] = answer

        return render(request, template, c)

def logout(request):
    from django.contrib.auth import logout
    logout(request)
    print(request)
    return HttpResponse("HI")
