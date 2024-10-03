from flask import Flask
from app.api.v1.endpoints.translation import router as translation_router

# Create Flask app instance
app = Flask(__name__)

# Register the translation router (assuming it's a Blueprint)
app.register_blueprint(translation_router, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
