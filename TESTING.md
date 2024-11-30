# Testing

- Testing was conducted regularly in small intervals throughout the development process as well as at the end of the project to ensure functionality and identify any potential issues early on.
- Bugs that were encountered during testing have been thoroughly documented in the Bug section, detailing the nature of the issue and the steps taken to resolve it.
- Validators were used to ensure that the code meets all necessary standards and specifications. More details can be found in the Validators chapter.
- Logic checks were performed to verify that the program's operations and algorithms were working as intended. This included testing different scenarios and edge cases to ensure robustness.
- Manual input tests were carried out to simulate real-world usage of the application. This involved entering data manually into the system to ensure that all inputs were handled correctly and that the user interface responded appropriately.



## Manual Testing Plan

This testing plan outlines the steps and tests to ensure that critical features of the methodology library website work as expected.

| **Test Area** | **Objective** | **Test Steps** | **Test Cases** | **Test Completed** | **Comments** |
|---------------|---------------|----------------|----------------|--------------------|--------------|
| **1. Log-in Functionality**     | Ensure that users can log in successfully with valid credentials and receive appropriate error messages for invalid credentials. | 1. Navigate to the login page. <br> 2. Enter a valid username/email and password. <br> 3. Click the "Sign In" button. <br> 4. Verify successful login and redirection to homepage. <br> 5. Logout and verify proper logout behavior. | - **Valid Credentials**: Ensure the system logs the user in successfully. <br> - **Invalid Credentials**: Verify that an error message appears for incorrect credentials. <br> - **Session Management**: Verify that the user remains logged in until they log out manually.|[ y ]||                                                          
| **2. Sign-up (Registration)**   | Ensure that users can successfully sign up and create an account.                                      | 1. Navigate to the register page. <br> 2. Fill in required fields (name, password). <br> 3. Click "Sign Up"  button. <br> 4. Verify registration and redirection. <br> 5. Check for confirmation email. | - **Valid Registration**: Verify successful registration. <br> - **Email Format Validation**: Enter invalid email and ensure an error message appears. <br> - **Password Requirements**: Test for validation (e.g., too short password). <br> - **Duplicate Email**: Test registration with an already existing email. <br> - **Successful Registration**: Ensure proper redirection after registration.|[ y ]||
| **3. Log-out Functionality**    | Ensure that users can log out of their accounts successfully.                                          | 1. After logging in, click "Log Out". <br> 2. Verify logout success and redirection. <br> 3. Ensure session data is cleared.                                                               | - **Log-out**: Ensure the user is logged out correctly. <br> - **Session Expiry**: Verify the user cannot access protected pages after logging out.|[ y ]||
| **4. Navigation Functionality** | Ensure that the website navigation is intuitive and functional.                                        | 1. Open the homepage. <br> 2. Click on various menu items or links. <br> 3. Verify correct redirection. <br> 4. Verify active menu item highlight. <br> 5. Test all internal and external links. | - **Responsive Navigation**: Test navigation across different screen sizes. <br> - **Menu Items**: Ensure the menu items lead to correct pages. <br> - **Footer Links**: Verify that footer links work and redirect correctly.|[ y ]||
| **5. Landing Page & Method Filters** | Ensure users can interact with filters, view content, and navigate to method pages.                     | 1. Enter the landing page. <br> 2. Apply various filters (by category, popularity, etc.). <br> 3. Use "Next" button to load more results. <br> 4. Select a method to view full content. <br> 5. Verify redirection to method page. | - **Filters**: Verify that filters apply correctly. <br> - **Pagination**: Test the "Next" button and ensure new methods load correctly. <br> - **Method Details**: Ensure clicking on a method title redirects to the correct method page. <br> - **Empty Filter Results**: Check for appropriate messaging when no results are found after applying filters.|[ y ]||
| **6. About Page Content**      | Ensure that the About page is accessible and displays full content correctly.                           | 1. Navigate to the "About" page. <br> 2. Verify that the full content of the page loads. <br> 3. Ensure the page layout is correct and text/images display properly. | - **Content Verification**: Ensure text and media are accurate and up-to-date. <br> - **Broken Links**: Verify all links on the About page work. <br> - **Responsive Design**: Verify proper display across devices.|[ y ]||
| **7. Single Method Page Interactions** | Ensure users can interact with methods (view content, add/edit/delete comments, "like" a method).         | 1. Select a method to view its page. <br> 2. View full content of the method. <br> 3. Add a comment. <br> 4. Edit or delete a comment. <br> 5. Click the "Like" button to activate it. | - **View Content**: Ensure that full content of the method is displayed. <br> - **Commenting**: Verify adding, editing, and deleting comments works. <br> - **Like Button**: Ensure the "Like" button works and changes state visually. <br> - **Error Handling**: Verify that appropriate error messages appear when actions fail (e.g., comment submission errors).|[ y ]||
| **8. Private Collection**      | Ensure users can view and interact with their private collection of methods and comments.                | 1. Navigate to the "Private Collection" or user dashboard. <br> 2. Verify that the correct methods and comments are displayed. <br> 3. Test that all links work. | - **Access Control**: Ensure only the logged-in user can access their private collection. <br> - **Method Links**: Verify that links to methods navigate correctly. <br> - **Comments in Collection**: Ensure user comments appear and can be edited or deleted. <br> - **Data Integrity**: Ensure no data is lost or missing (e.g., methods or comments).|[ y ]||

