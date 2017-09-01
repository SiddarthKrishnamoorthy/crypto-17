# Winds of Winter

The long night will come and go, but George RR Martin will never release his
book.

Alas, all we have are snippets of it.

# Running Instructions

Only WindsOfWinter.pdf should be made public.

# Solution

The pdf file contains three things (`binwalk` it to know):
a excerpt from GRRM's new novel, a python script containing the encoding function,
and a flag.zip containing an encoded flag file.

The encryption is a Running Key Cipher (search for it) with the book being the
excerpt from the novel.

Decrypt it to get the flag.