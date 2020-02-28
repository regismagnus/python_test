names = []
assignments = []
grades = []

put_name = True
while(put_name):
    names.append(input("Preencha um nome: "))
    
    put_name = input("Continuar colocando nomes? ").lower() == "y"
    
for name in names:
    assignments.append(int(input("Assigments {}: ".format(name))))
    grades.append(float(input("Grade {}: ".format(name))))
        
# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, 0))