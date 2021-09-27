# The Collector

[Here is a link to the final project]()

This project... 
(Description)

![Final project image home page]()

## Contents

* [User Experience (UX)](#user-experience-(ux))
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
  * [Flowchart](#flowchart)
  * [Features](#features)
  * [Future Features](#future-features)

* [Information Architecture](#information-architecture)
  * [Database Design](#database-design)
  * [Users Collection](#users-collection)
  * [Comic Info Collection](#comic-info-collection)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

* [Deployment](#deployment)
  * [Initial Deployment](#initial-deployment)
  * [How to Fork it](#how-to-fork-it)
  * [How to Clone it](#how-to-clone-it)
  * [Making a Local Clone](#making-a-local-clone)

* [Testing](#testing)
  * [W3C Validator](#w3c-validator)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
  * [Further Testing](#further-testing)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)
  * [Lighthouse](#lighthouse)
    * [Performance](#performance)
    * [Accessibility](#accessibility)
    * [Best Practices](#best-practices)
    * [SEO](#seo)

* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

---

## User Experience (UX)

### User Stories

#### First Time Visitor Goals

As a first time visitor to this site, a user should be able to :

* Easily navigate the site.
* Intuitively and easily understand what to do.
* Register for an account.
* Get visual feedback when an action on the site is completed.

#### Returning Visitor Goals

In addition to the First Time Visitor Goals, a Returning Visitor should be able to :

* Log in.
* Be confident that their password is be stored securely.
* Navigate intuitively, with no need to use the browser's back button.

#### Admin Goals

In addition to the First Time and Returning Visitor Goals, as an administrator of this site, an admin user should be able to:

* Be confident that a user can't force their way into the restricted pages.
* Edit or delete any user.
* Add a comic book field.
* Edit or delete any field.
* Give or remove admin rights.

[Back to Top](#the-collector)

---

## Design

### Overall

* 

### Colour Scheme

![Colours used in this site]()

* 

### Typography

* 

### Imagery

* The icons used...
* The images used...
* The avatars were chosen....

### Wireframes

[Here are the wireframes for desktop, mobile and tablet for this project](static/docs/wireframes.pdf).

### User Journey

![Flowchart]()

### Features

* Add a comic book.
* Create and Delete a profile.
* Create, Edit and Delete a comic book from the user's own catalogue.
* Create, Edit and Delete a comic book from 'The Collectors' for admin users only.
* Edit admin rights and edit or delete a user for admin users only.
* Confirm to delete modal.
* Auto-updating copyright year.

### Future Features

* Email verification before a user can add comic books.
* Enter user's password to delete user account.
* A toggle to allow the user to select whether they want to set their Catalogue as public or private.

[Back to Top](#the-collector)

---

## Information Architecture

### Navigation bar

The navigation bar changes depending on user status and screen size:

| Nav Link | Logged Out | Logged In (User) | Logged In (Admin) |
|-------|-----|-----|-----|
| Logo (Profile page if logged in, Landing Page if not) | &#9989; | &#9989; | &#9989; |
| Log In | &#9989; | &#10060; | &#10060; |
| Register | &#9989; | &#10060; | &#10060; |
| Add Comics | &#10060; | &#9989; | &#9989; |
| The Collectors Page | &#10060; | &#9989; | &#9989; |
| Profile | &#10060; | &#9989; | &#9989; |
| Manage User's Comic Books | &#10060; | &#10060; | &#9989; |
| Manage Comic Book Fields | &#10060; | &#10060; | &#9989; |
| Manage Users | &#10060; | &#10060; | &#9989; |
| Log Out | &#10060; | &#9989; | &#9989; |

### Database Design

MongoDB was used to store data for this site in a database. The data has been set out in two collections, which are described below:

### Users Collection

| Users |    |    |
|---|---|---|
| _id | ObjectId |    |
| full_name | string |    |
| username | string |    |
| email | string |    |
| password | string |    |
| avatar_no | int |    |
| is_admin| boolean |    |
| my_catalogue | array | comics._id |

### Comic Fields Collection

| Comics |    |
|---|---|
| _id | ObjectId |
| title | string |
| publisher | string |
| year | string |
| issue_no | string |
| grade | string |
| for_sale | string |
| price | string |
| notes | string |
| image_url | string |
| show_contact_details | string |
| email_address | string |

### Overall Database

![Overall Database]()

### Users Collection Screenshot

![Users Collection Example]()

### Comics Collection Screenshot

![Comics Collection Example]()

[Back to Top](#the-collector)

---

## Technologies Used

### Languages Used

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
* [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3#:~:text=CSS3%20is%20the%20latest%20evolution,flexible%20box%20or%20grid%20layouts.)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://www.python.org/)

### Workspace

#### GitPod

[GitPod](https://gitpod.io/) was used as a virtual IDE workspace to build this site.

### Version Control

#### Git

[Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to add and commit to Git and push to GitHub.

#### GitHub

[GitHub](https://github.com/) is used to store the code for this project after being pushed from Git.

### Wireframing

#### Balsamiq

[Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design process.

### Responsive Design

#### Am I Responsive Design



### Site Design

#### Font Awesome

[Font Awesome](https://fontawesome.com/) was used on all pages to add the icons.

#### Adobe Online



#### Favicon.io



### Database Design Technologies

#### MongoDB

[MongoDB](https://www.mongodb.com/) was used to store the contents of the database, and allow full CRUD functionality.

#### Flask-PyMongo

[Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) was used to connect this Python / Flask app to MongoDB.

### Frameworks, Libraries and Others

#### Heroku

[Heroku](https://www.heroku.com) was used to deploy the live site.

#### Google DevTools



#### Lighthouse



#### Flask

[Flask](https://flask.palletsprojects.com/en/2.0.x/) was used to help create the templating for this site.

#### Bootstrap

[Bootstrap](https://getbootstrap.com/) was used to create a beautiful, responsive website.

#### jQuery

[jQuery](https://jquery.com/) was used to make the DOM traversal easier within the JavaScript.

#### Jinja

[Jinja](https://jinja.palletsprojects.com/en/3.0.x/) was used to auto-populate the site with the contents of the database.

#### RandomKeygen

[RandomKeygen](https://randomkeygen.com/) was used to generate a strong `SECRET_KEY`.

#### Flask-paginate



#### pip

[pip](https://pip.pypa.io/en/stable/) was used to install the required dependancies for this site.

#### dnspython

[dnspython](https://pypi.org/project/dnspython/) was used to provide access to DNS.

[Back to Top](#the-collector)

---

## Deployment

### Requirements for Deployment

* Python
* MongoDB account and database
* GitHub account
* Heroku account

### Initial Deployment

MONGO_DBNAME - This is the name of the database you need to connect to in MongoDB.

MONGO_URI - This can be found on the MongoDB website by following these steps:
    * In the clusters tab of your database, click connect on the associated cluster.
    * Click 'Connect', then 'Connect your application'.
    * Copy the string, then substitute the password (from Database access NOT your MongoDB password) and change "myFirstDB" to your MONGO_DBNAME.

SECRET_KEY - This is a custom string set up to keep sessions secure. I recommend using a 'Fork Knox' level password generated by [RandomKeygen](https://randomkeygen.com/).

This site was deployed to Heroku by following these steps:

1. Heroku needs to be told what the requirements are for this project, so go into your GitPod terminal, and create files to explain the requirements by using the following commands:
    * `pip3 freeze --local > requirements.txt`
    * `echo web: python run.py > Procfile` - Ensure there is no blank line after the contents of this file
2. Push these changes to your repository.
3. Ensure you have a .gitignore file in your repository, and if not, create one.
4. Add `env.py` and `__pycache__/` into your .gitignore file, and save the file. This is to avoid any sensitive information being added into your repository.
5. Create an env.py file, and add the following information to it, updating the '## x ##' values with your own values:

    ``` python
    import os

    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", " ## YOUR SECRET_KEY ## ")
    os.environ.setdefault("MONGO_URI", " ## YOUR MONGO_URI ## ")
    os.environ.setdefault("MONGO_DB", " ## YOUR MONGO_DBNAME ## ")
    ```

6. Login or sign up to [Heroku](https://www.heroku.com).
7. Select 'Create New App' in the top right of your dashboard.
8. Choose a unique app name, and select the region closest to you, before clicking 'Create App'.
9. Go to the 'Deploy' tab, find 'Deployment Method' and select 'GitHub'.
10. Search to find your GitHub repository, and click 'Connect'. Don't enable automatic deployment yet, as this can cause errors.
11. Go to the 'Settings' tab, find 'Config Vars', and click 'Reveal Config Vars'.
12. Enter key value pairs that match those in your env.py file, displayed like this :

    | Key | Value |
    |---|---|
    | IP | 0.0.0.0 |
    | PORT | 5000 |
    | MONGO_DBNAME | ## YOUR DATABASE NAME ## |
    | MONGO_URI | ## YOUR MONGO_URI ## |
    | SECRET_KEY | ## YOUR SECRET_KEY ## |

13. Go to the 'Deploy' tab, and click 'Enable Automatic Deployment'.
14. In 'Manual Deploy', choose which branch you'd like to deploy from (I chose 'master' branch, this is also known as 'main').
15. Click 'Deploy Branch' to deploy your app onto the Heroku servers.
16. Once the app has finished building, click 'Open App' to open your site.

### How to Fork it

1. Login or Sign Up to [GitHub](www.github.com).
2. On GitHub, go to [CarlaBuongiorno/The-Collector](https://github.com/CarlaBuongiorno/The-Collector).
3. In the top right, click "Fork".
4. You will need to create an env.py file with your own values, and create a MongoDB database with the data keys and types as shown above.
5. You will also need to install all of the project requirements. This can be done using the command `pip3 install -r requirements.txt`.
6. Type `python3 app.py` in your GitPod terminal to run your local site of this project.

### Making a Local Clone

1. Log in to [GitHub](https://www.github.com) and locate the [Repository](https://github.com/CarlaBuongiorno/The-Collector) for this site.
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should clone the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new location, where you want the cloned directory to be.
7. Type `git clone`, and then paste the URL that was copied in Step 4.
8. Press Enter, and your local clone will be created.
9. You will need to create an env.py file with your own values, and create a MongoDB database with the data keys and types as shown above.
10. You will also need to install all of the project requirements. This can be done using the command `pip3 install -r requirements.txt`.
11. Type `python3 app.py` in your GitPod terminal to run your local site of this project.

[Back to Top](#the-collector)

---

## Testing

### W3C Validator

1. W3C Markup Validator
    * [HTML Results]()

2. W3C CSS Validator
    * [CSS Results]()

3. markdownlint GitPod Extension
    * [markdownlint Extension](https://open-vsx.org/vscode/item?itemName=DavidAnson.vscode-markdownlint)

4. JSHint GitPod Extension
    * [JSHint Extension](https://open-vsx.org/vscode/item?itemName=dbaeumer.jshint)

5. PyLint Extension
    * [PyLint Extension](https://pypi.org/project/pylint/)

[Back to Top](#the-collector)

### Testing User Stories

#### First Time Visitor

##### Easily navigate the site

* 

##### Intuitively and easily understand what to do

* 

##### Register for an account

* 

##### Profile

* 

##### Get visual feedback when an action on the site is completed

* 

#### Returning Visitor

##### Log in

* 

##### Update their Profile

* 

##### See the Collections of other Collectors

* 

##### Be confident that their password is be stored securely

* 

##### Navigate intuitively, with no need to use the browser's back button

* 

#### Admin

##### Be confident that a user can't force their way into the restricted pages

* 

##### Edit or delete any user

* 

##### Add a new comic book field

* 

##### Edit or delete any comic books

* 

##### Give or remove admin rights

* 

[Back to Top](#the-collector)

### Full Testing

#### Desktop / Laptop

1. Google Chrome
    * 

2. Microsoft Edge
    * 

3. Mozilla Firefox
    * 

4. Safari
    * 

#### Tablet

1. Safari
    * 

#### Mobile

1. Google Chrome
    * 

2. Safari
    * 

3. Samsung Internet
    * 

Further Testing

* 

[Back to Top](#the-collector)

### Solved Bugs

1. It was possible to register a duplicate username regardless of the code written to check if the username already exists in the database. The flash message that tells the user that the username already exists did not display, and instead the registration was successful.
    * Fixed the 'for' of the username label to 'username' instead of 'name'.
    * The collection I used to check 'existing_user' was 'users' with an 's' at the end, while the one I tried to insert was 'user' without the 's'. Correcting this solved the bug.
2. 
    * 
3. 
    * 
4. 
    * 

### Known Bugs

* 

### Lighthouse Testing



#### Desktop Lighthouse

#### Mobile Lighthouse

#### Performance

* 

#### Accessibility

* 

#### Best Practices

* 

#### SEO

* 

[Back to Top](#the-collector)

---

## Credits

### Code

* [Code Institute](https://codeinstitute.net/) was the main source of information used to create this project, specifically the Task Manager Mini Project Walkthrough.
* [Boostrap](https://getbootstrap.com/): Throughout the site, to create a beautiful responsive site.

### Content

### Media

### Acknowledgements

* 

[Back to Top](#the-collector)