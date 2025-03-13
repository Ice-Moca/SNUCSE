# Decommenter

(This programming assignment is slightly modified from an assignment of Princeton COS217.)

Your task is to write a C program named *decomment* that performs a subset of the de-comment job of the C preprocessor. Your program should (1) read C source code from the standard input stream, (2) write that same text to the standard output stream with each comment replaced by a space, and (3) write error and warning messages as appropriate to the standard error stream. A typical execution of your program from the shell might look like this:

`./decomment < somefile.c > somefilewithoutcomments.c 2> errorandwarningmessages`

## Important Dates

| Date | Description |
|:---  |:--- |
| Thursday, March 20, 21:00 | Submission deadline |

## Requirements

In the following examples a space character is shown as "<sub>s</sub>" and a newline character as "<sub>n</sub>".

#### (1) Your program should replace each comment with a space. Examples:

|         Standard Input Stream          |           Standard Output Stream           | Standard Error Stream |
| :------------------------------------: | :----------------------------------------: | --------------------- |
|       abc/\*def*/ghi<sub>n</sub>       |       abc<sub>s</sub>ghi<sub>n</sub>       |                       |
| abc/\*def*/<sub>s</sub>ghi<sub>n</sub> | abc<sub>s</sub><sub>s</sub>ghi<sub>n</sub> |                       |
| abc<sub>s</sub>/\*def*/ghi<sub>n</sub> | abc<sub>s</sub><sub>s</sub>ghi<sub>n</sub> |                       |

#### (2) Your program should support both types of comments. One is a single line comment in the form of (//...) and the other is a multi-line comment in the form of (/\*...\*/). Your program should add blank lines as necessary to preserve the original line numbering. Examples: 

|                          Standard Input Stream                          |                        Standard Output Stream                         | Standard Error Stream |
| :---------------------------------------------------------------------: | :-------------------------------------------------------------------: | --------------------- |
|                          abc//def<sub>n</sub>                           |                      abc<sub>s</sub><sub>n</sub>                      |                       |
|        abc/\*def<sub>n</sub>ghi*/jkl<sub>n</sub>mno<sub>n</sub>         |       abc<sub>s</sub><sub>n</sub>jkl<sub>n</sub>mno<sub>n</sub>       |                       |
| abc/\*def<sub>n</sub>ghi<sub>n</sub>jkl*/mno<sub>n</sub>pqr<sub>n</sub> | abc<sub>s</sub><sub>n</sub><sub>n</sub>mno<sub>n</sub>pqr<sub>n</sub> |                       |

#### (3) A multi-line comment begins when the preprocess encounters "/\*" for the first time. The comment ends when it encounters "\*/" after the comment begins. Everything between "/\*" and "\*/" pair is a comment. Example:

|         Standard Input Stream          |  Standard Output Stream  | Standard Error Stream |
| :------------------------------------: | :----------------------: | --------------------- |
| abc/\*def/*ghi\*/jkl\*/mno<sub>n</sub> | abc<sub>s</sub>jkl*/mno<sub>n</sub> |                       |

#### (4a) Exception: Do not de-comment the comment when it is a part of the string. Examples:

|       Standard Input Stream        |       Standard Output Stream       | Standard Error Stream |
| :--------------------------------: | :--------------------------------: | --------------------- |
| abc"def/\*ghi*/jkl"mno<sub>n</sub> | abc"def/\*ghi*/jkl"mno<sub>n</sub> |                       |
| abc"def//ghi*/jkl"mno<sub>n</sub>  | abc"def//ghi*/jkl"mno<sub>n</sub>  |                       |
| abc//"defghi*/jkl"mno<sub>n</sub>  |    abc<sub>s</sub><sub>n</sub>     |                       |
| abc/\*def"ghi"jkl*/mno<sub>n</sub> |   abc<sub>s</sub>mno<sub>n</sub>   |                       |
| abc/\*def"ghijkl*/mno<sub>n</sub>  |   abc<sub>s</sub>mno<sub>n</sub>   |                       |

#### (4b) Exception: Do not de-comment the comment when the comment is a part of the character constant. Examples:

|       Standard Input Stream        |       Standard Output Stream       | Standard Error Stream |
| :--------------------------------: | :--------------------------------: | --------------------- |
| abc'def/\*ghi*/jkl'mno<sub>n</sub> | abc'def/\*ghi*/jkl'mno<sub>n</sub> |                       |
| abc/\*def'ghi'jkl*/mno<sub>n</sub> |   abc<sub>s</sub>mno<sub>n</sub>   |                       |
| abc/\*def'ghijkl*/mno<sub>n</sub>  |   abc<sub>s</sub>mno<sub>n</sub>   |                       |

