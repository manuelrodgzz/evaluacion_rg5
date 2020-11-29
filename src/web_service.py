import csv
from flask import Flask, jsonify

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def read_csv():

    #Path to csv file
    file_path='data/employees.csv'

    #List of employees
    list=[]

    try:
        with open(file_path, 'r') as csv_file:

            #Get employees in a dictionary
            dic_reader=csv.DictReader(csv_file)

            #Push each employee to list
            for employee in dic_reader:
                list.append(employee)


        return jsonify(list)

    #Handle error
    except EnvironmentError:
        return({
            'error': True,
            'message': 'Oops! .csv file could not be found'
        })

if (__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0')