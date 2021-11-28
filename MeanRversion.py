import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import date, timedelta

# Standardize datetime
Start = date.today() - timedelta(60)
Start.strftime('%Y-%m-%d')

End = date.today() + timedelta(2)
End.strftime('%Y-%m-%d')


#
def closing_price(ticker):
    Asset = pd.DataFrame(yf.download(ticker, period= '60d', interval= '15m')['Adj Close'])
    return Asset

SPY = closing_price('SPY')                  # CALL THE FUNCTION

plt.plot(SPY)
plt.show()