from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


class QuizView(View):
    def get(self, request):
        return render(request, 'quiz.html')

    def post(self, request):
        # Здесь можно обработать результаты
        return JsonResponse({'status': 'success'})
