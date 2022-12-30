from django.shortcuts import render,redirect,HttpResponse
import math

def home_0(request):
    if request.method =='POST':

        # Pega os input do front
        get_box1 = eval(request.POST['somar1'])
        get_box2 = eval(request.POST['somar2'])
        opr = request.POST['opr']

        # faz as operação e retorna pro usuario com o resultado
        if opr == "Somar":

            resul = get_box1 + get_box2
            return render (request, "html/main_home.html",{'resul':resul})

        elif opr == "Diminuir":

            resul = get_box1 - get_box2
            return render (request, "html/main_home.html",{'resul':resul})

        elif opr == "Dividir":

            resul = get_box1 / get_box2
            return render (request, "html/main_home.html",{'resul':resul})

        elif opr == "Multiplicar":

            resul = get_box1 * get_box2
            return render (request, "html/main_home.html",{'resul':resul})

        elif opr == "Porcentagem":
            
            resul = get_box1 % get_box2
            return render (request, "html/main_home.html",{'resul':resul})



        else:
            HttpResponse('nao funcionou')
       

    if request.method == 'GET':
        
        return render (request, "html/main_home.html")

# Create your views here.
