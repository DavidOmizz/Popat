from django import forms
from .models import MakeReservation, Event
from django.shortcuts import render, get_object_or_404




Gender = [
    ('male','male'),
    ('female','female')
]

# class MakeReservationForm(forms.ModelForm):
#     Name = forms.CharField(label='First name', widget= forms.TextInput(attrs={'placeholder':'Enter your full name', 'class':'form-control', 'required':True}))
#     # name = forms.CharField(label = 'Last name', widget=forms.TextInput(attrs={'placeholder':'lastname', 'class':'form-control', 'required': True}))
#     Email_address = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control', 'required': True}))
#     Number_of_guest = forms.IntegerField()
#     # Confirm_address = forms.EmailField(label='Email2', widget=forms.TextInput(attrs={'placeholder':'Re-email', 'class':'form-control', 'required': True}))
#     Gender = forms.RadioSelect()

#     class Meta:
#         model = MakeReservation
#         fields = ('Name', 'Email_address','Number_of_guest', 'Gender')
#         # fields = '__all__'



class MakeReservationForm(forms.ModelForm):
    Name = forms.CharField(label='First name', widget= forms.TextInput(attrs={'placeholder':'Enter your full name', 'class':'form-control', 'required':True}))
    # Lastname = forms.CharField(label = 'Last name', widget=forms.TextInput(attrs={'placeholder':'lastname', 'class':'form-control', 'required': True}))
    Email_address = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control', 'required': True}))
    Confirm_address = forms.EmailField(label='Confirm email', widget=forms.TextInput(attrs={'placeholder':'Re-enter email', 'class':'form-control', 'required': True}))
    Number_of_guest = forms.IntegerField()
    Gender = forms.RadioSelect()
    # add private password field for private events
    private_password = forms.CharField(label='Private password', widget=forms.PasswordInput(attrs={'class':'form-control'}), required=False)

    class Meta:
        model = MakeReservation
        fields = ('Name', 'Email_address','Confirm_address','Number_of_guest', 'Gender', 'private_password')
        # fields = '__all__'


    # def clean_private_password(self):
    #     # check if event is private
    #     event = self.cleaned_data.get('event')
    #     if event.is_private:
    #         private_password = self.cleaned_data.get('private_password')
    #         if private_password != event.private_password:
    #             # password is incorrect, raise validation error
    #             raise forms.ValidationError('Incorrect password')
    #     return private_password



    # def clean_private_password(self):
    #     # get the event object from the cleaned data
    #     event = self.cleaned_data.get('event')

    #     if event.is_private:
    #         # get the private password entered by the user
    #         private_password = self.cleaned_data.get('private_password')
    #         if private_password != event.private_password:
    #             # raise validation error if the password is incorrect
    #             raise forms.ValidationError('Incorrect password')
    #     return private_password


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("Email_address")
        confirm_email = cleaned_data.get("Confirm_address")

        if email != confirm_email:
            raise forms.ValidationError(
                "Email addresses must match."
            )
        return cleaned_data
