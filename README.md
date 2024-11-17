# Method library

Welcome to my fourth project, 'method library'. This website supports team coaches and scrum masters to plan trainings to find new inspriation for methods and energizer (small little games) to keep the workshop member motivated. The wording "method" is used for methodology used in the context of training and coaching. The focus is on the method library since there are currently just basic functinallities deployed such as methods idea stored in a data base, comment function and a log in area to create and collect its own content.

<img src="README.images/AmIresponsive.PNG" alt="image shows responisveness by presenting preview on different devices" width="700">


## Website overview/ features
### Landing page, index.html
<img src="README.images/README_landing_page.PNG" alt="shows landing page" width="700">
<img src="README.images/README_landing_page_use_filter.PNG" alt="shows landing page" width="700">

Here a first look at the landing page. There is a navigation element on top, a filter area and below all methods are shown which have been shared within the community.
The user gets a first overview of the activities on the webiste and he can directly start to filter throug hthe list of methods to find an idea he can use for his next workshop. Once he selects on method, he is guided to the subpage of the relevant method.


### Navigation
<img src="README.images/README_nav_not_logged_in.PNG" alt="shows navigation in logged out mode" width="700">
<img src="README.images/README_nav_logged_in.PNG" alt="shows navigation in logged in mode" width="700">

The navigation displayes different elements based on the log-in status.
If the user is logged out he sees the elements Home, About, Register and Login. In addition, here recevies the hint that he is logged out "".
If the user is logged in he sees Home, About, Add a Mehtod, Your private Collection and Logout. In addition, here recevies the hint that he is logged in "".


### About page, about.html
Shows what the webiste is about and introduces the creator of the website.

<img src="README.images/README_about_page.PNG" alt="shows about page" width="700">


### Detailed method view, method_page.html
Displays instruction and further information which can be useful for integrating this method in a workshop. In addition, there is a comment section and the possibility to add a comment.
<img src="README.images/README_detailed_method_page.PNG" alt="shows detailed method page" width="700">


### Log-in / Log-out process, (add . html sites)

Register

<img src="README.images/README_register_process.PNG" alt="shows register process" width="700">

<img src="README.images/README_register_process2.PNG" alt="shows register process" width="700">

Log-in

<img src="README.images/README_log_in_process.PNG" alt="shows log-in process" width="700">

<img src="README.images/README_log_in_process2.PNG" alt="shows log-in process" width="700">



Sign-out

<img src="README.images/README_sign_out_process.PNG" alt="shows sign-out process" width="700">

<img src="README.images/README_sign_out_process2.PNG" alt="shows sign-out process" width="700">


### Add a Method, method_creation.html
<img src="README.images/README_add_a_Method_page.PNG" alt="shows add method page" width="700">


### Your private Collection, private_collection.html
<img src="README.images/README_private collection_page.PNG" alt="shows private collection page" width="700">




### Feature overview:

| No. | Feature | Description  | code |
| --- | ------- |------------- | ---- |
| 1 | Filter function | purpose, duration, location ... however, the filter options are hard coded, has to be added as asoon as a new purpose is implemented by the admin | |
| 2 | View functions | various view function are used within the project generic ListView and TempalteView (class based) and further function-based ones. To see and sort the methods on the index.html, on private_collection.html, method_page.html (add examples)||
| 3 | Authentification | User log in area to provide rights to create, update, comment and collect methods. Using allauth package ||
| 4 | Add comments | CRUD for Comments | |
| 5 | add Methods | Part of CRUD for Methods using using CrispyForms, adding summernote feature for a better editing||
| 6 | admin panel customization | filtering, view adjustment (examples), adding summernote, adding info texts when entering values i.e. about, methods ||
| 7 | From for about me content | Can be added easily by admin. Restriction is made by define queryset.filter.first() so taht only the first about page entry is shown. In addition, there is a hint in the admin panel, that just the first entry is displayed on the website by using fieldsets in class AboutAdmin (admin.py). |
| 8 | Super user functionalities | ... |
| 9 | like function | The logged-in User is able to like a method. Furthermore, there the like model is used to count the likes. The total number of likes is displayed and on the landing page it is sorted - the method with the highest number of likes is shown on the top. ||
| 10 | Automatically slug transfer | By adding a ne method the user don't have to include content in the slug input filed (it might be deleted soon) ||





