from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .forms import UserRegistrationForm,ProfileEditForm
from django.contrib.auth import login,logout,update_session_auth_hash
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('auth:login')
    else:
            form=UserRegistrationForm()
    return render(request,'accounts/register.html',{'form':form})


def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('product_list')
    else:
            form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('auth:login')
@login_required
def user_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request,'accounts/profile.html',{'user':request.user,'profile':profile})

def edit_profile_view(request):
    profile=get_object_or_404(Profile,user=request.user)
    
    if request.method=='POST':
        form=ProfileEditForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully created the profile!!')
            return redirect('profile')
        else:
            form=ProfileEditForm(instance=profile)
        return render(request,'edit_profile.html',{'form':form})
    
def security_settings_view(request):
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password updated successfully!!')
            return redirect('security_settings')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'security_settings.html',{'form':form})
     
