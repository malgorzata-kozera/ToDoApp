from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Account has been created for {username}.')

            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', context={'form': form})


@login_required
def profile_site(request):

    if request.method == 'POST':

        update_form = UserUpdateForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, f'Your profile has benn update')
            return redirect('profile')

    else:
        update_form = UserUpdateForm(instance=request.user)

    context = {'update_form': update_form}
    return render(request, 'users/profile.html', context)
