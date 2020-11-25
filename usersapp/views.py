from django.shortcuts import render, redirect
from .register import RegisterForm
from django import forms
# importing login requfred decorator before accesing profile page
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .register import UserUpdateForm, ProfileUpdateForm
from PIL import Image


# Create your views here.
def register(request):
    # create instance of form , if request is not posted or if posted.
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('usersapp:login')
    else:
        form = RegisterForm()
    return render(request, 'usersapp/register.html', {'form': form})


@login_required
def user_profile(request, template_name='usersapp/profile.html'):
    # here v check whether the method is post or not
    if request.method == 'POST':
        # v instantiate our forms with the current values in the form AND PASS THE POSTED DATA INTO IT.
        # request.FILES r used since v post images.
        update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # if both r valid forms
        if update_form.is_valid() & profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, 'Your Account has bee updated!')

            # later redirect to our profile page after saving the data to db
            return redirect('usersapp:user_profile')
    # if not, still leave the form wth the current values
    else:
        update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    # later create context which key value pairs of that new isntance of form
    context = {
        'update_form': update_form, 'profile_form': profile_form
    }
    # pass that context to template
    return render(request, template_name, context)
