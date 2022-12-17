from django.contrib import admin

from Jobportal.models import Author, JobPost, Location, Skills

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)