---

# Additional Testing Considerations

These are additional tests to ensure the overall quality, performance, security, and compatibility of the website across different platforms.

| **Test Area** | **Objective** | **Test Steps**| **Test Cases** | **Test Completed** | **Comments** |
|---------------|-------------- |---------------|----------------|--------------------|--------------|
| **1. Cross-browser Testing** | Ensure the website works correctly across different web browsers.                                                | 1. Open the website in Chrome. <br> 2. Open the website in Firefox. <br> 3. Open the website in Edge. <br> 4. Open the website in Safari. <br> 5. Test basic functionality (navigation, login, forms) in each browser. | - **Browser Compatibility**: Ensure that features are functional across Chrome, Firefox, Edge, and Safari. <br> - **CSS and Layout**: Verify the website layout and styles appear correctly in all browsers. <br> - **JavaScript**: Ensure JavaScript runs properly across all browsers. <br> - **Responsive Layout**: Test that the website is responsive and adapts to different screen sizes in each browser. |[ y ]||
| **2. Mobile Testing**        | Ensure that the website is fully responsive and works on different mobile devices.                               | 1. Open the website on a mobile device (or simulate using browser dev tools). <br> 2. Test website navigation. <br> 3. Test form submissions and interactive elements (login, comment forms, etc.) on mobile. <br> 4. Test responsiveness on different screen sizes. | - **Mobile Compatibility**: Ensure the website is usable on mobile browsers (Chrome, Safari, Firefox). <br> - **Touch Interaction**: Test touch interactions, such as tapping and swiping. <br> - **Mobile Layout**: Verify proper layout on small screens and large mobile devices. <br> - **Performance on Mobile**: Ensure the website loads and interacts on mobile devices. |[ y ]||
| **3. Performance Testing**   | Ensure the website performs optimally under various conditions, especially with large datasets.                  | 1. Load the website with a large number of methods and comments. <br> 2. Test the "Next" button, pagination, and filtering with large data sets. <br> 3. Measure page load time and response times for actions (e.g., adding comments). | - **Load Time**: Test how long it takes for the website to load and interact with large amounts of data. <br> - **Smooth Navigation**: Ensure pagination and filtering work smoothly without delays. <br> - **Stress Testing**: Test how the website behaves with large user actions (e.g., adding multiple comments, methods). <br> |[ y ]| The accordion section on private_collection.html works but by adding a lot commetns or methods the overview is challenging since its a very big list. Here there is opportunity for improvements when the first MVP is successful. |
| **4. Security Testing**      | Ensure that user data is securely handled and sensitive information is protected.                                | 1. Test the login and registration process | - **Login Security**: Ensure passwords are double checked and the validation works. <br> - **SSL Encryption**: Verify that SSL is enabled and the website uses HTTPS. <br> - **Session Management**: Ensure that user sessions are managed securely and session data is cleared upon logout. <br> - **Sensitive Data Protection**: Test that sensitive user information (e.g., passwords) is not exposed in logs, URLs, or front-end code. |[ y ]||


