import requests

print("Welcome to our Exchange Rate Site! We're excited to have you join us on this journey of exploring international currencies and making informed financial decisions. Enjoy your stay and feel free to dive into the world of exchange rates!")
def user_prompt():
    money = float(input("Enter the amount you want to be converted: "))
    source_currency = float(input("Please enter the source currency: "))
    target_currency = float(input("Enter the currency you want to exchange to: "))

    source_currency = "KES"
    target_currency = "USD"
    request_url = "https://api.apilayer.com/exchangerates/latest?access_key=c8be12fdd1b2e455cb535031"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        if 'rates' in data:
            conversion_rates = data['rates']
            if target_currency in conversion_rates:
                conversion_rate = conversion_rates[target_currency]
                print(f"The conversion rate from {source_currency} to {target_currency} is: {conversion_rate}")
                return money, conversion_rate
            else:
                print("Error: Target currency not found.")
        else:
            print("Error: Conversion rates not available.")
    else:
        print("Error: Failed to retrieve the conversion rates.")
    
    return None, None
def calculate_conversion(money, conversion_rate):
    if money is not None and conversion_rate is not None:
        return money * conversion_rate
    else:
        return None
def display_conversion(converted_amount, target_currency):
    if converted_amount is not None:
        print(f"The converted amount is: {converted_amount} {target_currency}")
    else:
        print("Error: Failed to calculate the converted amount.")
print("Thank for using our system if u were not satisfied inform us so that we can improve !!!")
money, conversion_rate = user_prompt()
converted_amount = calculate_conversion(money, conversion_rate)
display_conversion(converted_amount, "USD")