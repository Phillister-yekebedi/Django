from django.shortcuts import render
from .forms import ProductUploadForm
from .models import Product

def upload_product(request):
    if request.method == "POST":
        upload_product = request.FILES.get("images",None)
        # upload_product = request.FILES["images"]
        form = ProductUploadForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit =False)
            product.image=upload_product
            product.save()
    else:
        form=ProductUploadForm()
        
    return render(request, 'inventory/product_upload.html',{"form": form} )








