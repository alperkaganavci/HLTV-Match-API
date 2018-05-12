import datetime, requests
from bs4 import BeautifulSoup

class Matches:
    def __init__(self):
        self.matchlinks_um = []
        self.matchlinks_lm = []
        self.matchlinks_rts = []
        self.teamNames = []
        self.dates = []
        self.events = []
        self.clocks = []

    def source (self, link):
        self.r = requests.get(link)
        self.sauce = self.r.content
        self.soup = BeautifulSoup(self.sauce, 'lxml')

    def todaymatches(self):
        print('\nTHESE ARE TODAY\'S UPCOMING MATCHES\n')
        self.source('https://hltv.org/matches')

        for self.links in self.soup.find(class_="standard-headline", text=(datetime.date.today())).find_parent().find_all(class_="upcoming-match"):
            self.matchlinks_um.append('https://hltv.org' + self.links.get('href'))

        for self.x in range(len(self.matchlinks_um)):
            self.source(self.matchlinks_um[self.x])
            self.time_class = self.soup.find('div', class_= 'time')['data-unix']
            self.clock = datetime.datetime.fromtimestamp(int(self.time_class[:10])).time()
            if str(self.clock) != '00:00:00':
                for self.tn in self.soup.find_all('div', class_='teamName'):
                    self.teamNames.append(self.tn.text)
                self.date = self.soup.find('div', class_='date').text
                self.dates.append(self.date)
                self.eventname = self.soup.find('div', class_='event text-ellipsis').text
                self.events.append(self.eventname)
                self.clocks.append(self.clock)

            else:
                pass

        self.teamA = self.teamNames[0::2]
        self.teamB = self.teamNames[1::2]

        for self.number in range(len(self.dates)):
            print(self.teamA[self.number], 'vs', self.teamB[self.number], 'on', self.dates[self.number], 'at', self.clocks[self.number], self.events[self.number])

    def livematches(self):
        print('\nTHESE ARE LIVE MATCHES\n')
        self.source('https://hltv.org/matches')

        for self.links in self.soup.find('div', class_='live-matches').find_all('a'):
            self.matchlinks_lm.append('https://hltv.org' + self.links.get('href'))

        for self.x in range(len(self.matchlinks_lm)):
            self.source(self.matchlinks_lm[self.x])
            self.time_class = self.soup.find('div', class_='time')['data-unix']
            self.clock = datetime.datetime.fromtimestamp(int(self.time_class[:10])).time()
            for self.tn in self.soup.find_all('div', class_='teamName'):
                self.teamNames.append(self.tn.text)
            self.date = self.soup.find('div', class_='date').text
            self.dates.append(self.date)
            self.eventname = self.soup.find('div', class_='event text-ellipsis').text
            self.events.append(self.eventname)
            self.clocks.append(self.clock)


        self.teamA = self.teamNames[0::2]
        self.teamB = self.teamNames[1::2]

        for self.number in range(len(self.dates)):
            print(self.teamA[self.number], 'vs', self.teamB[self.number], 'on', self.dates[self.number], 'at',
                  self.clocks[self.number], self.events[self.number])

Matches().livematches()
Matches().todaymatches()



# Linkleri çekeceğiz
# Linklerin içinden saatlere bakacağız
# Eğer saat 00:00 değilse bilgilerini

