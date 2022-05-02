from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description']
    # prepopulated_fields = {'slug': ('title',)}
    list_editable = ['description']
    inlines = [CommentInline]

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'user', 'published', 'created_at', 'updated_at']
    list_filter = ['published', 'created_at']
    list_editable = ['published']
