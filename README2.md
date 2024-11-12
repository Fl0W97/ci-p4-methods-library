# Method library

Welcome to my fourth project, 'method library'. It is a script that supports team coaches and scrum masters to plan trainings and especially finding new inspriation for methods and  energizer games to keep the workshop member motivated. The focus is on the method library since there are currently just basic functinallities deployed such as methods idea stored in a data base, comment function and a log in area to create and collect its own methods.

<img src="README.images/AmIresponsive.PNG" alt="image shows responisveness by presenting preview on different devices">


<img src="README.images/overview_features.PNG" alt="shows the start view">


## User Stories, Project scope
see in GItHub project [documented User Stories](https://github.com/Fl0W97/ci-p4-methods-library/issues) 

### Site Users (MVP1)

- As a Site User I can *see directly the purpose of the website * so that get an orientation what I can do
- As a Site User I can view all methods so that I can choose one, get motivated to share comments and use the methods in my workshops
- As a Site User I can comment on a method so that I can interact with the community
- As a Site User I can read the methods in an structured way so that *it's easy to go through them.
- As an early Site User I can view existing methods on the site so that I am getting inspiration and are willing to share my methods
- As a Site User I can register an account so that I can comment on a method
- As a Site User I want to get a notification once I change something so that I get feedback of my actions
- As a Site User I can modify or delete my comment on a method so that * I can be involved in the conversation*

### Site Admin (MVP1)

- As a Site Admin I can create, read, update and delete methods so that I can manage my content
- As a Site Admin I can approve comments so that I can manage and control the content on the website

### Site Users (MVP2)

- As a Site User I can view the different methods with images and teaser so that I get an idea what I can see on the detail site
- As a Site User I can see images and a good color contrast so that I like to sty on the website form a visual perspective
- As a Site User I can get a notification once I change something so that I receive feedback of my actions
- As a Site User I can filter methods on the main page so that I can optimize my search
- As a Site User I want to get a notification once I change something so that I get feedback of my actions
- As a Site User I can create, update and delete my own methods so that *I can share my methods and adjust those with the community*

### Site Admin (MVP2)

- As a Site Admin I can approve methods from other Site Users so that I have control of the content
- As *Site Admin* I can *approve new methods from Site Users* so that *I can have control of the content on the website*


## Remarks for handeling the program


## Features

### Feature overview:

| Feature | Description  |
| ------------- |------------- |
|Database | Django database for methods|
|Authentification | User log in area to provide rights to create, update, comment and collect methods. Using allauth package|
|Comments | |
|Super user functionalities | |
|different user roles | |
|CRUD for Comments | using CrispyForms |
|CRUD for Methods | |
| summernote admin panel customization | ...
| Filter function | purpose, duration, location ...
| like function | ...

## UX Design


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


### Code

| No | Description  | Source | URL |
| -- | ------------ | ------ | --- |
| 1 | Python Specific core concepts | Code institute | i.e. https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+CPP_06_20+3/courseware/f780287e5c3f4e939cd0adb8de45c12a/8d9c1efb1864472bb682a0c233898a17/ |
| like button | 



using view, model and template code from Code Institute -- project "Therefore I Blog"


### Template

Python Essential Template from Code Institute
https://github.com/Code-Institute-Org/p3-template