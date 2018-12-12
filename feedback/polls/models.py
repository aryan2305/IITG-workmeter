from django.db import models

from organisation.models import Gymkhana_body


class Question(models.Model):
    body = models.ForeignKey(
        "organisation.Gymkhana_body", on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    totalvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
