from django.contrib import admin

from .models import Blog

# Register your models here.

admin.site.register(Blog)
admin.site.register(Crop)
class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class FarmlandAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
    ]

admin.site.register(Farmland, FarmlandAdmin)
