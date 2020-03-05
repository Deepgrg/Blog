from django.shortcuts import render


def indexPage(request):
    context ={

    }
    return render(request , 'core/indexPage.html' , context)