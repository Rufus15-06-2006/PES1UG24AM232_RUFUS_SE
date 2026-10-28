\# Lab 5: Static Code Analysis — Reflection



Static code analysis helped identify potential bugs, security weaknesses,

and style violations without requiring the program to execute.



Pylint identified code-quality problems, including the mutable default

argument, missing docstrings, naming violations and unused variables.

Bandit identified security risks such as unsafe expression evaluation,

weak hashing, insecure PIN generation, shell execution and a hardcoded

API token. Flake8 detected formatting problems, unused imports and

other PEP 8 violations.



The code was improved by replacing unsafe operations with safer

alternatives, validating inputs, improving file handling, and applying

consistent naming and formatting conventions.



The Pylint score improved from 4.00/10 to 10.00/10. The final Bandit

scan reported no issues, and Flake8 reported no violations.



This exercise demonstrated that static analysis can improve code

quality and security before deployment. However, clean static-analysis

reports do not guarantee that the program is functionally correct;

runtime testing is also necessary.

