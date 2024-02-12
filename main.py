# main.py
from fastapi import FastAPI
import trade

app = FastAPI()

@app.get('/')
async def root():
    return {'example': 'This is an example'}


@app.get('/buy')
def buy():
    trade.tradebuy("XAUUSD","BUY",0.0,0.0,0.06,"ok")
    return {'success': 'Success'}