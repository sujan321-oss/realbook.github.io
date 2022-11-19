from django.contrib import admin
from social.models import Upload

class UploadImage(admin.ModelAdmin):
    list_display=("status","uploadimage",)


admin.site.register(Upload,UploadImage)    




# Register your models here.
