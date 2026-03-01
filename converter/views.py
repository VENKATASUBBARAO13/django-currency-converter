from django.shortcuts import render
import requests

def home(request):
    result = None

    if request.method == "POST":
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = request.POST.get('amount')

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        data = requests.get(url).json()

        rate = data['rates'][to_currency]
        result = round(float(amount) * rate, 2)

    return render(request, 'index.html', {'result': result})


def about(request):
    return render(request, 'about.html')