from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from ..models import Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'recent_questions'

    def get_queryset(self):
        """
        Return the last five published questions.
        Exclude polls set to be published in the future.
        """

        questions = Question.objects.filter(pub_date__lte=timezone.now())
        return questions.order_by('-pub_date')[:5]
