# SQLLight

Petyr Baelish wants to enter the Vale of Arryn, but the knights of the Vale
are not letting him in. Help him talk to them and get entry.

Gate of the vale: $URL

# Running Instructions

Set up flask and run `FLASK_APP=server.py flask run`.

# Solution

This was an SQL injection problem, with the table schema containing
`NAME`, `PASSWORD`, and `USER_GROUP`.

When _exactly_ one user with the `USER_GROUP` equal to `user_guest`
is selected, the flag is returned. Else, a message giving some hint
is given.

Bonus: There were some username/password combos which would give
the answers directly eg 'baelish/baelish'.