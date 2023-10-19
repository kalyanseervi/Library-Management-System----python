from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    mobile_number = forms.CharField(max_length=15, required=True, help_text='Required. Enter your mobile number.')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    college_or_institute_name = forms.CharField(max_length=100, required=True, help_text='Required. Enter your college or institute name.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile_number', 'gender', 'college_or_institute_name', 'password1', 'password2']
class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search Query', required=False)
    category = forms.ChoiceField(label='Category', required=False,
                                 choices=[('programming', 'Programming'), ('fiction', 'Fiction')])
    author = forms.CharField(label='Author', required=False)
    publication_year = forms.IntegerField(label='Publication Year', required=False)

class Dealers2Form(forms.ModelForm):
    class Meta:
        model = dealers2
        fields = '__all__'

class Book2Form(forms.ModelForm):
    class Meta:
        model = book2
        fields = '__all__'

class Purchase2Form(forms.ModelForm):
    class Meta:
        model = purchase2
        fields = '__all__'

class RPurchaseForm(forms.ModelForm):
    class Meta:
        model = R_Purchase
        fields = '__all__'

# class BookTransactionForm(forms.ModelForm):
#     class Meta:
#         model = Book_transaction
#         fields = '__all__'



class WishlistItemForm(forms.Form):
    book_id = forms.CharField(max_length=255) 
    book_isbn = forms.CharField(max_length=255, widget=forms.HiddenInput()) 