## User Stories, Project scope
see in GItHub project [Methods library](https://github.com/Fl0W97/ci-p4-methods-library/issues)

### Site Users (MVP)

- As a Site User I can *see directly the purpose of the website * so that get an orientation what I can do
- As a Site User I can view all methods so that I can choose one, get motivated to share comments and use the methods in my workshops
- As a Site User I can comment on a method so that I can interact with the community
- As a Site User I can read the methods in an structured way so that *it's easy to go through them.
- As an early Site User I can view existing methods on the site so that I am getting inspiration and are willing to share my methods
- As a Site User I can register an account so that I can comment on a method
- As a Site User I want to get a notification once I change something so that I get feedback of my actions
- As a Site User I can modify or delete my comment on a method so that * I can be involved in the conversation*

### Site Admin (MVP)

- As a Site Admin I can create, read, update and delete methods so that I can manage my content
- As a Site Admin I can approve comments so that I can manage and control the content on the website

### Site Users

- As a Site User I can view the different methods with images and teaser so that I get an idea what I can see on the detail site
- As a Site User I can see images and a good color contrast so that I like to sty on the website form a visual perspective
- As a Site User I can get a notification once I change something so that I receive feedback of my actions
- As a Site User I can filter methods on the main page so that I can optimize my search
- As a Site User I want to get a notification once I change something so that I get feedback of my actions
- As a Site User I can create, update and delete my own methods so that *I can share my methods and adjust those with the community*

### Site Admin

- As *Site Admin* I can *approve new methods from Site Users* so that *I can have control of the content on the website*
- summernote, filter comments and methods, show comment text or method title... in admin panel view

## UX Design

For this project Bootsrap is used. Reusage of many Bootstrap utility classes such as "row", "md-3", "bg-primary" ... 

General tempaltes, methods_library/templates
  base.html (methods_library/templates) to defined Header and Footer
  register.html (methods_library/templates/account) to provide content and function for login process
  login.html (methods_library/templates/account) to provide content and function for login process
  signout.html (methods_library/templates/account) to provide content and function for login process


Custom Templates, methods_library/view_methods/templates
  index.html
  about.html
  method_creation.html
  method_page_html
  private_collection.html

 
### Stylesheed 

Within style.css standard Bootstrap utility classes are defined.

The color schema should be light with dark accents. Encauraging to share and inspire.

body #F9FAFC

.light-bg background-color: #fff

.dark-bg background-color: #445261

.main-bg background-color: #F9FAFC



### User feedback/ guidance / CRUD
There are various notifications which representing feedback for the user after CRUD activity. Besides log-in and sign-out, which is already shown in the above chapter, there are notifications for dealing with methods, comments and like buttons. The standard function message.add_message() is used and mostly combined with an if-clause. In the following a few examples are shared:

<img src="README.images/README_feedback_comment.PNG" alt="shows feedback comment">
<img src="README.images/README_feedback_comment_edit.PNG" alt="shows feedback comment">
<img src="README.images/README_feedback_comment_delete.PNG" alt="shows feedback comment">
<img src="README.images/README_feedback_method.PNG" alt="shows feedback comment">
<img src="README.images/README_feedback_like.PNG" alt="shows feedback comment">


## Databases
PostgreSQL is used for production and Sqlite3 is used for .

#### ERD_method
Main database to store and manage methods. Can be created by Admin and logged-in users.
Admin has to approve the new method before it is displayed on the website. Edit or delete functionality is only given to Admin.

<img src="README.images/README_ERD_method.PNG" alt="shows ERD_method">
<img src="README.images/README_ERD_method_code.PNG" alt="shows ERD method code">


#### ERD_comments
Database to store and manage comments. Can be created by Admin and logged-in users
Admin has to approve the new comment before it is displayed on the website. Edit or delete functionality is only given to Admin and authorized users.

<img src="README.images/README_ERD_comments.PNG" alt="shows ERD_comments">
<img src="README.images/README_ERD_comments_code.PNG" alt="shows ERD comments code>

#### ERD_about
Database to store and manage content for the about page. Can be adjsuted only by Admin.
The form helps the Admin to adjsut the content without ajdusting the code so that the admin don't need coding skills to make adjustments.

<img src="README.images/README_ERD_about.PNG" alt="shows ERD_about">
<img src="README.images/README_ERD_about_code.PNG" alt="shows ERD about code">

#### ERD_like
Database to store likes. Based on that the numbers of likes are displayed. Furthermore, the ListView on the landing page sorts the methods based on the number of likes. The more likes a method gets the more on top the method is displayed.

<img src="README.images/README_ERD_like.PNG" alt="shows ERD_like">
<img src="README.images/README_ERD_like_code.PNG" alt="shows ERD like code">



## Testing

- Testing was conducted regularly in small intervals throughout the development process as well as at the end of the project to ensure functionality and identify any potential issues early on.
- Bugs that were encountered during testing have been thoroughly documented in the Bug section, detailing the nature of the issue and the steps taken to resolve it.
- Validators were used to ensure that the code meets all necessary standards and specifications. More details can be found in the Validators chapter.
- Logic checks were performed to verify that the program's operations and algorithms were working as intended. This included testing different scenarios and edge cases to ensure robustness.
- Manual input tests were carried out to simulate real-world usage of the application. This involved entering data manually into the system to ensure that all inputs were handled correctly and that the user interface responded appropriately.


### Automated testing

#### view_methods/test_views.py

TestMethodViews: Tests if the method page correctly displays a method and its comments.

class TestMethodViews(TestCase)
    def setUp(self)
    def test_render_method_detail_page_with_comment_form(self)

<img src="README.images/README_testing_TestMethodView.PNG" alt="shows TestMethodView">
    

TestMethodFilteringViews(TestCase): Tests filtering by purpose, duration, and location for the MethodList view.

class TestMethodFilteringViews(TestCase)
    def setUp(self)
    def test_filter_methods_by_purpose(self)

<img src="README.images/README_testing_TestMethodFiltering.PNG" alt="shows TestMethodFiltering">


#### view_methods/test_forms.py

TestCommentForm(TestCase); Tests adding a new comment with valid and invalid input

class TestCommentForm(TestCase)
    def test_form_is_valid(self)
    def test_form_is_invalid(self)

<img src="README.images/README_testing_TestCommentForm.PNG" alt="shows TestCommentForm">



/// further IDEAS for automated tests ///
Test_views.py
CommentCreateTest: Tests creating a new comment on the method page.
CommentEditTest: Tests editing a comment and ensuring only the author can edit it.
CommentDeleteTest: Tests deleting a comment and ensuring only the author can delete it.
Testing Like counter
Testing new app "collection"
/// IDEAS for testing ///


### Decisions during development

1) Dealling with generic ViewList also for filtering etc. (reusability)

