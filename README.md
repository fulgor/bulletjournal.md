# bulletjournal.md
Python script to create a bullet journal in an plain textfile with Markdown formatting

This project is not about software in the first place. It is about the idea using the concept of a [bulletjournal](http://bulletjournal.com/) in a plain textfile. The second idea is to use [markdown-formatting](https://daringfireball.net/projects/markdown/). Thus, the bulletjournal-file could be used with a markdown-editor or copied into a CMS like [yellow](https://github.com/datenstrom/yellow). In addition to templates, there is a [python script](#python-script-bjmdpy) to create templates on your own.

## TOC
* [Keys](#keys)
* [Views](#views)
* [Templates](#templates)
* [Python Script bjmd.py](#python-script-bjmdpy)
* [FAQ](#faq)
* [Tipps And Tricks](#tipps-and-tricks)


## Keys

Keys need 4 spaces prefix to be formatted

    .  task [2]
    X  done
    >  postponed
    O  event
    !  adds priority

**Example: daily tasklist:**

    .   check yesterday's list
    >   call webmaster
    x   [1] Write README.md for bulletjournal.md
    x!  Present for Peter
    o   Peter's birthday party


## Views

view    |  templates  |  script
--------|-------------|----------
future log  | no  |  no
year   |  yes  | yes
month  | yes   | yes
daily tasklist   | yes   | yes
projects    | no   | no
indexnumbers: [1]    | no  | no


## Templates

See [templates/](templates)


## Python Script bjmd.py

Use the [script](scripts) in a terminal like this:

> $> python bjmd.py > mybulletjournal.txt

* Use this script to create a bullet journal textfile for a whole year.
* The Language of textfile follows the **locale** of your OS.
* See [standard-output.md](https://github.com/fulgor/bulletjournal.md/blob/master/scripts/standard-output.md) of bjmd.py when options are unaltered on a system with locale EN.
* Settings (that you may change in the script, of course):
  * prefix = 4 blanks before day in shortlist
  * suffix = 2 blanks after weekday list
  * this year or specified year
  * include keys and their meaning on top 
  * include calendarmatrix (off, needs manual correction)
  * reversemonth = list order is December to January
  * reverseday = list order is last day of week to first day of week
  * set first day of week (MONDAY)

## FAQ

* **Why is the default list order descending?** It's because Soren Kierkegaard said, that life must be lived forwards, but can only be understood backwards. Moreover, in a textfile it seems easier to work upwards. But you may change the script easily.
* **What are the advantages of bulletjournaling in a textfile?** You may: search the full text, copy and paste, replace, delete. Moreover, you don't have to estimate how many pages you need to spare for a project or list.
* **What are the limitations of bulletjournaling in a textfile?** Obviously, you need a laptop or smartphone. Then, in a file there are no pagenumbers for an index. And there is no color-coding.


## Tipps And Tricks
* Use linux command 'cal' to create calendars as text
