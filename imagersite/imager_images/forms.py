from django import forms


class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    title = forms.CharField(label='Title', max_length=30)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public'),
    ]
    published = forms.ChoiceField(
        choices=PUBLISHED
    )
