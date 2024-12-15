from django import forms
from django.contrib.auth.password_validation import validate_password
from users.models import UsersModel

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-500',
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-500',
        })
    )

    class Meta:
        model = UsersModel
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-500',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-500',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-500',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-500',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

        try:
            validate_password(password)
        except forms.ValidationError as e:
            raise forms.ValidationError(e.messages)

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-500',

        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-500',

        })
    )

    def clean(self):
        """Проверяет корректность введённых данных"""
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Проверяем, существует ли пользователь с таким email
        try:
            user = UsersModel.objects.get(email=email)
        except UsersModel.DoesNotExist:
            raise forms.ValidationError("Invalid email or password")

        # Проверяем пароль
        if not user.check_password(password):
            raise forms.ValidationError("Invalid email or password")

        # Сохраняем объект пользователя в cleaned_data
        cleaned_data['user'] = user
        return cleaned_data