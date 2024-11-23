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
