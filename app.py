from quastion import Question
question_prompts = [
    "Какого цвета яблоки? /n (a)Зелёные /n (b) Красные /n/n"
]
    
questions = [
    Question(question_prompts[0], "a")
]

def run_Test(questions):
    score = 0
    for question in questions :
        otvet = input(question.vopros)
        if otvet == question.otvet:
            score += 1
    print("Правильных ответов " + str(score) + " из " + str(len(questions)) + " верны! ")



run_Test (questions)    
    