## Testing User Stories

**User Stories for Site User**

**No.** | **User Story** | **Requirement met (y/n)** |  **Image**|
| ------|--------------- |---------------------------|-----------|
| #11 | As a Site User I can view existing methods on the site so that I am getting inspiration and are willing to share my methods | y |<img src="readme.images/readme_landing_page.PNG" alt="show image for User story" width="500">||
| #2  | As a Site User I can read the methods in an structured way so that it's easy to go through them. | y |<img src="readme.images/readme_userstory_2.PNG" alt="show image for User story" width="500">>||
| #5  | As a Site User I can register an account so that I can comment on a method | y |<img src="readme.images/readme_register_process.PNG" alt="show image for User story" width="500">||
| #14 | As a Site User I can view methods so that I get motivated to share my methods as well | y |<img src="readme.images/readme_landing_page.PNG" alt="show image for User story" width="500">||
| #16 | As a Site User I can see images and a good color contrast so that I like to stay on the website form a visual perspective | y |<img src="readme.images/readme_landing_page.PNG" alt="show image for User story" width="500">||
| #6  | As a Site User I want to get a notification once I change something so that I get feedback of my actions | y |<img src="readme.images/readme_sign_out_process2.PNG" alt="show image for User story" width="250"> <img src="readme.images/readme_log_in_process2.PNG" alt="show image for User story" width="250">||
| #1  | As a Site User I can see directly the purpose of the website so that get an orientation what I can do | y |<img src="readme.images/readme_landing_page.PNG" alt="show image for User story" width="500">||
| #8  | As a Site User I can filter methods on the main page so that I can optimize my search | y |<img src="readme.images/readme_userstory_1.PNG" alt="show image for User story" width="500">||
| #22 | As a Site User I can add methods so that I can share my own methods with the community. | y |<img src="readme.images/readme_add_a_method_page.PNG" alt="show image for User story" width="500">||
| #20 | As a Site User I can see information about the creator of the website and/or the misson so that I get an idea of the person(s) behind the project and/or the team. | y |<img src="readme.images/readme_about_page.PNG" alt="show image for User story" width="500">||
| #31 | As a Site user I see the most liked methods on top' so that 'I see the best ones when I enter the site' | y |<img src="readme.images/readme_landing_page.PNG" alt="show image for User story" width="500">||
| #41 | As a Site User I can see feedback when I clicked on the like button so that I am sure it was successful. | y |<img src="readme.images/readme_userstory_41a.PNG" alt="show image for User story" width="250"> <img src="readme.images/readme_userstory_41b.PNG" alt="show image for User story" width="250">||
| #40 | As a Site User I can go back after I clicked the next button so that I can go back to the first methods on the overview | y |<img src="readme.images/readme_userstory_40.PNG" alt="show image for User story" width="500">||
| #28 | As a Site User I can identify the website in my browser via an symbol so that I find the open website faster | y |<img src="readme.images/readme_userstory_28.PNG" alt="show image for User story" width="500">||
| #18 | As a Site User I can view the different methods with images and summary so that I get an idea what I can see on the detail site | y |<img src="readme.images/readme_userstory_18.PNG" alt="show image for User story" width="500">||
| #30 | As a Site User I can define a unique title and I don't have to worry about the slug text is generated automatically so that I don't have to write a slug text | y |<img src="readme.images/readme_userstory_30a.PNG" alt="show image for User story" width="300"> <img src="readme.images/readme_userstory_30b.PNG" alt="show image for User story" width="300">||
| #38 | As a Site User I can see in the navigation which site is currently active so that I know where I am and find the relevant content faster | y |<img src="readme.images/readme_userstory_38a.PNG" alt="show image for User story" width="250">||
| #34 | As a Site User I can see clearly if I liked a method already, before I click on the Like-button' so that 'I don't click twice. | y |<img src="readme.images/readme_userstory_34.PNG" alt="show image for User story" width="200">||
| #36 | As a Site User (disabled) I can use arial-current/label attributes so that I can follow the content on the website properly. | y |||
| #16 | As a Site User I can see images and a good color contrast so that I read and see all relevant elements | y | <img src="readme.images/readme_landing_page.PNG" alt="show image for User story" width="500">||
| #47 | As a Site User I see a well structured navigation and highlighted sections' so that I have a good overview where I am' | y |<img src="readme.images/readme_nav_logged_in.PNG" alt="show image for User story" width="500">||
| #48 | As a Site User I can see a well designed website with structure, good organized elements and not to much elements so that I like to stay on the website and coming back | y | <img src="readme.images/readme_landing_page.PNG" alt="show image for User story" width="500">||
| #49 | As a Site User I can see all my created content well structured on one site so that I have a good overview about what I provided to the comunity | y | <img src="readme.images/readme_private collection_page.PNG" alt="show image for User story" width="500">||
| #21 | As a (logged-in) Site User I can like and bookmark my own favorite methods so that I can collect them and use them for planning my workshops. | y |<img src="readme.images/readme_userstory_21.PNG" alt="show image for User story" width="500">||
| #27 | As a (logged-in) Site User I can adjust the text-style in the submit form so that it's possible to structure and formatting my content easily | y |<img src="readme.images/readme_userstory_27.PNG" alt="show image for User story" width="500">|
| #15 | As a (logged-in) Site User I can comment on a method so that I get motivated to share my methods | y |<img src="readme.images/readme_userstory_15.PNG" alt="show image for User story" width="500">||
| #4  | As a (logged-in) Site User I can modify or delete my comment on a method so that I can be involved in the conversation | y |<img src="readme.images/readme_userstory_4.PNG" alt="show image for User story" width="500">||


