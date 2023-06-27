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
    