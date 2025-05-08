# -*- coding: utf-8 -*-
import json

def calcolo_media(gradeslist):
    sum = 0
    for numb in gradeslist:
        sum += numb 
    Average_Grade = sum  / len(gradeslist)
    Average_Grade = round(Average_Grade, 2)
    return Average_Grade

def media_studente(stud_code, dbsize):
    gradeslist = []
    filepath=str(dbsize)+"_exams.json"
    with open (filepath, 'r') as file:
        file_contents_str = file.read()
    student_grades = json.loads(file_contents_str)
    for element in student_grades:
       if str(stud_code) in element["stud_code"]:
           gradeslist.append(element["grade"])
    
    return calcolo_media(gradeslist)
    
               
def media_corso(course_code, dbsize):
    gradeslist = []
    filepath=str(dbsize)+"_exams.json"
    with open (filepath, 'r') as file:
        file_contents_str = file.read()
    student_grades = json.loads(file_contents_str)
    for element in student_grades:
       if course_code in element["course_code"]:
           gradeslist.append(element["grade"])
           
    return calcolo_media(gradeslist)
           

def media_docente(teach_code, dbsize):
    courseslist = []
    gradeslist = []
    filepath=str(dbsize)+"_courses.json"
    filepath1=str(dbsize)+"_exams.json"
    with open (filepath, 'r') as file:
        file_contents_str = file.read()
    Teacher_Courses_List = json.loads(file_contents_str)
    for element in Teacher_Courses_List:
        if str(teach_code) in element["teach_code"]:
            courseslist.append(element["course_code"])       
    with open (filepath1, 'r') as file:
        file_contents_str = file.read()
    Teacher_Grades_List = json.loads(file_contents_str)
    for obj in Teacher_Grades_List:
        for item in courseslist:
            if item in obj["course_code"]:
                gradeslist.append(obj["grade"])
    
    return calcolo_media(gradeslist)

    
def studenti_brillanti(dbsize):
    smart_students_list = []
    smart_students_average_grade = []
    smart_students_names_surnames = []
    all_students_list=[]
    output_list = []
    sorted_smart_students_list= []
    filepath=str(dbsize)+"_exams.json"
    filepath1 = str(dbsize)+"_students.json"
    with open (filepath, 'r') as file:
        file_contents_str = file.read()
    with open (filepath1, 'r') as text:
        file_contents_str1 = text.read()
    students_surname_name = json.loads(file_contents_str1)
    student_grades = json.loads(file_contents_str)
    for local_dic in student_grades:
        if local_dic["stud_code"] in  all_students_list:
            pass
        else:
            all_students_list.append(local_dic["stud_code"])
    for student in all_students_list:
        average_grade = media_studente(student, dbsize)
        if average_grade >= 28:
            smart_students_average_grade.append(average_grade)
            smart_students_list.append(student)
    for good_student in smart_students_list:
        for local_dic in students_surname_name:
            if good_student in local_dic["stud_code"]:
                smart_students_names_surnames.append(str(local_dic["stud_surname"]+" "+local_dic["stud_name"]))
    exams = list(zip(smart_students_names_surnames, smart_students_average_grade, smart_students_list))
    
    sorted_smart_students_list =sorted(exams, key=lambda x: (-x[1], x[0], x[2]))
    for student_code in sorted_smart_students_list :
        output_list.append(student_code[2])


    return output_list
                     
     
def stampa_verbale(exam_code, dbsize, fileout):
   filepath=str(dbsize)+"_exams.json"
   with open(filepath, 'r') as file:
       file_contents_str = file.read()
   filepath1=str(dbsize)+"_students.json"
   with open(filepath1, 'r') as file:
       file_contents_str1 = file.read()
   filepath2=str(dbsize)+"_teachers.json"
   with open(filepath2, 'r') as file:
       file_contents_str2 = file.read()
   filepath3=str(dbsize)+ "_courses.json"
   with open(filepath3, 'r') as file:
       file_contents_str3 = file.read()   
   exams_data = json.loads(file_contents_str)
   students_datas = json.loads(file_contents_str1)
   teachers_datas = json.loads(file_contents_str2) 
   courses_datas = json.loads(file_contents_str3)
   for local_dic in exams_data:
        if exam_code == local_dic["exam_code"]:
            date = local_dic["date"]
            grade = local_dic["grade"]
            stud_code = local_dic["stud_code"]
            course_code = local_dic["course_code"]
    

   for local_dic in students_datas:
       if stud_code in local_dic ["stud_code"]:
           stud_surname = local_dic["stud_surname"]
           stud_name = local_dic["stud_name"]

   for local_dic in courses_datas:
         if course_code in local_dic["course_code"]:
             course_name = local_dic["course_name"]
             teach_code = local_dic["teach_code"]

   for local_dic in teachers_datas:
         if teach_code in local_dic["teach_code"]:
             teach_surname = local_dic["teach_surname"]
             teach_name = local_dic["teach_name"]
             
   text_out = "Lo studente "+stud_name+" "+stud_surname+", matricola "+str(stud_code)+", ha sostenuto in data "+str(date)+" l'esame di "+course_name+" con il docente "+teach_name+" "+teach_surname+" con votazione "+str(grade)+"."
   with open(fileout, "w") as index:
        index.write(text_out)
      
   return grade


