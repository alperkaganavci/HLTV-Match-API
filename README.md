# UPDATED
This API will be updated as long as I live. :D
# HLTV-Match API
A bot which pulls upcoming, live and finished matches.(Results are only for today and yesterday) People can easily use who is interested with making bet websites etc.
# JSON Support
Real support for those that will use it. Anyone can pull match informations easily.
# An example of output
```{
  "matches": [
    {
      "team1": "Gambit",
      "team2": "AGO",
      "eventname": "DreamHack Open Tours 2018",
      "date": "20th of May 2018",
      "clock": "16:00:00",
      "bo": "Best of 3",
      "status": "UPCOMING",
      "team1logo": "https://static.hltv.org/images/team/logo/6651",
      "team2logo": "https://static.hltv.org/images/team/logo/8068"
} 
```
# Requirements
Python 3
```
pip install lxml #I dont know if this has to be installed.
pip install bs4
pip install requests
pip install tqdm
```
