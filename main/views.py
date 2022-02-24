from django.shortcuts import render

from main.models import Team, Portfolio, Blog, Edu




def index(request):
    team = Team.objects.all()
    ctx = {
        'team': team
    }
    return render(request, "main/index.html", ctx)



def blog_details(request):
    return render(request, "main/blog-details.html")



def blog(request):
    return render(request, "main/blog.html")