2) Since the current app (view_methods) already deals with displaying and interacting with methods, it seems logical to keep the method creation functionality in the same app. Advantages of Keeping it in the Same App:

Simplicity: You can handle both displaying and creating methods in the same app, making it easier to manage relationships between views and models.
Faster Development: If the creation of methods is relatively simple and closely tied to the same workflow as viewing them, you can keep things together and not worry about the overhead of a separate app.

If in the future the requirements become more complex and the view_methods app growing too large, it's always possible to refactor it into multiple smaller apps.
So, for now, keeping it within the same app (view_methods). It keeps things simpler and more maintainable.


### Bugs (not fixed)

| Bug | Description  | images (optional) | Correction |
| --- |------------- | ----------------- | -----------|
| django.db.utils.DataError: invalid input syntax for type integer: "indoor, outdoor" | Error during database migration. According to the error message the migration file 003 contains an error. However, after adjsuting the file the some error occured.| <img src="README.images/README_bug_error_message_syntax error_none.PNG" alt="shows error message"> | Old migration files has been saved outside the project and deleted in the project. New command "python3 manage.py migrate" has been done. A new migration file exists and is working. |
| django.db.utils.OperationalError: near "None": syntax error | The error occured during testing. The local database db.sqlite had an inconsistency. The migration file "view_methods.0003_alter_method_alt_atr_alter_method_duration_and_more" had a failre related to NONE. After seveal tries to fix the issue I decided to focus on the rest of the project. | ...| I saved all migration files and removed them from the project. Then I run pyhton3 manage.py makemigrations and python3 manage.py migrate.|
| Uncaught Type Error: this._element is undefined | Customization summernote for admin panel | <img src="README.images/README_bug_js_summernote_customization_code.PNG" alt="shows error message in console"> | function was deleted |

