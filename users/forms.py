from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post


# Create your forms here.

class RegisterUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username']

	def save(self, commit=True):
		user = super(RegisterUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']
		if commit:
			user.save()
		return user

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']

class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            # telling Django your password field in the mode is a password input on the template
        	'password': forms.PasswordInput() 
        }