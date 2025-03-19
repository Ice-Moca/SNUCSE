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
	movl	$1, -28(%rbp)
	movl	$-1, -16(%rbp)
	movl	$1, -24(%rbp)
	movl	$1, -12(%rbp)
	movl	$1, -8(%rbp)
.L23:
	movl	$0, -20(%rbp)
	call	getchar@PLT
	movl	%eax, -4(%rbp)
	cmpl	$-1, -4(%rbp)
	je	.L24
	movl	-4(%rbp), %eax
	movb	%al, -29(%rbp)
	cmpb	$-1, -29(%rbp)
	jne	.L4
	movl	$1, -20(%rbp)
.L4:
	cmpb	$34, -29(%rbp)
	jne	.L5
	cmpl	$1, -24(%rbp)
	jne	.L5
	cmpl	$1, -8(%rbp)
	jne	.L5
	movsbl	-29(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	cmpl	$0, -12(%rbp)
	sete	%al
	movzbl	%al, %eax
	movl	%eax, -12(%rbp)
	jmp	.L3
.L5:
	cmpb	$39, -29(%rbp)
	jne	.L6
	cmpl	$1, -24(%rbp)
	jne	.L6
	cmpl	$1, -12(%rbp)
	jne	.L6
	movsbl	-29(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	cmpl	$0, -8(%rbp)
	sete	%al
	movzbl	%al, %eax
	movl	%eax, -8(%rbp)
	jmp	.L3
.L6:
	cmpb	$47, -29(%rbp)
	jne	.L7
	cmpl	$1, -12(%rbp)
	jne	.L7
	cmpl	$1, -8(%rbp)
	jne	.L7
	call	getchar@PLT
	movl	%eax, -4(%rbp)
	movl	-4(%rbp), %eax
	movb	%al, -29(%rbp)
	cmpb	$47, -29(%rbp)
	jne	.L8
	movl	-28(%rbp), %eax
	movl	%eax, -16(%rbp)
	movl	$0, -24(%rbp)
	movl	$32, %edi
	call	putchar@PLT
.L11:
	call	getchar@PLT
	movl	%eax, -4(%rbp)
	movl	-4(%rbp), %eax
	movb	%al, -29(%rbp)
	cmpb	$10, -29(%rbp)
	jne	.L11
	addl	$1, -28(%rbp)
	movl	$1, -24(%rbp)
	movsbl	-29(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	nop
	jmp	.L20
.L8:
	cmpb	$42, -29(%rbp)
	jne	.L13
	movl	-28(%rbp), %eax
	movl	%eax, -16(%rbp)
	movl	$32, %edi
	call	putchar@PLT
	movl	$0, -24(%rbp)
	jmp	.L14
.L19:
	call	getchar@PLT
	movl	%eax, -4(%rbp)
	movl	-4(%rbp), %eax
	movb	%al, -29(%rbp)
	cmpb	$10, -29(%rbp)
	jne	.L15
	movl	$10, %edi
	call	putchar@PLT
	addl	$1, -28(%rbp)
.L15:
	cmpb	$42, -29(%rbp)
	jne	.L16
	call	getchar@PLT
	movl	%eax, -4(%rbp)
	cmpl	$47, -4(%rbp)
	jne	.L17
	movl	$1, -24(%rbp)
	jmp	.L16
.L17:
	movq	stdin(%rip), %rdx
	movl	-4(%rbp), %eax
	movq	%rdx, %rsi
	movl	%eax, %edi
	call	ungetc@PLT
.L16:
	cmpb	$-1, -29(%rbp)
	jne	.L14
	movl	$1, -20(%rbp)
	movq	stderr(%rip), %rax
	movl	-16(%rbp), %edx
	leaq	.LC0(%rip), %rcx
	movq	%rcx, %rsi
	movq	%rax, %rdi
	movl	$0, %eax
	call	fprintf@PLT
	movl	$1, %eax
	jmp	.L18
.L14:
	cmpl	$0, -24(%rbp)
	je	.L19
	jmp	.L20
.L13:
	movl	$47, %edi
	call	putchar@PLT
	movsbl	-29(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
	jmp	.L20
.L7:
	cmpb	$10, -29(%rbp)
	jne	.L21
	addl	$1, -28(%rbp)
.L21:
	cmpl	$0, -20(%rbp)
	jne	.L25
	movsbl	-29(%rbp), %eax
	movl	%eax, %edi
	call	putchar@PLT
.L20:
	jmp	.L23
.L24:
	nop
	jmp	.L3
.L25:
	nop
.L3:
	movl	$0, %eax
.L18:
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
