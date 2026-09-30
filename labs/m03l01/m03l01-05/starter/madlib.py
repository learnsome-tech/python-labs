def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt).strip() # 3.2 Windows bug fix
    dictionary[cue] = response
