from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from ..models import Question, Choice

class DetailView(generic.DetailView):
    pk_url_kwarg = 'question_id'
    model = Question

class ResultsView(DetailView):
    template_name = 'polls/results.html'
