from django.contrib import admin
from .models import Questions

# Register your models here.


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question', 'author', 'votes']
    list_filter = ['created']
    search_fields = ['question', 'author', 'content']
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {"slug": ("question", "author")}


admin.site.register(Questions, QuestionsAdmin)
