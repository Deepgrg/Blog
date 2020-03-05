from django.shortcuts import render


from .models import Post

def indexPage(request):
    post = Post.objects.all()
    context ={
        'title' : 'Blog',
        'posts' : post,
    }
    return render(request , 'core/indexPage.html' , context)


def aboutPage(request):
    context ={
        'title' : 'About Us'
    }
    return render(request , 'core/aboutPage.html' , context)