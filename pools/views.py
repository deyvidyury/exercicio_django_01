from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
	questions = Question.objects.order_by('-pub_date')
	return render(request, 'index.html',{'questions':questions})

def question(request, question_id):
	question = Question.objects.get(id=question_id)
	choices = question.choices.all()
	return render(request,'question.html',{'question':question, 'choices': choices})

def results(request, question_id):
	question = Question.objects.get(id=question_id)
	choices = question.choices.all()
	totalVotes = 0;
	for ch in choices:
		totalVotes += ch.votes
	return render(request,'results.html',{'question':question, 'choices': choices,'totalVotes': totalVotes})

def vote(request, question_id,choice_id):
	choice = Choice.objects.get(id=choice_id)
	choice.votes += 1;
	choice.save()
	return redirect('pools:results',question_id=question_id)

def manage(request, question_id):
	question = Question.objects.get(id=question_id)
	choices = question.choices.all()
	all_choices = Choice.objects.filter(question=None)
	return render(request, 'manage.html',{'question':question, 'choices': choices,'all_choices': all_choices})

def add(request, question_id,choice_id):
	choice = Choice.objects.get(id=choice_id)
	question = Question.objects.get(id=question_id)
	choice.question = question
	choice.save()
	return redirect('pools:manage',question_id=question_id)

def remove(request, question_id,choice_id):
	choice = Choice.objects.get(id=choice_id)
	choice.votes = 0
	choice.question = None
	choice.save()
	return redirect('pools:manage',question_id=question_id)

def change_status(request, question_id):
	question = Question.objects.get(id=question_id)
	question.closed = not question.closed
	question.save()
	return redirect('pools:manage',question_id=question_id)