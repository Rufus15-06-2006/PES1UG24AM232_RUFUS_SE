\# Lab 5: Static Code Analysis — Reflection



Static code analysis helped identify code-quality issues, potential security vulnerabilities, and formatting violations without executing the program.



Pylint identified issues such as mutable default arguments, missing docstrings, naming violations, and unused variables. Bandit detected security risks, including unsafe expression evaluation, weak hashing, insecure PIN generation, shell execution, and a hardcoded API token. Flake8 identified formatting violations and unused imports.



The code was improved by replacing unsafe operations with safer alternatives, validating inputs, improving file handling, and applying consistent naming and formatting conventions.



The Pylint score improved from 4.00/10 to 10.00/10. The final Bandit scan reported no issues, and Flake8 reported no violations.



This exercise demonstrated that static analysis improves code quality and helps identify potential security problems. However, clean static-analysis reports do not guarantee functional correctness, so runtime testing remains necessary.

