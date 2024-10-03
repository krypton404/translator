from flask import request, jsonify, Blueprint
from app.services.translation_service import translate_text

router = Blueprint("translation", __name__)

@router.route("/translate", methods=["POST"])
def translate():
    # Print the incoming request for debugging purposes
    print("Incoming request:", request.data)

    # Attempt to parse the incoming JSON data
    try:
        data = request.get_json(force=True)  # Force=True ensures a 400 error is raised for invalid JSON
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return jsonify({"error": "Invalid JSON format"}), 400

    # Extract the necessary data from the JSON payload
    text = data.get("text")
    source_language = data.get("source_language")
    target_language = data.get("target_language")

    # Basic validation for required fields
    if not text or not source_language or not target_language:
        return jsonify({"error": "Missing required fields"}), 400

    # Use the translation service to get the translation result
    response = translate_text(text, source_language, target_language)
    
    # Return the translation result as a JSON response
    return jsonify(response)

@router.route("/test", methods=["GET"])
def testapi():
    print("Test endpoint hit")
    return jsonify({"success": "nice"})
