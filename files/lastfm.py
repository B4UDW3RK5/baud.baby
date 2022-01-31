#!/usr/pkg/bin/python3

import urllib.request, json, datetime

# calculate the start and end of last week
thisTimeLastWeek = datetime.datetime.today()-datetime.timedelta(days=7)
lastMonday = thisTimeLastWeek-datetime.timedelta(days=thisTimeLastWeek.weekday())
lastSunday = lastMonday+datetime.timedelta(days=6)

# convert the datetime values to epoch time
start = lastMonday.replace(hour=0,minute=00,second=00,microsecond=0).timestamp()
end = lastSunday.replace(hour=23,minute=59,second=59,microsecond=0).timestamp()

# grab the chart data using the start and end date above
# this all needs to be updated to not try and proces an empty list when there's
# no listens
with urllib.request.urlopen("http://ws.audioscrobbler.com/2.0/?method=user.getweeklyartistchart&user=[PASTE USERNAME HERE]&api_key=[PASTE API KEY HERE]&from=%s&to=%s&format=json" % (start,end)) as url:
   listeningData = json.loads(url.read().decode())
top10 = 0
print('Top 10 last.fm Artists for week ending ' + datetime.datetime.fromtimestamp(end).strftime('%A, %B %d'))
while (top10 <= 9):
   position = '{0: >2}'.format(str(top10+1))
   plays = '{0: >3}'.format(listeningData['weeklyartistchart']['artist'][top10]['playcount'])
   artist = listeningData['weeklyartistchart']['artist'][top10]['name'].encode('ascii','replace')
   print(position + '. ' + plays + ' plays: ' + artist.decode('ascii'))
   top10 = top10 +1
