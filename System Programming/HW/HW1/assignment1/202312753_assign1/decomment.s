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
.L54:
	call	getchar@PLT
	movl	%eax, -4(%rbp)
	movl	-4(%rbp), %eax
	movb	%al, -17(%rbp)
	cmpl	$8, -8(%rbp)
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
	.long	.L12-.L4
	.long	.L11-.L4
	.long	.L10-.L4
	.long	.L9-.L4
	.long	.L8-.L4
	.long	.L7-.L4
	.long	.L6-.L4
	.long	.L5-.L4
	.long	.L3-.L4
	.text
.L12:
	cmpb	$10, -17(%rbp)
	jne	.L13
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	addl	$1, -16(%rbp)
	jmp	.L20
.L13:
	cmpb	$47, -17(%rbp)
	jne	.L15
	movl	$3, -8(%rbp)
	jmp	.L20
.L15:
	cmpb	$34, -17(%rbp)
	jne	.L16
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$2, -8(%rbp)
	jmp	.L20
.L16:
	cmpb	$39, -17(%rbp)
	jne	.L17
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$1, -8(%rbp)
	jmp	.L20
.L17:
	cmpb	$-1, -17(%rbp)
	jne	.L18
	movl	$0, %eax
	jmp	.L19
.L18:
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	jmp	.L20
.L10:
	cmpb	$10, -17(%rbp)
	jne	.L21
	addl	$1, -16(%rbp)
.L21:
	cmpb	$92, -17(%rbp)
	jne	.L22
	movl	$5, -8(%rbp)
.L22:
	cmpb	$34, -17(%rbp)
	jne	.L23
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$0, -8(%rbp)
	jmp	.L20
.L23:
	cmpb	$-1, -17(%rbp)
	jne	.L25
	movl	$0, %eax
	jmp	.L19
.L25:
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	jmp	.L20
.L11:
	cmpb	$10, -17(%rbp)
	jne	.L26
	addl	$1, -16(%rbp)
.L26:
	cmpb	$92, -17(%rbp)
	jne	.L27
	movl	$4, -8(%rbp)
.L27:
	cmpb	$39, -17(%rbp)
	jne	.L28
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$0, -8(%rbp)
	jmp	.L20
.L28:
	cmpb	$-1, -17(%rbp)
	jne	.L30
	movl	$0, %eax
	jmp	.L19
.L30:
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	jmp	.L20
.L8:
	cmpb	$10, -17(%rbp)
	jne	.L31
	addl	$1, -16(%rbp)
	movl	$2, -8(%rbp)
.L31:
	cmpb	$92, -17(%rbp)
	jne	.L32
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	jmp	.L20
.L32:
	cmpb	$-1, -17(%rbp)
	jne	.L34
	movl	$0, %eax
	jmp	.L19
.L34:
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$1, -8(%rbp)
	jmp	.L20
.L7:
	cmpb	$10, -17(%rbp)
	jne	.L35
	addl	$1, -16(%rbp)
	movl	$2, -8(%rbp)
.L35:
	cmpb	$92, -17(%rbp)
	jne	.L36
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	jmp	.L20
.L36:
	cmpb	$-1, -17(%rbp)
	jne	.L38
	movl	$0, %eax
	jmp	.L19
.L38:
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$2, -8(%rbp)
	jmp	.L20
.L9:
	cmpb	$47, -17(%rbp)
	jne	.L39
	movl	$32, %edi
	call	putchar@PLT
	movl	-16(%rbp), %eax
	movl	%eax, -12(%rbp)
	movl	$6, -8(%rbp)
	jmp	.L20
.L39:
	cmpb	$42, -17(%rbp)
	jne	.L41
	movl	$32, %edi
	call	putchar@PLT
	movl	-16(%rbp), %eax
	movl	%eax, -12(%rbp)
	movl	$7, -8(%rbp)
	jmp	.L20
.L41:
	cmpb	$10, -17(%rbp)
	jne	.L42
	movl	$47, %edi
	call	putchar@PLT
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	addl	$1, -16(%rbp)
	movl	$0, -8(%rbp)
	jmp	.L20
.L42:
	cmpb	$-1, -17(%rbp)
	jne	.L43
	movl	$47, %edi
	call	putchar@PLT
	movl	$0, %eax
	jmp	.L19
.L43:
	movl	$47, %edi
	call	putchar@PLT
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	movl	$0, -8(%rbp)
	jmp	.L20
.L6:
	cmpb	$10, -17(%rbp)
	jne	.L44
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	addl	$1, -16(%rbp)
	movl	$0, -8(%rbp)
	jmp	.L55
.L44:
	cmpb	$-1, -17(%rbp)
	jne	.L55
	movl	$0, %eax
	jmp	.L19
.L5:
	cmpb	$42, -17(%rbp)
	jne	.L46
	movl	$8, -8(%rbp)
	jmp	.L56
.L46:
	cmpb	$10, -17(%rbp)
	jne	.L48
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	addl	$1, -16(%rbp)
	jmp	.L56
.L48:
	cmpb	$-1, -17(%rbp)
	jne	.L56
	movq	stderr(%rip), %rax
	movl	-12(%rbp), %edx
	leaq	.LC0(%rip), %rcx
	movq	%rcx, %rsi
	movq	%rax, %rdi
	movl	$0, %eax
	call	fprintf@PLT
	movl	$1, %eax
	jmp	.L19
.L3:
	cmpb	$47, -17(%rbp)
	jne	.L49
	movl	$0, -8(%rbp)
	jmp	.L20
.L49:
	cmpb	$42, -17(%rbp)
	jne	.L51
	movl	$8, -8(%rbp)
	jmp	.L20
.L51:
	cmpb	$10, -17(%rbp)
	jne	.L52
	movsbl	-17(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	addl	$1, -16(%rbp)
	jmp	.L20
.L52:
	cmpb	$-1, -17(%rbp)
	jne	.L53
	movq	stderr(%rip), %rax
	movl	-12(%rbp), %edx
	leaq	.LC0(%rip), %rcx
	movq	%rcx, %rsi
	movq	%rax, %rdi
	movl	$0, %eax
	call	fprintf@PLT
	movl	$1, %eax
	jmp	.L19
.L53:
	movl	$7, -8(%rbp)
	jmp	.L20
.L2:
	movl	$1, %eax
	jmp	.L19
.L55:
	nop
	jmp	.L54
.L56:
	nop
.L20:
	jmp	.L54
.L19:
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
