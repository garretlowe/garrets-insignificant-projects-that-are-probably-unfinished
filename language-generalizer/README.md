# Laguage Generalizer | November 2021 | Dropped

The Language Generalizer was intended, naievely, to take a list of words, splitting them into prefixes, middles, & suffixes of varying length, then creating new words based off of their popularity in the sample set.

I dropped this since the results were lacklustre at best and the problem itself is much more elegantly solved using machine learning.

### Ideas To Improve

Employing machine learning concepts would resolve a lot of the tedium I was finding when writing this.

An alternative approach could be sampling individual letters and selecting new ones based on the popularity of their neighbours.
(e.g. with the training set \["red", "bed", "credit"\] the string "red" is a very likely combination because there are 2 instances of "r" followed by "e" and 3 instances of "e" followed by "d".)

### How To Use

Run the program via CLI: `py ./main.py`.

Debug info and results are output to console.

### Learning Outcomes

Python, CSV

### Resources

Learning sample provided by: <https://www.townslist.co.uk>
