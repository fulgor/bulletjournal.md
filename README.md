# bulletjournal.md
Bullet Journal in an plain textfile with Markdown formatting

This project is no software. It is about the idea how to use the concept of a [bulletjournal](http://bulletjournal.com/) in a plain textfile. The second idea is to use [markdown-formatting](https://daringfireball.net/projects/markdown/). Thus, the bulletjournal-file could be used with a markdown-editor or copied into a CMS like [yellow](https://github.com/datenstrom/yellow). 

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

## Tipps And Tricks
* Use linux command 'cal' to create calendars as text