def stampa_esami_sostenuti(stud_code, dbsize, fileout):
    courses_names = []
    course_code = ""
    exams_dates = []
    exams_grades = []
    stud_name = ""
    stud_surname = ""
    max_name_lenght = 0
    total_row = 0
    filepath1= str(dbsize)+"_exams.json"
    filepath = str(dbsize)+"_students.json"
    with open(filepath, 'r') as file:
        file_contents_str = file.read()
    with open(filepath1, 'r') as text:
        file_contents_str1 = text.read()
    students_surname_name = json.loads(file_contents_str)
    student_exams = json.loads(file_contents_str1)
    filepath3=str(dbsize)+ "_courses.json"
    with open(filepath3, 'r',encoding="utf-8") as file:
        file_contents_str3 = file.read() 
    courses_datas = json.loads(file_contents_str3)
    for local_dic in student_exams:
        if local_dic["stud_code"] in stud_code:
            exams_dates.append(local_dic["date"])
            exams_grades.append(local_dic["grade"])
            course_code = local_dic["course_code"]
            for dic in courses_datas:
                if course_code in dic["course_code"]:
                    courses_names.append(dic["course_name"])
    for local_dictionary in students_surname_name:
        if stud_code in local_dictionary["stud_code"]:
           stud_surname = local_dictionary["stud_surname"]
           stud_name = local_dictionary["stud_name"]
    
    exams_datas_tuple_list = list(zip(courses_names, exams_dates,exams_grades))
    
    Sorted_exams_datas_tuple_list = sorted(exams_datas_tuple_list, key=lambda t: (t[1], t[0]))
    for local_name in courses_names:
        if len(local_name) > max_name_lenght:
            max_name_lenght = len(local_name)
    
    
    with open(fileout, "w", encoding="utf-8") as text_file:
        text_file.write("Esami sostenuti dallo studente "+stud_surname+" "+stud_name+", matricola "+str(stud_code))
        for tupla in Sorted_exams_datas_tuple_list:
            requested_spaces = max_name_lenght-len(tupla[0])
            text_file.write("\n"+tupla[0]+" "*requested_spaces+"\t"+tupla[1]+"\t"+str(tupla[2]))
            total_row += 1
    
    return total_row   
    
    
def stampa_studenti_brillanti(dbsize, fileout):
    smart_students_names_surnames_list =  []
    smart_students_codes_list = studenti_brillanti(dbsize)
    smart_students_grades_list = []
    row_number = 0
    Spaces = 7
    filepath1=str(dbsize)+"_students.json"
    if dbsize == "medium":
        Spaces = 5
    with open(filepath1, 'r') as file:
        file_contents_str = file.read()
    students_datas = json.loads(file_contents_str)
    for smart_student in smart_students_codes_list:
        good_grade= media_studente(smart_student, dbsize)
        smart_students_grades_list.append(good_grade)
        for local_dic in students_datas:
          if smart_student  in local_dic ["stud_code"]:
              smart_students_names_surnames_list.append(str(local_dic["stud_surname"]+" "+local_dic["stud_name"]))
    with open(fileout, "w") as index:
        for surname_and_name, grade in zip(smart_students_names_surnames_list, smart_students_grades_list):
            name_and_surname_and_name_len = len(surname_and_name)
            requested_spaces = 32 - Spaces - name_and_surname_and_name_len
            text_line = surname_and_name + " "* requested_spaces + "\t"+ str(grade) +"\n"
            index.write(text_line)
            row_number += 1
    return row_number
        