from django.shortcuts import render
from rest_framework.response import Response
import requests


def category_view(request):
    return render(request, "main.html", {})