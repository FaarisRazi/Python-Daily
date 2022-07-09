uofm = {'A+':4.5,'A':4,'B+':3.5,'B':3,'C+':2.5,'C':2,'D':1,'F':0}

rit = {'A':4, 'A-':3.667, 'B+': 3.333, 'B':3, 'B-':2.667, 
       'C+':2.333, 'C':2, 'C-': 1.667, 'D': 1, 'F': 0}

def valid_creds(creds, grades=[]):
    creds_error = '"all_creds" (i.e. all course-credits are the same) should be a number greater than 0.'
    
    if type(creds) == str:
        creds = creds.strip()
        if creds.isdigit() or creds.replace('.','').isdigit():
            creds = float(creds)
        else:
            raise creds_error
        
    if type(creds) in {int, float}:
        if creds < 0:
            raise creds_error
    else: # creds = 'bool' (True) or other data-type
        raise creds_error
          
    return True

def gpa(grades, evals = uofm, all_creds = 3):
    crs_cred_error = ("Course-credits not given, please include either course's credits per achieved grade"+
			    	  "\nor apply 'all_creds' (i.e. all course-credits are equal to some value).")
    if type(grades) != dict:
        if valid_creds(all_creds):
            return sum(map(uofm.get, grades)) / len(grades)

        raise crs_cred_error

    grade_creds, course_creds = map(uofm.get, grades), grades.values()
    gpa_weights = [g*c for g,c in zip(grade_creds, course_creds)]
    return sum(gpa_weights) / sum(course_creds)

class GPA:
    def __init__(self, grades, course_credits):
        
        self.gcreds, self.ccreds = grades, course_creds
