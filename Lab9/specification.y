%{
#include <stdio.h>
%}

%token IF
%token ELSE
%token THEN
%token WHILE
%token FOR
%token DO
%token INT 
%token CHAR
%token STRING
%token FLOAT
%token BOOL
%token READ
%token PRINT
%token ID

%left '+' 
%left '-'
%left DIV
%left MOD
%left '*'
%left '/'
%left OR
%left AND

%%

type:   INT
	| CHAR
	| STRING
	| FLOAT
	| BOOL
	;

expression: factor
	    | expression '+' expression
	    | expression '-' expression
	    | expression '*' expression
	    | expression '/' expression
	    | expression DIV expression
	    | expression MOD expression
	    ;

condition: logical_expression
	   | expression rel_op expression
	   ;

logical_expression: logical_factor
	  	    | logical_expression AND logical_expression
		    | logical_expression OR logical_expression
		    ;

rel_op: '='
	| '<'
	| '<='
	| '>='
	| '>'
	;

instruction: while_instruction
	     | if_instruction
	     | read_instruction
	     | print_instruction
	     ;

while_instruction: WHILE condition DO instruction
		   ;

if_instruction: IF condition THEN instruction else_branch
		;

else_branch: ELSE instruction
	     ;

read_instruction: READ variable
		  ;

print_instruction: PRINT variable
		   ;

variable: ID


