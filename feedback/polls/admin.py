from .models import Choice, Question
from django.contrib import admin

from organisation.models import Gymkhana_body


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['body']}),
        (None,               {'fields': ['question_text']}),
        ('Total votes', {'fields': ['totalvotes']}),
        ('Date information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


class Gymkhana_bodyAdmin(admin.ModelAdmin):

    inlines = [QuestionInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Gymkhana_body, Gymkhana_bodyAdmin)
