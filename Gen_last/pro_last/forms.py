from django import forms  
from .models import *

class BannerForm(forms.ModelForm): 
  
    class Meta: 
        model = Banner 
        fields = ['name', 'banner_image']



class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'description','attach_file']



class GalleryForm(forms.ModelForm):
    class Meta:
        model=Gallery
        fields=['title_g', 'images_g']
        