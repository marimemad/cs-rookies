if __name__ == '__main__':
    student=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])

    second_lowest=list(set([s for n,s in student ]))
    second_lowest.sort()
    second_lowest=second_lowest[1]
    
    lowest_student=[n for n,s in student if s==second_lowest]
    
    lowest_student.sort()
    lowest_student='\n'.join(lowest_student)
    
    print(lowest_student)
    
