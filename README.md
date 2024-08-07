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

2.Django 3.x or higher

3.pandas

4.numpy

5.matplotlib or seaborn

### Start the Development Server

python manage.py runserver

### Access the Application
Open your browser and go to
http://127.0.0.1:8000/ 
 to start using the application.

## Sample CSV File
 A sample CSV file for testing purposes can be found Media \csv_files

### Project Structure

CSV_Analyzer : Django app for core functionality.

data_analyzer: app core functionality and templates

templates\data_analyzer : HTML templates.

manage.py: Django administrative tool.

![1722970335919](https://github.com/user-attachments/assets/18dede8c-befa-4ee6-b518-57935eebaa34)

