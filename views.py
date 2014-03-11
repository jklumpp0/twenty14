from django.shortcuts import render
from django.template import RequestContext, Template, loader
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Answer
from django.http import HttpResponse

class ResponseHandler(object):
    import logging
    _logger = logging.getLogger('twenty14.views.ResponseHandler')
    _logger.info("Hi %s" % __name__)

    def __init__(self, request):
        self.request = request
        self.answer = Answer.objects.get_today(request.user)

    def _get_template(self):
        if self.answer is None:
            return 'twenty14/index.html'
        return 'twenty14/thanks.html'

    def _get_context(self):
        from .funcs import accum_map
        history = Answer.objects.for_user(user=self.request.user)
        answers = (h.result for h in history)
        history = zip(history, accum_map(answers))
        return {'response': self.answer, 'history': history}

    def render(self):
        method = getattr(self, '_' + self.request.method)
        ResponseHandler._logger.info("Calling %s" % method)
        return method()

    def _POST(self):
        is_better = self.request.POST['is_better']
        response = Answer(user=self.request.user)
        response.result = (True if is_better.upper() == "YES" else False)
        response.save()
        return HttpResponseRedirect(".")

    def _GET(self):
        c = RequestContext(self.request, self._get_context())
        return render(self.request, self._get_template(), c)

@login_required
def index(request):
    handler = ResponseHandler(request)
    return handler.render()
