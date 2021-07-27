from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'mlbteams'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'MLB Team Wins for 2012'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM mlbteams.mlbteams2012 order by team')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, teams=result)


@app.route('/view/<int:team_id>', methods=['GET'])
def record_view(team_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM mlbteams.mlbteams2012 WHERE id=%s', team_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', team=result[0])


@app.route('/edit/<int:team_id>', methods=['GET'])
def form_edit_get(team_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM mlbteams.mlbteams2012 WHERE id=%s', team_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', team=result[0])


@app.route('/edit/<int:team_id>', methods=['POST'])
def form_update_post(team_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Team'), request.form.get('Payroll_millions'), request.form.get('Wins'), team_id)
    sql_update_query = """UPDATE mlbteams.mlbteams2012 SET Team = %s, Payroll_millions = %s, Wins = %s WHERE id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/team/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Team Form')


@app.route('/team/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Team'), request.form.get('Payroll_millions'), request.form.get('Wins'))
    sql_insert_query = """INSERT INTO mlbteams.mlbteams2012 (Team,Payroll_millions,Wins) VALUES (%s, %s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:team_id>', methods=['POST'])
def form_delete_post(team_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM mlbteams.mlbteams2012 WHERE id = %s """
    cursor.execute(sql_delete_query, team_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/team', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM mlbteams.mlbteams2012')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/team/<int:team_id>', methods=['GET'])
def api_retrieve(team_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM mlbteams.mlbteams2012 WHERE id=%s', team_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/team/new', methods=['POST'])
def api_add() -> str:
    content = request.json
    #app.logger.info('content')
    #app.logger.info(content)
    cursor = mysql.get_db().cursor()
    inputData = (content['Team'], content['Payroll_millions'], content['Wins'])
    sql_insert_query = """INSERT INTO mlbteams.mlbteams2012 (Team,Payroll_millions,Wins) VALUES (%s, %s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/team/<int:team_id>', methods=['PUT'])
def api_edit(team_id):
    content = request.json

    cursor = mysql.get_db().cursor()
    inputData = (content['Team'], content['Payroll_millions'], content['Wins'], team_id)
    sql_update_query = """UPDATE mlbteams.mlbteams2012 SET Team = %s, Payroll_millions = %s, Wins = %s WHERE id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()

    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/team/<int:team_id>', methods=['DELETE'])
def api_delete(team_id) -> str:
    content = request.json

    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM mlbteams.mlbteams2012 WHERE id = %s """
    cursor.execute(sql_delete_query, team_id)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
