from django.shortcuts import render,redirect
from django.http import HttpResponse
from pro_last.functions.functions import handle_uploaded_file
from pro_last.forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'GET':
        Banners = Banner.objects.all() 
        Notices = Notice.objects.all()
        Gallerys = Gallery.objects.all() 
        return render(request, 'index.html', {'Note' : Notices, 'banner_images' : Banners, 'gal' : Gallerys })

def banner_upload(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        return redirect('/display_banner')
    else:
        form = BannerForm()
    return render(request,'banner_up.html',{'form': form})






def notice_upload(request):
    if request.method == 'POST':
        fo = NoticeForm(request.POST, request.FILES)
        
        if fo.is_valid():
            fo.save()
        return redirect('/display_notice')
    else:
        fo = NoticeForm()
    if 'user_id' not in request.session:
        return redirect('/admin')
    else:
        context = {
            "user": User.objects.get(id=request.session['user_id'])
        }
        return render(request,'notice_u.html',{'form': fo})
    #return render(request,'notice_u.html',{'form': fo})


def disg(request): 
  
    if request.method == 'GET':
        Gallerys = Gallery.objects.all()  
        return render(request, 'gallery.html',{'gal' : Gallerys})

def disb(request): 
  
    if request.method == 'GET':
        Banners = Banner.objects.all()  
        return render(request, 'banner_d.html',{'banner_images' : Banners})

def disn(request): 
  
    if request.method == 'GET':
        Notices = Notice.objects.all()  
        return render(request, 'notice_d.html',{'Note' : Notices})





def gallery_up(request):
    if request.method == 'POST':
        fo1 = GalleryForm(request.POST, request.FILES)
        
        if fo1.is_valid():
            fo1.save()
            return redirect('/display_gallery')
            
    else:
        fo1 = GalleryForm()
    return render(request,'gallery_up.html',{'form': fo1})

def con(request):
    if request.method == 'GET':
        Banners = Banner.objects.all()
        return render(request,'contact.html',{'banner_images' : Banners})
    
def about(request):
    if request.method == 'GET':
        Banners = Banner.objects.all()
        return render(request,'about.html',{'banner_images' : Banners})

def delete_notice(request, id):
    Notices = Notice.objects.get(id=id)
    Notices.delete()
    return redirect("display_notice")
def delete_banner(request, id):
    Banners = Banner.objects.get(id=id)
    Banners.delete()
    return redirect("/display_banner")
def dele_gallery(request, id):
    Gallerys = Gallery.objects.get(id=id)
    Gallerys.delete()
    return redirect('delete_gallery')
##########################################################################
# Create your views here.
def ind(request):
    if 'user_id' in request.session:
        return redirect('/success')
    else:
        return render(request, 'ind.html')


def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.add_message(request, messages.ERROR, value, extra_tags='register')
            return redirect('/admin')
        else:
            pw_hash = (request.POST['password'].encode())
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
            request.session['user_id'] = user.id
            return redirect("/success")
    else:
        return redirect("/admin")


def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.add_message(request, messages.ERROR, value, extra_tags='login')
            return redirect('/admin')
        else:
            user = User.objects.get(email=request.POST['email'])
            request.session['user_id'] = user.id
            return redirect("/wall")


def wall(request):
    if 'user_id' not in request.session:
        return redirect('/admin')
    else:
        context = {
            "user": User.objects.get(id=request.session['user_id'])
        }
        return render(request,'Admin.html', context)


def success(request):
    if 'user_id' not in request.session:
        return redirect('/admin')
    else:
        context = {
            "user": User.objects.get(id=request.session['user_id'])
        }
        return render(request, 'success.html', context)


def reset(request):
    if 'user_id' not in request.session:
        return redirect('/admin')
    else:
        request.session.clear()
        print("session has been cleared")
        return redirect("/admin")