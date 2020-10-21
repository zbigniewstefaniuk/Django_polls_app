from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    # basically it says to Django : Choice Obj are edited on admin site, render 3 choices forms
    model = Choice
    extra = 3


# allowing in admin panel to edit/add question
class QuestionAdmin(admin.ModelAdmin):
    fieldssets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)