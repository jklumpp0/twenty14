from django.db import models
from django.contrib.auth.models import User

class AnswerManager(models.Manager):
    def for_user(self, user):
        records = Answer.objects.filter(user=user)
        return records
    
    def get_today(self, user):
        import datetime
        today = datetime.date.today()
        all_today = Answer.objects.filter(date=today, user=user)
        today_response = None
       
        # Find the most recent result today (for testing only)
        if all_today is not None and len(all_today) > 0:
            size = len(all_today)
            today_response = all_today[size - 1]

        return today_response

class Answer(models.Model):
    result = models.BooleanField()
    date = models.DateField(auto_now_add = True)
    user = models.ForeignKey(User)
    objects = AnswerManager()

    def __unicode__(self):
        return "YES" if self.result else "NO"


