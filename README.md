# Games-Of-chance
#### Project Goals

You will work to write several functions that simulate games of chance. Each one of these functions will use a number of parameters, random number generation, conditionals, and return statements.


##### Task 1
In order to complete this project, you should have completed the first 3 sections of the [Learn Python 3 Course](https://www.codecademy.com/learn/learn-python-3).

This includes the lessons on Syntax, Functions, and Control Flow.

##### Task 2
The project starts by importing the `random` module. Every game of chance will involve generating a random number.

For example, to generate a random between `1` and `10` (inclusive) and store it in a variable named `num`, use this line of code:

```py
num = random.randint(1, 10)
```

The project also has a variable named `money` that starts at `100`. This represents your current amount of money. In every game of chance, you will be able to bet money. The value of `money` should change depending on whether you win or lose the game.

##### Task 3
Create a function that simulates flipping a coin and calling either `"Heads"` or `"Tails"`. This function (along with all of the other functions you will write in this project) should have a parameter that represents how much the player is betting on the coin flip.

This function should also have a parameter that lets the player call either `"Heads"` or `"Tails"`.

If the player wins the game, the function should return the amount that they won. If the player loses the game, the function should return the amount that they lost as a negative number.

Hint: Our function definition looked like this:

```py
def coin_flip(guess, bet):
```

Simulate a coin flip by randomly generating an integer between `1` and `2` (inclusive).

##### Task 4
Create a function that simulates playing the game [Cho-Han](https://en.wikipedia.org/wiki/Ch%C5%8D-han). The function should simulate rolling two dice and adding the results together. The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.

The function should have a parameter that allows for the player to guess whether the sum of the two dice is `"Odd"` or `"Even"`. The function should also have a parameter that allows the player to bet an amount of money on the game.

Hint: To simulate rolling a dice, generate a random integer between `1` and `6`.

##### Task 5
Create a function that simulates two players picking a card randomly from a deck of cards. The higher number wins.

Once again, this function should have a parameter that allows a player to bet an amount of money on whether they have a higher card. In this game, there can be a tie. What should be returned if there is a tie?

Check the hint to see an additional challenge for this game.

Hint: If the game is a tie, you should return `0`. The player doesn't win or lose any money.

It's possible that your solution doesn't _really_ simulate drawing two cards from the same deck. For example, if I draw a `4`, it is less likely that you will draw a `4` when you draw a card. As a challenge, think about how you might create a system that knows which cards have already been draw. 

Bonus Hint: if you're familiar with lists, this would be a good place to use them!

##### Task 6

Create a function that simulates some of the rules of [roulette](https://en.wikipedia.org/wiki/Roulette). A random number should be generated that determines which space the ball lands on.

When we wrote our function, we allowed the user to guess `"Odd"`, `"Even"`, or a specific number. We also implemented the logic associated with the `0` and `00` spots. For example, the player loses if they guess either `"Odd"` or `"Even"` and either `0` or `00` comes up.

Implement as many rules of roulette as you'd like. Make sure to consider the different ways roulette rewards a win. Check the hint to see more about this!

Hint: The amount of money you get back from roulette changes depending on what kind of guess you make. For example, if you bet 1 dollar on a specific number, and you win, you will get 35 dollars back. But if you bet 1 dollar on `"Even"` and win, you will only get one dollar back. The return value of your function should reflect the different ways roulette rewards its winners.

##### Task 7
Call each of your functions at least once. Below is an example of betting $10 on a coin flip and updating the amount of money you have based on whether you win or lose :

```py
money += coin_flip("Heads", 10)
```

Make sure there are enough print statements so you can understand what games were played, what happened during those games, and the amount of money you have after each game is played.

##### Task 8
Expand your program to check for edge cases. What should happen if a player tries to bet more money than they have? What should happen if a player bets a negative amount of money? What should happen if a player calls `"heads"` or `"Heads!"` rather than `"Heads"`.

Try to make it very difficult for someone to break your program.

##### Task 9
Great work! Visit [our forums](https://discuss.codecademy.com/t/games-of-chance-challenge-project-python/462399) to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that's okay! There are multiple ways to solve these projects, and you'll learn more by seeing others' code. 

