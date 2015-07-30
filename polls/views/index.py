from django.http import HttpResponse

from ..models import Question

def index(request):
    recent_questions = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question_text for p in recent_questions])
    return HttpResponse(output)
