import urllib.request  # for getting the json data from web
import json
import csv
from django.http import HttpResponse


def csv_view(request, id=None):  # function for converting json to csv file
    if id:
        search = "http://receitaws.com.br/v1/cnpj/"+str(id)
    else:
        search = "http://receitaws.com.br/v1/cnpj/71021091000190"

    response = HttpResponse(content_type='text/csv')  # Returns the csv file created
    response['Content-Disposition'] = 'attachment; filename="Search Results.csv"'
    writer = csv.writer(response)  # Creating the csv writer object
    # response = HttpResponse("success")

    with urllib.request.urlopen(search) as url:
        data = json.loads(url.read().decode())
        if data is not None:
            writer.writerow(data.keys())  # Writing header
            writer.writerow(data.values())  # Writing values
    return response
