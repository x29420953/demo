from django.shortcuts import render
from django import http
from rest_framework.views import APIView
import datetime, json

# Create your views here.

api = [{
    "content": "這是第一個備忘錄",
    "created_at": "Mon, 12 Apr 2021 21:41:31 GMT",
    "id": 3
}, {
    "content": "這是第二個備忘錄",
    "created_at": "Fri, 30 Jul 2021 04:14:51 GMT",
    "id": 27
}, {
    "content": "這是第三個備忘錄",
    "created_at": "Fri, 30 Jul 2021 04:15:43 GMT",
    "id": 28
}]


class ToDoListAllView(APIView):
    def get(self, request):

        return render(request, 'index.html', {'temp': api})


class ToDoListView(APIView):
    def get(self, request, id=None):
        for i in api:
            if i['id'] == int(id):
                return render(request, 'info.html', {'temp': i})


class ToDoListAllAjaxView(APIView):
    def get(self, request):
        data = {'objects': []}
        data['objects'] = api
        return http.JsonResponse(data)

