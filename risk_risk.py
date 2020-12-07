import pandas as pd

def drawdown(return_series: pd.Series):
  """
  Takes a time series of asset returns
  Computes and returns a DataFrame that contains:
  the wealth index
  the previous peaks
  percent drawdowns
  """
  wealth_index = 1000*(1+return_series).cumprod()
  previous_peaks = wealth_index.cummax()
  drawdowns = (wealth_index - previous_peaks)/previous_peaks
  return pd.DataFrame({
      "Wealth": wealth_index,
      "Peaks" : previous_peaks,
      "Drawdown": drawdowns
  })

def get_ffme_return():
  """
  Load the Fama-French Dataset for the returns of the Top and Bottom Deciles by MarketCap
  """
  me_m = pd.read_csv('data\Portfolios_Formed_on_ME_monthly_EW.csv',
                     header=0, index_col=0, na_values=-99.99)
  rets = me_m[['Lo 10','Hi 10']]
  rets.columns = ['SmallCap','LargeCap']
  rets = rets/100
  rets.index = pd.to_datetime(rets.index, format="%Y%m").to_period('M')
  return rets

def get_hfi_return():
  """
  Load the HDHEC Hedge Fund Index Dataset for the returns of the Top and Bottom Deciles by MarketCap
  """
  hfi = pd.read_csv('data\edhec-hedgefundindices.csv',
                     header=0, index_col=0, na_values=-99.99)
  hfi = hfi/100
  hfi.index = pd.to_datetime(hfi.index).to_period('M')
  return hfi

def skewness(r):
    """
    Alternative to scipy.stats.skew()
    Cimputes the skewness of the supplied Serires or DataFram
    Returns a float or a Series
    """
    demeaned_r = r - r.mean()
    #use the population standard deviation, so set dof=0
    sigma_r = r.std(ddof=0)
    exp = (demeaned_r**3).mean()
    return exp/sigma_r**3