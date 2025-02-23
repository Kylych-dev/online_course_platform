from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')
    list_filter = ('title', 'owner')
    search_fields = ('title',)
    # ordering = ('-published',)

admin.site.register(Article, ArticleAdmin)