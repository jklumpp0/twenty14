from django.db import models
from django.contrib.auth.models import User

class Answer(models.Model):
        result = models.BooleanField()
        date = models.DateField(auto_now_add = True)
        user = models.ForeignKey(User)
    
        def __unicode__(self):
            return "YES" if self.result else "NO"

