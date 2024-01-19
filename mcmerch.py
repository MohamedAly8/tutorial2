''' MVP Plan
 1. Get environment set up
-  one by one instead of many items
-  one province instead of many (ON)
- calculate tax + 5% discount for ON item
'''

ON_TAX = 0.13
DISCOUNT = 0.05
def main():
    item_price = float(input("Enter the price of the item: "))

    price_after_discount = item_price * (1-DISCOUNT)
    item_tax = price_after_discount * ON_TAX
    final_price = price_after_discount + item_tax
    print("Final price for item is ${:.2f}".format(final_price))

if __name__ == "__main__":
    main()
