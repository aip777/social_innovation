from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, TemplateView
from .models import Home, Process, About , Projects, Blog, Team, Services, ContactUs, Achievement, StaticContent
from .forms import ContactModel
from django.views import generic

def home(request):
    home_cms = Home.objects.filter(is_published=True)
    process = Process.objects.filter(is_published=True)
    about = About.objects.filter(is_published=True)
    projects = Projects.objects.filter(is_published=True)
    blog = Blog.objects.filter(is_published=True)
    services = Services.objects.filter(is_published=True)
    achieve = Achievement.objects.filter(is_published=True)



    context = {
        'home_cms': home_cms,
        'process': process,
        'about': about,
        'projects': projects,
        'blog': blog,
        'services': services,
        'achieve': achieve
    }
    return render(request, 'archlab/index.html', context)


def team(request):
    team = Team.objects.filter(is_published=True)
    static = StaticContent.objects.filter(is_published=True)
    context = {
        'team': team,
        'static': static
    }
    return render(request, 'archlab/team.html', context)

def about(request):
    about = About.objects.filter(is_published=True)
    static = StaticContent.objects.filter(is_published=True)
    context = {
        'about': about,
        'static': static
    }
    return render(request, 'archlab/about.html', context)

def services(request):
    services = Services.objects.filter(is_published=True)
    static = StaticContent.objects.filter(is_published=True)
    context = {
        'services': services,
        'static': static
    }
    return render(request, 'archlab/services.html', context)

def projects(request):
    projects = Projects.objects.filter(is_published=True)
    static = StaticContent.objects.filter(is_published=True)
    context = {
          'projects': projects,
          'static': static
    }
    return render(request, 'archlab/project.html', context)

def contact_static(request):
    static = StaticContent.objects.filter(is_published=True)
    context = {
          'static': static
    }
    return render(request, 'archlab/contact.html', context)

class ContactCreateView(CreateView):
    form_class = ContactModel
    model = StaticContent
    template_name = 'archlab/contact.html'
    success_url = "/"

class PostDetail(generic.DetailView):
    model = Blog
    template_name = 'blog-single.html'

def blog(request):
    blog = Blog.objects.filter(is_published=True)
    static = StaticContent.objects.filter(is_published=True)
    context = {
        'blog': blog,
        'static': static
    }
    return render(request, 'archlab/blog.html', context)

