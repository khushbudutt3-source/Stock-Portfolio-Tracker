stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420
}

total = 0

print("=== Stock Portfolio Tracker ===")

n = int(input("How many stocks do you own? "))

for i in range(n):

    stock = input("Enter stock name: ").upper()

    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:

        investment = stock_prices[stock] * quantity

        total += investment

        print(stock, "Value =", investment)

    else:

        print("Stock not found.")

print("\nTotal Investment Value =", total)

# Optional: Save result

file = open("portfolio.txt", "w")

file.write("Total Investment Value = " + str(total))

file.close()

print("Result saved in portfolio.txt")