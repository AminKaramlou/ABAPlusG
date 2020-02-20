
[![Build Status](https://travis-ci.com/AminKaram/FYP.svg?token=WUKwGEsuG3EUbwasy9R8&branch=master)](https://travis-ci.com/AminKaram/FYP)  
# ABA+G  
  
**Note:** Basic knowledge of argumentation theory is assumed throughout this documentation. If you are unfamiliar with this it's recommended that you read the material in the useful reading section before continuing.

  **Assumption Based Argumentation with goals and preferences (ABA+G)** is a newly proposed formalism for structured argumentation.
  
This project provides an interface which implements reasoning using the ABA+G formalism. There are algorithms for calculating extensions of these frameworks under various semantics, a problem which is of interest in fields such as AI, Law and Medicine. 

## Install

First install the relevant dependecies by running the command `make freeze && pip install -r requirements.txt`. Then install the CLI tool by running `pip install .` 

### Mac / Windows

- `python3 -m piptools compile --output-file requirements.txt setup.py`
- `pip3 install -r requirements.txt`
- `pip3 install .`

Some troubleshooting:
- `pip3 install --upgrade werkzeug` in case of complaints about `werkzeug`

## Use

A live version of the ABA+ app supporting ABA+G for reasoning with clinical guidelines is available as an API on `http://aba-plus-g.herokuapp.com/`. Currently the following endpoints are accessible:
 
 -   **/genereate_explanations** is an endpoint which accepts a post request containing a valid DSS JSON object and returns the relevant extensions and accompanying explanations for which actions need to be taken in the treatment of patients. 

### Deployed

To send POST requests to the [deployed ABA+G endpoint](https://aba-plus-g.herokuapp.com/generate_explanations), from `/requests` run `python post.py` (modify `URL` as required). 
`INPUT_FILE` .json needs to be in `/requests`, the output .json will be appended with `_arg` and placed in `/requests`.

### Stand-alone

Run `python src/app.py` from the main directory of the repository to run the flask server with ABA+G. 

To send POST requests to the [local ABA+G endpoint](http://127.0.0.1:5000/generate_explanations), from `/requests` run `python post.py` (modify `URL` as required). 
`INPUT_FILE` .json needs to be in `/requests`, the output .json will be appended with `_arg` and placed in `/requests`.
You also need the `requests` library for this (`pip3 install requests`).

***

Users can specify the components of an ABA+G framework (i.e. Assumptions, Rules, Contraries, Preferences) in a file as follows: (Note that goals are as of now still unimplemented) 
-   **myAsm(a).**  specifies that  **a**  is an assumption;
-   **contrary(a**,  **x).**  specifies that  **x**  is the contrary of assumption  **a**;
-   **myRule(h**,  **[b1**]).**  specifies that  **h <- b1** is a rule;
-   **myPrefLT(b**, **a).** specifies that assumption **a** is strictly preferred over assumption **b**;
-   **myPrefLE(b**, **a).** specifies that assumption **a** is strictly or equally preferred over assumption **b**;

***

## Useful reading

The following papers provide a background on argumentation theory and this project. 

 - Francesca Toni, 2014: [A tutorial on assumption-based argumentation](https://www.tandfonline.com/doi/abs/10.1080/19462166.2013.869878). A great introductory tutorial to Assumption Based Argumentation (ABA).
 - Kristijonas Cyras, Tiago Oliveira, 2019: [Resolving Conflicts in Clinical Guidelines using Argumentation](http://www.ifaamas.org/Proceedings/aamas2019/pdfs/p1731.pdf). The paper which introduces the ABA+G formalism. 

## Developing  
  
The project comes with a set of commands you can use to run common operations for your stack:  
  
 - `make install`: Installs run time dependencies.  
 - `make install-dev`: Installs dev dependencies together with run time dependencies.  
 - `make freeze`: Freezes dependencies from `setup.py` to `requirements.txt` (including transitive ones).  
 - `make lint`: Runs static analysis.  
 - `make component`: Runs component tests.  
 - `make coverage`: Runs all tests collecting coverage.  
 - `make test`: Runs `lint` and `component`.  
  
### Updating dependencies  
  
Dependencies are managed from the `setup.py` file and then frozen in `requirements.txt` (including transitive dependencies) using `make freeze` (which uses `pip-compile`). If you want to change dependencies, you will have to do it in `setup.py` and then regenerate them using `make freeze`.  
  
Imagine your `setup.py` looks like  
  
```  
install_requires = [  
 'pytest~=3.3.0',]  
```  
  
if you want to update `pytest` to use version 3.4, you need to change it to  
  
```  
install_requires = [  
 'pytest~=3.4.0',]  
```  
  
If you execute `make freeze`, it will regenerate the `requirements.txt` file with the new dependencies according to what the new version of `pytest` needs.  
  
### Deployment to Heroku

The Flask API available in `src/app.py` can easily be deployed to Heroku. Please refer to the `Procfile` in the root folder and the official [Heroku documentation](https://devcenter.heroku.com/categories/reference) for more information on how to do this.   

## Contributing

If you would like to contribute to the project please follow these steps:

 - Clone the project locally.
 - Create a new feature branch.
 - Implement your feature while adhering to the development practices outlined above.
 - Once you are happy with your changes, make sure that the TravisCI checks are passing and create a pull request with a description of what you have changed.  
 
 Your pull request will be peer reviewed and merged into the master branch once ready.
