from flask import Flask, jsonify, abort
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/database/city_count', methods=['GET'])
def count_source():
    sources = []
    qry = "SELECT city_name, count(*) FROM crunch group by city_name"
    con = sqlite3.connect('/home/kumaraman/pipeline/crunchbase.sqlite')
    c = con.cursor()
    c.execute(qry)
    rows = c.fetchall()
    for row in rows:
        sources.append(row)
    c.close()
    if len(row) == 0:
        abort(404)
    return jsonify({'source_count': sources[0]})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
