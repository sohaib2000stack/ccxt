# import ccxt

# class ExchangePriceChecker:
#     def __init__(self, exchange_id, api_key=None, api_secret=None):
#         self.api_key = api_key
#         self.api_secret = api_secret
#         self.exchange = getattr(ccxt, exchange_id)({
#             'apiKey': self.api_key,
#             'secret': self.api_secret,
#             # Add any additional parameters needed for your specific exchange
#         })

#     def get_symbol_price(self, symbol):
#         try:
#             ticker = self.exchange.fetch_ticker(symbol)
#             return {"symbol": symbol, "last_price": ticker['last']}
#         except ccxt.NetworkError as e:
#             return {"error": f"Network Error: {e}"}
#         except ccxt.ExchangeError as e:
#             return {"error": f"Exchange Error: {e}"}
#         except Exception as e:
#             return {"error": f"An error occurred: {e}"}

#     def fetch_all_symbols(self):
#         try:
#             all_symbols = []
#             symbols = self.exchange.fetch_tickers()
#             for symbol, ticker in symbols.items():
#                 all_symbols.append({"symbol": symbol, "last_price": ticker['last']})
#             return all_symbols
#         except ccxt.NetworkError as e:
#             return {"error": f"Network Error: {e}"}
#         except ccxt.ExchangeError as e:
#             return {"error": f"Exchange Error: {e}"}
#         except Exception as e:
#             return {"error": f"An error occurred: {e}"}



import ccxt

class ExchangePriceChecker:
    def __init__(self, availableExchanges, api_key=None, api_secret=None):
        # Initialize the exchange object based on the provided exchange_id and API credentials
        self.api_key = api_key
        self.api_secret = api_secret
        self.exchange={}
        for exchange in availableExchanges:
            self.exchange[exchange] = getattr(ccxt, exchange)({
                'apiKey': self.api_key,
                'secret': self.api_secret,
                # Add any additional parameters needed for your specific exchange
            })

    def get_symbol_price(self, symbol, exchange):
        try:
            # Fetch ticker for the specified symbol
            ticker = self.exchange[exchange].fetch_ticker(symbol)
            
            # Return the current price for the specified symbol
            return {"symbol": symbol, "last_price": ticker['last']}
        except ccxt.NetworkError as e:
            return {"error": f"Network Error: {e}"}
        except ccxt.ExchangeError as e:
            return {"error": f"Exchange Error: {e}"}
        except Exception as e:
            return {"error": f"An error occurred: {e}"}

    def fetch_all_symbols(self, exchange):
        try:
            all_symbols = []
            # Fetch all symbols supported by the exchange
            symbols = self.exchange[exchange].fetch_tickers()

            # Return the current prices for all symbols
            for symbol, ticker in symbols.items():
                all_symbols.append({"symbol": symbol, "last_price": ticker['last']})
            return all_symbols
        except ccxt.NetworkError as e:
            return {"error": f"Network Error: {e}"}
        except ccxt.ExchangeError as e:
            return {"error": f"Exchange Error: {e}"}
        except Exception as e:
            return {"error": f"An error occurred: {e}"}

































