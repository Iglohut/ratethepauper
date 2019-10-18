# ratethepauper
This is a hobby project aimed at making a website where residents of my house can rate certain aspects that the landlord ought to keep up-to-date. This could be used by the landlord for early detection of faulty aspects in the house. The website will use the python package Django as its core engine. 

*This website is still in development*

### Installation
You can test the website on your computer locally. 
##### Ubuntu 18.04.3 LTS


First clone this repository in your favourite directory. 
```sh
$ cd Documents/Github
$ git clone https://github.com/Iglohut/ratethepauper.git
```


**Using conda**

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

**Using Docker**
```sh
$ cd ratethepauper
$ docker-compose up
```

Now go to your browser to the server suggested (e.g. http://127.0.0.1:8000/ or http://0.0.0.0:8000/)


### To-dos
* ~~Model Aspects (e.g. shower, toilet, internet)~~
* ~~Model ratings (rate every aspects, hue's?)~~
* ~~Single page ratings~~
* ~~Display data interactively~~
	* Fix resize lose data plotly issue?
	* Display the real data
	* Display comments

* ~~Forms~~
	* ~~Aspects~~
	* ~~Generalize from Aspects~~
	* ~~Autoupdate plots on submit~~
	* ~~Contact form model~~

* Homepage
    * Stats of all models (choose wisely..)
	* ~~Introduction to what is this website~~
	* ~~Google maps to the house~~
	* More?

* About page
	* What is this
	* Goal: utilities; landlord detect, residents argue
	* low threshold of making remarks
	* Who am I-ish
	* Wanna contribute? GitHub or Contactpage

* Overall styling
	* ~~Colour scheme~~
	* ~~Navbar~~
	* ~~Footer~~
	*~~SCSS compatible~~
