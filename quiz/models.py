from django.db import models
from django.utils.translation import gettext_lazy as _     # gettext_lazy 
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)
    def __str__(self):
        return self.name

class Quizzes(models.Model):
    class Meta:
        verbose_name =_("Quiz")
        verbose_name_plural =_("Quizes")
        ordering = ['id']
    category =models.ForeignKey(Category,default=1,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=225,default=_("New Quiz"),verbose_name=_("Quiz Title"))
    date_created =models.DateTimeField(auto_now_add=True) # Update date Created auto_now = will add time of modification 
    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated =models.DateTimeField(auto_now=True,verbose_name=_("Last Updated"))
    class Meta:
        abstract = True


class Questions(Updated):
    class Meta:
        verbose_name =_("Question")
        verbose_name_plural =_("Questions")
        ordering = ['id']
    SCALE=(
        (0,_('Fundemental')),
        (1,_('Beginner')),
        (2,_('Intermediate')),
        (3,_('Advanced')),
        (4,_('Expert')),

    )
    quiz =models.ForeignKey(Quizzes,related_name='question',on_delete=models.DO_NOTHING)


class Answer(Updated):
    question =models.ForeignKey(Questions,related_name='answer',on_delete=models.DO_NOTHING)
