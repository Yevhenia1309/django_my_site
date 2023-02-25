from django.shortcuts import render, redirect
from .models import About_us, Home, Category, Dish, Events, Chefs, Gallery, Contact, Reservation
from .forms import ReservationForm, ContactForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()

def main(request):
    if request.method == 'POST':
        form_reserve = ReservationForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

    if request.method == 'POST':
        form_contact = ContactForm(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    events = Events.objects.filter(is_visible=True)
    home = Home.objects.all()
    about_us = About_us.objects.all()
    chefs = Chefs.objects.all()
    contact = Contact.objects.all()
    gallery = Gallery.objects.all()
    form_reserve = ReservationForm()
    form_contact = ContactForm()
    user_manager = request.user.groups.filter(name='manager').exists()
    user_auth = request.user.is_authenticated


    return render(request, 'main_content.html', context={
        'home': home,
        'about_us': about_us,
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'form_reserve': form_reserve,
        'form_contact': form_contact,
        'events': events,
        'chefs': chefs,
        'contact': contact,
        'gallery': gallery,
        'user_manager': user_manager,
        'user_auth': user_auth,
    })

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    Reservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('main_page:list_reservations')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def list_reservations(request):
    messages = Reservation.objects.filter(is_processed=False)
    return render(request, 'reservations.html', context={'reservations': messages})