from django.contrib import admin

from .models import Question, Choice


# allowing in admin panel to edit/add question
class QuestionAdmin(admin.ModelAdmin):
    fieldssets = [
        (None, {'fields': ['pub_date', 'question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
