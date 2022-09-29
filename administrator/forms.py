from django.forms import ModelForm
from django import forms
from excursions.models import Excursions,Photos

# Gets a already made form  and add the new excursion
class ExcursionForm(ModelForm):
    class Meta:
        model = Excursions
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ExcursionForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': ' Add title'})
        self.fields['Price'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add price..'})
        self.fields['image_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add an image name'})


# Gets a already made form and add the new excursion photos
class ExcursionFormPhotos(ModelForm):
    class Meta:
        model = Photos
        fields = ['images']
