from flask import *
from requests import *

bp = Blueprint('views',__name__, url_prefix='/')

# @bp.route('/index.html')
# @bp.route('/index')
# @bp.route('/inicio')
@bp.route('/', methods=['GET','POST'])
def index():
    return render_template('webapp/index.html')