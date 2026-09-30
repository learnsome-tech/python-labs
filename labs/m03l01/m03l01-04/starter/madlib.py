def tellStory():
    userPicks = dict()
    addPick('animal', userPicks)
    addPick('food', userPicks)
    addPick('city', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)
