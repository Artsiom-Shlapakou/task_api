from quiz.models import QuizResult


def count_right_answer():
    pass

def count_wrong_answer():
    pass

def count_mark():
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