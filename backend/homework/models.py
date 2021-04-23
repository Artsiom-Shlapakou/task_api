from django.db import models
from django.utils.translation import ugettext_lazy as _
from users.models import User
from homework.services import get_file_path
from homework.choices import CHOICES_STATUS, PENDING_STATUS

class HomeWork(models.Model):
    title = models.CharField(max_length=255, default=_(
        "New HomeWork"), verbose_name=_("HomeWork Title"))
    description = models.CharField(max_length=255, verbose_name=_("Homework description"))

    def __str__(self):
        return self.title

class HomeWorkResult(models.Model):
    
    user = models.ForeignKey(
        User, related_name='homeworkresult', on_delete=models.CASCADE)
    homework = models.ForeignKey(
        HomeWork, related_name='homeworkresult', on_delete=models.DO_NOTHING)
    file_answer = models.FileField(upload_to=get_file_path,
        verbose_name=_("Upload file"))
    note = models.CharField(max_length=255, verbose_name=_("Homework note"))
    created = models.DateTimeField(
        verbose_name=_("The Homework completed"), auto_now=True)
    deadline = models.DateTimeField(verbose_name=_("Deadline")),
    mark = models.PositiveSmallIntegerField(
        null=False, default=0, verbose_name=_("Mark"))
    status = models.CharField(max_length=20,
        choices=CHOICES_STATUS, default=PENDING_STATUS, verbose_name=_("Status"))

    class Meta:
        verbose_name = _("HomeWorkResult")
        verbose_name_plural = _("HomeWorkResults")