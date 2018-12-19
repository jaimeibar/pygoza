# pygoza

Fetch information about all Real Zaragoza matches.

Output: ics file ready to import into a Calendar app.

### Events description

| Event | Detail |
| ----- | ------ |
| SUMMARY | Localteam - Foreignteam |
| DTSTART | Match start date and time |
| DTEND | Match end date and time |
| DTSTAMP | Event timestamp |
| UUID | Event uuid |
| DESCRIPTION | Full match details. Match result. Not played yet in case the match is still pending |


### Full calendar ics file details

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//My calendar//EN//
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
SUMMARY:
UUID:
DTSTART:
DTEND:
DTSTAMP:
DESCRIPTION:
END:VEVENT
END:VCALENDAR
```


### TODO
 * Event end details
 * Extra info(TV channel)
 * Timezone