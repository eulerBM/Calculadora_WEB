from django.shortcuts import render,redirect
import math

def home_0(request):
    if request.method =='POST':

        # Pega os input do front
        get_box1 = eval(request.POST['somar1'])
        get_box2 = eval(request.POST['somar2'])

        # pega os input da operação
        soma = request.POST['soma']
        dimi = request.POST['dimi']
        divi = request.POST['divi']
        mul = request.POST['mul']
        porc = request.POST['porc']

        resul = soma1 + soma2

        if 
        
        
        return render (request, "html/main_home.html",{'resul':resul})

    if request.method == 'GET':
        
        return render (request, "html/main_home.html")

# Create your views here.
