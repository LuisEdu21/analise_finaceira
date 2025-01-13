import yfinance as yf

# Criar um objeto para a ação TSLA
tesla = yf.Ticker("BBAS3.SA")

# Informações gerais da empresa
info = tesla.info
print(info)

# Mostrar dividendos
dividendos = tesla.dividends
print(dividendos)
