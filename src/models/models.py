import os
import json
import google.generativeai as genai

from typing import List

from src.schemas.schemas import NewQuiz, NewQuizParams

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 0.3,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

class Model:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash"
        )
    
    def generate_quiz(self, quiz_params: NewQuizParams):
        prompt = f"""
        Generate a MCQ type quiz for the following subjects {quiz_params.subjects},
        - Each subject in the list should have 5 questions
        - Each question should have 4 options and 1 correct option
        - Create the quiz based on the difficulty rating for each subject {quiz_params.rating} (out of 5).

        Output the quiz in JSON format: 
        [
            {{
                "subject_name": {{
                    "questions": "A list of questions",
                    "options": "Nested list of options for each question",
                    "answer": "The correct answers index for each question" 
                }},
            }},
            ...
        ]
        """

        result = self.model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.3,
                top_p=0.95,
                top_k=64,
                response_mime_type="application/json",
            ),
        )

        data = json.loads(result.text)
    
        quizzes = [NewQuiz(**item) for item in data]
        
        return quizzes
