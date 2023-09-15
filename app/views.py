import csv
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CSVRequestForm
from .models import CSVRequest

def upload_csv(request):
    if request.method == 'POST':
        form = CSVRequestForm(request.POST)
        if form.is_valid():
            num_records = form.cleaned_data['num_records']
            new_file_name = form.cleaned_data['new_file_name']
            input_file_path = 'bhaghi.csv'
            df = pd.read_csv(input_file_path)
            processed_df = df.head(num_records)
            processed_file_path = f'media/{new_file_name}.csv'  
            processed_df.to_csv(processed_file_path, index=False)
            CSVRequest.objects.create(num_records=num_records, new_file_name=new_file_name)
            return redirect('download_csv', new_file_name=new_file_name)
    else:
        form = CSVRequestForm()
    return render(request, 'upload_csv.html', {'form': form})

def download_csv(request, new_file_name):
    processed_file_path = f'media/{new_file_name}.csv'
    with open(processed_file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{new_file_name}.csv"'
    return response
