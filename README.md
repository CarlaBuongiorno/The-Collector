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
| my_catalogue | array | comic_books._id |

### Comic Fields Collection

| comic_fields |    |
|---|---|
| _id | ObjectId |
| title | string |
| publisher | string |
| year | string |
| issue_no | string |
| grade | string |
| for_sale | string |
| price | string |
| image_url | string |
| notes | string |
| show_contact_details | boolean |

### Overall Database

![Overall Database]()

### Users Collection Screenshot

![Users Collection Example]()

### Comic info Collection Screenshot

![Comic info Collection Example]()

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



### Wireframing

#### Balsamiq

[Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design process.

### Responsive Design

#### Am I Responsive Design



### Site Design

#### Font Awesome



#### Adobe Online



#### Favicon.io



### Database Design Technologies

#### MongoDB



#### Flask-PyMongo



### Frameworks, Libraries and Others

#### Heroku



#### Google DevTools



#### Lighthouse



#### Flask



#### Bootstrap



#### jQuery



#### Jinja



#### RandomKeygen



#### Flask-paginate



#### pip



#### dnspython



[Back to Top](#the-collector)

---

## Deployment

### Requirements for Deployment

* Python
* MongoDB account and database
* GitHub account
* Heroku account

### Initial Deployment

### How to Fork it

### Making a Local Clone

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

1. 
    * 
    * 
    * 
    * 
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

* 

### Content

### Media

### Acknowledgements

* 

[Back to Top](#the-collector)