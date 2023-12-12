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

mixed_questions=question_and_answer()

temp_list = []

for j in range(3) :
    for dict_i in range(len(mixed_questions)) :
        mixed_questions[dict_i]["question"] = input("question: ")
        mixed_questions[dict_i]["answer"] = input("answer : ")
        mixed_questions[dict_i]["correct_index"] = int(input("correct_index : "))
        mixed_questions[dict_i]["score"] = int(input("score : "))
        temp_list.append(mixed_questions)


print(temp_list)




