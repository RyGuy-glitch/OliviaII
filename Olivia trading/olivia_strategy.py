import pandas as pd
import numpy as np

class OliviaVWAPScalp:
    def __init__(self, symbols=["MNQ", "MES", "MYM", "US50"], size=1, vwap_window=20, stop_loss=8, take_profit=16):
        self.symbols = symbols
        self.size = size
        self.vwap_window = vwap_window
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.data = {symbol: [] for symbol in symbols}

    def on_tick(self, tick):
        if tick.symbol not in self.symbols:
            return None

        self.data[tick.symbol].append({"price": tick.price, "volume": tick.volume})
        if len(self.data[tick.symbol]) < self.vwap_window:
            return None

        df = pd.DataFrame(self.data[tick.symbol][-self.vwap_window:])
        vwap = (df["price"] * df["volume"]).sum() / df["volume"].sum()
        price = df["price"].iloc[-1]

        signal = None
        if price > vwap:
            signal = {"action": "BUY", "symbol": tick.symbol, "size": self.size,
                      "stop_loss": self.stop_loss, "take_profit": self.take_profit}
        elif price < vwap:
            signal = {"action": "SELL", "symbol": tick.symbol, "size": self.size,
                      "stop_loss": self.stop_loss, "take_profit": self.take_profit}

        return signal

