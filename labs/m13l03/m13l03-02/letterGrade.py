# Hands-on Python: Complete Video Course & Book — lesson m13l03 — If Elif Chains
# https://learnsome.tech/courses/python-course/watch?lesson=m13l03
# © LearnSome.tech
def letterGrade(score): 
    if score >= 90: 
        letter = 'A' 
    else:   # grade must be B, C, D or F 
        if score >= 80: 
            letter = 'B' 
        else:  # grade must be C, D or F 
            if score >= 70: 
                letter = 'C' 
            else:    # grade must D or F 
                if score >= 60:
                    letter = 'D' 
                else: 
                    letter = 'F' 
    return letter
