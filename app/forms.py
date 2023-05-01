from django import forms

from app.models import *


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'
        
        
class WebpageForm(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = '__all__'
        #fields = ['topic_name','name','email']
        #exclude = ['email']
        #widgets = {'name':forms.PasswordInput, 'url':forms.Textarea}
        #labels = {'name': 'Enter Name'}
        help_texts = {'name':'Only alphabates',
                      'topic_name':'Select one',
                      'url':'ends with .com',
                      'email':'ends with @gmail.com'}
        
        
class AccessForm(forms.ModelForm):
    class Meta:
        model = AccessRecord
        fields = '__all__'