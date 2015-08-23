# "Let's Make A Deal" game

## What is it
This is a little game I wrote for leaning purposes to explain the right solution to the Monty Hall problem. 

From [Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem):

> The Monty Hall problem is a brain teaser, in the form of a probability puzzle (Gruber, Krauss and others), loosely 
based on the American television game show Let's Make a Deal and named after its original host, Monty Hall. The problem 
was originally posed in a letter by Steve Selvin to the American Statistician in 1975 (Selvin 1975a), (Selvin 1975b). 
It became famous as a question from a reader's letter quoted in Marilyn vos Savant's "Ask Marilyn" column in Parade 
magazine in 1990 (vos Savant 1990a):
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, 
goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, 
which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
Vos Savant's response was that the contestant should switch to the other door (vos Savant 1990a). Under the standard 
assumptions, contestants who switch have a 2/3 chance of winning the car, while contestants who stick to their choice 
have only a 1/3 chance.
Many readers of vos Savant's column refused to believe switching is beneficial despite her explanation. After the 
problem appeared in Parade, approximately 10,000 readers, including nearly 1,000 with PhDs, wrote to the magazine, 
most of them claiming vos Savant was wrong (Tierney 1991). Even when given explanations, simulations, and formal 
mathematical proofs, many people still do not accept that switching is the best strategy (vos Savant 1991a). 
The problem is a paradox of the veridical type, because the correct result (you should switch doors) is so 
counterintuitive it can seem absurd, but is nevertheless demonstrably true. 

## Main features
I wrote two programs, `single_player_game.py` lets you play a single player game against Monty Hall. 
`monte_carlo_simulation.py` is instead a strip-out version of the game, which is run 10,000 times and displays the 
results. The result of the simulation is aimed to help the reader to fully understand the paradox.

The resuls of the simulation have been used in a blog article I've published on my personal blog 
[Simplyanalyticsblog.org](http://simplyanalyticsblog.com/).

## How to play
