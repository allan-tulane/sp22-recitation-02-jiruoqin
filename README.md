# CMPS 2200  Recitation 02

**Name (Team Member 1):** Ruoqin Ji
**Name (Team Member 2):** Dachen Ni

In this recitation, we will investigate recurrences.
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.

## Setup

- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment.
- Click on your personal github repository for the assignment.
- Click on the "Work in Repl.it" button. This will launch an instance of `repl.it` initialized with the code from your repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.

## Running and testing your code

- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$
W(n) = aW(n/b) + f(n)
$$

where $W(1) = 1$.
S

- 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.
- 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.
- 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.
- 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO: your answer goes here**

> **Quesiton 4 Answer:** The total work is the sum of the work of each level from 0 to $\log_b(n)$, which is a form of geomertic series. Then we have 3 cases of total work, each correspoding to a case of ratio r in geomertic series, respectively (i.e., |r|=1, |r|>1, |r|<1>):
>
> $$
> W(n)=f(n)\cdot (\log_bn+1) \hspace{1cm} \text{if } \frac{a}{f(b)}=1\\ \space \\  W(n)=f(n) \cdot \frac{(\frac{a}{f(b)})^{\log_bn+1}-1}{(\frac{a}{f(b)})-1} \hspace{1cm} \text{if } \frac{a}{f(b)}>1\\ \space\\ W(n)=f(n) \cdot \frac{1-(\frac{a}{f(b)})^{\log_bn+1}}{1-(\frac{a}{f(b)})} \hspace{1cm} \text{if } \frac{a}{f(b)}<1
> $$
>
> Thus, (holds for all three cases of $W(n)$):
>
> * For $f(n) =1$, $W(n) = 1\cdot \log n \cdot x$, where x is an arbitrary constant (i.e., $\log_b n+1$ in the first case above). Therefore, in this case $W(n) = \Theta(\log n)$.
> * For $f(n) =\log n, W(n)= (\log n) \cdot (\log n) \cdot x = \Theta(\log n)^2$ .
> * For $f(n) =n, W(n) = n\cdot (\log n) \cdot x = \Theta(n\log n)$.
>
> The actual generated code matches

- 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer.

> **Question 5 Answer:** Set $a$ to 8, $b$ to 2, $c$ to 4 for $W_1$ (i.e., $c > \log_b a$), $c$ to 2 for $W_2$ (i.e., $c < \log_b a$), and $c$ to 3 for $W_3$. Then we have,
| n     | W_1               | W_2           | W_3            |
| ----- | ----------------- | ------------- | -------------- |
| 10    | 16536             | 1068          | 3024           |
| 20    | 292288            | 8944          | 32192          |
| 50    | 11730200          | 104780        | 614544         |
| 100   | 193841600         | 848240        | 5916352        |
| 1000  | 1985585282560     | 509190592     | 8143644672     |
| 5000  | 1248197623717376  | 143543110592  | 1416681916416  |
| 10000 | 19985580989739008 | 1148444884736 | 12333455331328 |

> For $\log_b a$ = 3
> In the case of $c=4$, we can tell $W(n) \approx n^4*1.5$. 
> In the case of $c=2$, we can tell $W(n) \approx n^{3}$
> In the case of $c=3$, we can tell $W(n) \approx n^{3}\cdot 3$
>Thus,
>when $c > \log_b a$,  $W(n)= O(n^c)$.
>when $c < \log_b a$, $W(n) = O(n^{\log_ba})$.
>when $c = \log_b a$, $W(n) = O(n^{\log_ba}\log n)$.

**TODO: your answer goes here**

- 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should.

**TODO: your answer goes here**
>**Question 6 Answer:** The table of results of span go as follow,
|     n |   W_1(1) |   W_2(logn) |   W_3(n) |
|-------|----------|-------------|----------|
|    10 |        4 |       5.605 |       18 |
|    20 |        5 |       8.601 |       38 |
|    50 |        6 |      13.506 |       97 |
|   100 |        7 |      18.111 |      197 |
|  1000 |       10 |      37.786 |     1994 |
|  5000 |       13 |      56.944 |     9995 |
| 10000 |       14 |      66.154 |    19995 |

> Based on the results we got, it follows that 
> for $f(n) = 1$, $W(n) = O(1)$
> for $f(n) = \log n $, $W(n) = O(\log n)$
> for $f(n) = n$, $W(n) = O(n)$