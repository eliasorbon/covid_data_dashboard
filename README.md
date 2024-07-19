# COVID-19 Data Visualization Dashboard

## Project Overview

This project is a Python-based interactive dashboard for visualizing COVID-19 data. It demonstrates basic data handling, visualization, and GUI development skills, serving as an introductory portfolio piece for data analysis and Python programming.

## Features

1. **Country Selection**: Users can choose a country from a dropdown menu to visualize its data.
2. **Multi-faceted Data Visualization**: The dashboard presents three aspects of COVID-19 data:
   - Daily New Cases (7-day average)
   - Daily New Deaths (7-day average)
   - Vaccination Progress
3. **Time Series Visualization**: All data is presented over time, allowing for basic trend visualization.

## Technologies and Methodologies Used

### 1. Data Acquisition and Processing
- **Data Source**: Our World in Data (OWID) COVID-19 dataset
- **Library Used**: Pandas
- **Methodology**: 
  - Data is fetched directly from OWID's GitHub repository using Pandas' `read_csv` function.
  - Basic data processing: Converting date strings to datetime objects for proper plotting.

### 2. Data Visualization
- **Library Used**: Matplotlib
- **Methodology**:
  - Line plots are used to visualize trends over time.
  - Separate plots are created for cases, deaths, and vaccination data.

### 3. Interactive GUI Development
- **Library Used**: Tkinter
- **Methodology**:
  - A simple GUI is created with a dropdown for country selection and tabs for different data views.
  - Basic event handling is implemented to update plots when a country is selected.

## Code Structure

1. **Class-based Design**: The code is organized into a `CovidDataDashboard` class, demonstrating basic object-oriented programming.
2. **Data Loading**: Data is loaded once at initialization and stored in a Pandas DataFrame.
3. **Plot Updates**: Separate methods handle the creation and updating of plots.

## Running the Project

1. Ensure Python 3.x is installed on your system.
2. Install required libraries:
   ```
   pip install pandas matplotlib
   ```
3. Run the script:
   ```
   python covid_dashboard.py
   ```

## Limitations and Potential Improvements

1. **Data Analysis**: The current implementation focuses on data visualization without performing additional statistical analysis.
2. **Data Refresh**: The dashboard loads data once at startup and doesn't include functionality to refresh or update the dataset.
3. **Error Handling**: Basic error handling is implemented, primarily for data loading issues.
4. **Performance**: For countries with large datasets, plot updates might be slow. Optimization could be implemented for larger datasets.

## Skills Demonstrated

1. **Basic Data Handling**: Using Pandas to load and process CSV data.
2. **Data Visualization**: Creating simple time-series plots with Matplotlib.
3. **GUI Development**: Building a basic interactive interface with Tkinter.
4. **Python Programming**: Demonstrating understanding of functions, classes, and basic Python syntax.
5. **Working with Real-world Data**: Handling and visualizing actual COVID-19 data.

## Conclusion

This COVID-19 Data Visualization Dashboard serves as a starting point for data visualization projects. It demonstrates basic skills in Python programming, data handling, and GUI development. While it doesn't include advanced statistical analysis or complex features, it provides a foundation for further learning and development in data analysis and visualization.
