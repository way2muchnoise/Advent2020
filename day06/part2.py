def count_questions(question_lines):
    questions = []
    for line in question_lines:
        questions.append(set([char for char in line[:-1]]))
    return len(questions[0].intersection(*questions))


total_questions = 0
with open('input.txt', 'r') as f:
    line = f.readline()
    question_lines = []
    while line:
        if line == "\n" or line == '':
            total_questions += count_questions(question_lines)
            question_lines = []
        else:
            question_lines.append(line)
        line = f.readline()
    total_questions += count_questions(question_lines)
print(total_questions)
