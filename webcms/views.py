from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import CreateView, TemplateView
from .models import Home, Process,Footer, About , Projects, Blog, Team, Services, ContactUs, Achievement, StaticContent, Navbar
from .forms import ContactModel
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    home_cms = Home.objects.filter(is_published=True)
    navbar = Navbar.objects.all()
    footer = Footer.objects.all()
    process = Process.objects.filter(is_published=True)
    about = About.objects.filter(is_published=True)
    projects = Projects.objects.filter(is_published=True)
    blog = Blog.objects.filter(is_published=True)
    services = Services.objects.filter(is_published=True)
    achieve = Achievement.objects.filter(is_published=True)

    page = request.GET.get('projects', 1)
    paginator = Paginator(projects, 6)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)


    page_blog = request.GET.get('blog', 1)
    paginator = Paginator(blog, 8)
    try:
        blog = paginator.page(page_blog)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)


    context = {
        'home_cms': home_cms,
        'process': process,
        'about': about,
        'projects': projects,
        'blog': blog,
        'services': services,
        'achieve': achieve,
        'navbar': navbar,
        'footer': footer
    }
    return render(request, 'archlab/index.html', context)


def team(request):
    team = Team.objects.filter(is_published=True)
    static = StaticContent.objects.filter(is_published=True)

    navbar = Navbar.objects.all()
    footer = Footer.objects.all()

    page = request.GET.get('team', 1)
    paginator = Paginator(team, 12)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    context = {
        'team': users,
        'static': static,
        'navbar': navbar,
        'footer': footer
    }
    return render(request, 'archlab/team.html', context)

def about(request):
    about = About.objects.filter(is_published=True)
    static = StaticContent.objects.filter(is_published=True)

    navbar = Navbar.objects.all()
    footer = Footer.objects.all()

    context = {
        'about': about,
        'static': static,
        'navbar': navbar,
        'footer': footer
    }
    return render(request, 'archlab/about.html', context)


def services(request):
    services = Services.objects.filter(is_published=True)
    static = StaticContent.objects.filter(is_published=True)

    navbar = Navbar.objects.all()
    footer = Footer.objects.all()

    page = request.GET.get('services', 1)
    paginator = Paginator(services, 2)
    try:
        services = paginator.page(page)
    except PageNotAnInteger:
        services = paginator.page(1)
    except EmptyPage:
        services = paginator.page(paginator.num_pages)


    context = {
        'services': services,
        'static': static,
        'navbar': navbar,
        'footer': footer
    }
    return render(request, 'archlab/services.html', context)

def projects(request):
    projects = Projects.objects.filter(is_published=True)
    static = StaticContent.objects.filter(is_published=True)

    navbar = Navbar.objects.all()
    footer = Footer.objects.all()

    page = request.GET.get('projects', 1)
    paginator = Paginator(projects, 6)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    context = {
          'projects': projects,
          'static': static,
        'navbar': navbar,
        'footer': footer
    }
    return render(request, 'archlab/project.html', context)

def contact_static(request):
    static = StaticContent.objects.filter(is_published=True)

    navbar = Navbar.objects.all()
    footer = Footer.objects.all()
    context = {
          'static': static,
        'navbar': navbar,
        'footer': footer
    }
    return render(request, 'archlab/contact.html', context)

class ContactCreateView(CreateView):
    form_class = ContactModel
    model = StaticContent
    template_name = 'archlab/contact.html'
    success_url = "/"

def blog(request):
    blog = Blog.objects.filter(is_published=True)
    static = StaticContent.objects.filter(is_published=True)

    navbar = Navbar.objects.all()
    footer = Footer.objects.all()

    page = request.GET.get('blog', 1)
    paginator = Paginator(blog, 8)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)


    context = {
        'blog': blog,
        'static': static,
        'navbar': navbar,
        'footer': footer
    }
    return render(request, 'archlab/blog.html', context)

def listing(request, listing_id ):
    listing = get_object_or_404(Blog, pk = listing_id)
    static = StaticContent.objects.filter(is_published=True)
    navbar = Navbar.objects.all()
    footer = Footer.objects.all()
    context = {
        'listing':listing,
        'static': static,
        'navbar': navbar,
        'footer': footer
    }

    return render(request, 'archlab/blog-single.html', context)



