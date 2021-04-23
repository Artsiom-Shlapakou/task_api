from quiz.models import QuizResult, Quiz, Question


def get_count_questions(id_quiz):
    questions = Question.objects.filter(quiz=id_quiz).count()
    return questions

def get_count_right_answer():
# SELECT COUNT(tb_right.is_right) as right, (SUM(tb_right.score))as total
# FROM (SELECT * FROM public.quiz_answer as t1 
# inner join public.quiz_question as t2 
# ON t1.question_id = t2.id
# where is_right = 'true' and quiz_id = 1) as tb_right;
    pass

def get_count_wrong_answer():
    pass

def get_count_mark():
    pass
    # try:
    #     results = Results.objects.filter(exam_name=name)
    # except Results.DoesNotExist:
    #     return 0

    # num_of_students = len(results)
    # marks = 0

    # for result in results:
    #     marks += result.total_marks
    # if marks > 0:
    #     average = marks/num_of_students
    # else:
    #     average = 0
    # return average