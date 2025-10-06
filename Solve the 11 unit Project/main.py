"""
Currency Converter Project
--------------------------

A simple terminal-based currency converter that allows users to convert
between predefined currencies (USD, EUR, MRC, RMB). The program displays
an ASCII-art introduction, requests user input for source and target
currencies, performs conversion using exchange rates stored in a
dictionary, and simulates processing delays for a better user experience.

Modules used:
    - time: to simulate delay and create a dynamic user experience.
    - os: to clear the terminal screen for better readability.

Main features:
    • Display available currencies with their conversion rates.
    • Convert an entered amount between selected currencies.
    • Display exchange rate and calculated converted amount.
    • Allow users to repeat or cancel conversions.
"""

import time
import os

currency = {
    "USD": 1.0,
    "EUR": 0.85,
    "MRC": 10.0,
    "RMB": 6.5,
}


def clear_scrine():
    os.system("cls" if os.name == "nt" else "clear")


def calculate_rate(to_currency, from_currenccy):
    """
    Calculate the exchange rate between two currencies.

    Args:
        to_currency (str): The target currency code (e.g., 'EUR').
        from_currenccy (str): The source currency code (e.g., 'USD').

    Returns:
        float: The exchange rate value representing how many units of
        `to_currency` equal one unit of `from_currenccy`.
    """
    return currency[to_currency] / currency[from_currenccy]


def calculate_converted(to_currency, from_currenccy):
    """
    Convert an entered amount from one currency to another.

    This function uses the global variable `amount_i_have` and multiplies
    it by the exchange rate calculated using `calculate_rate()`.

    Args:
        to_currency (str): The target currency code.
        from_currenccy (str): The source currency code.

    Returns:
        float: The converted currency amount.
    """
    return amount_i_have * calculate_rate(to_currency, from_currenccy)


def intro():
    clear_scrine()
    print("Welcome to *** 'Currency Converter' ***\n")
    print(
        """
    ||====================================================================||
    ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
    ||(100)==================|  Python RESERVE NOTE |================(100)||
    ||\\$//        ~         '------========--------'                \\$//||
    ||<< /        /$\              // ____ \\                         \ >>||
    ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
    ||<<|        \\ //           || <||  >\  ||                        |>>||
    ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
    ||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
    ||>>|  12                     *\\/___\_//*   1989                  |<<||
    ||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
    ||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
    ||(100)===================  ONE HUNDRED DOLLARS =================(100)||
    ||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
    ||====================================================================||
    -------------------------------------------------------------------------------
    """
    )
    for key in currency:
        print(f"{key} : {currency[key]}")


while True:
    intro()
    currency_convert_from = input(
        "Choose a currency to convert from:  "
    ).upper()
    while True:
        amount_i_have = float(input("Enter the amount:  "))
        if (
            input(
                f"\nYou entered {amount_i_have} {currency_convert_from}. Confirm? (y/n):  "
            ).lower()
            == "y"
        ):
            break

    intro()
    currency_convert_to = input("Choose a currency to convert to:  ").upper()
    time.sleep(3)
    print("Analyzing your request ... Please wait.")
    time.sleep(3)
    print(
        f"Checking for {currency_convert_to}'s best rates available ... Please wait."
    )
    time.sleep(2)
    print(
        f"Getting a discount price for {currency_convert_from} ... Please wait.\n\n"
    )
    time.sleep(2)

    if currency_convert_from in currency and currency_convert_to in currency:
        clear_scrine()
        print(
            f"Preparing the deal from {currency_convert_from} to {currency_convert_to}... Please wait."
        )
        time.sleep(3)
        print(
            f"\nExchange rate: 1 {currency_convert_from} = {calculate_rate(currency_convert_to, currency_convert_from)} {currency_convert_to}"
        )
        time.sleep(2)

        print(
            f"\n\n{amount_i_have} {currency_convert_from} is equal to {calculate_converted(currency_convert_to, currency_convert_from):.2f} {currency_convert_to}"
        )
        if input("Do you accept this transaction? y/n:  ").lower() != "y":
            print("Trasaction Canceled.")

        if (
            input("Do you want to performs another conversion? y/n:  ").lower()
            != "y"
        ):
            break
        else:
            continue

    else:
        print("Sorry invalid currency. Convesion canceled..")
        time.sleep(5)
