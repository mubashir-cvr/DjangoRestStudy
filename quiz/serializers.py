from django.db.models import fields
from rest_framework import generics, serializers
from .models import Questions, Quizzes
from quiz import models

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model =Quizzes
        fields=[
            'title',
            'date_created',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Questions
        fields=[
            'quiz',
            'date_created',
            'difficulty',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):
    answer=serializers.StringRelatedField(many=True)

    class Meta:
        model=Questions
        fields=[
            'title','answer',
        ]