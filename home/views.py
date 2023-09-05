from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import random
# Create your views here.

def home(request):
    context = {'categories' : Category.objects.all()}

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request, "home.html", context)


def quiz(request):
    content = {'category': request.GET.get('category')}
    return render(request, "quiz.html", content)


def get_quiz(request):
    try:
        category_name = request.GET.get('category')
        
        if category_name:
            question_objs = Question.objects.filter(category__category_name__icontains=category_name)
        else:
            question_objs = Question.objects.all()
        
        question_objs = list(question_objs)

        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answers": question_obj.get_answers()
            })

        if not data:
            return JsonResponse({'status': False, 'message': 'No questions available for this category.'})

        payload = {'status': True, 'data': data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)
        return JsonResponse({'status': False, 'message': 'Something Went Wrong'})
