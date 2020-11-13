from django.db import models
from django.utils.timezone import now
# Create your models here.


class Home(models.Model):
    logo = models.ImageField(upload_to='logo', blank=True)
    company_name = models.CharField(max_length=50, blank=True)
    slider_headline = models.CharField(max_length=500, blank=True)
    slider_small_headline = models.TextField(max_length=800, blank=True)
    slider_images = models.ImageField(upload_to='slider', blank=True)
    is_published = models.BooleanField(default=True)
    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'

class Process(models.Model):
    icon_one = models.CharField(max_length=150, blank=True)
    process_title_one = models.CharField(max_length=500, blank=True)
    process_details_one = models.TextField(max_length=1000, blank=True)

    icon_two = models.CharField(max_length=150, blank=True)
    process_title_two = models.CharField(max_length=500, blank=True)
    process_details_two = models.TextField(max_length=1000, blank=True)

    icon_three = models.CharField(max_length=150, blank=True)
    process_title_three = models.CharField(max_length=500, blank=True)
    process_details_three = models.TextField(max_length=1000, blank=True)

    icon_four = models.CharField(max_length=150, blank=True)
    process_title_four = models.CharField(max_length=500, blank=True)
    process_details_four = models.TextField(max_length=1000, blank=True)

    is_published = models.BooleanField(default=True)
    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.process_title_one

    class Meta:
        verbose_name = 'Process'
        verbose_name_plural = 'Process'


class About(models.Model):
    about_title = models.CharField(max_length=500, blank=True)
    about_details = models.TextField(max_length=2000, blank=True)
    about_images = models.ImageField(upload_to='about', blank=True)
    is_published = models.BooleanField(default=True)

    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.about_title
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

class Achievement(models.Model):
    achieve_title = models.CharField(max_length=150, blank=True)
    achieve_number = models.CharField(max_length=150, blank=True)
    is_published = models.BooleanField(default=True)

    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.achieve_title

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievement'


class Projects(models.Model):
    TYPE_SELECT = (
        ('col-md-5 img js-fullheight', 'Left'),
        ('col-md-5 order-md-last img js-fullheight', 'Right'),
    )
    position = models.CharField(max_length=500, choices=TYPE_SELECT)
    projects_title = models.CharField(max_length=500, blank=True)
    projects_details = models.TextField(max_length=2000, blank=True)
    projects_images = models.ImageField(upload_to='projects')
    is_published = models.BooleanField(default=True)
    projects_headline = models.CharField(max_length=500, blank=True)


    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.projects_title

    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'


class Blog(models.Model):
    blog_headline_one = models.CharField(max_length=500, blank=True)
    blog_details_one = models.TextField(max_length=3000, blank=True)
    blog_images = models.ImageField(upload_to='blog', blank=True)

    blog_headline_two = models.CharField(max_length=1000, blank=True)
    blog_details_two = models.TextField(max_length=2000, blank=True)
    blog_images_two = models.ImageField(upload_to='blog', blank=True)
    author_name = models.CharField(max_length=100, blank=True)
    author_comment = models.TextField(max_length=1500, blank=True)
    author_images = models.ImageField(upload_to='author', blank=True)

    is_published = models.BooleanField(default=True)
    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_headline_one
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'


class Team(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    images = models.ImageField(upload_to='team')
    linkedin = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    twitter = models.CharField(max_length=300, blank=True)
    is_published = models.BooleanField(default=True)

    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'


class Services(models.Model):
    services_title = models.CharField(max_length=500, blank=True)
    services_details = models.TextField(max_length=1000, blank=True)
    icon = models.CharField(max_length=200, blank=True)

    is_published = models.BooleanField(default=True)
    date_time = models.DateTimeField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.services_title

    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'


class ContactUs(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length= 25, blank= True)
    address = models.CharField(max_length= 100, blank= True)
    message = models.TextField(max_length= 1000, blank= True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

class StaticContent(models.Model):
    about_page_image = models.ImageField(upload_to='about')
    about_page_headline = models.CharField(max_length=500, blank=True)
    team_page_image = models.ImageField(upload_to='team')
    team_page_headline = models.CharField(max_length=500, blank=True)
    service_page_image = models.ImageField(upload_to='service')
    service_page_headline = models.CharField(max_length=500, blank=True)
    project_page_image = models.ImageField(upload_to='project')
    project_page_headline = models.CharField(max_length=500, blank=True)
    blog_page_image = models.ImageField(upload_to='blog')
    blog_page_headline = models.CharField(max_length=500, blank=True)
    contact_page_image = models.ImageField(upload_to='contact')
    contact_page_headline = models.CharField(max_length=500, blank=True)

    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.about_page_headline

    class Meta:
        verbose_name = 'Static Content'
        verbose_name_plural = 'Static Content'



class Navbar(models.Model):
    home_nav_link = models.CharField(max_length=100, blank=True)
    about_nav_link = models.CharField(max_length=200, blank=True)
    community_nav_link = models.CharField(max_length=200, blank=True)
    services_nav_link = models.CharField(max_length=200, blank=True)
    projects_nav_link = models.CharField(max_length=200, blank=True)
    blog_nav_link = models.CharField(max_length=200, blank=True)
    contact_link = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.home_nav_link

    class Meta:
        verbose_name = 'Navbar'
        verbose_name_plural = 'Navbar'


class Footer(models.Model):
    community_name = models.CharField(max_length=100, blank=True)
    community_about = models.TextField(max_length=2000, blank=True)
    community_facebook = models.CharField(max_length=500, blank=True)
    community_twitter = models.CharField(max_length=500, blank=True)
    community_linkedin = models.CharField(max_length=500, blank=True)
    community_instagram = models.CharField(max_length=500, blank=True)


    nav_title = models.CharField(max_length=100, blank=True)
    about_link = models.CharField(max_length=50, blank=True)
    project_link = models.CharField(max_length=50, blank=True)
    services_link = models.CharField(max_length=50, blank=True)
    team_link = models.CharField(max_length=50, blank=True)
    blog_link = models.CharField(max_length=50, blank=True)
    contact_link = models.CharField(max_length=50, blank=True)

    contact_title = models.CharField(max_length=250, blank=True)
    contact_address = models.CharField(max_length=500, blank=True)
    contact_phone = models.CharField(max_length=250, blank=True)
    contact_email = models.CharField(max_length=250, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.community_name

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'