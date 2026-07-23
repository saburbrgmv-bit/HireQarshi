from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=Profile.JOOB_CHOOISE, widget=forms.RadioSelect(), label='Rolingiz')
    resume = forms.FileField(required=False) # Changed to False if it's optional, keep True if mandatory
    phone = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'resume', 'phone']
        widgets = {
            'password':forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        #user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()


        Profile.objects.create(
                user=user,
                resume=self.cleaned_data['resume'],
                role=self.cleaned_data['role']
              )
        return user
