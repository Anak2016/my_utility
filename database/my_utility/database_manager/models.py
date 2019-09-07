import datetime
from django.db import models
from django.utils import timezone
import pytz
class Productivity_log(models.Model):
    # text = models.DateTimeField('text', null=True)
    auto_increment_id = models.AutoField(primary_key=True, default=0)
    date = models.DateTimeField('past_date', blank=True, null=True) #title of the columns to be show in django database.
    # text = models.CharField(max_length=100, blank=True, null=True)
    # date = models.DateTimeField('past_date', primary_key=True, default="No date speciied") #title of the columns to be show in django database.
    details = models.TextField(max_length=100, blank=True)
    hour = models.FloatField('productivity hour', null=True)

    # hour = models.FloatField('productivity hour', null=False)

    # pub_date = models.DateTimeField('date published', auto_now=True)
    # def __str__(self):
    #     return 'Producitiviy_log'

# class Progress_log(models.Model):
#     text = models.DateTimeField('past_date', primary_key=True)
#     pub_date = models.DateTimeField('date published', auto_now=True)
#     task = models.CharField(max_length=50)
#     date = models.DateTimeField('date', null=True )
#     status = models.BooleanField('finished/unfinish?', default=False)


#=====================
#==examples
#=====================

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published', null=True)
#
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'
#
#     def __str__(self):
#         return self.question_text
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete= models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
#


