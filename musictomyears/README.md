# Music to My Ears

There is a song. A Song of Ice and Fire (or maybe not!!).
A song has no secrets. Or does it?

# Running Instructions

Only the file final.mp3 should be made public.

# Solution

The given file is an MP3 file of the song "Written in Reverse". Reversing
the song and listening to it will give you the clue "md5 jon snow".

On closer observation using `binwalk`, you will notice that it actually contains
a 7z archive also. Using `binwalk -e` doesn't seem to work, and after some googling,
it can be found that `binwalk --dd='.*' final.mp3` will extract the 7z archive.

The 7z archive is password protected. The password is the md5 of "jonsnow".