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
    TYPES=(
        (0,_('Multiple Choice')),
    )
    quiz =models.ForeignKey(Quizzes,related_name='question',on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPES,default=0,verbose_name=_("Type of Question"))
    title = models.CharField(max_length=225,verbose_name=_("Title"))
    difficulty = models.IntegerField(choices=SCALE,default=0,verbose_name=_("Difficulty"))
    date_created =models.DateTimeField(auto_now_add=True,verbose_name=_("Date Created"))
    is_active =models.BooleanField(default=False,verbose_name=_("Active Status"))
    def __str__(self):
        return self.title

class Answer(Updated):
    class Meta:
        verbose_name =_("Answer")
        verbose_name_plural =_("Answers")
        ordering = ['id']
    question =models.ForeignKey(Questions,related_name='answer',on_delete=models.DO_NOTHING)
    answe_text= models.CharField(max_length=225,verbose_name=_("Answer Text"))
    is_right=models.BooleanField(default=False)
