from django import forms
INTEGER_CHOICES = [tuple([x,x]) for x in range(1,32)]

class Addblogs(forms.Form):
    title = forms.CharField(required=False)
    post = forms.CharField(widget= forms.Textarea,required=False)
    user = forms.CharField(label='Select User id',required=False ,widget=forms.Select(choices= INTEGER_CHOICES))
    #static dropdown



    

