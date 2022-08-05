from django.contrib import admin
from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts admin model"""
    list_display = ('pk', 'user','title', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('photo',)
    list_filter = (
                'created',
                'modified'
    )
    search_fields = ('user__username','title',)
    readonly_fields = ('created', 'modified')