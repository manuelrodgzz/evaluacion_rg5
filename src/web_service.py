import csv
from flask import Flask, jsonify

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def read_csv():
    file_path='data/employees.csv'

    list=[]

    with open(file_path, 'r') as csv_file:
        dic_reader=csv.DictReader(csv_file)
        for dic in dic_reader:
            list.append(dic)


    return jsonify(list)

if (__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0')