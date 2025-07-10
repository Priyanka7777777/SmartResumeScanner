from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.models.user import User, db
from app.routes import auth_routes, resume_routes
from app.models.job import Job  # ✅ Add this
from app.routes import admin_routes  # ✅ Add this

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config.Config')
    
    # Initialize extensions
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(resume_routes.resume_bp)
    app.register_blueprint(admin_routes.admin_bp)

    return app
