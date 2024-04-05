# playwright-js-cvpom



## Install

- first of all, install all the necessary depenencies for Playwright
    - npx playwright install 
- Also install all the dependencies for cv_pom and run server:
    - git clone https://github.com/testdevlab/cv_pom.git
    - python -m pip install requirements.txt
    - python server.py --model ../../../resources/best.pt

<pre>
# Setup virtual environment and activate it
python -m pip install --upgrade pip

python -m venv venv
. venv/bin/activate
python -m pip install --upgrade pip

# Install requirements
python -m pip install -r requirements.txt
</pre>

## Run cases

First you will have to run the cv_sdk server:

<pre>
cd cv_sdk/
python server.py --model ../resources/best.pt
</pre>
