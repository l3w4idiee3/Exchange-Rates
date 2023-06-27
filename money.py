import requests

print("Welcome to our Exchange Rate Site! We're excited to have you join us on this journey of exploring international currencies and making informed financial decisions. Enjoy your stay and feel free to dive into the world of exchange rates!")
def user_prompt():
    money = float(input("Enter the amount you want to be converted: "))
    source_currency = float(input("Please enter the source currency: "))
    target_currency = float(input("Enter the currency you want to exchange to: "))
def ApiRequests(request):
    source_currency = "KES"
    target_currency = "USD"
    request_url = "https://api.apilayer.com/exchangerates/latest?access_key=c8be12fdd1b2e455cb535031"
    response = request.get(request_url)
    if response.status_code == 200:
        data = response.json()
        if 'rate' in data:
            conversion_rate = data['rate']
            print(f"The conversion rate from {source_currency} to {target_currency} is: {conversion_rate}")
        else:
            print("Error: Conversion rate not available.")
    else:
        print("Error: Failed to retrieve the conversion rate.")
def calcultionOfMoney():
    return (money * conversion_rate)/source_currency
def displayConversion():
    result = f"{calcultionOfMoney()} USD"
print("Thank for using our system if u were not satisfied inform us so that we can improve !!!")
user_prompt()
ApiRequests(request)
displayConversion()
