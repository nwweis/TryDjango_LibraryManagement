import re
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    '''Web layout for book information input'''
    
    title = forms.CharField(
        label='Book Title',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Book Title'}),
    )

    isbn = forms.IntegerField(
        label='ISBN',
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your description",
            "class": "IBSN",
        }))

    edition = forms.IntegerField(
        label='Edition',
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Book Edition",
            "class": "edition",
        }))

    year = forms.IntegerField(label='Year Released',
                              required=True,
                              widget=forms.TextInput(attrs={
                                  "placeholder": "Book Year",
                                  "class": "year",
                              }))

    pages = forms.IntegerField(
        label='Pages',
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "No. of Pages",
        }))

    summary = forms.CharField(
        label='Book Summary',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Book Summary'}),
    )

    class Meta:
        model = Book
        fields = [
            'title',
            'isbn',
            'edition',
            'year',
            'pages',
            'summary',
        ]

    def clean_title(self, *ars, **kwargs):
        title = self.cleaned_data.get('title')
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title.")
        return title