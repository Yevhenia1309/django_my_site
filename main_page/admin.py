from django.contrib import admin
from .models import Home, About_us, Category, Dish, Events, Reservation, Chefs, Gallery, Contact

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo']

@admin.register(About_us)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo']

class DishAdmin(admin.TabularInline):
    model = Dish
    raw_id_fields = ['category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']
    inlines = [DishAdmin]

@admin.register(Dish)
class DishAllAdmin(admin.ModelAdmin):
    model = Dish
    list_display = ['title', 'position', 'is_visible', 'ingredients', 'description', 'price', 'photo', 'category', 'is_special']
    list_filter = ['category', 'is_special', 'is_visible']
    list_editable = ['position', 'is_visible', 'price']

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'description', 'date', 'photo', 'is_visible']
    list_filter = ['date']
    list_editable = ['position', 'is_visible']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['date_processing', 'is_processed']
    list_filter = ['date']
    list_editable = ['is_processed']

@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible', 'description', 'photo']
    list_filter = ['position', 'is_visible']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo', 'order']
    list_filter = ['order']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['date_processing', 'is_processed']
    list_filter = ['date']
    list_editable = ['is_processed']
