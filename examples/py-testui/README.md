# Python-TestUI

The folder for Python-TestUI is in `examples/py-testui`

Now you can install the requirements:

        pip install -r examples/py-testui/requirements.txt

Run the cases like this:

        python -m pytest examples/py-testui/test_cv_pom.py -s


The code contains the fixture for creating the Python-TestUI driver:


```python
    @pytest.fixture(autouse=True)
    def testui_driver():
```

and the one for creating the CV POM Driver out of the python driver (this means it has to be defined later in the code):

```python
    @pytest.fixture(autouse=True)
    def cv_pom_driver(testui_driver):
```