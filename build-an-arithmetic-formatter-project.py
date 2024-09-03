def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    num1 = []
    operator = []
    num2 = []
    answers = []
    for problem in problems:
       
        element = problem.split(" ")
        num1.append(element[0])
        operator.append(element[1])
        num2.append(element[2])

        
    for ope in operator:
       if not ope in ["+", "-"]:
           return "Error: Operator must be '+' or '-'."

    for num in num1 + num2:
        if len(num) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        elif not num.isdigit():
            return 'Error: Numbers must only contain digits.'
  #answer 
    for i in range(len(operator)):
        if operator[i] == "+":
            answers.append(int(num1[i]) + int(num2[i]))
        else:
            answers.append(int(num1[i]) - int(num2[i]))

    
    row1 = ''
    row2 = ''
    dash = ''
    row4 = ''
    space_width = []
    for i in range(len(num1)):
        width = max(len(num1[i]), len(num2[i])) + 2
        space_width.append(width)
        
        row1 += num1[i].rjust(width)
        row2 += operator[i] + num2[i].rjust(width - 1)
        dash += "-" * width

        if show_answers:
            row4 += str(answers[i]).rjust(width)


        if i < len(num1) - 1:
            row1 += " " * 4
            row2 += " " * 4
            dash += " " * 4
            if show_answers:
             row4 += " " * 4
        
    if show_answers:
     return f"{row1}\n{row2}\n{dash}\n{row4}"
    else: 
     return f"{row1}\n{row2}\n{dash}"
    
  
    
    


   
   
#print(f'{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], True)}')


