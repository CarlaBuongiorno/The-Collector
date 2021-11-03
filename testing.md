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

### **First Time Visitor**

#### **Easily navigate the site.**

* Clicking on a menu item in the navigation bar displays the relevant page without errors.
* Clicking on a link in the footer displays the relevant page without errors.
* The navigation bar is easily visible on every page of the site.
* This displays differently depending on what access the user has.
* The navigation bar is easy to understand and always there for ease of navigation on the site.
* The logo at the top left of the page takes the user back to the home page at any given point.

#### **Intuitively and easily understand what to do.**

* All buttons are clearly labelled.
* All links and buttons have descriptive text.
* Each page and each step taken by a user, leeds a user through the site to the appropriate pages.

#### **Register for an account.**

* The Register button is visible for all users who aren't logged in.
* A user is able to register an acount by clicking the 'Register' link in the Menu, or by clicking the Register button at the bottom of the landing page.
* A form will be presented to the user to complete and a message is displayed to welcome the new user if everything was successful.
* The register form is clear and easy to follow.
* There are validation messages if you don't enter the correct format of information.

#### **Get visual feedback when an action on the site is completed.**

* There are validation messages for all the forms if you don't enter the correct format of information.
* Flash messages are presented to the user: 
    * when the user chooses a username already existing in the database.
    * upon successful registration.
    * upon logging in.
    * upon logging out.
    * upon updating their profile.
    * upon deleting their account.
    * upon successfully adding a comic to their catalogue.
    * upon editing a comic.
    * upon deleting a comic.

### **Returning Visitor**

#### **Log in**

* The Log In button is visible for all users who aren't logged in.
* The Log In button is positioned on the navbar and the footer.
* The form is clear and easy to follow.

#### **Be confident that their password is be stored securely.**

* Werkzeug's password hashing methods have been used to store all user's passwords in a secure and safe way.

#### **Navigate intuitively, with no need to use the browser's back button.**

* The navigation bar is constantly visible across the top of the site.
* This is either the full navigation bar, or the condensed burger icon menu bar on smaller screen sizes.

#### **Update and delete their profile/account.**

* Upon registration or logging in, a user is immediately taken to their 'Profile' page.
* Here the user has the option of either updating their profile, or deleting their account all together.

#### **Add comics to their catalogue.**

* The user can add comic books through a button on their profile page, a link on the navbar, as well as a button on their catalogue page.
* The Add Comic form is clear and easy to follow. 
* There are validation messages if you don't enter the correct format of information or skip required fields.

#### **View their catalogue.**

* Once a comic has been successfully added, it appears on the user's 'Catalogue' page.
* Clicking on a comic in the user's catalogue brings up a modal displaying all the information the user entered about that comic.

#### **Edit and delete comics.**

* The comic books' modals have the option to edit and delete the specific comic.
* Clicking on the delete button will bring up a second modal checking if the user is certain they wish to delete that comic.
* Clicking on the Edit button will take the user to the form they used to add the comic with all the information prefilled. There they can then adjust the information about the comic and save it by clicking the 'Edit Comic' button.

#### **Browse and search other collector's comics.**

* 

#### **Log out.**

* The Log Out button is visible for all users who are logged in.
<!-- * The Log Out button is positioned on the navbar and the footer. -->

### **Admin**

#### **Be confident that a user can't force their way into the restricted pages.**

* 

#### **Edit or delete any user.**

* 

#### **Delete user's comics.**

* 

#### **Give or remove admin rights.**

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
