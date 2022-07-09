uofm = {'A+':4.5,'A':4,'B+':3.5,'B':3,'C+':2.5,'C':2,'D':1,'F':0}

def gpa(grades, evals = uofm, all_creds = 3):
    course_creds = [all_creds]
    crs_cred_error = ("Course-credits not given, please include either course's credits per achieved grade"+
			    	  "\nor apply 'all_creds' (i.e. all course-credits are equal to some value).")
    all_creds_error = '"all_creds" (i.e. all course-credits are the same) should be a number greater than 0.'
    if all_creds:
        if type(all_creds) == str:
            all_creds = all_creds.strip()
            if all_creds.is_digit() or all_creds.replace('.','').is_digit():
                all_creds = float(all_creds)
            else:
                raise all_creds_error
        
        if type(all_creds) == int or type(all_creds) == float:
            if all_creds < 0:
                raise all_creds_error
        else: # all_creds is 'bool' (True) or other data-type
            raise all_creds_error

        course_creds *= len(grades)

    else:
        if type(grades) != dict:
            raise crs_cred_error
        course_creds = grades.values()    

    grade_creds = map(uofm.get, grades)
    gpa_weights = [g*c for g,c in zip(grade_creds, course_creds)]
    return sum(gpa_weights) / sum(course_creds)
