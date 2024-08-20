from django.contrib import admin
from .models import *

# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = [ 'username', 'email',  'phone', 'is_active']
#     list_filter = ('is_active',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']    


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Course) 
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
      

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'email','subject','message','created_at']    
    prepopulated_fields = { "slug": ('first_name', 'last_name'), }