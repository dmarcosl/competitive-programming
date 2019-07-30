if __name__ == '__main__':

    grades = dict()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if not grades.get(score):
            grades[score] = list()
        grades[score].append(name)

    scores = list(grades.keys())
    scores.sort()
    
    names = grades.get(scores[1])
    names.sort()

    print('\n'.join(names))

