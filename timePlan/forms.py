from django import forms


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class NewUserForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    cPassword = forms.CharField(widget=forms.PasswordInput)
    image = forms.ImageField()

    def clean(self):
        cleaned_data = super(NewUserForm, self).clean()
        confirm_password = cleaned_data.get('cPassword')
        password = cleaned_data.get('password')
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
