from django.shortcuts import render, redirect

# Create your views here.
from address.forms import addr_update
from address.models import address


def home(request):          # Backend of The Homepage
    if request.method == 'POST':
        name = request.POST.get('name', '')         # Recieving user Input
        l1 = request.POST.get('line1', '')          # and Saving those into
        l2 = request.POST.get('line2', '')          # Local Variables
        lat = request.POST.get('latitude', '')
        long = request.POST.get('longitude', '')

        sv = address(name=name, ad_l1=l1, ad_l2=l2,lat=lat,long=long)   #Assigning the User Input
        sv.save()                                                       #Values to the Database


    obj = address.objects.all()                     # Taking All the objects to display all
    return render(request,"home.html",{'obj':obj})  # the saved address in Home Page

def delete(request, addr_id):
    dl = address.objects.get(id=addr_id)            # To delete The Address with selected id
    if request.method == 'POST':
        dl.delete()
        return redirect('/')
    return render(request, "delete.html")

def update(request, addr_id):
    tk = address.objects.get(id=addr_id)
    f = addr_update(request.POST or None, instance=tk)
    if f.is_valid():                                        # editing the current address using Modelform
        f.save()
        return redirect('/')
    return render(request, "update.html",{'f':f})