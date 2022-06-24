# Test

2. [tests](#tests)
    *   [coverage](#use-coverage)
    
## tests
* ###### use coverage:
     I use coverage package for measure the quality of the test:
     ```text
      coverage run manage.py test
      coverage report -m
     ```
    for dont check Extra files must:
    ```text
      coverage run —omit='*/venv/*' manage.py test
    ```