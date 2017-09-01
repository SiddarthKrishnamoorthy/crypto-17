# SQLHeavy

After drinking the poisoned wine given to her by Jaime, Olenna
Tyrell has become delirious. Now, she is only responding
to SQL Queries.

Bronn has been given the opportunity to interrogate her and find
out the last of her secrets. Bronn is stuck. Analyze this carefully
and help Bronn find the flag so that he might finally become Lord
of a Castle.

# Running Instructions

Install flask and run `FLASK_APP=server.py flask run` to start
question on port 5000 on localhost.

# Solution

This problem allows you to run almost any statement on a SQLite server.

You don't know any tables on that server, but accessing `sqlite_master` table
or using `.tables` causes an error (they are not allowed).

Similarly, dropping tables is not allowed.

To get around this, you can use `analyze` which causes an sqlite-specific
table to be made called `sqlite_stat1` which contains all the table names.

The newly obtained table name, when selected, shows the flag in some weird
encoding with a message saying "u jelly".

This is actually valid code in the code golf language `jelly` which gives
the final flag when run.