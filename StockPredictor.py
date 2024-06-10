import streamlit as s
from datetime import date 
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as g

START="2018-01-01"
CURRENT=date.today().strftime("%Y-%m-%d")

s.title("Stock Market Predictor")
stocks=("HYLN","AMZN","RBLX","CVNA","AAPL","RIVN")
  
picked_stocks=s.selectbox("Pick data set for the prediction", stocks)
quantity_years= s.slider("Years of prediction:",1,4)
timePeriod=quantity_years*365
@s.cache_data
def load_All_Data(ticker):
    data= yf.download(ticker, START, CURRENT)
    data.reset_index(inplace=True)
    return data
data_loading_states=s.text("Loading this data....")
data=load_All_Data(picked_stocks)
data_loading_states.text("Loading's complete!")

s.subheader('Raw information')
s.write(data.tail())

def plottingRawData():
    fig=g.Figure()
    fig.add_trace(g.Scatter(x=data['Date'],y=data['Open'],name='stock_open'))
    fig.add_trace(g.Scatter(x=data['Date'],y=data['Close'],name='stock_close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    s.plotly_chart(fig)
plottingRawData()

df_train=data[['Date','Close']]
df_train =df_train.rename(columns={"Date":"ds", "Close":"y"})

mm=Prophet()
mm.fit(df_train)
future=mm.make_future_dataframe(periods=timePeriod)
forecast=mm.predict(future)
s.subheader('Forecast data')
s.write(forecast.tail())
s.write('forecast data')
fig1=plot_plotly(mm,forecast)
s.plotly_chart(fig1)
s.write('forecast components')
figure2=mm.plot_components(forecast)
s.write(figure2)
