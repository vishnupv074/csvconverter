import urllib.request
import json
import csv
from django.http import HttpResponse


def csv_view(request, id=None):
    if id:
        search = "http://receitaws.com.br/v1/cnpj/"+str(id)
    else:
        search = "http://receitaws.com.br/v1/cnpj/71021091000190"

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Search Results.csv"'
    writer = csv.writer(response)
    # response = HttpResponse("success")

    with urllib.request.urlopen(search) as url:
        data = json.loads(url.read().decode())
        if data is not None:
            writer.writerow(data.keys())
            writer.writerow(data.values())
    return response
