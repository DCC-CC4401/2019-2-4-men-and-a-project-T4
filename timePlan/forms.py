from django import forms


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class NewUserForm(forms.Form):
    usuario = forms.CharField()
    correoR = forms.EmailField()
    contrasenaR = forms.CharField(widget=forms.PasswordInput)
    cContrasena = forms.CharField(widget=forms.PasswordInput)
    image = forms.ImageField(required=False)

    def clean(self):
        cleaned_data = super(NewUserForm, self).clean()
        confirm_password = cleaned_data.get('cContrasena')
        password = cleaned_data.get('contrasenaR')
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(required=True)
    new_password = forms.CharField(max_length=20, min_length=4, required=True)
    confirmation_password = forms.CharField(max_length=20, min_length=4, required=True)
