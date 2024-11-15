# src/controllers/quiz_controller.py
from flask import Blueprint, request, jsonify
from src.services.quiz_service import QuizService

quiz_bp = Blueprint('quiz', __name__, url_prefix='/api/quizzes')


@quiz_bp.route('', methods=['POST'])
def create_quiz():
    service = QuizService()
    data = request.get_json()
    quiz_id = service.create_quiz(data)
    return jsonify({"message": "Quiz created", "quiz_id": quiz_id}), 201


@quiz_bp.route('/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    service = QuizService()
    quiz = service.get_quiz(quiz_id)
    if (quiz):
        return jsonify({"title": quiz.title, "questions": quiz.questions}), 200
    return jsonify({"error": "Quiz Not Found."}), 404


@quiz_bp.route('/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    service = QuizService()
    user_answers = request.json.get('answers')
    score, message = service.evaluate_quiz(quiz_id, user_answers)
    if (score):
        return jsonify({"score": score, "message": message}), 200
    return jsonify({"error": "No Score!"}), 404
