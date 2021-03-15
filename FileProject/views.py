from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required

from .models import User, File
from .encryption import Encryptor

key = settings.AES_KEY
enc = Encryptor(key)


password = "12345"

# Create your views here.
def index(request):
    return render(request, 'fileproject/index.html',{
        'test' : File.objects.all()
    })

@login_required(login_url='/login')
def main_app(request):
    files = File.objects.filter(user=request.user)

    return render(request, 'fileproject/mainapp.html', {
        "files" : files
    })


def register_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "fileproject/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "fileproject/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect(main_app)
    else:
        return render(request, "fileproject/register.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect(main_app)
        else:
            return render(request, "fileproject/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "fileproject/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



@xframe_options_exempt
@login_required(login_url='/login')
def upload_file(request):
    if request.method == 'POST':
        myfile = request.FILES.get('myfile')
        encrypt_bool = request.POST.get('encrypted')
        user = request.user
        if encrypt_bool == None:
            files = File(user=user, upload=myfile)
            files.save()
        else:
            files = File(user=user, upload=myfile, encryption=True)
            files.save()
        
            url = files.upload.url
            f = enc.encrypt_file(str(url[1:]))
        
            file_name = f.name[6:]
            File.objects.filter(id=files.id).update(upload=file_name)
        
         
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
def download_page(request, pk):
    files = File.objects.get(id=pk)
    return render(request, 'fileproject/download.html', {
        'files' : files
    })

def delete_file(request, pk):
    files = File.objects.get(id=pk)
    if files.user != request.user:
        return JsonResponse({"Message" : "You Have no access"}, status=405)
    files.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login')
def decrypt_func(request, pk):
    files = File.objects.get(id=pk)
    if request.user != files.user:
        return JsonResponse({"Message" : "You Have No Access"})
    if files.encryption == False:
        return JsonResponse({"Message" : "File Already Encrypted"})

    url = files.upload.url
    f = enc.decrypt_file(str(url[1:]))
    file_name = f.name[6:]
    File.objects.filter(id=files.id).update(upload=file_name, encryption=False)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login')
def encrypt_func(request, pk):
    files = File.objects.get(id=pk)
    if request.user != files.user:
        return JsonResponse({"Message" : "You Have No Access"})
    if files.encryption == True:
        return JsonResponse({"Message" : "File Already Decrypted"})
    
    url = files.upload.url
    f = enc.encrypt_file(str(url[1:]))
    file_name = f.name[6:]
    File.objects.filter(id=files.id).update(upload=file_name, encryption=True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    