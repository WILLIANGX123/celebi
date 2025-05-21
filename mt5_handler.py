import MetaTrader5 as mt5

def send_order(symbol, action, lot):
    if not mt5.initialize():
        return f"Erro ao conectar MT5: {mt5.last_error()}"

    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None or not symbol_info.visible:
        return f"Símbolo {symbol} não visível ou inválido"

    price = mt5.symbol_info_tick(symbol).ask if action == "buy" else mt5.symbol_info_tick(symbol).bid
    order_type = mt5.ORDER_TYPE_BUY if action == "buy" else mt5.ORDER_TYPE_SELL

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": price,
        "deviation": 10,
        "magic": 234000,
        "comment": "Ordem enviada via webhook",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    mt5.shutdown()

    return f"Ordem enviada: {result}" if result.retcode == 10009 else f"Erro: {result.retcode}"
