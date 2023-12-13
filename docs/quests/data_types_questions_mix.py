'''
def question_and_answer() :
    mixed_questions = [
    {
        "question":"",
        "answer": [],
        "correct_index": 0,
        "score": 0
    }
    ]
    return mixed_questions

mixed_questions = question_and_answer()

temp_list = []
pass
for j in range(3) :
    for dict_i in range(len(mixed_questions)) :
        mixed_questions[dict_i]["question"] = input("question: ")
        mixed_questions[dict_i]["answer"] = input("answer : ")
        mixed_questions[dict_i]["correct_index"] = int(input("correct_index : "))
        mixed_questions[dict_i]["score"] = int(input("score : "))
        temp_list.append(mixed_questions)



print(temp_list)
'''


mixed_questions = [
    {
        "question":"",
        "answer": [],
        "correct_index": 0,
        "score": 0
    }
    ]

def question_and_answer():
    input_list = []
    for j in range(3):
        question = input("question: ")
        answer = input("answer: ")
        correct_index = int(input("correct_index: "))
        score = int(input("score: "))

        input_list.append({
            "question": question,
            "answer": answer,
            "correct_index": correct_index,
            "score": score
        })

    return input_list

mixed_questions = question_and_answer()
print(mixed_questions)



# for j in range(3) :
#     pass
#     for dict_i in range(len(mixed_questions)) :
#         pass
#         mixed_questions[dict_i]["question"] = input("question: ")
#         pass
#         mixed_questions[dict_i]["answer"] = input("answer : ")
#         pass
#         mixed_questions[dict_i]["correct_index"] = int(input("correct_index : "))
#         pass
#         mixed_questions[dict_i]["score"] = int(input("score : "))
#         temp_list.append(mixed_questions)
