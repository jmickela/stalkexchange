from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import WishlistItem
from .forms import WishlistForm

@login_required
def wishlist_add_item(request):
    if request.method == "POST":
        form = WishlistForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            if WishlistItem.objects.filter(owner=request.user, produce=item.produce).count() > 0:
                return redirect("home")
            item.save()
            return redirect("home")
    else:
        form = WishlistForm()

    return render(request, "wishlist_add_item.html", {'form': form})

# @login_required
# def wishlist_edit_item(request, item_id):
#     item = WishlistItem.objects.get(item_id)
#     form = None
#
#     if request.user.pk != item.owner.pk:
#         return redirect("home")
#
#     if request.method == "POST":
#         form = WishlistForm(request.POST, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = WishlistForm(instance=item)
#     return render(request, "wishlist_edit_item.html", {'form': form})

@login_required
def remove_wishlist_item(request, item_id=None):
    if item_id is None:
        return redirect("home")
    item = WishlistItem.objects.get(pk=item_id)
    if request.user.pk != item.owner.pk:
        return redirect("home")

    if request.method == "POST":
        item.delete()
        return redirect("home")

    return render(request, "wishlist_remove_confirm.html")