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

| No. | Feature | Description  |
| No. | ------------- |------------- |

| No. | Filter function | purpose, duration, location ... however, the filter options are hard coded, has to be added as asoon as a new purpose is implemented by the admin |
| No. | View functions | various view function are used within the project generic ListView and TempalteView (class based) and further function-based ones. To see and sort the methods on the index.html, on private_collection.html, method_page.html (add examples)|
| No. | Authentification | User log in area to provide rights to create, update, comment and collect methods. Using allauth package |
| No. | Add comments | CRUD for Comments |
| No. | add Methods | Part of CRUD for Methods using using CrispyForms, adding summernote feature for a better editing|
| No. | admin panel customization | filtering, view adjustment (examples), adding summernote, adding info texts when entering values i.e. about, methods |

| No. | From for about me content | Can be added easily by admin. Restriction is made by define queryset.filter.first() so taht only the first about page entry is shown. In addition, there is a hint in the admin panel, that just the first entry is displayed on the website by using fieldsets in class AboutAdmin (admin.py). |
| No. | Super user functionalities | ... |
| No. | like function | ... |
| No. | ... | ... |

## User Stories, Project scope
see in GItHub project [documented User Stories](https://github.com/Fl0W97/ci-p4-methods-library/issues) 

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
style.css

colr schema

### User feedback/ guidance
notifications
(example)


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
- Testing was conducted regularly in small intervals throughout the development process as well as at the end of the project to ensure functionality and identify any potential issues early on.
- Bugs that were encountered during testing have been thoroughly documented in the Bug section, detailing the nature of the issue and the steps taken to resolve it.
- Validators were used to ensure that the code meets all necessary standards and specifications. More details can be found in the Validators chapter.
- Logic checks were performed to verify that the program's operations and algorithms were working as intended. This included testing different scenarios and edge cases to ensure robustness.
- Manual input tests were carried out to simulate real-world usage of the application. This involved entering data manually into the system to ensure that all inputs were handled correctly and that the user interface responded appropriately.




####view_methods/test_views.py

TestMethodViews: Tests if the method page correctly displays a method and its comments.

class TestMethodViews(TestCase)
    def setUp(self)
    def test_render_method_detail_page_with_comment_form(self)

TestMethodFilteringViews(TestCase): Tests filtering by purpose, duration, and location for the MethodList view.

class TestMethodFilteringViews(TestCase)
    def setUp(self)
    def test_filter_methods_by_purpose(self)


####view_methods/test_forms.py

TestCommentForm(TestCase); Tests adding a new comment with valid and invalid input

class TestCommentForm(TestCase)
    def test_form_is_valid(self)
    def test_form_is_invalid(self)



/// IDEAS for testing ///
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
| Error during migrate | django.db.utils.DataError: invalid input syntax for type integer: "indoor, outdoor" | ... | 


**Error message in terminal**

**Suggestion for fixation. However, implementation was not successful**


### Bugs (fixed)

| Bug | Description  | images (optional) | Correction |
| --- |------------- | ----------------- | -----------|
| ... | ... | <img src="README.images/" alt="image shows Error message"> | ... |
django.db.utils.OperationalError: near "None": syntax error | The error occured during testing. The local database db.sqlite had an inconsistency. The migration file "view_methods.0003_alter_method_alt_atr_alter_method_duration_and_more" had a failre related to NONE. After seveal tries to fix the issue I decided to focus on the rst of the project. I saved all migration files and removed them from the project. Then I did pyhton3 manage.py makemigrations and python3 manage.py migrate.


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
- test JS
- test Phython
- Bootstrap
- Crsipy Forms package
- summernote package
- allauth package



## Deployment
The site was deployed to a Heroku page using a GitHub repository for data storage.

    Heroku page: ...

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


### Configure Heroku 
The steps to configure Heroku are as follows:

Log in to your account, or set up a new one
Create a new app on Heroku

<img src="README.images/heroku_create_new_app.PNG" alt="image shows infos about heroku set up"> 

#### Connect to GitHub
Next, you can configure deploys with Github. If you prefer to deploy without using Github, you can read Heroku's deployment ([documentation](https://devcenter.heroku.com/categories/deployment)). 

In the Deploy tab, select the option to Connect this app to GitHub

<img src="README.images/heroku_connect_to_github1.PNG" alt="image shows infos about heroku set up" width="600px">

Select the branch you want to deploy your app from

<img src="README.images/heroku_manually_deployment.PNG" alt="image shows infos about heroku set up" width="600px">

#### Add Discord credentials
Before your app can go online, you'll have to configure your Heroku environment with your Discord bot's credentials:
Add your bot’s TOKEN, GUILD_ID, CLIENT_ID, and any other credentials your bot might need. More details on credentials for Baker bot can be found in the tutorial.

<img src="README.images/heroku_credentials.PNG" alt="image shows infos about heroku set up" width="600px">

#### Add a buildpack
Next, add a Heroku buildpack to your app. Click add a buildpack to your app and configure it for NodeJS.

<img src="README.images/heroku_add_builpack.PNG" alt="image shows infos about heroku set up" width="600px">


### Configure database
see Code Institute documentation


## Improvements and ideas for subsequent projects

- adding a tool to provide a scheudle for a whwole workshop day incl. mehtods and games

## Credits

### Content
By going through the API documentation and further examples of Alpha Vantage I decided which options will be added. Series update and smybol search seems a good start for providing stock information.


Description of Heroku deployment is resused from github project
https://github.com/discord/heroku-sample-app/blob/main/README.md

Ideas and documentation of The walkthrough Project4  were was reused and adjusted.

https://www.sessionlab.com/

Insiration for functionalities


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