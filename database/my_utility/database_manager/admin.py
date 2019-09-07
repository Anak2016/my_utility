from django.contrib import admin
# from .models import Progress_log, Productivity_log
from .models import Productivity_log



class Productivity_logAdmin(admin.ModelAdmin):
    search_fields = ['date', "details", "hour", 'auto_increment_id']
    list_filter =  ['date']
    # list_filter =  ['text']
    list_display = ('date', 'auto_increment_id', 'hour')

# class Progress_logAdmin(admin.ModelAdmin):
#     search_fields = ['date', 'task', 'status', 'text']
#     list_filter =  ['date']
#     list_display = ('text', 'date')


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']

# admin.site.register(Progress_log, Progress_logAdmin)
admin.site.register(Productivity_log, Productivity_logAdmin)