from flask import Flask
from .config import get_settings


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB upload limit
    settings = get_settings()
    app.secret_key = settings.secret_key

    from .routes import main
    app.register_blueprint(main)
    return app
