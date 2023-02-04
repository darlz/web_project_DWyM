from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.

def inicio(request):
	return render(request, 'base.html')


def users(request):
    #pull data from third party rest api
    response = requests.get('https://api-rest-project.onrender.com/api/users/')
    #convert reponse data into json
    users = response.json()
    #print(users)
    #return HttpResponse("Users")
    return render(request, "users.html", {'users': users})
    pass


def cursos(request):
    #pull data from third party rest api
    response = requests.get('https://api-rest-project.onrender.com/api/cursos/')
    #convert reponse data into json
    cursos = response.json()
    #print(cursos)
    #return HttpResponse("Cursos")
    return render(request, "cursos.html", {'cursos': cursos})
    pass