Clearly, this is an erroneous statement. The de-commenter should not worry. The compiler will handle this error.

#### (5a) Process backslash '\\' and the following character as the ordinary characters when they are within the string constant. Note that backslash ('\\') may appear as the Korean Won (₩) symbol in your screen. Your program should consider text of the form ("...\\"...") to be a valid string constant which happens to contain the double quote character. Examples:

|     Standard Input Stream     |    Standard Output Stream     | Standard Error Stream |
| :---------------------------: | :---------------------------: | --------------------- |
| abc"def\\"ghi"jkl<sub>n</sub> | abc"def\\"ghi"jkl<sub>n</sub> |                       |
| abc"def\\'ghi"jkl<sub>n</sub> | abc"def\\'ghi"jkl<sub>n</sub> |                       |

#### (5b) Similarly, process backslash '\\' and the following character as the ordinary characters when they are within the character constant. Your program should consider text of the form ('...\\'...') to be a valid character constant which happens to contain the quote character. Examples:

|     Standard Input Stream     |    Standard Output Stream     | Standard Error Stream |
| :---------------------------: | :---------------------------: | --------------------- |
| abc'def\\'ghi'jkl<sub>n</sub> | abc'def\\'ghi'jkl<sub>n</sub> |                       |
| abc'def\\"ghi'jkl<sub>n</sub> | abc'def\\"ghi'jkl<sub>n</sub> |                       |

Note that the C compiler would consider both of those examples to be erroneous (multiple characters in a character constant). But many C preprocessors would not, and your program should not.

#### (6a) Your program should handle newline characters in C string constants without generating errors or warnings. Examples:

|                      Standard Input Stream                       |                        Standard Output Stream                        | Standard Error Stream |
| :--------------------------------------------------------------: | :------------------------------------------------------------------: | --------------------- |
|              abc"def<sub>n</sub>ghi"jkl<sub>n</sub>              |                abc"def<sub>n</sub>ghi"jkl<sub>n</sub>                |                       |
| abc"def<sub>n</sub>ghi<sub>n</sub>jkl"mno/\*pqr*/stu<sub>n</sub> | abc"def<sub>n</sub>ghi<sub>n</sub>jkl"mno<sub>s</sub>stu<sub>n</sub> |                       |

Note that a C compiler would consider those examples to be erroneous (newline character in a string constant). But many C preprocessors would not, and your program should not.

#### (6b) Similarly, your program should handle newline characters in C character constants without generating errors or warnings. Examples:

|                      Standard Input Stream                       |                        Standard Output Stream                        | Standard Error Stream |
| :--------------------------------------------------------------: | :------------------------------------------------------------------: | --------------------- |
|              abc'def<sub>n</sub>ghi'jkl<sub>n</sub>              |                abc'def<sub>n</sub>ghi'jkl<sub>n</sub>                |                       |
| abc'def<sub>n</sub>ghi<sub>n</sub>jkl'mno/\*pqr*/stu<sub>n</sub> | abc'def<sub>n</sub>ghi<sub>n</sub>jkl'mno<sub>s</sub>stu<sub>n</sub> |                       |

Note that a C compiler would consider those examples to be erroneous (multiple characters in a character constant, newline character in a character constant). But many C preprocessors would not, and your program should not.

#### (7) Your program should handle unterminated string and character constants without generating errors or warnings. Examples:

|     Standard Input Stream      |     Standard Output Stream     | Standard Error Stream |
| :----------------------------: | :----------------------------: | --------------------- |
| abc"def/\*ghi*/jkl<sub>n</sub> | abc"def/\*ghi*/jkl<sub>n</sub> |                       |
| abc'def/\*ghi*/jkl<sub>n</sub> | abc'def/\*ghi*/jkl<sub>n</sub> |                       |

Note that a C compiler would consider those examples to be erroneous (unterminated string constant, unterminated character constant, multiple characters in a character constant). But many C preprocessors would not, and your program should not.

#### (8) If your program detects end-of-file before a comment is terminated, it should write the message "Error: line X: unterminated comment" to the standard error stream. "X" should be the number of the line on which the unterminated comment begins. Examples:

