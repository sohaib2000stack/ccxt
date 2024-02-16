# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from services import ExchangePriceChecker

# app = FastAPI(description="Created By Osama Ahmed", version='1.0')
# app.add_middleware(CORSMiddleware, allow_origins=['*'])

# exchange_price_checkers = {
#     "binance": ExchangePriceChecker(exchange_id='binance'),
#     "mexc": ExchangePriceChecker(exchange_id='mexc'),
#     "bybit": ExchangePriceChecker(exchange_id='bybit')
# }

# current_exchange_id = None

# @app.get('/exchanges')
# async def get_exchanges():
#     return list(exchange_price_checkers.keys())

# @app.post('/setexchange/{exchange_id}')
# async def set_exchange(exchange_id: str):
#     global current_exchange_id
#     if exchange_id not in exchange_price_checkers:
#         raise HTTPException(status_code=404, detail="Exchange not found")
#     current_exchange_id = exchange_id

# @app.get('/getsymbols')
# async def get_symbols():
#     if current_exchange_id is None or current_exchange_id not in exchange_price_checkers:
#         raise HTTPException(status_code=404, detail="Exchange not set")
#     return exchange_price_checkers[current_exchange_id].fetch_all_symbols()

# @app.post('/getprice')
# async def get_price(symbol: str):
#     if current_exchange_id is None or current_exchange_id not in exchange_price_checkers:
#         raise HTTPException(status_code=404, detail="Exchange not set")
#     result = exchange_price_checkers[current_exchange_id].get_symbol_price(symbol)
#     if 'error' in result:
#         raise HTTPException(status_code=500, detail=result['error'])
#     return result

# if __name__ == "__main__":
#     import uvicorn 
#     uvicorn.run(app, host='0.0.0.0', port=8000)




from fastapi import FastAPI, HTTPException
from services import ExchangePriceChecker
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from pydantic import BaseModel

app = FastAPI(description="Created By Osama Ahmed", version='1.0')
# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create an instance of the ExchangePriceChecker class
class AvailableExchanges(str, Enum):
    binance = 'binance'
    mexc = 'mexc'
    bybit = 'bybit'
    okx = 'okx'
    kucoin = 'kucoin'
    gateio = 'gateio'
    bitget = 'bitget'

class ForGetPriceModel(BaseModel):
    symbol: str
    exchange: AvailableExchanges
exchanges = [exchange.value for exchange in AvailableExchanges]
price_checker = ExchangePriceChecker(exchanges)# @app.get('/exchanges')


@app.get("/getsymbols/{exchange}")
async def get_symbols(exchange:AvailableExchanges):
    return price_checker.fetch_all_symbols(exchange)
@app.get("/getexchanges")
async def get_exchanges():
    return exchanges
@app.post('/getprice')
async def get_price(data: ForGetPriceModel):
    print(data.symbol, data.exchange)
    result = price_checker.get_symbol_price(data.symbol, data.exchange)
    if 'error' in result:
        raise HTTPException(status_code=500, detail=result['error'])
    return result

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host='0.0.0.0', port=8000)




































































