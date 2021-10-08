from django import forms
from django.core import validators


class ConatactMeForm(forms.Form):
    fullname = forms.CharField(max_length=25,
                               widget=forms.TextInput(attrs={"class": "input input__icon form-control",
                                                             "id": "nameContact",
                                                             "name": "nameContact",
                                                             "placeholder": "first name and last name",
                                                                            "required": "required",
                                                                            "autocomplete": "on",
                                                                            "oninvalid": "setCustomValidity('Please enter your first and last name')",
                                                                            "onkeyup": "setCustomValidity('')"}),
                               validators=[
                                   validators.MinLengthValidator(
                                       3, 'The entered name is invalid'),
                                   validators.MaxLengthValidator(
                                       30, 'The entered name is invalid')]
                               )
    email = forms.EmailField(widget=forms.TextInput(attrs={"type": "email",
                                                           "class": "input input__icon form-control",
                                                           "id": "emailContact",
                                                           "name": "emailContact",
                                                           "placeholder": "Email address",
                                                           "required": "required",
                                                           "autocomplete": "on",
                                                           "oninvalid": "setCustomValidity('Enter the desired email')",
                                                           "onkeyup": "setCustomValidity('')"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "textarea form-control",
                                                           "id": "messageContact",
                                                           "name": "messageContact",
                                                           "placeholder": "Your message",
                                                           "rows": "7",
                                                           "required": "required",
                                                           "oninvalid": "setCustomValidity('Fill in the desired field')",
                                                           "onkeyup": "setCustomValidity('')"}))