|          Standard Input Stream           |            Standard Output Stream             | Standard Error Stream                                                                       |
| :--------------------------------------: | :-------------------------------------------: | ------------------------------------------------------------------------------------------- |
|   abc/\*def<sub>n</sub>ghi<sub>n</sub>   |    abc<sub>s</sub><sub>n</sub><sub>n</sub>    | Error:<sub>s</sub>line<sub>s</sub>1:<sub>s</sub>unterminated<sub>s</sub>comment<sub>n</sub> |
|   abcdef<sub>n</sub>ghi/*<sub>n</sub>    | abcdef<sub>n</sub>ghi<sub>s</sub><sub>n</sub> | Error:<sub>s</sub>line<sub>s</sub>2:<sub>s</sub>unterminated<sub>s</sub>comment<sub>n</sub> |
| abc/\*def/ghi<sub>n</sub>jkl<sub>n</sub> |    abc<sub>s</sub><sub>n</sub><sub>n</sub>    | Error:<sub>s</sub>line<sub>s</sub>1:<sub>s</sub>unterminated<sub>s</sub>comment<sub>n</sub> |
| abc/\*def*ghi<sub>n</sub>jkl<sub>n</sub> |    abc<sub>s</sub><sub>n</sub><sub>n</sub>    | Error:<sub>s</sub>line<sub>s</sub>1:<sub>s</sub>unterminated<sub>s</sub>comment<sub>n</sub> |
|  abc/\*def<sub>n</sub>ghi*<sub>n</sub>   |    abc<sub>s</sub><sub>n</sub><sub>n</sub>    | Error:<sub>s</sub>line<sub>s</sub>1:<sub>s</sub>unterminated<sub>s</sub>comment<sub>n</sub> |
|  abc/\*def<sub>n</sub>ghi/<sub>n</sub>   |    abc<sub>s</sub><sub>n</sub><sub>n</sub>    | Error:<sub>s</sub>line<sub>s</sub>1:<sub>s</sub>unterminated<sub>s</sub>comment<sub>n</sub> |

#### (9) Your program (more precisely, its main function) should return EXIT_FAILURE if it detects an unterminated comment and so was unable to remove comments properly. Otherwise it should return EXIT_SUCCESS or, equivalently 0. Note that EXIT_FAILURE and EXIT_SUCCESS are defined as macros in stdlib.h, so add #include <stdlib.h> to your C code.

#### (10) Your program should work for standard input lines of any length.

#### (11) You may assume that the final line of the standard input stream ends with a newline character.

#### (12) Your program may assume that the backslash-newline character sequence does not occur in the standard input stream. That is, your program may assume that logical lines are identical to physical lines in the standard input stream.

In this assignment, **you may place all source code in a single file.** Subsequent assignments will ask you to write programs consisting of multiple source code files.

We suggest that your program use the standard C getchar() function to read characters from the standard input stream. To print out an error message to the standard error stream, you can use fprintf(stderr, "error string\n"); and if you replace stderr with stdout in fprintf(), the output to the standard output stream. That is, printf(...) is actually the same as fprintf(stdout, ...).

## Logistics

### Step 1: Design a State Transition Diagram (also known as Deterministic Finite Automata)
Express the algorithm of decommentor using state transition diagram, i.e. with the traditional "ovals and labeled arrows" notation. The oval and arrow correspond to the state and input to the state (or action), respectively. First, define a set of states for your program. Most importantly, define "begin" state and "end" state. There can be two end states in your diagram: success and failure. Give each state a descriptive name. Let each arrow represent a transition from one state to another. Label each arrow with a character, or a class of characters, that causes the transition from state to another to occur. We encourage (but do not require) you also to label each arrow with action(s) that should occur (e.g. "print the character") when the corresponding transition occurs.

Express as much of the program's logic as you can within your state transition diagram. The more logic you express in your state transition diagram, the better your grade on the state transition diagram will be. To properly report unterminated comments, your program must contain logic to keep track of the current line number of the standard input stream. You need not show that logic in your state transition diagram.

The state transition diagram you draw is formally called Finite State Automata (FSA) or Finite State Machine (FSM). Finite State Machine is defined by the tuple of five elements: (set of states, a set of input symbols, transition function, begin state, a set of termination states). Further interested students are referred to "Kohavi et al. Switching and Finite Automata Theory, 3rd ed" or <a href="https://www.amazon.com/Switching-Finite-Automata-Theory-Kohavi/dp/0521857481">here</a>.

### Step 2: Create Source Code
Create the source code for your state transition diagram. Name it decomment.c.

### Step 3: Preprocess, Compile, Assemble, and Link
Use the gcc800 command to preprocess, compile, assemble, and link your program. Perform each step individually, and examine the intermediate results to the extent possible. Name the intermediate files as decomment.i, decomment.s, decomment.o after preprocessing, compiling, assembling, respectively,

### Step 4: Execute
Execute your program multiple times on various input files that test all logical paths through your code. For the test, use the sample files provided here.

(1) Download all files to your project directory. You will find sampledecomment and 6 test C source files. You need to make sampledecomment executable (by changing file permission) by

`chmod u+x sampledecomment`

(2) sampledecomment is an executable version of a correct assignment solution. For full credit, your program should write exactly (character for character) the same data to the standard output stream and the standard error stream as sampledecomment does. You should test your program using commands similar to these:

`./sampledecomment < somefile.c > output1 2> errors1`

`./decomment < somefile.c > output2 2> errors2`

`diff -c output1 output2`

`diff -c errors1 errors2`

`rm output1 errors1 output2 errors2`

The Unix `diff` command finds differences between two given files. The executions of the `diff` command shown above should produce no output. If the command `diff -c output1 output2` produces output, then sampledecomment and your program have written different characters to the standard output stream. Similarly, if the command `diff -c errors1 errors2` produces output, then sampledecomment and your program have written different characters to the standard error stream.

You also should test your program against its own source code using a command sequence such as this:

`./sampledecomment < decomment.c > output1 2> errors1`

`./decomment < decomment.c > output2 2> errors2`

`diff -c output1 output2`

`diff -c errors1 errors2`

`rm output1 errors1 output2 errors2`

### Step 5: Create a readme File

Create readme file (not readme.txt, or README, or Readme, etc.). The readme file should contain the followings:

Your name, student ID, and the assignment number.
A description of whatever help (if any) you received from others while doing the assignment, and the names of any individuals with whom you collaborated, as prescribed by the course Policy web page.
(Optionally) An indication of how much time you spent doing the assignment.
(Optionally) Your assessment of the assignment: Did it help you to learn? What did it help you to learn? Do you have any suggestions for improvement? Etc.
(Optionally) Any information that will help us to grade your work in the most favorable light. In particular you should describe all known bugs.
Descriptions of your code should not be in the readme file. Instead they should be integrated into your code as comments.

Your readme file should be a plain text file. Don't create your readme file using Microsoft Word, Hangul (HWP) or any other word processor.

### Step 6: Submit

Your submission should include your decomment.c / decomment.i / decomment.s / decomment.o files, readme file, and state transition diagram. You can use drawing software (e.g. Microsoft PowerPoint) for your transition diagram. Or you can draw it on a paper, and subtmit the captured image, e.g., *.pdf or *.jpg. Either way, please name the file as dfa.xxx like dfa.pptx, dfa.png, dfa.pdf, etc.. Make sure that the image is readable with good enough resolution.
Create a local directory named 'YourID_assign1' and place all files into that directory. Example:   

```
202500000_assign1
  |-decomment.c (source file)
  |-decomment.i (preprocessed file)
  |-decomment.s (assembly file)
  |-decomment.o (object file)
  |-readme
  `-dfa.pptx or dfa.pdf or dfa.jpg …
```

Then, compress the submission files into tar format using the following command (assuming YourID is 202500000):   
   
`mkdir 202500000_assign1`

`mv decomment.c decomment.i decomment.o decomment.s 202500000_assign1/`

`mv readme dfa.pptx 202501234_assign1`

`tar zcf 202500000_assign1.tar.gz 202500000_assign1`   

Upload your submission file (20250000_assign1.tar.gz) to eTL submission page. We do not accept e-mail submission (unless our course eTL page is down).

## Grading
We will grade your work on two kinds of quality: quality from the user's point of view, and quality from the programmer's point of view. To encourage good coding practices, we will deduct points if gcc800 generates warning messages.

**From the user's point of view**, a program has quality if it behaves as it should. The correct behavior of your program is defined by the previous sections of this assignment specification, and by the behavior of the given sampledecomment program.

**From the programmer's point of view**, a program has quality if it is well styled and thereby easy to maintain. Here are the examples:

**Names**: You should use a clear and consistent style for variable and function names. One example of such a style is to prefix each variable name with characters that indicate its type. For example, the prefix c might indicate that the variable is of type char, i might indicate int, pc might mean char*, ui might mean unsigned int, etc. But it is fine to use another style -- a style that does not include the type of a variable in its name -- as long as the result is a clear and readable program.

**Comments**: Each source code file should begin with a comment that includes your name, the number of the assignment, and the name of the file.

**Comments**: Each function -- especially the main function -- should begin with a comment that describes what the function does from the point of view of the caller. (The comment should not describe how the function works.) It should do so by explicitly referring to the function's parameters and return value. The comment also should state what, if anything, the function reads from the standard input stream or any other stream, and what, if anything, the function writes to the standard output stream, the standard error stream, or any other stream. Finally, the function's comment should state which global variables the function uses or affects. In short, a function's comments should describe the flow of data into and out of the function.

**Function modularity (most important)**: Your program should not consist of one large main function. Instead your program should consist of multiple small functions, each of which performs a single well-defined task. For example, you might create one function to implement each state of your DFA.

**Line lengths**: Limit line lengths in your source code to 72 characters. This should fit the most terminal without breaking one line into two or more lines just for display.
