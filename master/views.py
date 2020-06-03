import urllib.request  # for getting the json data from web
import json
import csv
from django.http import HttpResponse
from django.shortcuts import render


def csv_view(request, id=None):  # function for converting json to csv file
    response = ""
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Not a CSV file")
        else:
            data_set = csv_file.read().decode('UTF-8')
            response = HttpResponse(content_type='text/csv')  # Returns the csv file created
            response['Content-Disposition'] = 'attachment; filename="Search Results.csv"'
            writer = csv.writer(response)  # Creating the csv writer object
            # data_set = json.loads(csv_file)
            ds = data_set.split('\n')
            count = 0
            for d in ds[1:len(ds)-1]:
                search = "http://receitaws.com.br/v1/cnpj/" + str(d)
                try:
                    with urllib.request.urlopen(search) as url:
                        data = json.loads(url.read().decode())
                        if data is not None and count == 0:
                            writer.writerow(data.keys())  # Writing header
                            count += 1
                        if data is not None and count != 0:
                            writer.writerow(data.values())  # Writing values

                except:
                    return HttpResponse("Url Not found")

            return response


    else:

        if id == 'file':
            search = 'master/71021091000190.json'
        elif id:
            search = "http://receitaws.com.br/v1/cnpj/"+str(id)
        else:
            search = "http://receitaws.com.br/v1/cnpj/71021091000190"

        response = HttpResponse(content_type='text/csv')  # Returns the csv file created
        response['Content-Disposition'] = 'attachment; filename="Search Results.csv"'
        writer = csv.writer(response)  # Creating the csv writer object
        # response = HttpResponse("success")
        if id == 'file':
            file = open(search)
            data = json.load(file)
            if data is not None:
                writer.writerow(data.keys())  # Writing header
                writer.writerow(data.values())  # Writing values



        else:
            try:
                with urllib.request.urlopen(search) as url:
                    data = json.loads(url.read().decode())
                    if data is not None:
                        writer.writerow(data.keys())  # Writing header
                        writer.writerow(data.values())  # Writing values

                return response

            except:
                return HttpResponse("Url Not found")

    return render(request, 'index.html', {response:response})
