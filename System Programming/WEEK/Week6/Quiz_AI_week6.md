# 2025 Spring SNU System Programming - Weekly Quiz (Week 6)

We have prepared some light quizzes related to class content of week 6.  
These problems have been selected from those generated by **AI tool (Cramify)**,  
based on your class ppt content.

There is no need to submit anything after reviewing this material,  
but we hope it will help you review the class content you learned this week and prepare for the quiz.

---

Weekly Quiz has two documents, one with only the problems and  
the other with both the problems and solutions.  

# Question 1

Arrange the following steps in the correct order to represent the life cycle of a C program from source code to a running process:

- Loader (execve)
- C compiler (cc1/cpp)
- Dynamic linker (ld-linux.so)
- Assembler (as)
- Linker (ld/collect2)

A) The correct order is C compiler, Assembler, Linker, Loader, and Dynamic linker.  
B) The correct order is Loader, C Compiler, Assembler, Linker, and Dynamic linker.  
C) The correct order is C compiler, Linker, Assembler, Loader, and Dynamic linker.  
D) The correct order is Assembler, C compiler, Linker, Loader, and Dynamic linker.

# Question 2

A program consists of two files, main.c and helper.c.  
main.c calls a function calculate() defined in helper.c, and accesses a global variable data also defined in helper.c.  
During the linking process, what actions does the linker take to ensure the program executes correctly?

A) The linker copies the code of calculate() and data into main.c, eliminating the need for external references.  
B) The linker resolves references to calculate() and data by finding their definitions, and then relocates them by assigning load addresses and updating references.  
C) The linker dynamically loads helper.c at runtime, resolving the symbols only when they are needed by main.c.  
D) The linker creates a mapping between the names calculate() and data and their corresponding memory addresses in helper.c, but does not modify the code.

# Question 3

Regarding the Executable and Linkable Format (ELF), which of the following statements are true?  
Indicate True or False for each statement.

a) ELF is a standard binary format used for object files, executables, and shared libraries, promoting code modularity and efficient memory usage.  

b) The ELF header contains essential information such as word size, byte ordering, file type, and machine type, enabling the system to correctly interpret and execute the binary.  

c) The .bss section in an ELF file contains initialized global and static variables, contributing to the initial memory image of the program.  

d) Relocation information within ELF files, such as found in .rel.text and .rel.data, guides the linker in adjusting addresses of code and data during the linking process.  

e) The symbol table (.symtab) in an ELF file stores information about global variables and functions, but not local variables, simplifying the linking process.  

# Question 4

Regarding the three types of object files in a system, which of the following statements are true?  
Indicate True or False for each statement.

a) Relocatable object files (.o files) contain code and data that can be combined with other relocatable object files to create an executable object file.  

b) Executable object files (e.g., a.out files) are ready to be directly loaded into memory and executed without further linking.  

c) Shared object files (.so files) are a type of relocatable object file that can be dynamically linked at either load time or runtime.  

d) Relocatable object files can be directly executed by the operating system.  

e) Shared object files are statically linked at compile time, resulting in a larger executable size.  

# Question 5

A large software project is divided into multiple source files, each responsible for a specific feature.  
Discuss how separate compilation enhances both the development process and the maintainability of this project, focusing on the aspects of modularity and efficiency.  
Specifically, address how changes to a single feature impact the overall build process.

# Question 6

The K&R malloc implementation uses a first-fit strategy with a circular linked list of free blocks.  
Discuss the advantages and disadvantages of this approach, specifically addressing its impact on memory utilization (fragmentation), execution time for malloc and free operations, and the overall complexity of implementation.

# Question 7

In dynamic memory allocation, how does a binning approach with segregated free lists improve performance compared to a single explicit free list, especially when allocating blocks of varying sizes?  
Consider both the time complexity for allocation and the potential for memory fragmentation.

# Question 8

In a dynamic memory allocator using an explicit free list, explain how the introduction of headers and footers in each memory block improves the efficiency of the `free()` operation, specifically regarding coalescing with adjacent free blocks.  
Consider a scenario where a block `B` is being freed, and both its preceding and succeeding blocks in memory are already free.  

# Question 9

In a dynamic memory allocation system, a program has just freed a block of memory at address 0x00001000 with a size of 16 bytes.  
Adjacent to this freed block, at address 0x00001010, there is another free block of 24 bytes.  
If coalescing is enabled, what will be the starting address and size of the resulting free block after the 16-byte block is freed?

A) Starting address: 0x00001000, Size: 40 bytes  
B) Starting address: 0x00001000, Size: 16 bytes  
C) Starting address: 0x00001010, Size: 24 bytes  
D) Starting address: 0x00001010, Size: 40 bytes

# Question 10

A long-running server application experiences performance degradation due to memory fragmentation.  
The current dynamic memory allocation strategy employs a first-fit approach with a single free list.  
Discuss two alternative memory allocation strategies that could mitigate this fragmentation issue and explain the advantages and disadvantages of each in this scenario.  
Consider factors such as allocation speed, memory utilization, and implementation complexity.
