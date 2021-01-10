from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "dbdaaf3cb6msh7bf50ee8d2e174dp150852jsn2e3b66c3decc",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()
#print(response.text)

def covidview(request):
    list1 =[]
    num_results = int(response['results'])
    for x in range(0, num_results):
        list1.append(response['response'][x]['country'])
    
    if request.method == "POST" :# gets executed if post request
        selcountry = request.POST['selcountry']
        print(selcountry)
        #everything is correct till here

        for x in range(0, num_results):
            if selcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new'] # errror in this line figure it out
                active = response['response'][x]['cases']['active']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                critical = response['response'][x]['cases']['critical']
                deaths = int(total) - int(active) - int(recovered)
                #print(response['response'][x]['cases'])

        context = {'list1': list1,'selcountry':selcountry,'new': new,'active':active, 'critical': critical,'recovered': recovered, 'total': total, 'deaths': deaths}
        return render(request,'covid.html',context)

    #else this gets executed
    context = {'list1': list1 }
    return render(request,'covid.html',context)

#def style(request):
#    return render(request,'covid.css',) 