from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    # 注册蓝图
    # CORS(app, supports_credentials=True)
    # CORS(app, resources=r'/*')
    from .login import login as login_blueprint  # 这是必须的，需要在这里导入，有关于包导入顺序的问题 要在db之后导入
    from .blast import blast as blast_blueprint
    app.register_blueprint(login_blueprint, url_prefix='/login')
    app.register_blueprint(blast_blueprint, url_prefix='/blast')

    return app