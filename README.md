# Simple Lexical Analyzer in Python

## Overview
This project is a basic lexical analyzer (lexer) built using Python.

It takes source code as input and classifies tokens into:
- Keywords
- Identifiers
- Operators
- Symbols
- Integers / Floats

## Objective
The main objective of this project is to understand the first stage of compiler design: lexical analysis.

## Features
- Tokenizes input source code
- Identifies basic keywords and operators
- Classifies identifiers and numeric values
- Demonstrates simplified compiler frontend logic

## Technologies Used
- Python
- Regular Expressions (re module)

## Example Input
int x = 10;

## Example Output
int        --> Keyword
x          --> Identifier
=          --> Operator
10         --> Integer
;          --> Symbol
