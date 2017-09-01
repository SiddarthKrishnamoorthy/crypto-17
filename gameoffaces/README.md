# The Game of Faces

Arya is playing the Game of Faces. She has to
convince The Waif that she is noone, but the
Waif is not convinced by her statements. Help
Arya fool the Waif into thinking that she is
no one.

Question By: Yash Srivastav <yashsriv>

# Running

Just run the node server in the server folder

# Solution

When you are met with the login page, you'll see that you are asked for
a name. If you enter any random name (like `arya`), you get a cookie
associated with that name with 2 fields:
* userid
* auth

Now, as per the question, you need to convince the server that you are
noone. If you observe the auth token, it ends with `%3d%3d`. If you do
a URLDecode on it, it is `==`. Hmm, looks suspiciously like a base64
encoding.

If you try out the base64 of your entered username, you'll find that it
matches.

So basically you just need to change your cookie `userid` to `noone` and
`auth` to `bm9vbmU=` and enter the answer to `Who are You?` as `noone`
and  submit. Submitting that gives you the flag:

```
flag{@rya_is_@ctually_the_waif}
```
