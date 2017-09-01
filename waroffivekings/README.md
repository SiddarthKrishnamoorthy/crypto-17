# War of Five Kings

The War of the Five Kings is on! What king will you play
as? Who increases your odds of winning?

Choose wisely, or let fate decide.

# Running Instructions

The file index.php is all that needs to be hosted.

# Solution

This question is basically full of needless distractions. The entire JavaScript
"game" is a distraction. What you need to notice is that when you press the
submission button, a POST request is sent to the server containing a certain
probability, which is randomly generated.

If you set that to 1, the flag is shown. You can either keep trying like a billion
times before you get lucky or you can simply set the probability to 1. There are many
ways to do this, for example:

* Sending POST through HTTPie
* Setting `Math.random = () => 1;`
