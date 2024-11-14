# tests/test_quiz.py
from unittest.mock import patch, MagicMock
from src.services.quiz_service import QuizService


@patch.object(QuizService, 'create_quiz')
def test_create_quiz(mock_create_quiz, client):
    mock_create_quiz.return_value = 1
    response = client.post(
        '/api/quizzes',
        json={
            "title": "Scariest Monsters",
            "questions": [
                {"text": "spongebob", "answer": "susbob"}
            ]
        }
    )
    assert response.status_code == 201
    assert response.json.get('quiz_id') == 1
    assert mock_create_quiz.called


@patch.object(QuizService, 'get_quiz')
def test_get_quiz(mock_get_quiz, client):
    mock_quiz = MagicMock(
        id=1,
        title="Swag",
        questions=[{
            "text": "AI WIT THE BRAIDS",
            "answer": "no 38!"
        }]
    )
    mock_get_quiz.return_value = mock_quiz
    response = client.get('/api/quizzes/1')
    assert response.status_code == 200
    assert response.json.get('title') == "Swag"
    assert mock_get_quiz.called_once


@patch.object(QuizService, 'evaluate_quiz')
def test_submit_quiz(mock_evaluate_quiz, client):
    mock_evaluate_quiz.return_value = (
        1,
        "Quiz evaluated successfully"
    )
    response = client.post(
        '/api/quizzes/1/submit',
        json={"answers": ["susbob"]}
    )
    assert response.status_code == 200
    assert response.json.get('score') == 1
    assert response.json.get('message') == "Quiz evaluated successfully"
    assert mock_evaluate_quiz.called_once
