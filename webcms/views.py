from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, TemplateView
from .models import Home, Process, About , Projects, Blog, Team, Services, ContactUs, Achievement


def index(request):
    return render(request,'archlab/index.html')

class Index(TemplateView):
    template_name = 'archlab/index.html'



def home(request):
    home_cms = Home.objects.filter(is_published=True)
    process = Process.objects.filter(is_published=True)
    about = About.objects.filter(is_published=True)
    projects = Projects.objects.filter(is_published=True)
    blog = Blog.objects.filter(is_published=True)
    team = Team.objects.filter(is_published=True)
    services = Services.objects.filter(is_published=True)
    achieve = Achievement.objects.filter(is_published=True)



    context = {
        'home_cms': home_cms,
        'process': process,
        'about': about,
        'projects': projects,
        'blog': blog,
        'team': team,
        'services': services,
        'achieve': achieve
    }
    return render(request, 'archlab/index.html', context)