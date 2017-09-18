from django.contrib import admin
from .models import Category, Item, FeedBack, Comment


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', 'slug')


class ItemAdmin(admin.ModelAdmin):
    list_filter = ['creation_date']
    search_fields = ['name']
    list_display = ('name', 'category', 'price', 'views', 'creation_date')
    fieldsets = [
        (None,
            {'fields': ['category']}),
        ('Item information',
            {'fields':
                ['name', 'description', 'price', 'photo']}),
    ]


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'time', 'published')
    list_filter = ['time']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('item', 'name', 'email', 'message', 'time', 'published')
    list_filter = ['time']
    fieldsets = [
        (None,
            {'fields': ['item']}),
        (None,
            {'fields':
                ['name', 'email', 'message', 'published']}),
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(FeedBack, FeedBackAdmin)
admin.site.register(Comment, CommentAdmin)
