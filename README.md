# CSV_Analyzer : A Django-based CSV Data Analysis Web Application

## project overview
CSV_Analyzer is a Django-based web application that allows users to upload CSV files, perform data analysis using pandas and numpy, and view the results and visualizations directly on the web interface.

### Features
1.Upload CSV Files: Users can upload CSV files via a web form.
2.Data Analysis: Display the first few rows, summary statistics (mean, median, std), and handle missing values.
3.Data Visualization: Generate histograms and display them on the web page.
4.User Interface: Simple and clean interface to view results and plots.

### Requirements
1.Python 3.x
2.Django
3.pandas
4.numpy
5.matplotlib or seaborn

### Start the Server

python manage.py runserver

### Access the App
http://127.0.0.1:8000/

### Project Structure

CSV_Analyzer : Django app for core functionality.
templates\data_analyzer : HTML templates.
manage.py: Django administrative tool.
