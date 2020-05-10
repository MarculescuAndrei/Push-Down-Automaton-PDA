# Push-Down-Automaton-PDA-
A working Push-Down-Automaton in Python 3 - (Automata Theory)
<br>
<hr>
<br>

<p align="center">
<b> How the Source is Structured: </b>
</p>

<br>

First line : Initial State(s)
<br>
Second line : Final State(s)
<br>
Other Lines : X Y W Z | Where the State X goes to State Y when the value W is read from the word, and Z is the action taken upon the Stack, it can be 'Pop' (it deletes the last item added), it can be '-' (doesn't affect the Stack) or any other element such as 'A' or 'BBB' (they will be added to the stack, one by one in the case of 'BBB')
<br>
<br>
<b> Note: </b> The value W can also be '&' (a substitute for Lambda - empty element, can be read at any time, despite the current letter in the word;
<br>

<br>

<b>Example:</b> 
<br>

q0 <br>
q4 <br>
q0 q1 a A <br>
q1 q0 a - <br>
q0 q2 b BBB <br>
q2 q2 b BBB <br>
q2 q3 c Pop <br>
q3 q3 d Pop <br>
q3 q3 c Pop <br>
q3 q4 & - <br>
<br>
<hr>
The program takes that information and turns it into a dictionary, such as : {'q0': [('q1', 'a', 'A'), ('q2', 'b', 'BBB')], 'q1': [('q0', 'a', '-')], 'q2': [('q2', 'b', 'BBB'), ('q3', 'c', 'Pop')], 'q3': [('q3', 'd', 'Pop'), ('q3', 'c', 'Pop'), ('q4', '&', '-')]}
<br> <br>

A key is a State that can go to another state, and it's corresponding elements are tuples where the first element represents the State that the 'key' goes to, and the 2nd element is the value of the move, and the third one represents the action taken upon the Stack.
<br> <br>
At the start of the program you can choose the criteria through which the program decides if a word is accepted or not: <br>
1 = By Empty Stack<br>
2 = By Final State<br>
3 = By Empty Stack & Final State<br>
<br>
<br>
<hr>
<br>
<p align="center">
<b>Visual Representation:</b>
<br>
 <br>
 <img src="https://i.gyazo.com/1b69c8b2700e42f072f2c9016e16a638.png">
 </p>
<br>
<b> An accepted word is : aaaaaabbccccccddd </b>
<br>
<hr>
<br>
In the theory of computation, a branch of theoretical computer science, a pushdown automaton (PDA) is a type of automaton that employs a stack. <br>
<br>

Pushdown automata are used in theories about what can be computed by machines. They are more capable than finite-state machines but less capable than Turing machines. Deterministic pushdown automata can recognize all deterministic context-free languages while nondeterministic ones can recognize all context-free languages, with the former often used in parser design. <br>
<br>

The term "pushdown" refers to the fact that the stack can be regarded as being "pushed down" like a tray dispenser at a cafeteria, since the operations never work on elements other than the top element. A stack automaton, by contrast, does allow access to and operations on deeper elements. Stack automata can recognize a strictly larger set of languages than pushdown automata. A nested stack automaton allows full access, and also allows stacked values to be entire sub-stacks rather than just single finite symbols.

