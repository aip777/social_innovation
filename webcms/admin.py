from django.contrib import admin
from .models import Home, Process, About , Projects, Blog, Team, Services, ContactUs, Achievement,StaticContent
# Register your models here.
admin.site.register(Home)
admin.site.register(Process)
admin.site.register(About)
admin.site.register(Achievement)
admin.site.register(Projects)
admin.site.register(Blog)
admin.site.register(Team)
admin.site.register(Services)
admin.site.register(StaticContent)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ContactUs, ContactAdmin)