**User Stories for Admin Admin**

**No.** | **User Story** | **Requirement met (y/n)** |  **Image**|
| ------|--------------- |---------------------------|-----------|
| #29 | Do readme documentation | y ||
| #9  | As a Site Admin I can create, read, update and delete methods so that I can manage my content | y |<img src="readme.images/readme_userstory_9.PNG" alt="show image for User story" width="500">|
| #10 | As a Site Admin I can approve comments so that I can manage and control the content on the website | y |<img src="readme.images/readme_userstory_10.PNG" alt="show image for User story" width="500">|
| #45 | As a Site Admin I can create, update and delete the text content of the about.html site | y |<img src="readme.images/readme_userstory_45.PNG" alt="show image for User story" width="500">|
| #46 | As a Site Admin I can create, update and delete Site Users | y |<img src="readme.images/readme_userstory_46.PNG" alt="show image for User story" width="500">|
| #33 | As a Site Admin I can use a filter function for comments in the admin panel so that I can manage the comments efficient | y |<img src="readme.images/readme_userstory_33.PNG" alt="show image for User story" width="500">|
| #12 | As a Site Admin I can approve methods from other Site Users so that I have control of the content | y |<img src="readme.images/readme_userstory_12.PNG" alt="show image for User story" width="500">|
| #47 | As a Site Admin I can approve comments from other Site Users so that I have control of the content | y |<img src="readme.images/readme_userstory_47.PNG" alt="show image for User story" width="500">|
| #43 | As a 'Site Admin' I wan to restrict the uploaded image size of one image to 3MB so that my storage at cloudinary is sufficient. | y |<img src="readme.images/readme_userstory_43.PNG" alt="show image for User story" width="500">||
| #42 | As a 'Site Admin' I want to make sure that the Users don't crash the website by adding to much content | y | I added 30 test comments and 30 methods. It all worked fine. For the first MVP it is sufficient. |
| #37 | As a User I can use a working website so that I don't receive error messages or are harmed to use certain functionalities of the website | y | no more error found which cause an error. |


