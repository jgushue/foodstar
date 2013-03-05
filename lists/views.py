# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("Welcome to FoodStar!")

def fresh(request):
	return HttpResponse("Create a List!")