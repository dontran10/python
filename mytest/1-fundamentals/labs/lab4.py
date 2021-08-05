def find_student_average_mark(students, query_name):
    result = None
    # TODO: Enjoy your solving here
    student = next((x for x in students if x[0] == query_name), [None])
    if student != None:
        return "{:.2f}".format((float(student[1]) + float(student[2]) + float(student[3]))/3)
    return result


if __name__ == '__main__':
    students = []
    query_name = None
    # TODO: Collect input information from console
    N = int(input("Enter numer of students:"))
    if (N <= 2) or (N > 10):
        print('Invalid number 2 < N <= 10')
    else:
        for i in range(N):
            strtext = str(input("Student " + str(i) + ": "))
            student = strtext.split(' ')
            students.append(student)
        query_name = str(input("Query name:"))
        print(find_student_average_mark(students, query_name))
