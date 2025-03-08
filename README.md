# Bike Rental Dashboard

This project is an interactive dashboard used to analyze bike rental data based on various factors such as weather, time, user type, holidays, and workdays. The dashboard is built using Streamlit and Plotly to provide interactive data visualizations that are easy to understand.

## Key Features

- **Data Filters**: Provides multiple filter options, including season, time range, weather conditions, holidays, workdays, and user type (casual or registered).
- **Weather Impact Visualization**: A box plot showing the impact of weather conditions on the number of bike rentals.
- **Rental Trend by Time**: A line chart showing the trend of bike rentals throughout the day.
- **Casual vs Registered Usage**: A histogram comparing bike rentals by casual and registered users.
- **Holiday Impact**: A box plot illustrating the impact of holidays on bike rentals.
- **Workday vs Weekend Impact**: A box plot showing the difference in bike rentals on workdays vs weekends.

## Installation

### 1. Using **Anaconda/Miniconda**

If you are using **Anaconda** or **Miniconda**, follow the steps below:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RanggaJS/bike-analytics-dashboard.git
   cd bike-analytics-dashboard
   ```
2. **Create and activate a conda environment:**
   ```bash
   conda create --name bike_dashboard python=3.9
   conda activate bike_dashboard
   ```
3. **Install required dependencies:**
   Install all the required packages using `conda`:
   ```bash
   conda install --file requirements.txt
   ```
4. **Prepare the Data:**
   Make sure the CSV file `all_data.csv` is in the correct directory as the Python script. Adjust the file path if necessary.
5. **Run the Streamlit app:**
   Once the dependencies are installed, run the app using:
   ```bash
   streamlit run dashboard.py
   ```
6. **Open the dashboard in your browser:**
   Open the URL shown in the terminal to access the dashboard.

---

### 2. Using **Terminal** (Virtual Environment)

If you're not using **Anaconda/Miniconda**, you can use a virtual environment with **pip**. Follow the steps below:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RanggaJS/bike-analytics-dashboard.git
   cd bike-analytics-dashboard
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
3. **Activate the virtual environment:**
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
4. **Install required dependencies:**
   Install all the required packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
5. **Prepare the Data:**
   Ensure that the CSV file `all_data.csv` is in the same directory as the Python script.
6. **Run the Streamlit app:**
   After installing the dependencies, run the app using:
   ```bash
   streamlit run dashboard.py
   ```
7. **Open the dashboard in your browser:**
   Open the URL shown in the terminal to access the dashboard.
