# calculator-command-pattern-refactor

I came across a coding challenge from almost a decade ago on an external drive. The interviewer asked me to make a calculator that could chain operations. For example, I had to create something like this:

```
calculator(0).add(10).multiply(4).subtract(20).divide(10).total == 2  # True
```

Psh! That's easy. I wrote up a small calculator class and thought I was straight on my way to six figures, equity, and ping pong tables. But not so fast... Then he asked me to extend my design to include an undo feature. Well... suffice to say I wasn't hired. I set the problem aside to figure out later, and then I forgot.

Now that I'm a "senior engineer" I know how to do this sort of thing. Here is the calculator but refactored to use the command pattern. It's a bit over-engineered for a simple calculator, but now you can easily hook it up to a frontend and/or build on top of it and plug it into anything where you might need to keep track of amounts.

So I had to refactor it twice actually because the first time around I wasn't able to undo multiplication by zero. I had to approach the command pattern from a different way to get it. Maybe I'll write a Medium article about it later to explain how I did it, but you can find it in the code. Or you can just point ChatGPT to my repo and ask it to explain! In any case, hope you like it. Enjoy!

In short, I created three different implementations:
1. `calculator_naive` is a single class implementation. It doesn't support undo/redo.
2. `calculator_command_state_history` is a refactor using the command pattern. I keep track of the state of the calculator total and use mathematical operations and their opposite operations to handle undo/redo. For example, to undo an add command, I subtract. This works for the most part, but fails when trying to undo a multiplication by zero, because dividing by zero (the opposite operation) is undefined!
3. `calculator_command_event_history` is alao a refactor using the command pattern. I keep a running list of the calculator commands (events) perfomed on the calculator. I am able to calculate and display the calculator total by performing all of the commands in the running list. To undo/redo, I simply manipulate the index of the command list and recalculate. By handling undo this way, I avoid the division-by-zero issues I experienced earlier.

## Test

Install `pytest-cov` if you haven't. Then, from root project directory, on the terminal run:

`$ pytest --cov --cov-branch --cov-report term-missing tests/`
