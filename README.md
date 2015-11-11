# dead
A console app to see your deadlines.

# Usage
dead reads in deadlines from a CSV file. Each deadline is written on a new line:
```
Graphical Models, 23/11/15 12:00, Textbook questions
Research Methods, 15/01/16 23:55, Coursework 2 (Group)
```

Currently you need to have your deadlines file in the same directory as dead.py. To display your deadlines, run `python dead.py deadlines.csv`. You will see your deadlines sorted in ascending order:

```
+------------------+---------------------+-----------------+----------------------+
|      Module      |       Due date      |  Time remaining |     Description      |
+------------------+---------------------+-----------------+----------------------+
| Graphical Models | 2015-11-23 12:00:00 |  1 week, 4 days |  Textbook questions  |
| Research Methods | 2016-01-15 23:55:00 | 9 weeks, 2 days | Coursework 2 (Group) |
+------------------+---------------------+-----------------+----------------------+ 
```