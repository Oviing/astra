from fbprophet import Prophet
import yfinance as yf
import datetime
import pandas as pd


class oracle():

  def __init__(self):
    
    return

  def get_data(stock_symbol, time_span):

    stock = yf.Ticker(stock_symbol)
    start_day = datetime.datetime.today().strftime('%Y-%m-%d')

    data = stock.history(period = time_span, interval= '1d', end= start_day)
    data = data.drop(['Open', 'High', 'Low', 'Volume', 'Dividends', 'Stock Splits'], axis = 1)



    data = data.reset_index()

    data = data.rename(columns={'Date': 'ds', 'Close': 'y'})

    data = data.reindex(index=data.index[::-1])
    return data


  def predict(self, stock_symbol, time_span, forecast, return_graph = False):

    stock = stock_symbol
    t = time_span
    t_forecast = forecast

    data = get_data(stock, t)
    m = Prophet(daily_seasonality=True)
    m.fit(data)

    future = m.make_future_dataframe(periods=t_forecast)
    forecast = m.predict(future)


    if return_graph == False:

      l = [forecast, m]
      return l
    else:
      plot_graph = m.plot(forecast)
      l = [forecast, m]
    return l