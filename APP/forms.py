from django import forms
from .models import *

# student register form


class StudentRegistrationForm(forms.ModelForm):
    rollNumber = forms.CharField(max_length=10, required=True, label="RollNumber", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter RollNumber'}))
    dob = forms.DateField(required=True, label="DOB", widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'dob'}))
    dep = forms.ModelChoiceField(queryset=Departments.objects.all(
    ), required=True, widget=forms.Select(attrs={'class': 'dep'}))
    year = forms.ModelChoiceField(queryset=Years.objects.all(), required=True, widget=forms.Select(attrs={'class': 'year'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))
    batch = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'enter batch like 20XX-20XX'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        student = Student.objects.create(user=user, rollNumber=self.cleaned_data['rollNumber'], dob=self.cleaned_data[
                                         'dob'], dep=self.cleaned_data['dep'], year=self.cleaned_data['year'], gender=self.cleaned_data['gender'],batch=self.cleaned_data['batch'])
        return user


# student login form

class StudentLoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter UserName'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))


# staff login form

class StaffLoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter UserName'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))

# staff register form


class StaffRegisterForm(forms.ModelForm):
    dep = forms.ModelChoiceField(queryset=Departments.objects.all(
    ), required=True, widget=forms.Select(attrs={'class': 'dep'}))
    year = forms.ModelChoiceField(queryset=Years.objects.all(
    ), required=True, widget=forms.Select(attrs={'class': 'year'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_student = False
        user.save()
        staff = Staff.objects.create(
            user=user, dep=self.cleaned_data['dep'], year=self.cleaned_data['year'])
        return user
