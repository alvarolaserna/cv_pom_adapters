# Desktop Native

The folder for Python-TestUI is in `examples/py-testui`

Now you can install the requirements:
```bash
pip install -r examples/desktop_native/requirements.txt
```
Run the cases like this:
```bash
python -m pytest examples/desktop_native/test_cv_pom.py -s
```

The code contains the fixture for creating the CV POM Driver:

```python
    @pytest.fixture(autouse=True)
    def cv_pom_driver():
```