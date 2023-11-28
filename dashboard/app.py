import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='dark')

df = pd.read_csv("/content/day.csv", delimiter=",")
df['dteday'] = pd.to_datetime(df['dteday'])

st.header('Dashboard')

min_date = df["dteday"].min()
max_date = df["dteday"].max()

with st.sidebar:
    st.header('Bike Sharing Dashboard')

    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
main_df = df[(df["dteday"] >= str(start_date)) &
                (df["dteday"] <= str(end_date))]

st.subheader('Jumlah Rental Sepeda Harian')
fig, ax = plt.subplots(figsize=(32, 16))
ax.plot(
    main_df["dteday"],
    main_df["cnt"],
    marker='o',
    linewidth=5,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

st.subheader('Jumlah Rental Sepeda Menurut Cuaca dan Hari Kerja')
col1, col2 = st.columns(2)
df1 = main_df.groupby('weathersit')['cnt'].sum()
df1 = pd.DataFrame(df1)
df2 = main_df.groupby('weekday')['cnt'].sum()
df2 = pd.DataFrame(df2)

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        y='cnt',
        x=df1.index,
        data=df1,
        ax=ax
    )
    ax.set_title("Jumlah Rental Sepeda berdasarkan cuaca", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))

    colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(
        y='cnt',
        x=df2.index,
        data=df2,
        palette=colors,
        ax=ax
    )
    ax.set_title("Jumlah Rental Sepeda berdasarkan hari", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

st.markdown(
    """
    # Keterangan
    **Cuaca**
    - 1: Cerah
    - 2: Berawan
    - 3: Hujan/Salju Ringan
    - 4: Badai

    **Hari**
    - 0: Minggu
    - 1: Senin
    - 2: Selasa
    - 3: Rabu
    - 4: Kamis
    - 5: Jumat
    - 6: Sabtu
    """
)