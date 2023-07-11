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
            ip = form.cleaned_data["ip_address"]
            try:
                url = 'http://ip-api.com/batch'
                address = [ip]
                res = requests.post(url, json=address)
                res_data = json.dumps(res.json())
                json_data = json.loads(res_data)


                query = json_data[0]["query"]
                country = json_data[0]["country"]
                country_code =json_data[0]["countryCode"]
                region = json_data[0]["region"]
                region_name = json_data[0]["regionName"]
                city = json_data[0]["city"]
                zip_code = json_data[0]["zip"]
                lat = json_data[0]["lat"]
                lon = json_data[0]["lon"]
                timezone = json_data[0]["timezone"]
                isp = json_data[0]["isp"]
                isp_org = json_data[0]["org"]
                isp_ass = json_data[0]["as"]
                


                data = {
                    "query":query,
                    "country":country,
                    "country_code":country_code,
                    "region":region,
                    "region_name":region_name,
                    "city":city,
                    "zip_code":zip_code,
                    "lat":lat,
                    "lon":lon,
                    "timezone":timezone,
                    "isp":isp,
                    "isp_org":isp_org,
                    "isp_ass":isp_ass
                }
                return render(request, "home.html", {"data":data, "form":form})
            
            except:
                messages.error(request, "unable to get IP info")

            # return render(request, "home.html", data)
            
        else:
            messages.error(request, "Please provide a valid input")
    else:
        form = AddressForm()
    return render(request, "home.html", {"form":form})
        
