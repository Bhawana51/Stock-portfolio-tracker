stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130
}

user_stocks = {
    "AAPL": 10,
    "TSLA": 5,
    "GOOGL": 8,
    "AMZN": 12
}

def calculate_portfolio_value(stock_prices, user_stocks, save_to_file=False, filename="portfolio_report.txt"):
    total_value = 0
    lines = ["Stock\tQty\tPrice\tTotal"]
    for stock, qty in user_stocks.items():
        price = stock_prices.get(stock, 0)
        total = qty * price
        total_value += total
        lines.append(f"{stock}\t{qty}\t{price}\t{total}")
    lines.append(f"\nTotal Investment Value: {total_value}")

    if save_to_file:
        with open(filename, 'w') as file:
            file.write("\n".join(lines))
    return "\n".join(lines)

print(calculate_portfolio_value(stock_prices, user_stocks, save_to_file=True))
