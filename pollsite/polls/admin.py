from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import AdvancedChoice, Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class ChoiceChildAdmin(PolymorphicParentModelAdmin):
    base_model = Choice


class AdvancedChoiceAdmin(ChoiceChildAdmin):
    pass


class ChoiceParentAdmin(PolymorphicParentModelAdmin):
    base_model = Choice
    child_models = (
        (AdvancedChoice, AdvancedChoiceAdmin)
    )


class AdvancedChoiceInline(admin.TabularInline):
    model = AdvancedChoice
    readonly_fields = ['choice_ptr']


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline, AdvancedChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
