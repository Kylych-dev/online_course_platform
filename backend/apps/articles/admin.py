from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')
    list_filter = ('title', 'owner')
    search_fields = ('title',)
    # ordering = ('-published',)

admin.site.register(Article, ArticleAdmin)

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = (
#         'email',
#         'first_name',
#         'last_name',
#         'is_staff',
#         'is_active'
#     )
#     list_filter = ('is_staff', 'is_active')

#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal Info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         ('Important dates', {'fields': ('last_login',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')}
#          ),
#     )
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)
#     filter_horizontal = ()
# admin.site.register(CustomUser, CustomUserAdmin)