
from django import forms
from django.utils.translation import gettext_lazy as _

from Jobportal.models import Author, Subscribe,JobPost,Location

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        # exclude=('first_name',)
        labels={
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter email')
        }
        error_messages={
            'first_name':{
                'required':_('You cannot move forward without first name')
            }
        }

class AddJobPost(forms.ModelForm):
    class Meta:
        model=JobPost
        fields=['title','description','salary','author','job_type']
        # exclude=('first_name',)

class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields='__all__'

class AuthorForm(forms.ModelForm):
    class Meta:
        model= Author
        fields='__all__'