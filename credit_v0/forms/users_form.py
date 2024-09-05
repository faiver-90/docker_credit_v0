from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from credit_v0.models import UserProfile, Dealership


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name_manager', 'last_name_manager', 'middle_name_manager', 'date_of_birth_manager',
            'phone_number_manager', 'dealership_manager', 'organization_manager', 'status_manager', 'role_manager',
            'passport_series_manager', 'passport_number_manager',
            'division_code_manager', 'issued_by_manager', 'issue_date_manager'
        ]
        widgets = {
            'date_of_birth_manager': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'issue_date_manager': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status_manager': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'dealership_manager': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'first_name_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'organization_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'role_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'division_code_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_series_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'issued_by_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'passport_number_manager': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(BaseProfileForm, self).__init__(*args, **kwargs)

        if self.request and self.request.user.is_authenticated:
            user_profile = self.request.user.userprofile

            if self.request.user.is_superuser:
                self.fields['dealership_manager'].queryset = Dealership.objects.all()
            elif user_profile.role_manager == 'owner':
                user_organization = user_profile.organization_manager
                self.fields['dealership_manager'].queryset = Dealership.objects.filter(
                    organisation_name=user_organization
                )
                # Удаление полей
                self.fields.pop('organization_manager')
                self.fields.pop('role_manager')
            elif user_profile.role_manager == 'Менеджер ДЦ':
                # Удаляем поля для менеджеров
                self.fields.pop('dealership_manager')
                self.fields.pop('organization_manager')
                self.fields.pop('role_manager')
                self.fields.pop('status_manager')


class UserEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields.pop('username')

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'username': 'Имя пользователя',
            'email': 'Электронная почта'
        }


class ProfileEditForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name_manager'].required = False
        self.fields['last_name_manager'].required = False
        self.fields['middle_name_manager'].required = False

    def save(self, commit=True):
        profile = super().save(commit=False)
        selected_dealerships = self.cleaned_data.get('dealership_manager')
        if commit:
            profile.save()
        self.save_m2m()  # Сохраняем отношения many-to-many
        if selected_dealerships:
            profile.dealership_manager.set(selected_dealerships)
        return profile


class ProfileRegistrationForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields = [
            'dealership_manager', 'organization_manager', 'role_manager', 'status_manager'
        ]

    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
            self.save_m2m()  # Save many-to-many relationships
            selected_dealership = self.cleaned_data.get('dealership_manager').first()
            if selected_dealership:
                profile.set_active_dealership(selected_dealership)
        return profile


class UserRegistrationForm(UserCreationForm):
    usable_password = None

    email = forms.EmailField(required=True, label='Email', initial='fa2@mail.ru',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))
    username = forms.CharField(required=True, label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}))
    password1 = forms.CharField(required=True, label='Пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(required=True, label='Повторите пароль',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Введите пароль еще раз'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))

    def confirm_login_allowed(self, user):
        profile = user.userprofile

        # Преобразуем статус менеджера в логическое значение
        status_manager = bool(int(profile.status_manager))
        if not status_manager:
            raise forms.ValidationError(
                "Авторизация запрещена для данного пользователя.",
                code='inactive',
            )
