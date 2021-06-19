from django.shortcuts import render
from django.http import JsonResponse
import json


def home(request):
    import requests
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=17b835e66adf43fe8ae360dfb2f64f71")
    api=json.loads(news_api_request.content)
    return render(request,'index.html',{'api':api})