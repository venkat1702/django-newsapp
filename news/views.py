from django.shortcuts import render
from django.http import JsonResponse
import json
from .serializers import UserSerailizer
from django.contrib.auth.models import User

def home(request):
    import requests
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=17b835e66adf43fe8ae360dfb2f64f71")
    api=json.loads(news_api_request.content)
    return render(request,'index.html',{'api':api})


def userSettings(request):
	user, created = User.objects.get_or_create(id=1)
	setting = user.setting

	seralizer = UserSerailizer(setting, many=False)

	return JsonResponse(seralizer.data, safe=False)


def updateTheme(request):
	data = json.loads(request.body)
	theme = data['theme']
	
	user, created = User.objects.get_or_create(id=1)
	user.setting.value = theme
	user.setting.save()
	print('Request:', theme)
	return JsonResponse('Updated..', safe=False)
