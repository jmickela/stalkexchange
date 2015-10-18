from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from produce.forms import ProduceSearchForm

from .models import UserProfile
from .forms import ProfileForm

# Create your views here.
def home(request):
    search_form = ProduceSearchForm()
    if not request.user.is_anonymous():
        if not hasattr(request.user, 'profile'):
            return redirect('profile_create')
        return render(request, 'home_profile.html', {'profile': request.user.profile, "search_form": search_form})

    return render(request, "main.html", {"search_form": search_form})

def profile_view(request, user_id):
    if request.user.pk == user_id:
        return redirect("home")

    user = get_user_model().objects.get(pk=user_id)

    search_form = ProduceSearchForm()
    return render(request, "profile_view.html", {"user": user, "search_form": search_form})

@login_required
def profile_edit(request):
    form = None
    if request.POST:
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, "profile_edit.html", {'form': form})


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