## Automated testing

| **test file** | **Objective** | **Test Code (image)** | **Test Completed** | **Comments** |
|---------------|-------------- |-------------|--------------------|--------------|
| view_methods/test_views.py | Tests if the method page correctly displays a method and its comments. | <img src="readme.images/readme_testing_test_method_view.PNG" alt="shows TestMethodView"> |[ y ]||
| view_methods/test_views.py | Tests filtering by purpose, duration, and location for the MethodList view. | <img src="readme.images/readme_testing_test_method_filtering_views.PNG" alt="shows TestMethodFiltering"> |[ y ]||
| view_methods/test_forms.py | Tests adding a new comment with valid and invalid input | <img src="readme.images/readme_testing_test_comment_form.PNG" alt="shows TestCommentForm"> |[ y ]||

**Important Hint:**  The current Sqlite3 database has been deleted to avoid expressing sensitive data. Date files names: db.sqlite3 and db_backup.json.

## Bugs (not fixed)

| Bug | Description  | images (optional) | Correction |
| --- |------------- | ----------------- | -----------|
| django.db.utils.DataError: invalid input syntax for type integer: "indoor, outdoor" | Error during database migration. According to the error message the migration file 003 contains an error. However, after adjusting the file the some error occured.| <img src="readme.images/bug_error_message_syntax error_none.PNG" alt="shows error message" widht="250"> <img src="readme.images/bug_backuo_migration003.PNG" alt="shows error message" widht="250"> | Old migration files has been saved outside the project and deleted in the project. New command "python3 manage.py migrate" has been done. A new migration file exists and is working. |
| django.db.utils.OperationalError: near "None": syntax error | The error occured during testing. The local database db.sqlite had an inconsistency. The migration file "view_methods.0003_alter_method_alt_atr_alter_method_duration_and_more" had a failre related to NONE. After several tries to fix the issue I decided to focus on the rest of the project. | ...| I saved all migration files and removed them from the project. Then I run pyhton3 manage.py makemigrations and python3 manage.py migrate.|
| Uncaught Type Error: this._element is undefined | Customization summernote for admin panel. Bug fix was not possible, therefore the code was removed from the project. | <img src="readme.images/bug_js_summernote_customization_code.PNG" alt="shows error message in console"> | function was removed. |
| NameError: name 'request' is not defined | The error occurs because the request I am trying to access request.method outside of a method where request is not available. The request object is passed to views only during HTTP request processing, so trying to reference it outside of a method like get_context_data causes this error. To fix this, you should move the POST request handling inside the appropriate post method of the class-based view. In Django, TemplateView doesn't have a post method by default. | <img src="readme.images/bug_nameerror_name_requet_is_not_defined.PNG" alt="image shows Error message"> | TempalteView is still used for AboutPageView method in views.py, but the edit and delete functionality is removed. |
| Image overlay | Method_page line 6-7: By default, a div will expand based on its content - so does the div wit hthe image. It will not automatically adapt its height to the parent unless instructed to do so via CSS, which is why you're seeing the overlap. Setting height: 100% on an additional element such as .container.height_control should ensure it inherits the parent's height. However then the image appears very small, I prefer keeping the overlap. Since it's a responsive site the image is cutted on different heights. | <img src="readme.images/bug_image_overlap_masthead.PNG" alt="shows bug on website" width="250"> | none, compromise execpted. |
| None responsive input form | Summernote form on site 'add a method' is not responsive. The right end is cutted by the browser, the user has to scroll to the right. Bad UX| <img src="readme.images/bug_summernote_form_not_responsive.PNG" alt="show screenshot of bug on website" width="500"> | A solution might be to separated the method form inout fieds and implement via Bootstrap utility classes responsive elements i.e. divs which contain the input form. |
|  No p element in scope but a p end tag seen. | Appears first time in validator. The content inside {{ method.summary | safe }} seems to include an extra <p> tag on the rendered HTML site. This is what's causing the validator error about having "no <p> element in scope but a </p> end tag seen.". This it is not prevent the site form running the failure is documented and is observed. Pops up on the last date in the css validation docu it is not mentioned. | <img src="readme.images/bug_rendering_failure_create_method_validator.PNG" alt="show screenshot of bug on website" width="250"> <img src="readme.images/bug_rendering_failure_create_method.PNG" alt="show screenshot of bug on website" width="250">


