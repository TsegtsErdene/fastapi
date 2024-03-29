import MetaTrader5 as mt

mt.initialize()

# login = 212769315
# password = "Blackstar15"
# server = "OctaFX-Demo"
# mt.login(login, password, server)


def tradebuy(symbol, type, stop_loss, take_profit, lotsize,comment):

    if type == 0:
        type_trade = mt.ORDER_TYPE_BUY
        price = mt.symbol_info_tick(symbol).ask
    else:
        type_trade = mt.ORDER_TYPE_SELL
        price = mt.symbol_info_tick(symbol).bid

    request = {
        "action": mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": float(lotsize),
        "type": type_trade,
        "price": price,
        "tp": float(take_profit),
        "sl": float(stop_loss),
        "deviation": 20,
        "magic": 234000,
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC,
        "comment":comment
    }


    order = mt.order_send(request)

    return order.order

def tradeclose(comment):
    # Get a list of open positions
    positions = mt.positions_get()
    counter = False

    for position in positions:
        # Check if the position's comment matches the ticket
        print(type(position.comment),"  ")
        if position.comment == str(comment):
            
            mt.Close(position.symbol,ticket=position.ticket)
            counter = True

            print(f"Closed position with comment {comment}")
    if(counter):
        return True  # Return True if a position was closed
    else:
        print(f"No open position found with comment {comment}")
        return False  # Return False if no position was closed
