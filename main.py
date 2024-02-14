from fastapi import FastAPI, HTTPException
from services import ExchangePriceChecker
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(description="Created By Osama Ahmed", version='1.0')
app.add_middleware(CORSMiddleware, allow_origins = ['*'])
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




































































