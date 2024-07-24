# playwright-js-cvpom

## Install

move to playwright folder:

```bash
cd examples/playwrigth-ts/
```

- first of all, install all the necessary depenencies for Playwright
```bash 
npx playwright install
```
  - Also install all the dependencies for cv_pom and run server:
```bash 
git clone https://github.com/testdevlab/cv_pom.git
cd cv_pom
```
```bash
# Setup virtual environment and activate it
python -m pip install --upgrade pip
python -m venv venv
. venv/bin/activate
python -m pip install --upgrade pip
# Install requirements
python -m pip install -r requirements.txt
# Go back to parent directory
cd ../
```

## Run cases

First you will have to run the cv_sdk server:

```bash
cd cv_pom/
python server.py --model ../../../resources/best.pt
```

in a different terminal run the playwright test:

```bash
npm run testsWithAllure
```
