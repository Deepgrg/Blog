from django.shortcuts import render


def indexPage(request):
    context ={
        'title' : 'Blog'
        # 'posts' : post,
    }
    return render(request , 'core/indexPage.html' , context)


def aboutPage(request):
    context ={
        'title' : 'About Us'
    }
    return render(request , 'core/aboutPage.html' , context)