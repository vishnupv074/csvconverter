# Json to CSV converter
This will return a csv file created from given json.

# Installation

To install this in local server after downloading and extracting the repo.

1. Create a python 3.7 virtualenv and activate
2. Then run
    ```commandline
   cd csvconverter
   pip install -r requirements.txt
    ```
## Running the local server

 ```commandline
   python manage.py runserver
 ```
### Using app

You can use this app two ways.

1. Simply calling 127.0.0.1:8000/ will return the csv having the 
json in the link http://receitaws.com.br/v1/cnpj/71021091000190

2. You can pass the "Id" with the url to convert another json having id
instead of 71021091000190. eg. 127.0.0.1:8000/7102109111111.

3. You can import csv file containing ids then it fill return the csv file containing all the datas from url have that id.