**Error message in terminal**

**Suggestion for fixation. However, implementation was not successful**


### Bugs (fixed)

| Bug | Description  | images (optional) | Correction |
| --- |------------- | ----------------- | -----------|
| Wrong column order is displayed | Ater adjusting the mehtod_page.html the position of the div has been wrong and overlapping.| <img src="README.images/..." alt="image shows Error message"> | adding the correct Bootstrap utility class to the relevant divs (class="col-md-8" and class="col-md-4" so that column range 12/12 is valid) |
| "File not existing" and old css code is displayed in production | There was no error message, however, the requested result was not displayed. After adding the new images, new code I missed to run "python manage.py collectstatic" | ... | run "python manage.py collectstatic" |
| Couldn't find host |------------- | <img src="README.images/..." alt="image shows Error message"> | Add my host adress to settings.py allowed hosts.|
| Server 505, ... | failrue in views.py ... | <img src="README.images/..." alt="image shows Error message"> | -----------|
| indetation ... | failrue in views.py ... | <img src="README.images/..." alt="image shows Error message"> | -----------|


### Validator Testing
Validator testing has been done on:

#### [CI Python validator](https://pep8ci.herokuapp.com/)
No errors were returned for run.py

<img src="README.images/PI_python_linter_validation.PNG" alt="image shows preview of validator results" width="800px">

<details>
    <summary>further results of HTML, CSS Validator</summary>

<img src="" alt="image shows preview of validator results" width="500px">
<img src=""_html_end.PNG alt="image shows preview of validator results" width="800px">


#### [HTML validator](https://validator.w3.org/)
No errors were returned

<img src="README.images/HTML_validation.PNG" alt="image shows preview of validator results" width="500px">


#### [CSS validator](https://jigsaw.w3.org/css-validator/)
No errors were returned

<img src="README.images/CSS_validation.PNG" alt="image shows preview of validator results" width="500px">


#### [JS Validator] (https://jshint.com/)
Errors occured. However, since I reused the suggested template from Code Institute and I haven't made any adjustments I keep the current status.

Code from index.js and defaul.js checked. 

Here an example of index.js
<img src="README.images/JS_validation.PNG" alt="image shows preview of validator results" width="500px">

</details>


### Validations in the code

views.py
    # validation
    def clean(self):
        cleaned_data = super().clean()
        group_size_min = cleaned_data.get('group_size_min')
        group_size_max = cleaned_data.get('group_size_max')

...



#### Accessability
I confirm that the selected colors and fonts are easy to read and accessible by using Lighthouse in devtools (Chrome).

<img src="README.images/GoogleLighthouse.PNG" alt="image shows GoogleLighthouse analysis"> 


## Tools & Technologies used

The main functions are generated with Python. However, to set up the whole project a standard template consits of files of json, js, txt, html and css.

- node.js
- phython (import prettyTable, os, gspread, datetime, requests, json)
- Git used for version control (git status, git add, git commit)
- GitHub used for secure online code storage
- GitHub Pages used for hosting the deployed front-end site
- GitHub- template reused from love sandwiches
- Gitpod used for local IDE for development
- Heroku
- JavaScript
- Html
- CSS
- Django
- test JS 8MANDATORß
- test Phython
- Bootstrap5
- Crsipy Forms package
- summernote package
- allauth package

