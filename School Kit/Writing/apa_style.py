#----------------------------------------
# Script for convert a list of your references to APA Reference-list entries

def entry_APA(text, indent=1):

    indent = " "*(2+2*indent)

    if len(text) <= 73:
        return text
    else:
        words = text.split()
        sub_texts = []
        sub_text = ""
        for word in words:
            if len(sub_text + word) + 1 > 73:
                sub_texts.append(sub_text)
                sub_text = " " + word
            elif sub_text == "":
                sub_text = word
            else:
                sub_text += " " + word
        sub_texts.append(sub_text)
        return ("\n"+indent).join(sub_texts)



# --------------- TEST -----------------

# A list of all your reference entries (under your paper's "REFERENCES" section)
ref_list = [
'Brinkman, W. P. (2010b). Lecture ..... ',
'Brinkman, W. P. (2010a). Lecture 2: Empirical research methods IN4304—research plan. Retrieved from https://ocw.tudelft.nl/wp-content/uploads/lecture_2_ERM_2010.pdf',

'Hypothesis. (2014, March 5). In Wikipedia. Retrieved from http://en.wikipedia.org/w/index.php?title=Hypothesis&oldid=598257560',

'Research. (2014, March 1). In Wikipedia. Retrieved from http://en.wikipedia.org/w/index.php?title=Research&oldid=597720379',

'Ryerson University, Department of Student Services. (n.d.b). The research question and hypothesis. Retrieved from https://www.ryerson.ca/content/dam/academicintegrity/documents/Research%20question%20and%20hypothesis.pdf',

'Author, [Last-name initial]. (year). ....'
]

# Applying our APA-styling function on the list of entries
apa_refs = []

for i, ref in enumerate(sorted(ref_list)):
    
    entry = f"{i+1}. {entry_APA(ref,2)}\n"
    apa_refs.append(entry)

    print(entry)

# apa_refs: now has your Reference-list of APA-sorted entries.



# ------------- OUTPUT ----------------

# 1. Author, [Last-name initial]. (year). ....

# 2. Brinkman, W. P. (2010a). Lecture 2: Empirical research methods
#        IN4304�research plan. Retrieved from
#        https://ocw.tudelft.nl/wp-content/uploads/lecture_2_ERM_2010.pdf

# 3. Brinkman, W. P. (2010b). Lecture ..... 

# 4. Hypothesis. (2014, March 5). In Wikipedia. Retrieved from
#        http://en.wikipedia.org/w/index.php?title=Hypothesis&oldid=598257560

# 5. Research. (2014, March 1). In Wikipedia. Retrieved from
#        http://en.wikipedia.org/w/index.php?title=Research&oldid=597720379

# 6. Ryerson University, Department of Student Services. (n.d.b). The research
#        question and hypothesis. Retrieved from
#        https://www.ryerson.ca/content/dam/academicintegrity/documents/Research%20question%20and%20hypothesis.pdf
