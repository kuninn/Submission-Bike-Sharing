import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)
data_dframe_merge = pd.read_csv('https://raw.githubusercontent.com/kuninn/Submission-Bike-Sharing/main/dashboard/main_data.csv')

st.title("BIKE RENTAL DASHBOARD 🚲")

st.header('Daily Basis Rental')
total_users = data_dframe_merge[['casual', 'registered']].sum().sum()
percentage_casual = (data_dframe_merge['casual'].sum() / total_users) * 100
percentage_registered = (data_dframe_merge['registered'].sum() / total_users) * 100
st.metric('Casual User', f"{percentage_casual:.2f}%")
st.metric('Registered User', f"{percentage_registered:.2f}%")
st.metric('Total User', total_users)

min_date = pd.to_datetime(data_dframe_merge['dteday']).dt.date.min()
max_date = pd.to_datetime(data_dframe_merge['dteday']).dt.date.max()

start_date, end_date = st.sidebar.date_input(
    label='Rentang Waktu',
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

st.header("Bike Rental Trends By Month")
plt.figure(figsize=(10, 6))
sns.lineplot(data=data_dframe_merge, x='month_idn', y='cnt', hue='yr', marker='o')
plt.xlabel('Bulan')
plt.ylabel('Total Penggunaan Sepeda')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Ags', 'Sep', 'Okt', 'Nov', 'Des'])
plt.legend(title='Tahun')
st.pyplot()

st.header("Bike Rental By Workday and Weekday")
warna = ['red','lightblue']
total_workingday = data_dframe_merge[data_dframe_merge['workingday'] == 1]['cnt'].mean()
total_weekday = data_dframe_merge[data_dframe_merge['weekday'] == 0]['cnt'].mean()
plot_data = pd.DataFrame({
    'Hari': ['Hari Libur', 'Hari Kerja'],
    'Persentase': [total_weekday, total_workingday]
})
sns.barplot(data=plot_data, x='Persentase', y='Hari', palette=warna, orient='h')
plt.xlabel('Value rata-rata penyewaan sepeda')
plt.ylabel('Hari')
plt.title('Perbandingan rata-rata penyewaan sepeda antara hari kerja dan hari libur')
plt.show()
plt.grid(axis='x', linestyle='--', alpha=0.7)
st.pyplot()

st.header("Bike Rental Based on Weather")
plt.figure()
warna_2 = ['yellow','orange','lightblue', 'gray']
sns.barplot(data=data_dframe_merge, x='weathersit', y='cnt', palette=warna_2)
plt.xlabel('Cuaca')
plt.ylabel('Jumlah Penyewaan')
plt.title('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')
plt.xticks([0, 1, 2, 3], ["Cerah", " Cerah Berawan", "Mendung", "Gerimis"])
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot()

st.header("Bike Rental Based on Month")
avr_perbulan = data_dframe_merge.groupby('month_idn')['cnt'].mean().reset_index()
avr_perbulan = avr_perbulan.sort_values(by='month_idn')

plt.figure(figsize=(10, 6))
sns.lineplot(data=avr_perbulan, x='month_idn', y='cnt', palette='viridis')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(rotation=0)
plt.title('Jumlah distribusi rata-rata penyewaan sepeda setiap bulan')
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot()

st.caption('© Muhammad Irfan Adi Saputra')
