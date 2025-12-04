import yfinance as yf
import json

def get_stock_data():
    ticker = yf.Ticker("CDR.WA")
    hist = ticker.history(start="2014-01-01", end="2024-12-31")

    data = []
    for index, row in hist.iterrows():
        data.append({
            "date": index.strftime("%Y-%m-%d"),
            "open": float(row["Open"]),
            "close": float(row["Close"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "volume": int(row["Volume"])
        })

    return data

if __name__ == "__main__":
    print(json.dumps(get_stock_data(), indent=2))
