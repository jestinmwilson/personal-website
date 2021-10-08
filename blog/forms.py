from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={"class": "input input__icon form-control",
                                           "id": "nameContact",
                                           "name": "nameContact",
                                           "placeholder": "first name and last name",
                                           "required": "required",
                                           "autocomplete": "on",
                                           "oninvalid": "setCustomValidity('Fill in the desired field')",
                                           "onkeyup": "setCustomValidity('')"}),
            'email': forms.TextInput(attrs={"type": "email",
                                            "class": "input input__icon form-control",
                                            "id": "emailContact",
                                            "name": "emailContact",
                                            "placeholder": "Email address",
                                            "required": "required",
                                            "autocomplete": "on",
                                            "oninvalid": "setCustomValidity('Enter the desired email')",
                                            "onkeyup": "setCustomValidity('')"}),
            'body': forms.Textarea(attrs={"id": "commentForm",
                                          "class": "textarea textarea--white form-control",
                                          "required": "required",
                                          "placeholder": "Post a comment ...",
                                          "rows": "1"})
        }
