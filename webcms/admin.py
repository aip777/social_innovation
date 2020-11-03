from django.contrib import admin
from .models import Home, Process, About , Projects, Blog, Team, Services, ContactUs, Achievement,StaticContent
# Register your models here.



class HomeAdmin(admin.ModelAdmin):
    list_display = ('id','company_name', 'slider_headline', 'date_time')
    list_display_links = ('id','company_name', 'slider_headline')
    # list_editable = ['is_published']
    search_fields = ['company_name', 'slider_headline']
    list_per_page = 25

admin.site.register(Home, HomeAdmin)


class StaticContentAdmin(admin.ModelAdmin):
    list_display = ('about_page_headline', 'about_page_image','created_at')
    list_display_links = ('about_page_headline', 'about_page_image')
    # list_editable = ('is_published')
    search_fields = ['about_page_headline']
    list_per_page = 25

admin.site.register(StaticContent, StaticContentAdmin)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('services_title', 'icon','date_time')
    list_display_links = ('services_title', 'icon')
    # list_editable = ('is_published')
    search_fields = ['services_title']
    list_per_page = 25

admin.site.register(Services, ServicesAdmin)



class TeamAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','designation','date_time')
    list_display_links = ('first_name', 'last_name')
    # list_editable = ('is_published')
    search_fields = ['first_name', 'last_name','designation']
    list_per_page = 25

admin.site.register(Team, TeamAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'blog_headline_one','date_time')
    list_display_links = ('author_name', 'blog_headline_one')
    # list_editable = ('is_published')
    search_fields = ['author_name', 'blog_headline_one']
    list_per_page = 25

admin.site.register(Blog, BlogAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('position', 'projects_title','date_time')
    list_display_links = ('position', 'projects_title')
    # list_editable = ('is_published')
    search_fields = ['position', 'projects_title']
    list_per_page = 25

admin.site.register(Projects, ProjectsAdmin)



class AchievementAdmin(admin.ModelAdmin):
    list_display = ['achieve_title', 'achieve_number','date_time']
    list_display_links = ['achieve_title', 'achieve_number']
    # list_editable = ['is_published']
    search_fields = ['achieve_title', 'achieve_number']
    list_per_page = 25

admin.site.register(Achievement, AchievementAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id','about_title','date_time')
    list_display_links = ('id','about_title')
    # list_editable = ('is_published')
    search_fields = ['about_title']
    list_per_page = 25

admin.site.register(About, AboutAdmin)



class ProcessAdmin(admin.ModelAdmin):
    list_display = ('process_title_one', 'icon_one','date_time')
    list_display_links = ('process_title_one', 'icon_one')
    # list_editable = ('is_published')
    search_fields = ['process_title_one']
    list_per_page = 25

admin.site.register(Process, ProcessAdmin)







class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')


    list_display_links = ('name', 'email')
    # list_editable = ('is_published')
    search_fields = ['name', 'email', 'phone',]
    list_per_page = 25

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ContactUs, ContactAdmin)