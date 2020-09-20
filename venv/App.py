from Question import Question

question_prompts = [
    "The most electronegative element among the following is?\n(a) sodium\n(b)fluorine \n(c)Oxygen\n\n" ,
    "The most commonly used bleaching agent is?\n(a) alcohol\n(b) CO2\n(c)chlorine\n\n" ,
    "The ore which is found in abundance in India is?\n(a) monazite\n(b) bauxite\n(c) magnetite\n\n" ,

]
questions = [
    Question(question_prompts[0], "b") ,
    Question(question_prompts[1], "c") ,
    Question(question_prompts[2], "a") ,

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct" )

run_test(questions)


