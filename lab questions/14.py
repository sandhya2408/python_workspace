#display key value pairs
def show_info(student_dict):
    for k , v in student_dict.items():
        print(f"{k}:{v}")
student_dict = {"NCET-EC001":"RAJESH","NCET-EC002":"SURESH","NCET-EC003":"MAHESH"}
show_info(student_dict)