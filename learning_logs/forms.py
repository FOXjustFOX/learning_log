from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic

        fields = ['text', 'desc']
        labels = {'text':'Topic', 'desc':'Description'}


class EntryForm(forms.ModelForm):
     class Meta:
        model = Entry
        fields = ['text', 'desc']
        labels = {'text': '', 'desc':''} 
        widgets = {'text': forms.Textarea(attrs={'cols': 80}), 'desc': forms.Textarea(attrs={'cols': 80})}