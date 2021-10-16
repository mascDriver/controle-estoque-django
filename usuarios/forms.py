from django import forms
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib.auth.hashers import make_password


class NewUserForm(forms.ModelForm):
	senha_usuario = forms.CharField(label="Digite a senha", widget=forms.PasswordInput)
	password1 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super(NewUserForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control',
				'autofocus': True
			})
			if field == 'is_superuser':
				self.fields[field].label = 'Administrador?'

	class Meta:
		model = Usuario
		fields = ("nome_usuario", "email_usuario", "senha_usuario", "password1", "is_superuser")

	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("senha_usuario")
		password2 = self.cleaned_data.get("password1")
		if password1 and password2 and password1 != password2:
			msg = "Passwords don't match"
			raise forms.ValidationError("Password mismatch")
		return password2

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["senha_usuario"])
		if commit:
			user.save()
		return user


class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())