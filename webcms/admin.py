from django.contrib import admin
from .models import Home, Process, About , Projects, Blog, Team, Services, ContactUs, Achievement
# Register your models here.
admin.site.register(Home)
admin.site.register(Process)
admin.site.register(About)
admin.site.register(Achievement)
admin.site.register(Projects)
admin.site.register(Blog)
admin.site.register(Team)
admin.site.register(Services)
admin.site.register(ContactUs)