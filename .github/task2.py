import requests

def get_stock_data(symbol):
    api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'
    url =f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def add_stock(portfolio, symbol):
    stock_data = get_stock_data(symbol)
    if 'Global Quote' in stock_data:
        portfolio[symbol] = stock_data['Global Quote']
        print(f"{symbol} added to the portfolio.")
    else:
        print(f"Failed to add {symbol}to the portfolio. please check the symbol.")

def remove_stock(portfolio, symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from the portfolio.")
    else:
        print(f"{symbol} not found in the portfolio. ")

def display_portfolio(portfolio):
    print("\nPortfolio Performance:")
    for symbol, data in portfolio.items():
        print(f"symbol: {symbol}")
        print(f"Price: {data['05. price']}")
        print(f"change: {data['10. change percent']}")
        print("")

def main():
    portfolio = {}
    while True:
        print("\n1. Add stock")
        print("2. Remove stock")
        print("3. Display portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice =='1':
            symbol = input("Enter the stock symbol: ").upper()
            add_stock(portfolio, symbol)
        elif choice == '2':
            symbol = input("Enter the stock symbol to remove: ").upper()
            remove_stock(portfolio, symbol)
        elif choice == '3':
            display_portfolio(portfolio)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
                                    
#if name == "main":
main()
