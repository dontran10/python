from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request=request,
        template_name='account/register.html', 
        context={'form': form}
    )

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout successfully.')
    return redirect('login')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    # TODO: Happy to enhance this
    return render(request=request,
        template_name='account/profile.html'
    )
