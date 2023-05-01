from django import forms
def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('Not Valid Data')
    
def len_sname(value):
    if len(value)<=5:
        raise forms.ValidationError('lt5')

class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=100,validators=[check_for_a,len_sname])
    Sage=forms.IntegerField()
    Sgender=forms.CharField(max_length=100)