## Bugs (fixed)

| Bug | Description  | images (optional) | Correction |
| --- |------------- | ----------------- | -----------|
| Rendering issue of mehtod cards on landing page | TypeField for method.summary hasn't been rendered correctly deu to usage of summernote. | <img src="readme.images/bug_rendering_problem_safe.PNG" alt="show screenshot of bug on website" width="250"> <img src="readme.images/bug_rendering_problem_safe2.PNG" alt="show screenshot of bug fix on website" width="250"> | Including of "safe"-function for method.summary fixed the issue. |
| method cards overlapp filter section| The divs of the method cards are not aligned with the structure. There are more columns than the total grid (12 columns)inside a .row, the elements overlaps because Bootstrap can't correctly allocate space for each column. Issue come up twice, also related to another div. | <img src="readme.images/bug_filter_method overlay.PNG" alt="show screenshot of bug on website" width="500">| The missing bootstrap utility class "card-type" has been added and the correct number of grid columns has been adjusted. |
| The image in the masterhead section is dislocated | It seems dislocated. There has been a breakpoint adjustment to a fixed 200px height. In a responisve set up this is not a good idea since the masterhead's height can change. |  <img src="readme.images/bug_image_size_masterhead_method_page.PNG" alt="show screenshot of bug on website" width="500"> | The fixed height has to be removed. The image is more flexible, however, when zooming out 250% it still can be (depending on the screen size) that there is again space between bottom of masterhead and image. But that's sufficient. If the image size would always be depending on the masterhead size the ratio would be a problem and the iamge would look strange. Here the best compomise currently is made (keeping in mind a responsive and flexible setup) |
| Like button is not visible | The Like button is not visible, only the blue text color. | <img src="readme.images/bug_like_button_no_button.PNG" alt="show screenshot of bug on website" width="500"> | Background-color and text color has been mixed up. It is corrected: color = white, background-color = blue .|
| Phone view on site private_collection | The symbol "|" which separates method title and date can be irritation in the mobile view. | <img src="readme.images/bug_phone_view_strange_I.PNG" alt="show screenshot of bug on website" width="500"> | The symbol "|" has been removed. in private_collection.html . |
| "File not existing" and old css code is displayed in production | There was no error message, however, the requested result was not displayed. After adding the new images, new code I missed to run "python manage.py collectstatic" | ... | run "python manage.py collectstatic" |
| DisallowedHost at /create | Invalid HTTP_Host header | <img src="readme.images/bug_disallowedhost.PNG" alt="show Error message" width="500">| Add the correct host address to settings.py allowed hosts.|
| IndentationError: unexpected indent | failrue in views.py at function def method_create(request):  |  <img src="readme.images/but_indentation_error_unexpected ident1.PNG" alt="shows failure in code" width="250">  <img src="readme.images/but_indentation_error_unexpected ident2.PNG" alt="shows Error message" width="250">| Correct indentation by pushing the marked code area to the right |


## Validator Testing
Validator testing has been done on:

### [CI Python validator](https://pep8ci.herokuapp.com/)
No errors were returned.

<details>
    <summary>see details about CI Python validator</summary>

#### methods_library/settings.py

<img src="readme.images/testing_python_validator_methods_library_settings.PNG" alt="shows result of validation of methods_library/settings.py" width="650">

#### methods_library/urls.py

<img src="readme.images/testing_python_validator_methods_library_url.PNG" alt="shows result of validation of methods_library/url.py" width="650">


#### view_methods/admin.py

