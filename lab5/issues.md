\# Lab 5: Static Code Analysis — Issues and Fixes



| Issue | Tool | Fix |

|---|---|---|

| Mutable default argument | Pylint | Replaced the shared list default with None and initialized it inside the function. |

| Unsafe eval() | Pylint, Bandit | Replaced dynamic expression evaluation with a validated numeric surcharge rate. |

| Weak MD5 hash | Bandit | Replaced MD5 with SHA-256. |

| Insecure random PIN | Bandit | Replaced random.randint() with secrets.randbelow(). |

| Shell command execution | Bandit | Removed os.system() and used print() instead. |

| Hardcoded API token | Bandit | Read the token from an environment variable and stopped printing its value. |

| Bare exception | Pylint, Flake8, Bandit | Replaced broad exception handling with explicit validation. |

| File handling and encoding | Pylint | Used a context manager and explicitly specified UTF-8 encoding. |

| Naming, docstrings and formatting | Pylint, Flake8 | Applied snake\_case names, docstrings, line formatting and a final newline. |



\## Final Results



\- Pylint: 10.00/10

\- Bandit: No issues identified

\- Flake8: No violations