requirements.txt:

- asgiref==3.8.1
- crispy-bootstrap5==0.7
- dj-database-url==0.5.0
- Django==4.2.7
- django-allauth==0.57.2
- django-crispy-forms==2.3
- django-summernote==0.8.20.0
- gunicorn==20.1.0
- oauthlib==3.2.2
- psycopg2==2.9.10
- PyJWT==2.9.0
- python3-openid==3.2.0
- requests-oauthlib==2.0.0
- sqlparse==0.5.1
- whitenoise==6.5.0


## Deployment
The site was deployed to a Heroku page using a GitHub repository for data storage.

    Heroku page: https://dashboard.heroku.com/apps/methods-library/deploy/github

    GitHub repository: https://github.com/Fl0W97/ci-p4-methods-library

### GitHub

The steps to set up your repository in GitHub are as follows:

- In the GitHub repository, navigate to the Settings tab
- From the source section drop-down menu, select the Main Branch, then click "Save"
- The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

<details>
    <summary>Cloning repository</summary>

1. Visit the GitHub repository.
2. Find the Code button situated above the file list and give it a click.
3. Choose your preferred cloning method — whether it's HTTPS, SSH, or GitHub and hit the copy button to copy the URL to your clipboard.
4. Launch Git Bash or Terminal.
5. Navigate to the directory where you want the cloned directory to reside.
6. In your IDE Terminal, input the following command to clone the repository:
 git clone https://github.com/Code-Institute-Org/p3-template 
7. Press Enter to create your local clone.

</details>

### settings.py
The settings.py file is already included in Djangp orject. However, to set up this project further adjustements has to be done:


#### Secret Key
To ensure that the secret.key is not provided to heroku or the git storage an env.py file is created to store the sensitive data.
The keys will be passed via os.environ.setdefault() function. There are two keys, which both has to be provided to heroku. First, the postgreSQL key which is generated via Code Institute and the secret_key which also mentioned in settings.py.

<img src="README.images/README_settings_secret_key.PNG" alt="image shows secret key documentation in settings.py"> 

#### Allowed Hosts
Make sure to document your own host name as well as the heroku host name. In addition you can add further hosts if needed in the same list.
<img src="README.images/README_settings.py_allowed_hosts.PNG" alt="image shows allowed hosts documentation in settings.py"> 

#### CRSF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS setting is used to specify a list of trusted domains or origins for Cross-Site Request Forgery (CSRF) protection. When you include CSRF_TRUSTED_ORIGINS in your settings.py file, you are telling Django which domains or URLs are trusted when submitting CSRF tokens, specifically for cross-origin requests (e.g., when your frontend and backend are served from different domains).

<img src="README.images/README_settings.py_CSRF_TRUSTED.PNG" alt="image shows csrf trusted documentation in settings.py"> 

#### Middleware
In Django, middleware is a framework of hooks that allows you to process requests globally before they reach the view (request processing) and after they leave the view (response processing). Middleware components are processed in the order they are listed in the MIDDLEWARE setting in your settings.py file.

Middleware is essentially a layer that sits between the request and the response, providing a way to process and modify requests before they reach the view, and modify responses before they are returned to the client.
<img src="README.images/README_settings.py_middleware.PNG" alt="image shows middleware list documentation in settings.py">

#### Templates
In Django, templates are a framework used via Bootstrap to simplify the handling of multiple site wihtin one project. There is one base.html which defines the header and footer of the webiste. The main section is mostly empty and filled with various custom template input. The relevant Bootstrap tags which aer used for the combination of base.html and i.e. index.html are {% block content %}, {% endblock content %} and in index.html {% extends "base.html" %}, {% block content %}, {% endblock %}. To enale this functionality the following content has to be added to the settings.
<img src="README.images/README_settings.py_templates.PNG" alt="image shows template documentation in settings.py">

#### Databases
In this project two databases are used.More information is shared in the subchapter databases. Here it is documented how both databases are added to the project in the settings.
<img src="README.images/README_settings.py_databases.PNG" alt="image shows database documentation in settings.py">