<img src="readme.images/testing_python_validator_view_methods_admin.PNG" alt="shows result of validation of view_methods/admin.py" width="650">

#### view_methods/forms.py
<img src="readme.images/testing_python_validator_view_forms.PNG" alt="shows result of validation of view_methods/forms.py" width="650">

#### view_methods/models.py
<img src="readme.images/testing_python_validator_view_models.PNG" alt="shows result of validation of view_methods/models.py" width="650">

#### view_methods/test_forms.py
<img src="readme.images/testing_python_validator_view_test_forms.PNG" alt="shows result of validation of view_methods/test_form.py" width="650">

#### view_methods/test_views.py
<img src="readme.images/testing_python_validator_view_test_views.PNG" alt="shows result of validation of view_methods/test_views.py" width="650">

#### view_methods/urls.py
<img src="readme.images/testing_python_validator_view_methods_urls.PNG" alt="shows result of validation of view_methods/urls.py" width="650">

#### view_methods/views.py
<img src="readme.images/testing_python_validator_view_methods_views.PNG" alt="shows result of validation of view_methods/views.py" width="650">

</details>


### [HTML validator](https://validator.w3.org/)
No errors were returned.

<details>
    <summary>see details about HTML validator</summary>

No errors were returned

#### base.hmtl + index.html
<img src="readme.images/w3_html_validator_index.PNG" alt="shows result of HTML validation" width="650">

#### base.hmtl + about.html
<img src="readme.images/w3_html_validator_about.PNG" alt="shows result of HTML validation" width="650">

#### base.hmtl + method_creation.html
<img src="readme.images/w3_html_validator_method_creation.PNG" alt="shows result of HTML validation" width="650">

#### base.hmtl + method_page.html
<img src="view_methods/templates/view_methods/method_page.html" alt="shows result of HTML validation" width="650">

#### base.hmtl + private_collection.html
<img src="view_methods/templates/view_methods/private_collection.html" alt="shows result of HTML validation" width="650">

</details>


### [CSS validator](https://jigsaw.w3.org/css-validator/)
No errors were returned

<details>
    <summary>see details about CSS validator</summary>

#### base.hmtl + index.html
<img src="readme.images/w3c_css_validator_result.PNG" alt="shows result of HTML validation" width="650">

</details>



### [JS Validator] (https://jshint.com/)
No errors were returned

<details>
    <summary>see details about JS validator</summary>

#### buttons_method_form.js
<img src="readme.images/testing_jshint_validator_buttons_method_form.PNG" alt="image shows preview of validator results" width="500px">

#### comments.js
<img src="readme.images/testing_jshint_validator_comments.PNG" alt="image shows preview of validator results" width="500px">

</details>


### Validation Functions
In a Django project, validations are typically added in forms.py and models.py. In forms.py, custom validation can be applied by defining methods like clean_fieldname or overriding the clean() method for form-level validation. In models.py, validations are usually added using field options like validators or by overriding the model's clean() method to ensure data integrity before saving to the database. Both approaches help enforce business logic and ensure valid data.


### Image validation
The MethodForm class includes custom validation logic for the featured_image field. The clean_featured_image method is a custom validator that handles the validation of the featured_image field in the MethodForm. It checks for the image size and handles various scenarios:

