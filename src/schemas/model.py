import google.generativeai as genai

new_quiz = genai.protos.Schema(
    type=genai.protos.Type.OBJECT,
    properties={
        'subject_name': genai.protos.Schema(
            type=genai.protos.Type.ARRAY,
            items=genai.protos.Schema(type=genai.protos.Type.STRING)
        ),
        'questions': genai.protos.Schema(
            type=genai.protos.Type.ARRAY,
            items=genai.protos.Schema(type=genai.protos.Type.STRING)
        ),
        'options': genai.protos.Schema(
            type=genai.protos.Type.ARRAY,
            items=genai.protos.Schema(
                type=genai.protos.Type.ARRAY,
                items=genai.protos.Schema(type=genai.protos.Type.STRING)
            )
        ),
        'answer': genai.protos.Schema(
            type=genai.protos.Type.ARRAY,
            items=genai.protos.Schema(type=genai.protos.Type.INTEGER)
        )
    },
    required=['subject_name', 'questions', 'options', 'answer']
)

generate_subject_quiz = genai.protos.FunctionDeclaration(
    name="generate_subject_quiz",
    description="Generates a new quiz based on some subject and given topic and topic content",
    parameters=new_quiz
)

generate_new_quiz = genai.protos.FunctionDeclaration(
    name="generate_new_quiz",
    description="Generates quizzes for subjects and topics mentioned",
    parameters=new_quiz
)
