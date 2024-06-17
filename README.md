**Overview:**

The Stock Market Predictor is a web application built using Streamlit that allows users to predict future stock prices of selected companies. It leverages historical stock data from Yahoo Finance and uses the Prophet forecasting model to generate predictions.

****Features******
Select stock from a predefined list of companies.
Choose the number of years for future prediction (1 to 4 years).
View raw stock data.
Visualize historical stock prices.
Generate and display future stock price predictions.
Analyze forecast components such as trends and seasonal patterns.
**Technologies Used
**Streamlit: For creating the web application.
yFinance: For fetching historical stock data.
Prophet: For forecasting future stock prices.
Plotly: For data visualization.
**Installation**
To run this application, you need to have Python installed. Follow the steps below to set up the environment:

**Clone the repository:**
git clone https://github.com/yourusername/StockMarketPredictor.git
cd stock-market-predictor
Install the required packages:

Code:
pip install streamlit yfinance prophet plotly
Running the Application
To start the application, run the following command in the terminal:

Code:
streamlit run app.py
Application Structure
app.py: The main file that contains the Streamlit application code.
requirements.txt: List of required packages for the application.
Code Explanation
Here is a breakdown of the main parts of the application:

**Imports**
Code:
import streamlit as s
from datetime import date 
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as g
These are the necessary libraries for building the application, handling dates, fetching stock data, forecasting, and visualization.

**Constants**
Code:
START = "2018-01-01"
CURRENT = date.today().strftime("%Y-%m-%d")
stocks = ("HYLN", "AMZN", "RBLX", "CVNA", "AAPL", "RIVN")
Defines the start date for fetching historical data, the current date, and the list of available stocks for prediction.

**User Inputs**
Code:

picked_stocks = s.selectbox("Pick data set for the prediction", stocks)
quantity_years = s.slider("Years of prediction:", 1, 4)
timePeriod = quantity_years * 365
Creates user interface elements for selecting the stock and the prediction period.

**Data Loading**
Code:

@s.cache_data
def load_All_Data(ticker):
    data = yf.download(ticker, START, CURRENT)
    data.reset_index(inplace=True)
    return data

data_loading_states = s.text("Loading this data....")
data = load_All_Data(picked_stocks)
data_loading_states.text("Loading's complete!")
Defines a function to load historical stock data and displays a loading text while the data is being fetched.

**Raw Data Display**
Code:

s.subheader('Raw information')
s.write(data.tail())
Displays the raw stock data.

**Raw Data Plotting**
Code:

def plottingRawData():
    fig = g.Figure()
    fig.add_trace(g.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(g.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    s.plotly_chart(fig)

plottingRawData()
Creates a function to plot the historical stock prices and calls it to display the plot.

Data Preparation and Forecasting

Code:

df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

mm = Prophet()
mm.fit(df_train)
future = mm.make_future_dataframe(periods=timePeriod)
forecast = mm.predict(future)
Prepares the data for the Prophet model, fits the model, and makes future predictions.

**Forecast Display**
Code:

s.subheader('Forecast data')
s.write(forecast.tail())
s.write('forecast data')
fig1 = plot_plotly(mm, forecast)
s.plotly_chart(fig1)
s.write('forecast components')
figure2 = mm.plot_components(forecast)
s.write(figure2)
Displays the forecast data and components.

**Conclusion**
This application provides a user-friendly interface for predicting future stock prices using historical data and advanced forecasting models. It's a powerful tool for investors and analysts looking to gain insights into stock market trends.





