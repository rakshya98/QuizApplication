
from django.urls import path
from quiz_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('api/get_quiz/',views.get_quiz,name='get_quiz'),
    path('quiz/',views.quiz,name='quiz'),
   
]
