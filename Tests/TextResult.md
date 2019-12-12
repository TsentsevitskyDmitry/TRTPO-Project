|Scenario|Action|Expected results|Actual result| Test Passed|
|:---|:---|:---|:---|:---|
|Save new Notifications from db|Call add() method of NotificationORM|New row in database|New row in database|+ |
|Show new Notifications from db|Call show_all() method of NotificationORM|String of all the rows of database|String of all the rows of database| +|
|Delete new Notifications from db|Call delete_instance() method of Notification instance|Deleted row in database|Deleted row in database| + |
|Help echo|Send '/help' message to the bot |Quick help with basic commands|Quick help with basic commands|  +|
|Show active notifications echo|Send '/show' message to the bot |List of pending notifications|List of pending notifications| +  |
|Parsing relative timelable|Send 'напочни через 1 час поесть' like message to the bot |Creating new notificaton with: [time: current time + 1 hour, content: 'поесть'|For some inputs bot print Usage string| -|
|Parsing absolute timelable|Send 'напочни завтрв в 8 проверить почту' like message to the bot |Creating new notificaton with: [time: next_day.08.00, content: 'поесть'|For some inputs bot print Usage string| -|
|Executing payload from user messages|Send Usage-like message to the bot |Create new Notification|When parsing timelable passed, this case also created new notification| +|
