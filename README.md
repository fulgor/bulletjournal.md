# bulletjournal.md
Python script to create a bullet journal in an plain textfile with Markdown formatting

This project is not about software in the first place. It is about the idea using the concept of a [bulletjournal](http://bulletjournal.com/) in a plain textfile. The second idea is to use [markdown-formatting](https://daringfireball.net/projects/markdown/). Thus, the bulletjournal-file could be used with a markdown-editor or copied into a CMS like [yellow](https://github.com/datenstrom/yellow). In addition to templates, there is a [python script](#python-script-bjmd.py) to create templates on your own.

## Limitations
* in a file there are no pagenumbers for an index
* there are no colors

## Views
See [templates/](templates)

* future log
* year
* month
* daily tasklist
* projects - indexnumbers: [1]

## Keys
Keys need 4 spaces prefix to be usable formatted

    .  task [2]
    X  done
    >  postponed
    O  event
    !  adds priority

## Example: daily tasklist
    .   check yesterdays list
    >   call webmaster
    x   [1] Write README.md for bulletjournal.md
    x!  Present for Peter
    o   Peter's birthday party

## Templates/
These templates are available to copy into your bulltejournal.md:

* Year: 2018, 2018
* month.md

## Python Script bjmd.py

Use the script in a terminal like this:

> $>python bjmd.py > mybulletjournal.md

* Use this script to create a bullet journal textfile for a whole year
* settings (that you may change in the script, of course):
  * prefix = 4 blanks before day in shortlist
  * suffix = 2 blanks after weekday list
  * this year or specified year
  * include keys and their meaning on top 
  * include calendarmatrix (off, needs manual correction)
  * reversemonth = list order is December to January
  * reverseday = list order is last day of week to first day of week
  * set first day of week (MONDAY)

## FAQ

**Why is the default list order descending?** It's because Soren Kierkegaard said, that life must be lived forwards, but can only be understood backwards. Moreover, in a textfile it seems easier to work upwards. But you may change the script easily.

## Tipps And Tricks
* Use linux command 'cal' to create calendars as text
