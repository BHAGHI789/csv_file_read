from django import forms

class CSVRequestForm(forms.Form):
    num_records = forms.IntegerField()
    new_file_name = forms.CharField(max_length=255)