from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import UserProfile
from .forms import ProfileForm

# Create your views here.
def home(request):
    if not request.user.is_anonymous():
        if not hasattr(request.user, 'profile'):
            return redirect('profile_create')
        return render(request, 'home_profile.html', {'profile': request.user.profile})

    return render(request, "main.html")

def profile_view(request, user_id):
    if request.user.pk == user_id:
        return redirect("home")

    user = get_user_model().objects.get(pk=user_id)
    return render(request, "profile_view.html", {"user": user})


@login_required
def profile_create(request):
    form = None

    if hasattr(request.user, 'profile'):
        return redirect("home")

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            try:
                profile.save()
            except Exception as e:
                print str(e)
            redirect("home")
    else:
        form = ProfileForm()

    return render(request, 'create_profile.html', {'form': form})