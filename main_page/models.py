from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class Home(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='home/')

    def __str__(self):
        return f'{self.title}'


class About_us(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='about_us/')

    def __str__(self):
        return f'{self.title}'

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)

    def __iter__(self):
        for item in self.dishes.all():
            yield item

class Dish(models.Model):

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/%Y-%m-%d/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position',)

class Events(models.Model):

    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=1000)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='events/%Y-%m-%d/', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('-date', )

class Reservation(models.Model):

    phone_validator = RegexValidator(regex=r'^\+?1?\d{8,15}$', message='Введіть свій номер телефону в форматі 380501234556 або +380501234556')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    number_of_persons = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=500, blank=True)
    date = models.DateField(default=timezone.now)
    date_processing = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', )

    def __str__(self):
        return f'{self.name}: {self.phone}'

class Chefs(models.Model):

    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='chefs/', blank=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return self.title

class Gallery(models.Model):

    title = models.CharField(max_length=50, unique=True, blank=True)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='gallery/', blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=20)
    name = models.TextField(max_length=50)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    date_processing = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', )
