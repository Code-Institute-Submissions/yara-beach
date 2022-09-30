from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from excursions.models import Excursions, Photos
from rentals.models import Rentals
from rentals.models import Photos as Rental_photos
from .forms import ExcursionForm, ExcursionFormPhotos, RentalForm, RentalFormPhotos
from django.contrib import messages

# Create your views here.

# Administrator function
def administrator(request):
    total_users = User.objects.all().count()
    context = {'total_users': total_users}
    return render(request, 'administrator/administrator.html', context)


# Query all rentals for admin
def admin_rentals(request):
    rentals = Rentals.objects.all()
    context = {'rentals': rentals}
    return render(request, 'administrator/rentals/admin_rentals.html', context)

# Add rentals
def add_rentals(request):
    form = RentalForm()
    if request.method == 'POST':
        user = request.user
        author = Rentals(user=user)
        form = RentalForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rental created Succesfullly')
        return redirect('admin-rental')
    context = {'form': form}
    return render(request, 'administrator/rentals/add_rentals.html', context)

# Edit rentals and add more photos
def edit_rentals(request,pk):
    rentals = Rentals.objects.get(id=pk)
    form = RentalForm(instance=rentals)
    formPhotos = RentalFormPhotos()
    if request.method == 'POST':
        form = RentalForm(request.POST, request.FILES, instance=rentals)
        images = request.FILES.getlist('images')
        if form.is_valid():
            if images:
                # Loop through all images and save then 
                for image in images:
                    photo = Rental_photos.objects.create(
                    rental=rentals,
                    image_name = rentals.image_name,
                    images= image,
                    )
                    photo.save()
            form.save()
            messages.success(request, 'Rental edit Succesfullly')
        return redirect('admin-rental')
    context = {'form':form, 'formPhotos':formPhotos, 'rentals':rentals}
    return render(request, 'administrator/rentals/edit_rental.html', context)

# Delete rental photos
def delete_rentals_photos(request, pk):
    photo = Rental_photos.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        messages.success(request, 'Photo deleted Succesfullly')
        return redirect('edit_rental', pk=photo.rental.id)
    context = {'photo':photo}
    return render(request, 'administrator/rentals/delete_rental_photos.html', context)


# All admin excursion functions are from here below

# Query all excursions for admin
def admin_excursions(request):
    excursions = Excursions.objects.all()
    context = {'excursions': excursions}
    return render(request, 'administrator/excursions/admin_excursions.html', context)

# Add excursion
def add_excursions(request):
    form = ExcursionForm()
    if request.method == 'POST':
        user = request.user
        author = Excursions(user=user)
        form = ExcursionForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, 'Excursion created Succesfullly')
        return redirect('admin-excursion')
    context = {'form': form}
    return render(request, 'administrator/excursions/add_excursions.html', context)

# Edit excursion and add more photos
def edit_excursions(request,pk):
    excursions = Excursions.objects.get(id=pk)
    form = ExcursionForm(instance=excursions)
    formPhotos = ExcursionFormPhotos()
    if request.method == 'POST':
        form = ExcursionForm(request.POST, request.FILES, instance=excursions)
        images = request.FILES.getlist('images')
        if form.is_valid():
            if images:
                # Loop through all images and save then 
                for image in images:
                    photo = Photos.objects.create(
                    excursion=excursions,
                    image_name = excursions.image_name,
                    images= image,
                    )
                    photo.save()
            form.save()
            messages.success(request, 'Excursion edit Succesfullly')
        return redirect('admin-excursion')
    context = {'form':form, 'formPhotos':formPhotos, 'excursions':excursions}
    return render(request, 'administrator/excursions/edit_excursion.html', context)

# Delete excursion
def delete_excursions(request, pk):
    excursion = Excursions.objects.get(id=pk)
    title = excursion.title
    if request.method == 'POST':
        excursion.delete()
        messages.success(request, 'Excursion deleted Succesfullly')
        return redirect('admin-excursion')
    context = {'excursion':excursion,'title':title}
    return render(request, 'administrator/excursions/delete_excursion.html', context)

# Delete excursion photos
def delete_excursions_photos(request, pk):
    photo = Photos.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        messages.success(request, 'Photo deleted Succesfullly')
        return redirect('edit_excursion', pk=photo.excursion.id)
    context = {'photo':photo}
    return render(request, 'administrator/excursions/delete_excursion_photos.html', context)