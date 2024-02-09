from fastapi import FastAPI, HTTPException, Query
from services import ExchangePriceChecker

app = FastAPI(description="Created By Osama Ahmed", version='1.0')

# Create an instance of the ExchangePriceChecker class
price_checker = ExchangePriceChecker(exchange_id='binance')  # Specify your exchange here

@app.get('/getsymbols')
async def get_symbols():
    return price_checker.fetch_all_symbols()

@app.post('/getprice')
async def get_price(symbol: str):
    result = price_checker.get_symbol_price(symbol)
    if 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])
    return result

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host='0.0.0.0', port=8000)













# from services import ExchangePriceChecker
# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# # Get user input for the exchange
# # user_exchange = input("Enter the exchange you want to use (e.g., 'bybit', 'binance'): ")
# user_exchange = 'binance'

# # Create an instance of the ExchangePriceChecker class for the specified exchange
# price_checker = ExchangePriceChecker(user_exchange)

# @app.post('/getsymbols') 
# async def get_symbols():
#     try:
#         # Assuming there are no parameters to handle in the POST request body
#         return price_checker.fetch_all_symbols()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# if __name__ == "__main__":
#     import uvicorn 
#     uvicorn.run(app, host='0.0.0.0', port=8000)


























# from services import ExchangePriceChecker
# from fastapi import FastAPI

# app = FastAPI()
# # Get user input for the exchange
# # user_exchange = input("Enter the exchange you want to use (e.g., 'bybit', 'binance'): ")
# user_exchange = 'binance'

# # Create an instance of the ExchangePriceChecker class for the specified exchange
# price_checker = ExchangePriceChecker(user_exchange)

# @app.get('/getsymbols')
# async def getSymbols():
#     return price_checker.fetch_all_symbols()

# if __name__ == "__main__":
#     import uvicorn 
#     uvicorn.run(app, host='0.0.0.0', port=8000)