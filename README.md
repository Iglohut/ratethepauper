# ratethepauper
This is a hobby project aimed at making a website where residents of my house can rate certain aspects that the landlord ought to keep up-to-date. This could be used by the landlord for early detection of faulty aspects in the house. The website will use the python package Django as its core engine. 

*This website is still in development*

### Installation
You can test the website on your computer locacally. 
##### Ubuntu 18.04.3 LTS

First clone this repository in your favourite directory. 
```sh
$ cd Documents/Github
$ git clone https://github.com/Iglohut/ratethepauper.git
```

Create a virtualenvironment using conda.
```sh
$ cd ratethepauper
$ cd environment
$ conda env create -f environment.yml
```
Activate the environment and run the server:
```sh
$ conda activate ratethepauper
$ cd ../src
$ python manage.py runserver
```
Now go to your browser to the server suggested (e.g. http://127.0.0.1:8000/)

### To-dos
* ~~Model Aspects (e.g. shower, toilet, internet)~~
* Model ratings (rate every aspects, hue's?)
* ~~Single page ratings~~
* ~~Display data interactively~~
	* Fix resize lose data plotly issue?

* Form
	* Aspects
	* subchoices (internet:wifi)
	* Generalize from Aspects
	* Autoupdate plots on submit

* Homepage
	* Introduction to what is this website
	* Google maps to the house
	* More?

* Overall styling
	* Colour scheme
	* Navvar
	* Footer?

