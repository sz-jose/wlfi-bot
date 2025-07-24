from binance.client import Client
import time

api_key = "XOgL8pLnHgPqVHrmvczJ1nYVOpgeTTgV6Tk83NiJbTZabnXSZ7pJwF57eE0HIKC4"
api_secret = "lcbjL6bSiCs4pgpJxyKc2FQjMJGAsk78FbtH8QvoqCy3zJ6a9xeeCs9mVPVyLwhn"

client = Client(api_key, api_secret)

symbol = 'WLFIUSDT'
usdt_amount = 10  # Monto que quieres usar para comprar

def symbol_exists(symbol):
    try:
        info = client.get_symbol_info(symbol)
        return info is not None
    except:
        return False

def buy_token(symbol, usdt_amount):
    price = float(client.get_symbol_ticker(symbol=symbol)['price'])
    quantity = round(usdt_amount / price, 4)
    order = client.order_market_buy(
        symbol=symbol,
        quantity=quantity
    )
    return order

print(f"⏳ Esperando que {symbol} esté disponible en Binance...")

while not symbol_exists(symbol):
    print(".", end="", flush=True)
    time.sleep(5)

print(f"\n✅ {symbol} ahora está disponible. Comprando...")

try:
    order = buy_token(symbol, usdt_amount)
    print("🎉 Orden ejecutada con éxito:")
    print(order)
except Exception as e:
    print("❌ Error al ejecutar orden:", e)
