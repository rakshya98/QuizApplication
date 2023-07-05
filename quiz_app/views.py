import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from quiz_app.models import Category, Question

# Create your views here.
def index(request):
      context = {'categories': Category.objects.all()}
      if request.GET.get('category'):
        category = request.GET.get('category')
        return redirect('/quiz/?category=' + category)
    # context={'categories':Category.objects.all()}
    # if request.GET.get('category'):
    #     return redirect(f"/quiz/?category={request.GET.get('category')}")
      return render(request,'quiz_app/index.html',context)

def quiz(request):
    context={'category':request.GET.get('category')}
    return render(request,'quiz_app/quiz.html',context)





def get_quiz(request):
    try:
        question_objects=Question.objects.all()
        
        if request.GET.get('category'):
            question_objects=question_objects.filter(category__category_name__icontains=request.GET.get('category'))
            question_objects=list(question_objects)
        data=[]
        random.shuffle((question_objects))
        for question_object in question_objects:
            data.append({
                "uid":question_object.uid,
                "category":question_object.category.category_name ,
                "question":question_object.question,
                "marks":question_object.marks,
                "answers":question_object.get_answers()
            })


        payload={'status':True , 'data':data}


        return JsonResponse(payload) 
        
    
    except Exception as e:
        print(e)

    return HttpResponse("Something went wrong")  
