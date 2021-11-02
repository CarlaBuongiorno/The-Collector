# **Testing And Project Barrier Solutions**

[Return to README.md](https://github.com/CarlaBuongiorno/The-Collector/blob/master/README.md)

[View the live site here](https://the-collector-project.herokuapp.com/)

![Final project image home page](static/docs/readme-images/amiresponsive.png)

## **Contents**

[Testing User Stories](#testing-user-stories)

[Code Validation](#code-validation)

[Responsiveness And Compatibility](#responsiveness-and-compatibility)

[Testing Performance](#testing-performance)
* [Lighthouse](#lighthouse)
* [Performance](#performance)
* [Accessibility](#accessibility)

[Project Barriers and Solutions](#project-barriers-and-solutions)
* [Solved Bugs](#solved-bugs)
* [Known Bugs](#known-bugs)

---

## **Testing User Stories**

### First Time Visitor

##### Easily navigate the site.

* Clicking on a menu item in the navigation bar displays the relevant page without errors.
* Clicking on a link in the footer displays the relevant page without errors.

##### Intuitively and easily understand what to do.

* 

##### Register for an account.

* 

##### Get visual feedback when an action on the site is completed.

* 

#### Returning Visitor

##### Log in

* 

##### Be confident that their password is be stored securely.

* 

##### Navigate intuitively, with no need to use the browser's back button.

* 

##### Update and delete their profile/account.

* 

##### Add comics to their catalogue.

* 

##### View their catalogue.

* 

##### Edit and delete comics.

* 

##### Browse and search other collector's comics.

* 

##### Log out.

* 

#### Admin

##### Be confident that a user can't force their way into the restricted pages.

* 

##### Edit or delete any user.

* 

##### Delete user's comics.

* 

##### Give or remove admin rights.

* 

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Code Validation**

W3C Markup Validator
* [HTML Results]()

W3C CSS Validator
* [CSS Results]()

Markdownlint GitPod Extension
* [markdownlint Extension](https://open-vsx.org/vscode/item?itemName=DavidAnson.vscode-markdownlint)

JSHint GitPod Extension
* [JSHint Extension](https://open-vsx.org/vscode/item?itemName=dbaeumer.jshint)

PyLint Extension
* [PyLint Extension](https://pypi.org/project/pylint/)

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Responsiveness And Compatibility**


[Back to Top](#testing-and-project-barrier-solutions)

---

## **Testing Performance**

### Lighthouse

### Performance

### Accessibility

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Project Barriers and Solutions**

### Solved Bugs

1. It was possible to register a duplicate username regardless of the code written to check if the username already exists in the database. The flash message that tells the user that the username already exists did not display, and instead the registration was successful.
    * Fixed the 'for' of the username label to 'username' instead of 'name'.
    * The collection I used to check 'existing_user' was 'users' with an 's' at the end, while the one I tried to insert was 'user' without the 's'. Correcting this solved the bug.
2. The Bootstrap toggle switch for the 'For Sale' field, remains 'checked' upon inspection, despite being toggled 'off'.
    * This could be Bootstrap applying javascript behind the scenes.
    * More investigation is necessary...
3. Deleting a comic would remove it from the 'comics' collection, but the ObjectId would remain in the 'user' collection where it is stored in the 'my_catalogue' field in an array.
    * Originally, I was only deleting the comic from the 'comics' collection.
    * To do fix this, I needed to grab the user from the session, get the user from the database using the user from the session, get the user's ID and use the '$pull' command, with the id of the comic, and then remove it from the user's 'my_catalogue'.
4. The 'Notes' textarea field in Edit Comic would render empty instead of what the user previously filled.
    * This was due to the 'id', 'name', and 'for' attributes not being consistent with each other. 
5. Admin could delete another user's comic, but the user's 'my_catalogue' array of comic ids would not be updated.
    * This first issue was that the function was first deleting the comic, then in the 'if user is admin', trying to find the 'the_collector' from a comic id that no longer existed.
    * Moving the delete functionality to after the IF block brought me a step closer to the fixing this bug.
    * The second issue was that I was trying to find the user's collection, in order to update their catalogue, by their '_id' (which I did not have). By substituting this for what I did have ('username'), the issue was resolved.

### Known Bugs

[Back to Top](#testing-and-project-barrier-solutions)
