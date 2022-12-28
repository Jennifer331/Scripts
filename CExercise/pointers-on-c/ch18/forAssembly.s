	.file	"forAssembly.c"
	.text
	.data
	.align 4
_staticInt:
	.long	5
	.section .rdata,"dr"
	.align 4
LC0:
	.ascii "%d, %d, %d, %d, %d, %d, %d, %d\12\0"
	.text
	.globl	_f
	.def	_f;	.scl	2;	.type	32;	.endef
_f:
LFB13:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%edi
	pushl	%esi
	pushl	%ebx
	subl	$76, %esp
	.cfi_offset 7, -12
	.cfi_offset 6, -16
	.cfi_offset 3, -20
	movl	$1, %esi
	movl	$2, %edi
	movl	$3, -28(%ebp)
	movl	$4, -32(%ebp)
	movl	$5, %ecx
	movl	$6, %edx
	movl	$7, %eax
	movl	$8, %ebx
	movl	%ebx, 32(%esp)
	movl	%eax, 28(%esp)
	movl	%edx, 24(%esp)
	movl	%ecx, 20(%esp)
	movl	-32(%ebp), %eax
	movl	%eax, 16(%esp)
	movl	-28(%ebp), %eax
	movl	%eax, 12(%esp)
	movl	%edi, 8(%esp)
	movl	%esi, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	nop
	addl	$76, %esp
	popl	%ebx
	.cfi_restore 3
	popl	%esi
	.cfi_restore 6
	popl	%edi
	.cfi_restore 7
	popl	%ebp
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE13:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC1:
	.ascii "Test for assembly\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB14:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$LC1, (%esp)
	call	_printf
	nop
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE14:
	.ident	"GCC: (i686-posix-dwarf-rev0, Built by MinGW-W64 project) 8.1.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