#### Forms (CrispyForms)
'Crispy Forms' is a package provided by Django. It offers a range of edit possibilites in a from for the creator. See below how it is included in the settings.
<img src="README.images/README_settings.py_crispyForms.PNG" alt="image shows crispyForm documentation in settings.py">


### Configure Heroku 
The steps to configure Heroku are as follows:

Log in to your account, or set up a new one
Create a new app on Heroku

<img src="README.images/README_heroku_create_new_app.PNG" alt="image shows infos about heroku set up"> 

There are two keys, which both has to be provided to heroku. First, the postgreSQL key which is generated via Code Institute and the secret_key


#### Connect to GitHub
Next, you can configure deploys with Github. If you prefer to deploy without using Github, you can read Heroku's deployment ([documentation](https://devcenter.heroku.com/categories/deployment)). 

In the Deploy tab, select the option to Connect this app to GitHub

<img src="README.images/README_heroku_connect_to_github1.PNG" alt="image shows infos about heroku set up" width="600px">

Select the branch you want to deploy your app from

<img src="README.images/README_heroku_manually_deployment.PNG" alt="image shows infos about heroku set up" width="600px">


#### Add Discord credentials
Before your app can go online, you'll have to configure your Heroku environment with your Discord bot's credentials:
Add your bot’s TOKEN, GUILD_ID, CLIENT_ID, and any other credentials your bot might need. More details on credentials for Baker bot can be found in the tutorial.

<img src="README.images/README_heroku_credentials.PNG" alt="image shows infos about heroku set up" width="600px">


#### Add a buildpack
Next, add a Heroku buildpack to your app. Click add a buildpack to your app and configure it for NodeJS.

<img src="README.images/README_heroku_add_builpack.PNG" alt="image shows infos about heroku set up" width="600px">


### Configure database
see Code Institute documentation for more details.
/// Instruction coming ///



## Improvements and ideas for subsequent projects

There are still open User Stories in the Backlog which can be added to the project for further improvments. There are ideas to provide more possibilites for the method managment for the Site Users. Not just creating, but editing. In addition, the Site User might have an additional area where he can storage methods he finds well to and reuse them for his workshops.

## Credits

### Content

Description of Heroku deployment is resused from github project
https://github.com/discord/heroku-sample-app/blob/main/README.md


Ideas and documentation of The walkthrough Project4 was reused and adjusted.

https://www.sessionlab.com/ - Insiration for functionalities and content for methods




filters:
https://stackoverflow.com/questions/34739680/how-to-add-filters-to-a-query-dynamically-in-django
https://www.youtube.com/watch?app=desktop&v=FTUxl5ZCMb8
https://www.youtube.com/watch?v=T862gjtlFvs

Like-button: 
https://stackoverflow.com/questions/73683387/how-to-add-like-button-to-each-blog-post-in-the-same-page-with-django
https://stackoverflow.com/questions/15407985/django-like-button?rq=3
https://www.youtube.com/watch?v=ZUiTiUj-tZw
https://www.youtube.com/watch?v=AZwc9hDBi04


Hint for Admin panel
fieldsets
how to use filedsets https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
use help_text: https://docs.djangoproject.com/en/5.1/ref/models/fields/#help-text

HInt for super() function and used in about and edit method views
https://docs.djangoproject.com/en/5.1/topics/class-based-views/, https://docs.python.org/3/library/functions.html#super

### Code

| No | Description  | Source | URL |
| -- | ------------ | ------ | --- |
| 1 | Python Specific core concepts | Code institute | i.e. https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+3/courseware/f780287e5c3f4e939cd0adb8de45c12a/8d9c1efb1864472bb682a0c233898a17/ |
| like button | 
| Summernote adjustment in forms | https://summernote.org/deep-dive/
| Fieldsets | https://docs.djangoproject.com/en/5.1/ref/contrib/admin/


using view, model and template code from Code Institute -- project "Therefore I Blog"


### Template

Python Essential Template from Code Institute
https://github.com/Code-Institute-Org/p3-template