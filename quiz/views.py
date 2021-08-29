from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Quizzes,Questions
from .serializers import QuizSerializer,QuestionSerializer,RandomQuestionSerializer
from quiz import serializers


class Quiz(generics.ListAPIView):
    serializer_class=QuizSerializer
    queryset=Quizzes.objects.all()


class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        questions=Questions.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer =RandomQuestionSerializer(questions,many=True)
        return Response(serializer.data)

class Question(generics.ListAPIView):
    serializer_class=QuestionSerializer
    queryset=Questions.objects.all()

# Create your views here.
