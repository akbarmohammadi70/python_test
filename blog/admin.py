from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Category, Comments

#@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author' , 'counted_view', 'status', 'published_date',)    
    list_filter = ('status', 'author')
    ordering = ['-created_date']
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post' , 'approved', 'created_date')    
    list_filter = ('post', 'approved')
    search_fields = ['name', 'post']
    
admin.site.register(Category)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Post, PostAdmin)