If the user checks the delete checkbox (delete_featured_image), the image is removed by setting the value of featured_image to None. This ensures that no image is retained in the database if the user wishes to delete it. If no image is uploaded, the method returns None, which allows the field to remain empty. If the uploaded image is a URL (for example, returned by an external service like Cloudinary), the method simply returns the URL string as-is without further processing. If the image is uploaded as a file object, the method checks whether the size exceeds the 3MB limit. If the file size is greater than the limit, a ValidationError is raised, informing the user that the image size must be under 3MB. If the uploaded file is not a valid image (i.e., it doesn't have a size attribute), the method raises a ValidationError indicating that the uploaded file is not a valid image.

<img src="readme.images/features_def_clean_featured_image().PNG" alt="shows relevant code" width="700">


#### Input field validation
Several input field validators have been implemented to ensure data integrity and consistency within the database.

- No Blank Input Validator: Required fields, such as title and description, are set with blank=False to prevent empty submissions, ensuring critical data is always provided
- Length Limit Validator: The max_length attribute restricts input lengths for fields like descriptions or titles. Custom validators enforce additional length restrictions as needed
- Choice Field Validator: Fields with predefined values, such as status, use the choices option to restrict input to valid options, preventing data entry errors.
- Group Size Validator: For fields like group size, custom validation ensures the input falls within a specified range, using MinValueValidator and MaxValueValidator
- Cloudinary Image Validator: A custom validator checks that images uploaded to Cloudinary are in acceptable formats (JPG, JPEG, PNG) and under a 3MB size limit

These validators are applied across the project to ensure that data entered is valid, reducing errors and maintaining consistency. They are defined in models.py to enforce rules during data entry:

<img src="readme.images/testing_validation_slug_entry.PNG" alt="shows relevant code" width="700">

<img src="readme.images/testing_validation_title_entry.PNG" alt="shows relevant code" width="700">

<img src="readme.images/testing_validation_group_size.PNG" alt="shows relevant code" width="700">


## Lighthouse Reports
LightHouse is a web performance testing tool used to assess a website's performance. The report is generated through Google Chrome.

<details>
    <summary>see LightHouse report for each site</summary>

#### Index.html
<img src="readme.images/testing_lighthouse_report_index.PNG" alt="shows Lighthouse report generated by GoogleChrome" width="700">

#### Method_page.html
<img src="readme.images/testing_lighthouse_report.PNG" alt="shows Lighthouse report generated by GoogleChrome" width="700">

#### About.html
<img src="readme.images/testing_lighthouse_report_about.PNG" alt="shows Lighthouse report generated by GoogleChrome" width="700">

#### private_collection.html
<img src="readme.images/testing_lighthouse_collection.PNG" alt="shows Lighthouse report generated by GoogleChrome" width="700">

#### Method_page.html
<img src="readme.images/testing_lighthouse_create.PNG" alt="shows Lighthouse report generated by GoogleChrome" width="700">

</details>


## Responisvness
The responsiveness was manually tested using Chrome's devtools throughout the entire development process.

<img src="readme.images/testing_validation_responsiveness.PNG" alt="shows usage of DevTool by GoogleChrome" width="700">

<img src="readme.images/readme_am_i_responsive.PNG" alt="shows usage of DevTool by GoogleChrome" width="700">


## Accessability
I confirm that the selected colors and fonts are easy to read and accessible by using Lighthouse in devtools (Chrome), see chapter "Lighthouse reports".


### ARIA (Accessible Rich Internet Applications)

**ARIA Labels:**
Added aria-label to buttons like "Toggle methods details", "Toggle comments details", and "Toggle liked methods details" for better accessibility.
Added specific aria-label to links, such as the method link and liked method link, to clearly describe the action for screen reader users (e.g., "Visit method page for liked method: {{ method.title }}").

**Accordion Components:**
Each accordion button now has aria-expanded to indicate whether the section is expanded or collapsed, and aria-controls to associate the button with the content it controls.
The accordion items have appropriate aria-live="polite" to ensure that changes (like expanding sections) are announced by screen readers.

**Images:**
I’ve updated the alt text for the image in the masthead to be more descriptive (alt="A placeholder image for user content").

**ARIA Roles and Regions:**
I’ve added role="region" for each section (methods, comments, and liked methods) to indicate that these are distinct, thematic regions of the page. Each section is also assigned an aria-labelledby attribute pointing to a relevant heading (e.g., aria-labelledby="methodSection").

**Live Regions:**
Used aria-live="polite" for sections that dynamically change (e.g., when an accordion expands or collapses), ensuring that screen readers notify users about new content.

**Empty State:**
If no methods or comments are available, it announces “No methods found” or “No comments found” to provide meaningful feedback to the user.
