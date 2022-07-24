from django.contrib import admin

# Register your models here.

class CommentAdmin(admin.ModelAdmin):

    list_display= ('user','text','book','datetime_created')



from .models import Book , Comment

admin.site.register(Book)
admin.site.register(Comment,CommentAdmin)