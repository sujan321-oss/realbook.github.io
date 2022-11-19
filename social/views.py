from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from social.models import Upload


def socialbook(request):
    
    val=Upload.objects.all()
    show={
        "val":val
    }
    
    print(val)
    if request.method=="POST":
        try:
            status=request.POST["uploadyourstatus"]
            image=request.FILES["uploadimage"]
            print(image.name)
            data=Upload(status=status,uploadimage=image)
            data.save()
            
            
            # show the uploaded data
            
            
            
            
            
            
        except:
            pass
    
    
    
    
    
    
    return render(request,"index.html",show)


# taeke image and the uploaded things from the user

def uploaded(request):
   
    
    
    return render(request,"socialbook.html")










# Create your views here.
