def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dashes = []
    answers = []
    
    for problem in problems:
        parts = problem.split()
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        operand1, operator, operand2 = parts
        width = max(len(operand1), len(operand2)) + 2
        
        first_line.append(operand1.rjust(width))
        second_line.append(operator + " " + operand2.rjust(width - 2))
        dashes.append("-" * width)
        
        if show_answers:
            answer = str(eval(problem))
            answers.append(answer.rjust(width))
    
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dashes)
    if show_answers:
        arranged_problems += "\n" + "    ".join(answers)
    
    return arranged_problems
