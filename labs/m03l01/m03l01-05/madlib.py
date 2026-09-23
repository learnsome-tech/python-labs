# Hands-on Python: Complete Video Course & Book — lesson m03l01 — A Sample Program, Explained
# https://learnsome.tech/courses/python-course/watch?lesson=m03l01
# © LearnSome.tech
def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt).strip() # 3.2 Windows bug fix
    dictionary[cue] = response
