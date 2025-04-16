from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from rest_framework import views, response

from .tasks import say_hello


class DedublicateView(views.APIView):
    def post(self,request):
        say_hello.delay(request.data)
        return response.Response({'message': 'Success'})