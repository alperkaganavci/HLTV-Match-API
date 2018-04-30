import urllib.request
from bs4 import BeautifulSoup

print('_____ Welcome to HLTV Match BOT _____')
print('__ Programmed by akagna __')
print('Note: This is my first complex program.')
print('This program can only pull today\'s live and upcoming matches and yesterday\'s matches.')
print('* 1) Only live matches * 2) Only today\'s upcoming matches\n * 3) Only yesterday\'s matches\n * 4) All')

while True:
    try:
        pick = int(input('My choice is: '))
        if (pick > 4 or pick <= 0):
            print('Please enter a valid number.')
        else:

    except:
        print ('Please enter a valid number.')

def upcoming_matches ():


headers = {}  # Headers gives information about you like your operation system, your browser etc.
headers['User-Agent'] = 'Mozilla/5.0'  # I defined a user agent because HLTV perceive my connection as bot.c
teamNames = []
eventNames = []
eventStatus = []
eventDates = []

a = 0
b = 1
# Getting the match pages' links.
for links in soup.find_all('div', class_='upcoming-matches'):  # Looking for "upcoming-matches" class in source.
    for links in soup.find_all('a'):  # Finding "a" tag under "upcoming-matches" class.
        clearlink = links.get('href')  # Getting the value of variable.
        if clearlink.startswith('/matches/'):  # Checking for if our link starts with "/matches/"
            matchlinks.append('https://hltv.org' + clearlink)  # Adding into list.
# Connecting to pages and getting what we want.
while True:

    print(len(matchlinks), "matches found")
    try:
        matchNumber = int(input('How many matches you want to get? ')) # We control if input equals to a string.
        print('Please be patient while matches are getting pulled. This can take a while.')

        if matchNumber <= len(matchlinks) and not matchNumber <= 0:
            for i in range(matchNumber):
                matchpages = urllib.request.Request(matchlinks[i], headers=headers) # We are connecting to each link one by one with loop.
                mpsession = urllib.request.urlopen(matchpages)
                mpsauce = mpsession.read() # I got the source code in a different variable because i don't know if it'll cause a problem. I just don't want to be busy with it.
                mpsoup = BeautifulSoup(mpsauce, 'lxml')

                for names in mpsoup.find_all('div', class_='teamName'):
                    teamNames.append(names.text)
                for enames in mpsoup.find_all('div', class_='event text-ellipsis'):
                    eventNames.append(enames.text)
                for edates in mpsoup.find_all('div', class_='date'):
                    eventDates.append(edates.text)

        teamA = teamNames[0::2] # We split the list to 2 list because it gives an error when we don't. I'm too lazy to try to solve it, that was the easiest way.
        teamB = teamNames[1::2]

        for x in range (len(teamA)):
            print(teamA[x], "vs", teamB[x], "at", eventDates[x], eventNames[x])
    except:
        print("Please enter a valid number !")

