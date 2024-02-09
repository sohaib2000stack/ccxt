import ccxt

class ExchangePriceChecker:
    def __init__(self, exchange_id, api_key=None, api_secret=None):
        # Initialize the exchange object based on the provided exchange_id and API credentials
        self.api_key = api_key
        self.api_secret = api_secret
        self.exchange = getattr(ccxt, exchange_id)({
            'apiKey': self.api_key,
            'secret': self.api_secret,
            # Add any additional parameters needed for your specific exchange
        })

    def get_symbol_price(self, symbol):
        try:
            # Fetch ticker for the specified symbol
            ticker = self.exchange.fetch_ticker(symbol)
            
            # Return the current price for the specified symbol
            return {"symbol": symbol, "last_price": ticker['last']}
        except ccxt.NetworkError as e:
            return {"error": f"Network Error: {e}"}
        except ccxt.ExchangeError as e:
            return {"error": f"Exchange Error: {e}"}
        except Exception as e:
            return {"error": f"An error occurred: {e}"}

    def fetch_all_symbols(self):
        try:
            all_symbols = []
            # Fetch all symbols supported by the exchange
            symbols = self.exchange.fetch_tickers()

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
































# from fastapi import FastAPI, HTTPException
# from typing import Dict, List
# import ccxt

# class ExchangePriceChecker:
#     def __init__(self, exchange_id, api_key=None, api_secret=None):
#         # Initialize the exchange object based on the provided exchange_id and API credentials
#         self.api_key = api_key
#         self.api_secret = api_secret
#         self.exchange = getattr(ccxt, exchange_id)({
#             'apiKey': self.api_key,
#             'secret': self.api_secret,
#             # Add any additional parameters needed for your specific exchange
#         })

#     def get_symbol_price(self, symbol):
#         try:
#             # Fetch ticker for the specified symbol
#             ticker = self.exchange.fetch_ticker(symbol)
            
#             # Return the current price for the specified symbol
#             return {"symbol": symbol, "last_price": ticker['last']}
#         except ccxt.NetworkError as e:
#             raise HTTPException(status_code=500, detail=f"Network Error: {e}")
#         except ccxt.ExchangeError as e:
#             raise HTTPException(status_code=500, detail=f"Exchange Error: {e}")
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

# app = FastAPI()
# exchange_id = 'binance'  # Default exchange ID

# # Create an instance of the ExchangePriceChecker class for the specified exchange
# price_checker = ExchangePriceChecker(exchange_id)

# @app.post('/getprice', response_model=Dict[str, float])
# async def get_price(exchange_id: str, symbol: str):
#     try:
#         price = price_checker.get_symbol_price(symbol)
#         return price
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))




























# import ccxt

# class ExchangePriceChecker:
#     def __init__(self, exchange_id, api_key=None, api_secret=None):
#         # Initialize the exchange object based on the provided exchange_id and API credentials
#         self.api_key = api_key
#         self.api_secret = api_secret
#         self.exchange = getattr(ccxt, exchange_id)({
#             'apiKey': self.api_key,
#             'secret': self.api_secret,
#             # Add any additional parameters needed for your specific exchange
#         })

#     def get_symbol_price(self, symbol):
#         try:
#             # Fetch ticker for the specified symbol
#             ticker = self.exchange.fetch_ticker(symbol)
            
#             # Print the current price for the specified symbol
#             print(f"Symbol: {symbol}, Last Price: {ticker['last']}")
#         except ccxt.NetworkError as e:
#             print(f"Network Error: {e}")
#         except ccxt.ExchangeError as e:
#             print(f"Exchange Error: {e}")
#         except Exception as e:
#             print(f"An error occurred: {e}")

#     def fetch_all_symbols(self):
#         try:
#             all_symbols = []
#             # Fetch all symbols supported by the exchange
#             symbols = self.exchange.fetch_tickers()

#             # Print the current prices for all symbols
#             for symbol, ticker in symbols.items():
#                 all_symbols.append({symbol:ticker['last']})
#             return all_symbols
#         except ccxt.NetworkError as e:
#             print(f"Network Error: {e}")
#         except ccxt.ExchangeError as e:
#             print(f"Exchange Error: {e}")
#         except Exception as e:
#             print(f"An error occurred: {e}")

    # def main(self):
    #     # Fetch and print all symbols and their prices
    #     self.fetch_all_symbols()

    #     # Get user input for the symbol
    #     user_symbol = input("Enter the symbol you want to check (e.g., BTC/USDT): ")

    #     # Call the function to get and print the price for the user-specified symbol
    #     self.get_symbol_price(user_symbol