from flask import Blueprint
from flask import current_app as app
from flask import render_template
from .. import mysql

# Blueprint Configuration
view_bp = Blueprint(
    'view_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@view_bp.route('/view/<int:team_id>', methods=['GET'])
def record_view(team_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM mlbteams.mlbteams2012 WHERE id=%s', team_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', team=result[0])
