from django import forms

### Did not use this form for now
### Maybe use in the future
class ContactForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, 
    	widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50,
    	widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', 
    	widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone', max_length=50, required=False,
    	widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Your Message', 
    	widget=forms.Textarea(attrs={'class': 'form-control'}))