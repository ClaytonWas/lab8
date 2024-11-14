# src/services/quiz_service.py
from src.models.quiz_model import QuizModel


class QuizService:
    def create_quiz(self, quiz_data):
        title = quiz_data["title"]
        questions = quiz_data["questions"]
        newQuiz = QuizModel(title, questions)
        newQuiz.save()
        return newQuiz.id


    def get_quiz(self, quiz_id):
        return QuizModel.get_quiz(quiz_id)
    

    def evaluate_quiz(self, quiz_id, user_answers):
        quiz = QuizModel.get_quiz(quiz_id)
        if(quiz == None): return quiz, "Quiz Not Found"
        score = 0
        for (answer, question) in zip(user_answers, quiz.questions):
            if (answer == question['answer']):
                score += 1
        return score
