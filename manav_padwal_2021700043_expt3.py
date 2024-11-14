import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Online-eCommerce.csv')# replace with the actual path to your CSV

# Title for the Dashboard
st.title("Order Data Dashboard")

# Display the dataset
st.subheader("Dataset")
st.dataframe(df)



# Pie chart for Sales distribution by State
st.subheader("Sales Distribution by State")
sales_by_state = df.groupby('State_Code')['Total_Sales'].sum()

fig2, ax2 = plt.subplots()
ax2.pie(sales_by_state, labels=sales_by_state.index, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig2)

# Line chart for Sales over time (assuming 'Order_Date' is in datetime format)
st.subheader("Sales Over Time")
df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='%d/%m/%Y')   # Parse the date format

sales_over_time = df.groupby('Order_Date')['Total_Sales'].sum().reset_index()

fig3, ax3 = plt.subplots()
ax3.plot(sales_over_time['Order_Date'], sales_over_time['Total_Sales'], marker='o')
ax3.set_xlabel('Date')
ax3.set_ylabel('Total Sales')
ax3.set_title('Total Sales Over Time')
st.pyplot(fig3)

# Scatter plot for Cost vs Sales
st.subheader("Cost vs Sales")
fig4, ax4 = plt.subplots()
sns.scatterplot(data=df, x='Cost', y='Sales', hue='Category', ax=ax4)
ax4.set_title('Cost vs Sales by Category')
st.pyplot(fig4)

# Histogram for Quantity distribution
st.subheader("Quantity Distribution")
fig5, ax5 = plt.subplots()
ax5.hist(df['Quantity'], bins=10, color='green', alpha=0.7)
ax5.set_xlabel('Quantity')
ax5.set_ylabel('Frequency')
ax5.set_title('Distribution of Quantity Sold')
st.pyplot(fig5)

# Advanced: Boxplot for Cost by Category
st.subheader("Cost Distribution by Category")
fig6, ax6 = plt.subplots()
sns.boxplot(x='Category', y='Cost', data=df, ax=ax6)
ax6.set_title('Cost Distribution by Product Category')
st.pyplot(fig6)

# Observations
st.subheader("Key Observations")
st.write("""
1. **Top Sales Product**: RYZEN 3rd gen. CPU has the highest total sales.
2. **Sales Distribution**: AP and AS states contribute the most to sales.
3. **Sales Over Time**: Sales remain consistent over the dates.
4. **Cost vs Sales Relationship**: Higher costs generally lead to higher sales.
5. **Quantity Distribution**: Most orders consist of 2-3 items.
6. **Cost Distribution by Category**: Significant variation in cost exists across categories.
""")

