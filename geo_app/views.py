from django.shortcuts import render
from django.contrib import messages 


from .forms import AddressForm

import requests  
import json 


# home view 
def HomeView(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data("ip_address")
            try:
                url = 'http://ip-api.com/batch'
                address = [ip]
                res = requests.post(url, json=address)
                res_data = json.dumpe(res.json())
                json_data = json.loads(res_data)

                context = {
                    "query": json_data[0]["query"],
                    "country":json_data[0]["country"],
                    "country_code":json_data[0]["CountryCode"],
                    "region":json_data[0]["region"],
                    "region_name":json_data[0]["regionName"],
                    "city":json_data[0]["city"],
                    "zip":json_data[0]["zip"],
                    "lat":json_data[0]["lat"],
                    "lon":json_data[0]["lon"],
                    "timezone":json_data[0]["timezone"],
                    "isp":json_data[0]["isp"],
                    "isp_org":json_data[0]["org"],
                    "isp_ass":json_data[0]["as"]
                }
                return render(request, "home.html", context=context)
            except:
                messages.error(request, "unable to get IP info")
            
        else:
            messages.error(request, "Please provide a valid input")
    else:
        form = AddressForm()
        return render(request, "home.html", {"form":form})
        
