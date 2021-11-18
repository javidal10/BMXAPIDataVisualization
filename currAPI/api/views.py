from django.shortcuts import render
from datetime import date,timedelta
import numpy as np
import requests
import json
from requests.api import get

from requests.models import HTTPError
# Create your views here.

def get_dates(request):
    """Request user to enter desired dates"""

    yest = date.today()-timedelta(1)
    context = {
        'date': yest.isoformat(),
    }
    return render(request,'api/info.html',context)

base = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/'
headers = {'bmx-token':'946afc3e778367dd3d2e678c632fe64b196d3b305de85b1f33f373192c9b9712'}


def home(request):
    """View UDIS and USD avergage. max value & min value for requested dates"""

    indate = request.GET['start_date']
    endate = request.GET['end_date']
    print(indate)
    print(endate)
    url = base + f'SP68257/datos/{indate}/{endate}'
    url_usd = base + f'SF63528/datos/{indate}/{endate}'

    try:
        response1 = requests.get(url,headers=headers)
        response2 = requests.get(url_usd,headers=headers)
        print(response1.status_code)
        print(response2.status_code)
        if response1.status_code == 200 and response2.status_code == 200:
            data = json.loads(response1.text)
            usd_data = json.loads(response2.text)
            context = data['bmx']['series']
            cont_data = usd_data['bmx']['series']
            
    except:
        raise HTTPError('unable to connect to API of BMX')

    elems = []
    usdp = []

    for i in context:
        for v in i['datos']:
            elems.append(v['dato'])

    for i in cont_data:
        for v in i['datos']:
            usdp.append(v['dato'])
    

    arr = np.array(elems).astype(np.float)
    maxv = np.amax(arr)
    avg = np.mean(arr)
    minv = np.amin(arr)
    usdarr = np.array(usdp).astype(np.float)
    maxd = np.amax(usdarr)
    avgd = np.mean(usdarr)
    mind = np.amin(usdarr)

    context = {
        'dat': json.dumps(context[0]['datos']),
        'max': maxv,
        'avg': avg,
        'min': minv,
        'usdat': json.dumps(cont_data[0]['datos']),
        'maxd': maxd,
        'avgd': avgd,
        'mind': mind,
    }
    return render(request,'api/home.html',context)

