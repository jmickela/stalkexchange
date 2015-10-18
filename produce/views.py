from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from wishlist.models import WishlistItem

from .models import GardenItem
from .forms import AddProduceForm, ProduceSearchForm

@login_required
def add_produce_to_profile(request):
    form = None

    if request.method == 'POST':
        form = AddProduceForm(request.POST)
        if form.is_valid():
            garden_item = form.save(commit=False)
            garden_item.owner = request.user
            garden_item.save()
            return redirect("home")
    else:
        form = AddProduceForm()

    return render(request, "add_produce_form.html", {'form': form})

@login_required
def remove_produce_from_profile(request, item_id=None):
    if item_id is None:
        return redirect("home")

    if request.method == "POST":
        item = GardenItem.objects.get(pk=item_id)
        item.delete()
        return redirect("home")

    return render(request, "produce_remove_confirm.html")

def garden_item_search(request):
    form = ProduceSearchForm(request.GET)
    results = None
    type = request.GET.get('type')
    if request.GET.get('produce') is not None:
        produce = request.GET.get('produce')
        if type == "gardens":
            results = GardenItem.objects.filter(produce__pk=produce).exclude(owner=request.user)
        elif type == "wishlists":
            results = WishlistItem.objects.filter(produce__pk=produce).exclude(owner=request.user)


        if request.GET.get('zip') is not None and request.GET.get('zip') != "":
            results = results.filter(owner__profile__zip=request.GET.get('zip'))

    return render(request, "produce_search.html", {'search_form': form, 'results': results})
