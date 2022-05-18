import requests

# Main Function that contains all user input and nested functions


def currency_converter():
    # Gets the user input for the from country conversion
    from_currency = (
        input("Enter in the currency you'd like to convert from: ")).upper()

    # Checks to make sure the input is a valid length
    if len(from_currency) < 3 or len(from_currency) > 3:
        print('Please enter a valid currency ISO.')
        currency_converter()

    # Checks to see if user input is a string or digit
    if not from_currency.isalpha():
        print('Please enter a valid currency ISO.')
        currency_converter()
    else:
        from_currency = str(from_currency)

    # Gets the user input for the from country conversion
    to_currency = str(
        input("Enter in the currency you'd like to convert to: ")).upper()

    # Checks to make sure the input is a valid length
    if len(to_currency) < 3 or len(to_currency) > 3:
        print('Please enter a valid currency ISO.')
        currency_converter()

    # Checks to see if user input is a string or digit
    if not to_currency.isalpha():
        print('Please enter a valid currency ISO.')
        currency_converter()
    else:
        to_currency = str(to_currency)

    # Gets the user input for the amount
    amount = (input("Enter in the amount of money: "))

    # Checks to make sure the input is a valid digit
    if amount.isdigit():
        amount = float(amount)
    else:
        print('Please enter a valid amount.')
        currency_converter()

    # Gets the data from the API
    response = requests.get(
        f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

    # Prints the conversion rate
    print(
        f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")


# Calls the main function
currency_converter()
