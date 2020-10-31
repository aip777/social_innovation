from django.db import models
from django.utils.timezone import now
# Create your models here.


class Home(models.Model):
    logo = models.ImageField(upload_to='logo', blank=True)
    company_name = models.CharField(max_length=50, blank=True)
    slider_headline = models.CharField(max_length=150, blank=True)
    slider_small_headline = models.CharField(max_length=150, blank=True)
    slider_images = models.ImageField(upload_to='slider', blank=True)
    is_published = models.BooleanField(default=True)
    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


class Process(models.Model):
    icon_one = models.CharField(max_length=150, blank=True)
    process_title_one = models.CharField(max_length=150, blank=True)
    process_details_one = models.TextField(max_length=250, blank=True)

    icon_two = models.CharField(max_length=150, blank=True)
    process_title_two = models.CharField(max_length=150, blank=True)
    process_details_two = models.TextField(max_length=250, blank=True)

    icon_three = models.CharField(max_length=150, blank=True)
    process_title_three = models.CharField(max_length=150, blank=True)
    process_details_three = models.TextField(max_length=250, blank=True)

    icon_four = models.CharField(max_length=150, blank=True)
    process_title_four = models.CharField(max_length=150, blank=True)
    process_details_four = models.TextField(max_length=250, blank=True)

    is_published = models.BooleanField(default=True)
    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.process_title_one


class About(models.Model):
    about_title = models.CharField(max_length=150, blank=True)
    about_details = models.TextField(max_length=1000, blank=True)
    about_images = models.ImageField(upload_to='about', blank=True)
    is_published = models.BooleanField(default=True)

    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.about_title

class Achievement(models.Model):
    achieve_title = models.CharField(max_length=150, blank=True)
    achieve_number = models.CharField(max_length=150, blank=True)
    is_published = models.BooleanField(default=True)

    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.achieve_title


class Projects(models.Model):
    projects_title = models.CharField(max_length=250, blank=True)
    projects_details = models.CharField(max_length=1000, blank=True)
    projects_images = models.ImageField(upload_to='projects')
    is_published = models.BooleanField(default=True)
    projects_headline = models.CharField(max_length=150, blank=True)


    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.projects_title


class Blog(models.Model):
    blog_headline = models.CharField(max_length=300, blank=True)
    blog_details = models.CharField(max_length=1500, blank=True)
    blog_images = models.ImageField(upload_to='blog')
    is_published = models.BooleanField(default=True)

    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_headline


class Team(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    images = models.ImageField(upload_to='team')
    linkedin = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    is_published = models.BooleanField(default=True)

    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Services(models.Model):
    services_title = models.CharField(max_length=150, blank=True)
    services_details = models.TextField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='logo')

    is_published = models.BooleanField(default=True)
    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.services_title


class ContactUs(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=35, blank=True)
    subject = models.EmailField(max_length=200, blank=True)
    message = models.EmailField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name