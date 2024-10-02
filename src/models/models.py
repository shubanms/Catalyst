import os
import json
import google.generativeai as genai

from src.schemas.quiz import TopicQuizParams
from src.schemas.model import generate_subject_quiz, generate_new_quiz

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
            model_name="gemini-1.5-flash",
            tools = [generate_subject_quiz, generate_new_quiz],
        )
        
    def generate_quiz(self, quiz_params: TopicQuizParams):
        """
            Generates a quiz for a new user on some selected subjects
        """
        
        prompt = f"""
        I am a intermediate in the subject {quiz_params.subject} and i want to learn more,
        so can you me {quiz_params.number_of_questions} question from the subject on the topic {quiz_params.topic}
        
        Give me 4 options and keep one of them as the right answer
        """
        
        result = self.model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=1,
                top_p=0.95,
                top_k=64,
            ),
            
            tool_config={'function_calling_config':'ANY'}
        )
        
        
        response = result.candidates[0].content.parts[0].function_call
        
        quiz = json.loads(json.dumps(type(response).to_dict(response), indent=4))['args']
        
        return quiz
        

    def generate_topic_quiz(self, quiz_params: TopicQuizParams):
        """
            Generates a quiz for a particular subject and topic for a user
        """
        
        prompt = f"""
        Generate a {quiz_params.number_of_questions} question quiz for the subject {quiz_params.subject},
        on the topic {quiz_params.topic} and the topic content {quiz_params.topic_content}
        
        - Each question should have 4 options and should only have 1 correct option, shuffle the correct answers position
        """
        
        result = self.model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=1,
                top_p=0.95,
                top_k=64,
            ),
            
            tool_config={'function_calling_config':'ANY'}
        )
        
        response = result.candidates[0].content.parts[0].function_call
        
        quiz = json.loads(json.dumps(type(response).to_dict(response), indent=4))['args']
        
        return quiz
