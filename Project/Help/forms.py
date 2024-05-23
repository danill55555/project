from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from .models import User, Department, Task, Category
from .validators import validate_cyrillic
from django.contrib.auth import authenticate

class signUpForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        min_length=6,  # Устанавливаем минимальную длину логина в 6 символов
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
        help_text="Обязательно. Минимум 6 символов."  # Добавляем подсказку для пользователя
    )

    department = forms.ModelChoiceField(
        label='Отдел',
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Отдел'}),
        empty_label=None  # Убираем пустую строку в начале списка
    )

    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль', 'required': 'required'}),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль', 'required': 'required'}),
    )

    last_name = forms.CharField(
        label="Фамилия",
        validators=[validate_cyrillic],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию', 'required': 'required'})
    )
    first_name = forms.CharField(
        label="Имя",
        validators=[validate_cyrillic],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя', 'required': 'required'})
    )
    patronymic = forms.CharField(
        label="Отчество",
        validators=[validate_cyrillic],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите отчество', 'required': 'required'})
    )

    phone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите телефон', 'required': 'required', 'placeholder': '+7(XXX)-XXX-XX-XX'}),
    )

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'patronymic', 'email', 'phone', 'password1', 'password2', 'department']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email', 'required': 'required'}),

        }

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label='Логин или Электронная почта', max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин или Электронная почта'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get('username_or_email')
        password = cleaned_data.get('password')

        if username_or_email and password:
            # Попытка аутентификации с использованием имени пользователя или электронной почты
            user = User.objects.filter(Q(username=username_or_email) | Q(email=username_or_email)).first()
            if user:
                self.user = authenticate(username=user.username, password=password)
            else:
                self.user = None

            if self.user is None:
                raise forms.ValidationError("Неверный логин/электронная почта или пароль.")

        return cleaned_data


class ApplicationForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        label='Категория',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категории'}),
        empty_label=None  # Убираем пустую строку в начале списка
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'})
    )

    class Meta:
        model = Task
        fields = ['category', 'description']