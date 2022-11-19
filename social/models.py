from django.db import models


# this is to upload the image and the status
class Upload(models.Model):

    status=models.TextField(max_length=1000,null=True)
    uploadimage=models.FileField(upload_to="news/",null=True,default=None)
    

   
    
    
    

# Create your models here.
