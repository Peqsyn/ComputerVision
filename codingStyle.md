## CODING STYLE

We will be following the PEP-8 standard for our python formating, a link to the style guide can be found at the end
of this document. The following is a brief list of notable conventions outlined in PEP-8:
- - - - 
1. An indent must be 4 characters. (not a tab)
2. The maximum length of a line is 72 characters.
3. Multiline opperations should use () or [] when possible and / only when necessary.
4. Imports will be in the following order
	1. standard library imports
	2. third party imports
	3. local imports
5. We will use single quotes to define strings and chars unless double quotes are required for the use of single quote
6. No space around default value assignment.
	* i.e. -> def function(x, y=value)
7. Reduce white space according to order of opperation.
	* i.e. -> (a+b) * (c+d)
8. Two spaces after a sentence ending comment before the next sentence.
9. Capitalazie first letter of a comment unless absolutely necessary.
10. Class names should use 'CapWord' format. 
	* always use 'cls' for the first argument to class methods.
11. Modules should have short lowercase names.
12. Exceptions are classes and named as such.
13. Functions should be lowercase with underscores seperating words.
	* always use 'self' for the first argument to instance methods.
14. Variables follow the same convention as functions
15. Constants are all caps with underscores seperating words.
16. Non-public functions are marked by an underscore prefix
	* i.e. -> def _private_function(...):
17. Attributes of a class should be non-public by default.
18. Use def instead of lambda
- - - -

This list is not exhaustive but should give a relatively good outline of what is expected in terms of coding style.
If something cannot be found here it will very likely be on the python PEP-8 website. If not use your own
descretion.

- - - - 

## CODING FORMAT

We will be using the [Napoleon](https://pypi.org/project/sphinxcontrib-napoleon/) extension to Sphinx for it's [Google style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). Sphinx is an extremely useful tool for creating code documentation from the docstrings written for functions. Napoleon takes it one step further by making those docstrings readable. Of the two potential Napoleon formats, we will be using Google rather than NumPy.

Link [3](https://pypi.org/project/sphinxcontrib-napoleon/) give a list of all headers supported by Napoleon

Link [4](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) Provides plenty of example docstrings.


Resources:
1. [PEP 8 Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
2. [PEP 257 Docstring Convention](https://www.python.org/dev/peps/pep-0257/)
3. [Napoleon format](https://pypi.org/project/sphinxcontrib-napoleon/)
4. [Google Style Python Docstring](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)