import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Nexus Data Platform", layout="wide")

@st.cache_resource
def get_connection():
    return psycopg2.connect(
        host="172.17.0.1",
        port=5432,
        dbname="de_project",
        user="de_user",
        password="de_password"
    )

conn = get_connection()

customers_df = pd.read_sql("SELECT * FROM customers", conn)
orders_df = pd.read_sql("SELECT * FROM orders", conn)

# KPI Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", len(customers_df))
col2.metric("Total Orders", len(orders_df))
col3.metric("Total Revenue", f"${orders_df['amount'].sum():,.2f}" if not orders_df.empty else "$0")
col4.metric("Avg Order Value", f"${orders_df['amount'].mean():,.2f}" if not orders_df.empty else "$0")

st.divider()

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("🏆 Top Customers by Spend")
    if not orders_df.empty:
        top_customers = orders_df.groupby("customer")["amount"].sum().sort_values(ascending=False).reset_index()
        fig1 = px.bar(top_customers, x="customer", y="amount", title="Revenue by Customer")
        st.plotly_chart(fig1, use_container_width=True)

with col_b:
    st.subheader("🌆 Orders by City")
    if not orders_df.empty:
        city_orders = orders_df.groupby("city").size().reset_index(name="orders")
        fig2 = px.pie(city_orders, names="city", values="orders", title="Order Distribution by City")
        st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("👥 Customer Records (Full Data)")
st.dataframe(customers_df, use_container_width=True)

st.subheader("🧾 Order Records (Full Data)")
st.dataframe(orders_df, use_container_width=True)

st.divider()
st.caption("Built with Streamlit • Connected to PostgreSQL • Part of Nexus Data Platform")
