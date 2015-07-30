from django.http import HttpResponse
from django.template import RequestContext, loader

from ..models import Question

def index(request):
    recent_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'recent_questions': recent_questions,
    })
    return HttpResponse(template.render(context))
