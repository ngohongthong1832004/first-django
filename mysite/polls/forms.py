from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    bio = forms.CharField(label="Your bio", max_length=100)
    your_age = forms.IntegerField(label="Your age")

class UpdateForm(forms.Form):
    first_name = forms.CharField(label="Your name", max_length=100)
    last_name = forms.CharField(label="Your bio", max_length=100)
    age = forms.IntegerField(label="Your age")


class SearchForm(forms.Form):
    search_name = forms.CharField(label="Search name", max_length=100)
