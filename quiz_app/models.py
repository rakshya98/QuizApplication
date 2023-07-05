from django.db import models

# Create your models here.
import random
from django.db import models
import uuid

# Create your models here.
# Abstract base class inheritance is used when you want to put some common information into a number of other models.
# To do that you create a base class and put abstract=True in the Meta class.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract=True

class Category(BaseModel):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name



class Question(BaseModel):
    category=models.ForeignKey(Category , related_name='category', on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    marks=models.IntegerField(default=5)

    
    def __str__(self): 
        return self.question
    
    def get_answers(self):
        answer_objects=list(Answer.objects.filter(question=self))
        random.shuffle((answer_objects))
        data=[]
        for answer_object in answer_objects:
            data.append({
                'answer':answer_object.answer,
                'is_correct':answer_object.is_correct
            })
        return data
class Answer(BaseModel):
    question=models.ForeignKey(Question, related_name='question_answer',on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)

    
    def __str__(self):
        return self.answer
