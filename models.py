from django.db import models
from django.contrib.auth.models import User

class AnswerManager(models.Manager):
    def for_user(self, user):
        records = Answer.objects.filter(user=user)
        return records

class Answer(models.Model):
    result = models.BooleanField()
    date = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User)
    objects = AnswerManager()

    def __unicode__(self):
        return "YES" if self.result else "NO"


