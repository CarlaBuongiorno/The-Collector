# **Testing And Project Barrier Solutions**

[Return to README.md](https://github.com/CarlaBuongiorno/The-Collector/blob/master/README.md)

[View the live site here](https://the-collector-project.herokuapp.com/)

![Final project image home page](docs/screenshots/amiresponsive.png)

## **Contents**

[Testing User Stories](#testing-user-stories)

[Code Validation](#code-validation)

[Responsiveness And Compatibility](#responsiveness-and-compatibility)

[Testing Performance](#testing-performance)
* [Lighthouse](#lighthouse)

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
* The logo at the top left of the page, as well as in the footer, takes the user back to the home page at any given point.
    * ![Navbar Large Screen Logged Out User](docs/screenshots/navbar_logged_out_lg.png)
    * ![Navbar Small Screen Logged Out User](docs/screenshots/navbar_logged_out_sm.png)
    * ![Navbar Large Screen Logged In User](docs/screenshots/navbar_logged_in_lg.png)
    * ![Navbar Small Screen Logged In User](docs/screenshots/navbar_logged_in_sm.png)
    * ![Logo In Footer](docs/screenshots/full_footer.png)

---

#### **Intuitively and easily understand what to do.**

* All buttons are clearly labelled.
* All links and buttons have descriptive text.
* Each page and each step taken by a user, leads a user through the site to the appropriate pages.
    * ![Buttons](docs/screenshots/buttons.png)

---

#### **Register for an account.**

* The Register button is visible for all users who aren't logged in.
* A user is able to register an acount by clicking the 'Register' link in the Menu or, by clicking the 'Register' button in the footer.
* A form will be presented to the user to complete, and a message is displayed to welcome the new user if everything was successful.
* The Register form is clear and easy to follow.
* There are validation messages if you don't enter the correct format of information.
    * ![Navbar Register](docs/screenshots/login_register.png)
    * ![Footer Register](docs/screenshots/register_login.png)
    * ![Register Form](docs/screenshots/register.png)    

---

#### **Get visual feedback when an action on the site is completed.**

* There are validation messages for all the forms if a user doesn't enter the correct format of information.
* Flash messages are presented to the user: 
    * when the user chooses a username already existing in the database.
        * ![Username Already Exists](docs/screenshots/username_already_exists.png)

    * when the user enters an incorrect username or password.
        * ![Incorrect Username Or Password](docs/screenshots/incorrect_username_password.png)

    * upon successful registration.
        * ![Registration](docs/screenshots/registration.png)

    * upon logging in.
        * ![Welcome](docs/screenshots/welcome.png)

    * upon logging out.
        * ![Logged Out](docs/screenshots/logged_out.png)

    * upon updating their profile.
        * ![Profile Updated](docs/screenshots/profile_updated.png)

    * upon deleting their account.
        * ![Account Deleted](docs/screenshots/account_deleted.png)

    * upon successfully adding a comic to their catalogue.
        * ![Comic Added](docs/screenshots/comic_added.png)

    * upon editing a comic.
        * ![Comic Updated](docs/screenshots/comic_updated.png)

    * upon deleting a comic.
        * ![Comic Deleted](docs/screenshots/comic_deleted.png)

---

### **Returning Visitor**
#### **Log in**

* The Log In button is visible for all users who aren't logged in.
* The Log In button is positioned on the navbar and the footer.
* The form is clear and easy to follow.
    * ![Log In On Navbar Small Screen](docs/screenshots/navbar_logged_out_sm.png)
    * ![Log In On Navbar Large Screen](docs/screenshots/navbar_logged_out_lg.png)
    * ![Log In On Footer](docs/screenshots/full_footer.png)
    * ![Log In Form](docs/screenshots/login.png)

---

#### **Be confident that their password is being stored securely.**

* Werkzeug's password hashing methods have been used to store all user's passwords in a secure and safe way.

---

#### **Navigate intuitively, with no need to use the browser's back button.**

* The navigation bar is constantly visible across the top of the site.
* This is either the full navigation bar or, the condensed burger icon menu bar on smaller screen sizes.
* The logo at the top left of the navigation bar, as well as on the footer, always brings the user back to the home page.
    * ![Navbar Small Screen For The Logged Out User](docs/screenshots/navbar_logged_out_sm.png)
    * ![Navbar Large Screen For The Logged Out User](docs/screenshots/navbar_logged_out_lg.png)
    * ![Navbar Small Screen For The Logged In User](docs/screenshots/navbar_logged_in_sm.png)
    * ![Navbar Large Screen For The Logged In User](docs/screenshots/navbar_logged_in_lg.png)
    * ![Footer With Logo For The Logged Out User](docs/screenshots/full_footer.png)
    * ![Footer With Logo For The Logged In User](docs/screenshots/logout_footer.png)

---

#### **Update and delete their profile/account.**

* Upon registration, or logging in, a user is immediately taken to their 'Profile' page.
* Here, the user has the option of either updating their profile or, deleting their account all together.
* Clicking on the 'Delete Account' button will bring up a second modal checking if the user is certain they wish to delete their account.
    * ![Update And Delete Profile](docs/screenshots/profile.png)
    * ![Update And Delete Profile](docs/screenshots/confirm_delete_account.png)

---

#### **Add comics to their catalogue.**

* The user can add comic books through, a button on their profile page, a link on the navbar, as well as a button on their catalogue page.
* The 'Add Comic' form is clear and easy to follow. 
* There are validation messages if you don't enter the correct format of information or skip required fields.
    * ![Add Comic From Profile Page](docs/screenshots/profile.png)
    * ![Add Comic From Navbar](docs/screenshots/add_comic_nav.png)
    * ![Add Comic From My Catalogue Page](docs/screenshots/add_comic_my_catalogue.png)
    * ![Add Comic Form](docs/screenshots/add_comic_form.png)

---

#### **View their catalogue.**

* Once a comic has been successfully added, it appears on the user's 'Catalogue' page.
* Clicking on a comic in the user's catalogue brings up a modal displaying all the information the user entered about that comic.
    * ![Comic Information Modal From My Catalogue Page](docs/screenshots/info_modal_edit_delete.png)
    
---

#### **Edit and delete comics.**

* The comic books' modals have the option to edit and delete the specific comic.
* Clicking on the 'Delete' button will bring up a second modal checking if the user is certain they wish to delete that comic.
* Clicking on the 'Edit' button will take the user to the form they used to add the comic with all the information prefilled. There they can adjust the information about the comic and save it by clicking the 'Edit Comic' button.
    * ![Information Modal Edit Comic Button](docs/screenshots/info_modal_edit_delete.png)
    * ![Delete Confirmation Modal](docs/screenshots/confirm_delete_comic.png)
    * ![Edit Comic](docs/screenshots/edit_comic.png)

---

#### **Browse and search other collector's comics.**

* On the 'Collection' page, users are able to browse through all the comics that have been added by other collectors. 
* Clicking on a comic brings up a modal displaying relevant information about that comic, including the username of that Collector.
* On the 'Collection' page, users also have the option to search through 'The Collection'. 
* Users can search by 'Title', 'Publisher Name', 'Issue Number', by the words used within the collectors 'Notes', and by the actual 'Collector' him/herself.
    * ![Browse The Collection](docs/screenshots/the_collection.png)
    * ![Comic Information Modal From The Collection Page](docs/screenshots/info_modal.png)
    * ![Search](docs/screenshots/search.png)
    
---

#### **Log out.**

* The 'Log Out' button is visible for all users who are logged in.
* The Log Out button is positioned on the navbar and the footer.
    * ![Logout On Navbar](docs/screenshots/logout_navbar.png)
    * ![Logout On Footer](docs/screenshots/logout_footer.png)
---

### **Admin**
#### **Be confident that a user can't force their way into the restricted pages.**

* Admin users are set with an is_admin: 'True' in the database.
    * ![Admin User Set To "True"](docs/screenshots/admin_true.png)

---

#### **Delete user's comics.**

* If the user has the is_admin toggle set to true, then they will have access to edit or delete any comic book from the Collection.
    * ![Delete Comic](docs/screenshots/edit_delete_for_admin.png)

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Code Validation**

### W3C Markup Validation Service:

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website and returned no errors. Pages which can only be accessed by being logged in, were validated by direct input by viewing and copying the source code for each page. These also returned no errors.

Results below:-

* The Collector full website:
    * ![The Collector Website](docs/html_validation/the_collector.png)

* Home Page:
    * ![Home](docs/html_validation/home.png)

* Registration Page:
    * ![Registration Page](docs/html_validation/register.png)

* Log In Page:
    * ![Log In Page](docs/html_validation/login.png)

* Profile Page:
    * ![Profile Page](docs/html_validation/profile.png)

* My Catalogue Page:
    * ![My Catalogue Page](docs/html_validation/my_catalogue.png)

* The Collection Page:
    * ![The Collection Page](docs/html_validation/the_collection.png)

* Add Comic Page:
    * ![Add Comic Page](docs/html_validation/add_comic.png)

* Edit Comic Page:
    * ![Edit Comic Page](docs/html_validation/edit_comic.png)

* 404 Page:
    * ![404 Page](docs/html_validation/404.png)

---

### W3C CSS Validation Service:

The CSS file was tested with [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/) via direct input and returned no error.

The warning is due to that the imported style sheets are not checked in direct input and file upload modes by W3C validation services.

* CSS Validation Results:
    * ![CSS Validation Results](docs/css_validation/css_validation.png)

---

### JSHint:

All javascripts files were tested with [JSHint](https://jshint.com/) and returned no errors. 

* _add_comic.js_ File Results:
    * ![add_comic.js File Results](docs/jshint/add_comic.png)

* _edit_comic.js_ File Results:
    * ![edit_comic.js File Results](docs/jshint/edit_comic.png)

* _my_catalogue.js_ File Results:
    * ![my_catalogue.js File Results](docs/jshint/my_catalogue.png)

* register.js_ File Results:
    * ![register.js File Results](docs/jshint/register.png)

* _script.js_ File Results:
    * ![script.js File Results](docs/jshint/script.png)

* _the_collection.js_ File Results:
    * ![the_collection.js File Results](docs/jshint/the_collection.png)

---

### Python 8:

The python file was run through [PEP8](http://pep8online.com/) online and returned no errors.

* PEP8 Results:
    * ![PEP8 Results](docs/pep8/pep8.png)

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Responsiveness And Compatibility**

The website was tested through the following browsers:

### Google Chrome

* Comic Added
    * ![Google Chrome Comic Added](docs/physical_devices/chrome_comic_added.png)

* Comic Updated Successfuly
    * ![Google Chrome Comic Updated Successfuly](docs/physical_devices/chrome_comic_updated.png)

* Home
    * ![Google Chrome Home](docs/physical_devices/chrome_home.png)

* Registration Successful
    * ![Google Chrome Registration Successful](docs/physical_devices/chrome_registration_successful.png)

### Microsoft Edge

* My Catalogue
    * ![Microsoft Edge My Catalogue](docs/physical_devices/microsoft_edge_catalogue.png)

* Comic Deleted Successfully
    * ![Microsoft Edge Comic Deleted Successfully](docs/physical_devices/microsoft_edge_comic_deleted.png)

* Log In Successful - Profile
    * ![Microsoft Edge Log In Successful - Profile](docs/physical_devices/microsoft_edge_login.png)

### Mozilla Firefox

* Admin Delete And Edit Options On The Collection Page
    * ![Mozilla Firefox Admin Delete And Edit Options](docs/physical_devices/firefox_admin_edit_delete.png)

* Trying To Brute Force Into Site - Not Possible
    * ![Mozilla Firefox Trying To Brute Force Into Site - Not Possible](docs/physical_devices/firefox_login.png)

### Safari

* Account Deleted Successfully - Home
    * ![Safari Account Deleted Successfully - Home](docs/physical_devices/safari_account_deleted_home.png)

* Comic Updated Successfully
    * ![Safari Comic Updated Successfully](docs/physical_devices/safari_comic_updated.png) 

* Log In Successful - Profile
    * ![Safari Log In Successful - Profile](docs/physical_devices/safari_successful_login.png) 

All working as expected.

---

DevTools were used to test the site across a range of widths:

### Mobiles: 

* iphone5(320px)
    * Log In
        * ![iPhone5 Log In](docs/dev_tools/iphone5_login.png)
    * The Collection
        * ![iPhone5 The Collection](docs/dev_tools/iphone5_the_collection.png)

* Moto G4 (340px)
    * Add Comic
        * ![MotoG4 Add Comic](docs/dev_tools/moto_g4_add_comic.png)
    * Edit Comic Footer
        * ![Moto G4 Edit Comic Footer](docs/dev_tools/moto_g4_edit_comic_footer.png)

* iPhone 6/7/8 (375px)
    * Register
        * ![iPhone6/7/8 Register](docs/dev_tools/iphone678_register.png)
    * Information Window My Catalogue
        * ![iPhone6/7/8 Information Window My Catalogue](docs/dev_tools/iphone678_info_window_catalogue.png)

* iPhone 6/7/8 Plus (414px)
    * Register Footer
        * ![iPhone6/7/8 Plus Register Footer](docs/dev_tools/iphone678_plus_register_footer.png)
    * Open Menu
        * ![iPhone6/7/8 Plus Open Menu](docs/dev_tools/iphone678_plus_open_menu.png)

---

### Tablets:

* iPad (768px)
    * Home
        * ![iPad Home](docs/dev_tools/ipad_home.png)
    * My Catalogue
        * ![iPad My Catalogue](docs/dev_tools/ipad_my_catalogue.png)

* iPad Pro (1024px)
    * Information Window The Collection
        * ![iPad Pro Information Window The Collection](docs/dev_tools/ipad_pro_info_window_collection.png)
    * Profile
        * ![iPad Pro Profile](docs/dev_tools/ipad_pro_profile.png)

---

### Desktops:

* Laptop (1200px)
    * The Collection
        * ![Laptop The Collection](docs/dev_tools/laptop_the_collection.png)
    * Admin Information Window
        * ![Laptop Admin Information Window](docs/dev_tools/laptop_admin_info_window.png)

* Desktop screen (1400px)
    * Information Window The Collection
        * ![Desktop Information Window The Collection](docs/dev_tools/desktop_info_window_catalogue.png)
    * Profile
        * ![Desktop Profile](docs/dev_tools/desktop_profile.png)

All working as expected.

---

The site was tested on the following physical devices:

### Mobiles: 

* Huawei P30
    * Profile Buttons and Footer
        * ![Huawei P30 Profile Buttons And Footer](docs/physical_devices/huawei_profile_buttons.jpg)

    * My Catalogue
        * ![Huawei P30 My Catalogue](docs/physical_devices/huawei_my_catalogue.jpg)

    * Information Window From The Collection
        * ![Huawei P30 Information Window From The Collection](docs/physical_devices/huawei_info_window_collection.jpg)

    * 404: Page Not Found
        * ![Huawei P30 404: Page Not Found](docs/physical_devices/huawei_404.jpg)

* Sony Xperia 1 II
    * Successful Registration
        * ![Sony Successfuly Registration](docs/physical_devices/sony_registration_successful.png)

    * Comic Deleted
        * ![Sony Comic Deleted](docs/physical_devices/sony_comic_deleted.png)

    * Defensive Programming
        * ![Sony Defensive Programming](docs/physical_devices/sony_defensive_programming.png)

    * Account And Comics Deleted Successfully
        * ![Sony Account And Comics Deleted Successfully](docs/physical_devices/sony_account_deleted.png)

* iPhone X
    * Log In
        * ![iPhone X Log In](docs/physical_devices/iphone_x_login.png)

    * Add Comic Form
        * ![iPhone X Add Comic Form](docs/physical_devices/iphone_x_add_comic.png)

    * Search No Match - No Results Found
        * ![iPhone X Search No Match - No Results Found](docs/physical_devices/iphone_x_search.png)

    * Log Out Successful
        * ![iPhone X Log Out Successful](docs/physical_devices/iphone_x_logout.png)

---

### Laptops:

* MacBook Pro 13inch
    * Add Comic
        * ![MacBook Pro Add Comic](docs/physical_devices/macbook_pro_add_comic.png)

    * My Catalogue
        * ![MacBook Pro My Catalogue](docs/physical_devices/macbook_pro_catalogue.png)

    * My Catalogue
        * ![MacBook Pro Delete Account](docs/physical_devices/macbook_pro_delete_account.png)

    * My Catalogue
        * ![MacBook Pro Home](docs/physical_devices/macbook_pro_home.png)

* Acer Laptop Windows 10 (1080px)
    * Home - Account Successfully Deleted
        * ![Acer Home](docs/physical_devices/chrome_home.png)   

    * Comic Added Successfully
        * ![Acer My Catalogue](docs/physical_devices/chrome_comic_added.png)    

All working as expected.

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Testing Performance**

### Lighthouse
Google Lighthouse was run on different pages returning different results. Below is an extract of the reports for the 'Home' page, 'My Catalogue' page and 'Add Comic' page:

 * Home
    * ![Lighthouse Home Page](docs/lighthouse/lighthouse_home.png)

* My Catalogue
    * ![Lighthouse My Catalogue Page](docs/lighthouse/lighthouse_my_catalogue.png)

* Add Comic
    * ![Lighthouse Add Comic Page](docs/lighthouse/lighthouse_add_comic.png)

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Project Barriers and Solutions**

### Solved Bugs

1. It was possible to register a duplicate username regardless of the code written to check if the username already exists in the database. The flash message that tells the user that the username already exists did not display, and instead the registration was successful.
    * Fixed the `for` of the username label to `username` instead of `name`.
    * The collection I used to check `existing_user` was `users` with an 's' at the end, while the one I tried to insert was `user` without the 's'. Correcting this solved the bug.
2. The Bootstrap toggle switch for the 'For Sale' field, remains 'checked' upon inspection, despite being toggled 'off'.
    * This could be Bootstrap applying javascript behind the scenes.
    * Upon more investigation, this was remedied by adding and event listener to listen for a change in the toggle switch and if the field is 'checked', then set or remove the required attribute to the 'price' field.
3. Deleting a comic would remove it from the 'comics' collection, but the ObjectId would remain in the 'user' collection where it is stored in the `my_catalogue` field in an array.
    * Originally, the comic was only being deleted from the 'comics' collection.
    * To fix this, I needed to grab the user from the session, get the user from the database using the user from the session, get the user's ID and use the `$pull` command, with the ID of the comic, and then remove it from the user's `my_catalogue`.
4. The 'Notes' field within the 'Edit Comic' form, would render empty instead of what the user previously had filled.
    * This was due to the `id`, `name`, and `for` attributes not being consistent with each other. 
5. Admin could delete another user's comic, but the user's `my_catalogue` array of comic IDs would not be updated.
    * The first issue was that the function was first deleting the comic, then in the `if user is admin`, trying to find the `the_collector` from a comic id that no longer existed.
    * Moving the delete functionality to after the `if` block brought me a step closer to fixing this bug.
    * The second issue was that I was trying to find the user's collection, in order to update their catalogue, by their 'ID' (which I did not have). By substituting this for what I did have (`username`), the issue was resolved.
6. The Bootstrap information modals for the comics kept throwing an 'Uncaught TypeError: Cannot read properties of null (reading 'addEventListener').
    * The solution was to check that `myModal` is not `null` before adding an event listener. This was found on [Stack Overflow](https://stackoverflow.com/questions/26107125/cannot-read-property-addeventlistener-of-null).

### Known Bugs

* There are no known errors.

[Back to Top](#testing-and-project-barrier-solutions)
