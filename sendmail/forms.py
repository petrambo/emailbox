from django import forms

class Contactemail(forms.Form):
    Email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
        
    def __str__(self):
        return self.Email