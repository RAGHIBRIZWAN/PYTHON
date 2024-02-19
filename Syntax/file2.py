
stud = ["ram" , "Sham" , "Kishan" ,"Radha", "Radhika"]

for student in stud:
    if student == "Radha": #name stops on kishan
        break;
    print(student)

for student in stud:
    if student == "Kishan":
        continue; #kishan will be removed from list
    print(student)
