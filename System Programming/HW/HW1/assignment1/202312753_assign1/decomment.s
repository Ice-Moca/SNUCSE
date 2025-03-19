	.file	"decomment.c"
	.text
	.section	.rodata
	.align 8
.LC0:
	.string	"Error: line %d: unterminated comment\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movl	$1, -16(%rbp)
	movl	$-1, -12(%rbp)
	movl	$0, -8(%rbp)
.L42:
	call	getchar@PLT
	movl	%eax, -4(%rbp)
	movl	-4(%rbp), %eax
	movb	%al, -17(%rbp)
	cmpl	$6, -8(%rbp)
	ja	.L2
	movl	-8(%rbp), %eax
	leaq	0(,%rax,4), %rdx
	leaq	.L4(%rip), %rax
	movl	(%rdx,%rax), %eax
	cltq
	leaq	.L4(%rip), %rdx
	addq	%rdx, %rax
	notrack jmp	*%rax
	.section	.rodata
	.align 4
	.align 4
.L4:
	.long	.L10-.L4
	.long	.L9-.L4
	.long	.L8-.L4
	.long	.L7-.L4
	.long	.L6-.L4
	.long	.L5-.L4
	.long	.L3-.L4
	.text
.L10:
	cmpb	$10, -17(%rbp)
	jne	.L11
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	addl	$1, -16(%rbp)
	jmp	.L18
.L11:
	cmpb	$47, -17(%rbp)
	jne	.L13
	movl	$3, -8(%rbp)
	jmp	.L18
.L13:
	cmpb	$34, -17(%rbp)
	jne	.L14
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$2, -8(%rbp)
	jmp	.L18
.L14:
	cmpb	$39, -17(%rbp)
	jne	.L15
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$1, -8(%rbp)
	jmp	.L18
.L15:
	cmpb	$-1, -17(%rbp)
	jne	.L16
	movl	$0, %eax
	jmp	.L17
.L16:
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	jmp	.L18
.L7:
	cmpb	$47, -17(%rbp)
	jne	.L19
	movl	$32, %edi
	call	putchar@PLT
	movl	-16(%rbp), %eax
	movl	%eax, -12(%rbp)
	movl	$4, -8(%rbp)
	jmp	.L18
.L19:
	cmpb	$42, -17(%rbp)
	jne	.L21
	movl	$32, %edi
	call	putchar@PLT
	movl	-16(%rbp), %eax
	movl	%eax, -12(%rbp)
	movl	$5, -8(%rbp)
	jmp	.L18
.L21:
	cmpb	$10, -17(%rbp)
	jne	.L22
	movl	$47, %edi
	call	putchar@PLT
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	addl	$1, -16(%rbp)
	movl	$0, -8(%rbp)
	jmp	.L18
.L22:
	cmpb	$-1, -17(%rbp)
	jne	.L23
	movl	$47, %edi
	call	putchar@PLT
	movl	$0, %eax
	jmp	.L17
.L23:
	movl	$47, %edi
	call	putchar@PLT
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$0, -8(%rbp)
	jmp	.L18
.L8:
	cmpb	$10, -17(%rbp)
	jne	.L24
	addl	$1, -16(%rbp)
.L24:
	cmpb	$34, -17(%rbp)
	jne	.L25
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$0, -8(%rbp)
	jmp	.L18
.L25:
	cmpb	$-1, -17(%rbp)
	jne	.L27
	movl	$0, %eax
	jmp	.L17
.L27:
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	jmp	.L18
.L9:
	cmpb	$10, -17(%rbp)
	jne	.L28
	addl	$1, -16(%rbp)
.L28:
	cmpb	$39, -17(%rbp)
	jne	.L29
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$0, -8(%rbp)
	jmp	.L18
.L29:
	cmpb	$-1, -17(%rbp)
	jne	.L31
	movl	$0, %eax
	jmp	.L17
.L31:
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	jmp	.L18
.L6:
	cmpb	$10, -17(%rbp)
	jne	.L32
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	addl	$1, -16(%rbp)
	movl	$0, -8(%rbp)
	jmp	.L43
.L32:
	cmpb	$-1, -17(%rbp)
	jne	.L43
	movl	$0, %eax
	jmp	.L17
.L5:
	cmpb	$42, -17(%rbp)
	jne	.L34
	movl	$6, -8(%rbp)
	jmp	.L44
.L34:
	cmpb	$10, -17(%rbp)
	jne	.L36
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	addl	$1, -16(%rbp)
	jmp	.L44
.L36:
	cmpb	$-1, -17(%rbp)
	jne	.L44
	movq	stderr(%rip), %rax
	movl	-12(%rbp), %edx
	leaq	.LC0(%rip), %rcx
	movq	%rcx, %rsi
	movq	%rax, %rdi
	movl	$0, %eax
	call	fprintf@PLT
	movl	$1, %eax
	jmp	.L17
.L3:
	cmpb	$47, -17(%rbp)
	jne	.L37
	movl	$0, -8(%rbp)
	jmp	.L18
.L37:
	cmpb	$42, -17(%rbp)
	jne	.L39
	movl	$6, -8(%rbp)
	jmp	.L18
.L39:
	cmpb	$10, -17(%rbp)
	jne	.L40
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	addl	$1, -16(%rbp)
	jmp	.L18
.L40:
	cmpb	$-1, -17(%rbp)
	jne	.L41
	movq	stderr(%rip), %rax
	movl	-12(%rbp), %edx
	leaq	.LC0(%rip), %rcx
	movq	%rcx, %rsi
	movq	%rax, %rdi
	movl	$0, %eax
	call	fprintf@PLT
	movl	$1, %eax
	jmp	.L17
.L41:
	movl	$5, -8(%rbp)
	jmp	.L18
.L2:
	movl	$1, %eax
	jmp	.L17
.L43:
	nop
	jmp	.L42
.L44:
	nop
.L18:
	jmp	.L42
.L17:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
