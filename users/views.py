from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm #not use
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Profile, Like
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Success! An account has been created for {username}!')
            return redirect('login')   #('faqt-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def view_profile(request, pk=None):

    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    other_users = User.objects.all()

    num_likes = Like.get_num_likes(user)



    args = {'user': user, 'users': other_users, 'num_likes': num_likes}
    return render(request, 'users/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')   #('faqt-home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/edit_profile.html', context)

@login_required
def profile_page(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/public_profile.html', {'profile_user': user})

@login_required
def like(request, pk):
    Like.give_like(request.user, User.objects.get(pk=pk))
    return redirect('faqt-home')



