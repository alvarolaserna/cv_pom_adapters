# playwright-js-cvpom



## Install

move to playwright folder:

    cd examples/playwrigth-ts/


- first of all, install all the necessary depenencies for Playwright
    - npx playwright install 
  - Also install all the dependencies for cv_pom and run server:
      - git clone https://github.com/testdevlab/cv_pom.git
      - cd cv_pom
      - python -m pip install requirements.txt


    # Setup virtual environment and activate it
    python -m pip install --upgrade pip

    python -m venv venv
    . venv/bin/activate
    python -m pip install --upgrade pip

    # Install requirements
    python -m pip install -r requirements.txt

## Run cases

First you will have to run the cv_sdk server:

    cd cv_pom/
    python server.py --model ../../../resources/best.pt


in a different terminal run the playwright test:

    npx playwright test

or headed:

    npx playwright test --headed

