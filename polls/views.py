from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

def detail(request, question_id): # 질문 상세 페이지
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)
def results(request, question_id): # 투표 결과 페이지
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote(request, question_id): # 투표 페이지
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_questiond_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def vote(request, question_id):
    choice = request.GET.get('choice')
    data = Choice.objects.get(id=choice)
    votes = data.votes
    votes = votes + 1
    data.votes = votes
    data.save()
    return HttpResponse("you're voting on question %s" % question_id)
    
    #output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse("Hello, world. You're at the polls index.")
    #return HttpResponse(output)