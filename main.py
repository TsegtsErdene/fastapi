from fastapi import FastAPI, HTTPException
import trade

app = FastAPI()

@app.post("/buy")
async def process_buy_data(data: dict):
    try:
        action = data.get("action")
        received_data = data.get("data")

        if action == "added":
            process_added_data(received_data)
        elif action == "closed":
            process_closed_data(received_data)
        else:
            raise HTTPException(status_code=400, detail="Invalid action")

        return {"message": "Data processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

def process_added_data(data):
    print("Processing added data:", data)
    trade.tradebuy(data["Symbol"],data["Type"],0.0,0.0,data['Lot'],data['Ticket'])

def process_closed_data(data):
    print("Processing closed data:", data)
    trade.tradeclose(data['Ticket'])
