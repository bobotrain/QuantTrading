import FinanceDataReader as fdr
import matplotlib.pyplot as plt

# 종목코드, 시작날짜, 종료날짜를 입력합니다.
# 여기서는 삼성전자(005930)의 2022년 1월 1일부터 2022년 12월 31일까지의 주가 데이터를 가져옵니다.
#data = fdr.DataReader('005930', '2022-01-01', '2022-12-31')
#print(data)

# Hint) Stock Symbol for Apple Inc is "AAPL", Stock code for Samsung Electronics is "005930"

#구글
df = fdr.DataReader("AAPL", '2020')
df = fdr.DataReader('AAPL', '2020-01-01', '2020-01-15')
#print(df)

#삼성전자
#df = fdr.DataReader("005930", '2020')
#df = fdr.DataReader('005930', '2020-01-01', '2020-01-15')
#print(df)



# Retrieve list of stocks codes for KOSPI/KRX/NASDAQ/SP500/Korean ETFs.



#df_kospi = fdr.StockListing("KOSPI")
#df_krx = fdr.StockListing("KRX")
#df_nasdaq = fdr.StockListing("NASDAQ")
#df_sp500 = fdr.StockListing("SP500")
#df_etf_kr = fdr.StockListing("ETF/KR")

#print(df_sp500[:20]) 

#print(df_sp500[:5])  
#print(df_sp500.head())

#print(df_sp500[-5:])  
#print(df_sp500.tail())

# df.plot() 코드가 있는 부분
df.plot()

# 그래프 표시
plt.show()