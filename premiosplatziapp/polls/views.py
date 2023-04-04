from ast import arg
from pyexpat import model
from re import template
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choise, Question


#def index(request):
#    latest_question_list = Question.objects.all()
 #   return render(request,"polls/index.html",{
  #      "latest_question_list":latest_question_list
   # })

#def detail(request,question_id):
 #   question = get_object_or_404(Question,pk=question_id)
  #  return render(request,"polls/detail.html",{
   #     "question":question
    #})

#def results(request,question_id):
 #   question = get_object_or_404(Question, pk=question_id)
  #  return render(request,"polls/results.html"),{
   #     "question":question
    #}

class IndexView(generic.ListView):
    template_name= "polls/index.html"
    context_object_name= "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("pub_date")

class DetailView(generic.DetailView):    
    model = Question
    template_name = "polls/detail.html"

class ResulstView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choise = question.choise_set.get(pk=request.POST["choise"])
    except (KeyError,Choise.DoesNotExist):   
        render(request,"polls/detail.html",{
            "question":question,
            "error_message":"No elegiste la respuesta"
        })
    else:
        selected_choise.votes += 1
        selected_choise.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
