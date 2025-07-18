# 📈 Stock Portfolio Tracker

This Python project helps users track the value of their stock portfolio based on current stock prices and their holdings.

---

## ✅ Features

- Calculates total value for each stock in your portfolio.
- Computes the overall investment value.
- Option to save the report as a text file.
- Simple and easy-to-read output format.

---

## 🧠 How It Works

The script uses two dictionaries:
- `stock_prices`: Contains current prices for stocks.
- `user_stocks`: Contains quantity of each stock owned by the user.

The function `calculate_portfolio_value()` calculates:
- The individual value of each stock (`quantity × price`)
- The total portfolio value
- Optionally writes the result to a file named `portfolio_report.txt`.

---

## 📁 Files

- `portfolio_tracker.py` – Main script containing the function and example data.
- `portfolio_report.txt` – Output file (if enabled with `save_to_file=True`).
- `README.md` – Project documentation.

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/stock-portfolio-tracker.git
   cd stock-portfolio-tracker
   ```

2. Run the script:
   ```bash
   python portfolio_tracker.py
   ```

---

## 📝 Example Output

```
Stock   Qty     Price   Total
AAPL    10      180     1800
TSLA    5       250     1250
GOOGL   8       140     1120
AMZN    12      130     1560

Total Investment Value: 5730
```

---

## 🛠️ Technologies Used

- Python 3.x

---

**Author**: K.R. BHAWANA | CodeAlpha Internship (July 2025)

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).
