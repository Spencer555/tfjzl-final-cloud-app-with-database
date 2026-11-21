from django.contrib import admin

from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Question,
    Choice,
    Submission
)


# LESSON INLINE
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 2


# CHOICE INLINE
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# QUESTION INLINE
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


# COURSE ADMIN
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# LESSON ADMIN
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# QUESTION ADMIN
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']


# REGISTER MODELS
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
 