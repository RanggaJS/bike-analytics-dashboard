import pandas as pd
import plotly.express as px
import streamlit as st

# Load data
CSV_FILE = "all_data.csv"
all_df = pd.read_csv(CSV_FILE, parse_dates=["dteday"])

# Pastikan dataset memiliki kolom yang diperlukan
required_columns = {"season", "hr", "weathersit", "holiday", "workingday", "casual", "registered", "cnt"}
if not required_columns.issubset(all_df.columns):
    st.error("Dataset tidak memiliki semua kolom yang diperlukan. Periksa CSV Anda.")
    st.stop()

# Sidebar Filters
st.sidebar.header("Filter Data")
season = st.sidebar.selectbox("Pilih Musim:", all_df["season"].unique())
time_filter = st.sidebar.slider("Pilih Rentang Jam:", 0, 23, (0, 23))
weather_filter = st.sidebar.multiselect("Pilih Kondisi Cuaca:", all_df["weathersit"].unique(), default=all_df["weathersit"].unique())
holiday_filter = st.sidebar.radio("Hari Libur:", ["Semua", "Libur", "Bukan Libur"])
workingday_filter = st.sidebar.radio("Hari Kerja vs. Akhir Pekan:", ["Semua", "Hari Kerja", "Akhir Pekan"])
user_type_filter = st.sidebar.radio("Tipe Pengguna:", ["Semua", "Casual", "Registered"])

# Apply Filters
filtered_df = all_df[
    (all_df["season"] == season) &
    (all_df["hr"].between(time_filter[0], time_filter[1])) &
    (all_df["weathersit"].isin(weather_filter))
]

if holiday_filter == "Libur":
    filtered_df = filtered_df[filtered_df["holiday"] == 1]
elif holiday_filter == "Bukan Libur":
    filtered_df = filtered_df[filtered_df["holiday"] == 0]

if workingday_filter == "Hari Kerja":
    filtered_df = filtered_df[filtered_df["workingday"] == 1]
elif workingday_filter == "Akhir Pekan":
    filtered_df = filtered_df[filtered_df["workingday"] == 0]

# Tampilkan Data
st.title("Dashboard Bike Sharing")
st.write(f"Menampilkan data untuk musim {season} dan rentang jam {time_filter}")
st.dataframe(filtered_df)

# Visualisasi Pengaruh Cuaca terhadap Penyewaan Sepeda
fig_weather = px.box(
    filtered_df, 
    x="weathersit", 
    y="cnt", 
    color="weathersit",
    title="Pengaruh Cuaca terhadap Penyewaan Sepeda",
    labels={"cnt": "Jumlah Penyewaan", "weathersit": "Kondisi Cuaca"}
)
st.plotly_chart(fig_weather)

# Visualisasi Tren Penyewaan Berdasarkan Waktu
# Hanya menjumlahkan kolom numerik
fig_trend = px.line(
    filtered_df.groupby("hr")[["cnt", "casual", "registered"]].sum().reset_index(),
    x="hr", y="cnt",
    title="Tren Penyewaan Sepeda Berdasarkan Waktu",
    labels={"cnt": "Jumlah Penyewaan", "hr": "Jam"}
)
st.plotly_chart(fig_trend)

# Visualisasi Perbedaan Penggunaan antara Casual dan Registered
if user_type_filter == "Casual":
    fig_user = px.histogram(filtered_df, x="hr", y="casual", title="Penyewaan oleh Pengguna Kasual")
elif user_type_filter == "Registered":
    fig_user = px.histogram(filtered_df, x="hr", y="registered", title="Penyewaan oleh Pengguna Terdaftar")
else:
    fig_user = px.histogram(filtered_df, x="hr", y=["casual", "registered"], barmode="group", title="Perbedaan Penggunaan Kasual vs. Terdaftar")

st.plotly_chart(fig_user)

# Visualisasi Pengaruh Hari Libur
fig_holiday = px.box(
    all_df, 
    x="holiday", 
    y="cnt", 
    color="holiday",
    title="Dampak Hari Libur terhadap Penyewaan Sepeda",
    labels={"cnt": "Jumlah Penyewaan", "holiday": "Hari Libur (0=Biasa, 1=Libur)"}
)
st.plotly_chart(fig_holiday)

# Visualisasi Pengaruh Hari Kerja vs. Akhir Pekan
fig_workingday = px.box(
    all_df, 
    x="workingday", 
    y="cnt", 
    color="workingday",
    title="Dampak Hari Kerja vs. Akhir Pekan terhadap Penyewaan Sepeda",
    labels={"cnt": "Jumlah Penyewaan", "workingday": "Hari Kerja (0=Akhir Pekan, 1=Hari Kerja)"}
)
st.plotly_chart(fig_workingday)
