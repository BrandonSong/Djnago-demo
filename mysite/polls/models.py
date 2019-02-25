import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Chiocce(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# 测试代码
# class Manufacturer(models.Model):
#     pass
#
# 
# class Car(models.Model):
#     manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)  # 多对一的外键关系

class Topping(models.Model):
    pass


class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)