from Question import Question

qp = [
    "Do you like A?\n(a)aaa\n(b)gfsgfsg\n(c)dgdg\n\n",
    "How about B?\n(a)dfafd\n(b)bbb\n(c)dgdg\n\n",
    "This must be C?\n(a)dfafd\n(b)gfsgfsg\n(c)ccc\n\n"
]

questions = [
    Question(qp[0], "a"),
    Question(qp[1], "b"),
    Question(qp[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        print("\n")
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))


run_test(questions)