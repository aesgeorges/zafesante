from django.contrib import admin
from .models import Video
# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['created']
    search_fields = ['name', ]
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(Video, VideoAdmin)
