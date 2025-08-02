student_data = ("Hariom", "cse", 2025)

#Convert tuple to list
 
temp_list= list(student_data)

#Modify the list
temp_list[0] = "Aish"
temp_list.append("Aishu")

#  Convert list back to tuple
updated_tuple = tuple(temp_list)

print("Original tuple:", student_data)
print("Modified tuple:", updated_tuple)




#9.concatenate two tuples
frontend_skills = ("HTML", "CSS", "JavaScript")
backend_skills = ("Python", "Django")
full_stack_skills = frontend_skills + backend_skills
print("Full stack skills:", full_stack_skills)


#10 repeat a tuple 3 times


greeting = ("Hari", )
repeated_greeting = greeting * 3
print("Repeated 3 times:", repeated_greeting)



