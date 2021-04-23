from django.db import models
from django.utils.translation import ugettext_lazy as _
from quiz.choices import TYPE, MULTIPLE_CHOICE
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

class Quiz(models.Model):

    title = models.CharField(max_length=255, default=_(
        "New Quiz"), verbose_name=_("Quiz Title"))
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")

class Updated(models.Model):

    date_updated = models.DateTimeField(
        verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True

class Question(Updated):

    quiz = models.ForeignKey(
        Quiz, related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(
        choices=TYPE, default=MULTIPLE_CHOICE, verbose_name=_("Type of Question"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    score = models.IntegerField(
        default=1, verbose_name=_("Points for the task"))
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

class Answer(Updated):

    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")

class QuizResult(models.Model):
    
    user = models.ForeignKey(
        Question, related_name='quizresult', on_delete=models.CASCADE)
    quiz = models.ForeignKey(
        Quiz, related_name='quizresult', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(
        verbose_name=_("Starting the Quiz"), auto_now=True)
    deadline = models.DateTimeField(verbose_name=_("Finish the Quiz")),
    right_answers = models.PositiveSmallIntegerField(
        null=False, default=0, verbose_name=_("Right answers"))
    wrong_answers = models.PositiveSmallIntegerField(
        null=False, default=0, verbose_name=_("Wrong answers"))
    mark = models.PositiveSmallIntegerField(
        null=False, default=0, verbose_name=_("Mark"))

    class Meta:
        verbose_name = _("QuizResult")
        verbose_name_plural = _("QuizResults")