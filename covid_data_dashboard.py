import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class CovidDataDashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("COVID-19 Data Dashboard")
        self.master.geometry("800x600")

        # Load and prepare data
        self.df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.countries = sorted(self.df['location'].unique())

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Country selection
        ttk.Label(self.master, text="Select Country:").pack(pady=5)
        self.country_var = tk.StringVar()
        self.country_dropdown = ttk.Combobox(self.master, textvariable=self.country_var, values=self.countries)
        self.country_dropdown.pack(pady=5)
        self.country_dropdown.bind("<<ComboboxSelected>>", self.update_plots)

        # Create tabs
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Cases tab
        self.cases_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.cases_tab, text='Cases')

        # Deaths tab
        self.deaths_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.deaths_tab, text='Deaths')

        # Vaccinations tab
        self.vaccinations_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.vaccinations_tab, text='Vaccinations')

    def update_plots(self, event=None):
        country = self.country_var.get()
        country_data = self.df[self.df['location'] == country]

        # Clear previous plots
        for tab in [self.cases_tab, self.deaths_tab, self.vaccinations_tab]:
            for widget in tab.winfo_children():
                widget.destroy()

        # Cases plot
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(country_data['date'], country_data['new_cases_smoothed'], label='New Cases (7-day avg)')
        ax.set_title(f'Daily New COVID-19 Cases in {country}')
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Cases')
        ax.legend()
        self.embed_plot(fig, self.cases_tab)

        # Deaths plot
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(country_data['date'], country_data['new_deaths_smoothed'], label='New Deaths (7-day avg)', color='red')
        ax.set_title(f'Daily New COVID-19 Deaths in {country}')
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Deaths')
        ax.legend()
        self.embed_plot(fig, self.deaths_tab)

        # Vaccinations plot
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(country_data['date'], country_data['people_vaccinated_per_hundred'], label='People Vaccinated per 100', color='green')
        ax.set_title(f'COVID-19 Vaccination Progress in {country}')
        ax.set_xlabel('Date')
        ax.set_ylabel('People Vaccinated per 100')
        ax.legend()
        self.embed_plot(fig, self.vaccinations_tab)

    def embed_plot(self, fig, tab):
        canvas = FigureCanvasTkAgg(fig, master=tab)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = CovidDataDashboard(root)
    root.mainloop()
