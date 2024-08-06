import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from django.shortcuts import render, redirect
from .forms import CSVUploadForm
from .models import CSVFile

def home(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.save()
            return redirect('results', pk=csv_file.pk)
    else:
        form = CSVUploadForm()
    return render(request, 'data_analysis/home.html', {'form': form})

def results(request, pk):
    csv_file = CSVFile.objects.get(pk=pk)
    df = pd.read_csv(csv_file.file.path)
    
    # Data preview
    preview = df.head().to_html(classes='table table-striped')
    
    # Summary statistics
    summary_stats = df.describe().to_html(classes='table table-striped')
    
    # Missing values
    missing_data = df.isnull().sum().to_frame().reset_index()
    missing_data.columns = ['Column', 'Missing Values']
    missing_data['Percentage'] = (missing_data['Missing Values'] / len(df)) * 100
    missing_data_html = missing_data.to_html(classes='table table-striped', index=False)
    
    # Visualizations
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    plots = []
    for column in numeric_columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        
        graphic = base64.b64encode(image_png).decode('utf-8')
        plots.append(graphic)
        plt.close()
    
    context = {
        'preview': preview,
        'summary_stats': summary_stats,
        'missing_data': missing_data_html,
        'plots': plots,
    }
    
    return render(request, 'data_analysis/results.html', context)

from django.http import HttpResponse
from django.db import connection

def debug_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
    return HttpResponse(str(tables))