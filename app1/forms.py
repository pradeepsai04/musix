from django import forms
from .models import upload

##class UploadVideo(forms.ModelForm):
 #   class Meta:
 #       model=upload
  #      fields="__all__"

class UploadVideo(forms.Form):
  video = forms.FileField()

class faderange(forms.Form):
 duration= forms.IntegerField()
 color=forms.IntegerField()
 
class faderange2(forms.Form):
 duration2= forms.IntegerField()
 color2=forms.IntegerField()
 
class speedfactor(forms.Form):
 factor=forms.IntegerField()
 
class volumefactor(forms.Form):
 volfactor=forms.IntegerField()
 
class rotateangle(forms.Form):
 degree=forms.IntegerField()
 
class gammavalue(forms.Form):
 gamma=forms.IntegerField()

class uploadAudio(forms.Form):
 audio=forms.FileField()
 start=forms.IntegerField()
 end=forms.IntegerField()

class watermark(forms.Form):
 text=forms.CharField(max_length=40)

class uform(forms.Form):
 name=forms.CharField(max_length=30)
 age=forms.IntegerField()
