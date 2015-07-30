from django.shortcuts import render

from ..models import Question

def index(request):
    recent_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'recent_questions': recent_questions}
    return render(request, 'polls/index.html', context)
