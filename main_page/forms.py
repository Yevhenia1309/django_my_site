from django import forms
from .models import Reservation, Contact

class ReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'name',
        'class': 'form-control',
        'id': 'name',
        'placeholder': "Ваше ім'я",
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars'
    }))
    email = forms.EmailField(max_length=30, widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',
        'name': 'email',
        'id': 'email',
        'placeholder': 'Ваш Email',
        'data-rule': 'email',
        'data-msg': 'Please enter a valid email'
    }))
    phone = forms.CharField(max_length=20, widget=forms.NumberInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'phone',
        'id': 'phone',
        'placeholder': 'Ваш телефон',
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars'
    }))
    number_of_persons = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'class': 'form-control',
        'name': 'people',
        'id': 'people',
        'placeholder': 'Кількість осіб',
        'data-rule': 'minlen:1',
        'data-msg': 'Please enter at least 1 chars'
    }))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'message',
        'rows': '5',
        'placeholder': 'Повідомлення'
    }))
    date = forms.DateField(widget=forms.NumberInput(attrs={
        'type': 'text',
        'name': 'date',
        'class': 'form-control',
        'id': 'date',
        'placeholder': 'Дата',
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars'
    }))

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'number_of_persons', 'message', 'date']


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'name',
        'class': 'form-control',
        'id': 'name',
         'placeholder': "Ваше ім'я"
    }))
    email = forms.EmailField(max_length=30, widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',
        'name': 'email',
        'id': 'email',
        'placeholder': 'Ваш Email'
    }))
    description = forms.CharField(max_length=500, widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'subject',
        'id': 'subject',
        'placeholder': 'Тема'
    }))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'message',
        'rows': '5',
        'placeholder': 'Повідомлення'
    }))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'description', 'message']