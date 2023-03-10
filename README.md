# **TheMaintenanceCo**

TheMaintenanceCo is a fictional website for a fast food specific maintenance company. The website deploys a dashboard for three different types of users: manager, client and employee. The dashboard is customized for the needs of each user type. In the client dashboard the user can create categories and add equipments to each individual ones depending on the restaurant needs. The client can add, edit and delete jobs. In the manager dashboard the user can view, edit, delete and assign jobs to an employee. In the employee dashboard, the user is displayed with all jobs assigned to him only. The employee can add relevant feedback and mark jobs as done. When a job is marked as done, it moves to the completed jobs list. In this list a manager can still edit, delete or reopen jobs if needed, moving it back to the active list.
The website was developed with a minimalistic and clean design goal, only showing essencial elements when required to make the dashboard easy to use without overcomplicating things.
This fictional project was developed as a Portfolio Project 4 - Full Stack Website as part of the Diploma in Full Stack Software Development from [Code Institute](https://www.codeinstitute.net).

[You can view the live website here](https://the-maintenance-co.herokuapp.com)

![TheMaintenanceCo](readme/assets/images/cover.png)

# Table of Content

- [**Project**](#project)
    - [Objective](#objective)
    - [Site Users Goal](#site-users-goal)
    - [Site Owners Goal](#site-owners-goal)
    - [Project Management](#project-management)

- [**User Experience (UX)**](#user-experience-ux)
    - [Wireframes](#wireframes)
    - [User Stories](#user-stories)
    - [Site Structure](#site-structure)
    - [Design Choices](#design-choices)

- [**Features**](#existing-features)
    - [Home page](#home-page)
        - [*Home*](#home)
        - [*Navigation*](#navigation)
        - [*About*](#about)
        - [*Contact*](#contact)
        - [*Account*](#account)
        - [*Sign up*](#sign-up)
        - [*Login*](#login)
    - [Manager dashboard](#manager-dashboard)
        - [*Manager menu*](#manager-menu)
        - [*New jobs*](#new-jobs)
        - [*Active jobs*](#active-jobs)
        - [*Completed jobs*](#completed-jobs)
        - [*Filter*](#filter)
        - [*Users*](#users)
    - [Client dashboard](#client-dashboard)
        - [*Client menu*](#client-menu)
        - [*Jobs*](#jobs)
        - [*Categories*](#categories)
        - [*Equipments*](#equipments)
        - [*Add job*](#add-job)
        - [*Send message*](#send-message)
    - [Employee dashboard](#client-dashboard)
        - [*Jobs*](#employee-dashboard)

- [**Future Features**](#future-features)

- [**Technologies Used**](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Software](#frameworks--software)
    - [Libraries](#libraries)

- [**Testing**](#testing)

- [**Deployment**](#deployment)
    - [Deployment to Heroku](#deployment-to-heroku)
    - [To Fork the Repository](#how-to-fork-the-repository-on-github)
    - [Cloning The Project](#cloning-the-project)

- [**Credits**](#credits)

- [**Acknowledgements**]()

# **Project**

## Objective
The objective of this project was to create a dashboard job management tool that can be used by a maintenance company to keep track of jobs or tasks that need to be completed. It also serves as a tool for client, employee and management to communicate the different equipment maintenance needs. This was a good opportunity for me to develop and demonstrate my knowledge of HTML, CSS, JS, Python and the Django Framework all working together in a Full Stack solution.

## Site Users Goal
The site user if a client can log jobs for different maintenance needs of equipments in the restaurant. If an employee of the company it serves as a platform to organize all assigned jobs and a way to keep track of all the work done and feedback given.

## Site Owners Goal
The site owner uses the dashboard to organize the different maintenance services and is a powerfull tool to share with the company's clients.

## Project Management

### Github Board
In order to keep everything organized I used Github's built in project board to add all the different user stories and to move them along as they we're being completed. It worked really well for me and had a natural logical feel to it.

<details><summary><b>Github's project management board</b></summary>

![User Stories](readme/assets/images/project_board.png)
</details><br/>

[Back to top](#table-of-content)

### Database Schema
I wrote down the different models and fields I would need for the project in a numbers spreadsheet. It helped me go throught the logic of the different models and their relationship to one another.

I created the following models for the project:

- **Profile (user profile)** - A model created to store additional user information and is linked to the default user model from allauth.
- **Category** - Stores all the client created categories of equipments in the restaurant. It is a foreign key to the equipments model.
- **Equipment** - Stores all the different types of equipments in the store, it takes the category and user models as foreign key's.
- **Job** - This models stores all data relevant to the job a user created and has the user, category, equipment as foreign keys's.

<details><summary><b>Database ERD (Entity Relationship Diagram)</b></summary>

![Database ERD](readme/assets/images/erd.png)
</details><br/>

[Back to top](#table-of-content)

# **User Experience (UX)**

## Wireframes
A created all the initial wireframes using [Balsamiq](https://balsamiq.com). They were created with a desktop and responsive mobile options. There are some slight differences to the final project as some design choices where changed during the development process to pressent a better user experience.

<details><summary><b>Wireframes</b></summary>

![Wireframes1](readme/assets/images/dashboard.png)
![Wireframes2](readme/assets/images/home_page_wire.png)
![Wireframes3](readme/assets/images/mobile_add_job.png)
![Wireframes4](readme/assets/images/mobile_dashboard.png)

</details><br/>

[Back to top](#table-of-content)

## User Stories
This first step for this project was to write the user stories. They were used to guide the development and were divided in three user types: manager, client an employee. In the [testing](#testing) section I evaluate the outcome of each.

### Manager site user
|   |   |   |
|--------|--------|--------|
| As a Manager | I can access the managers dashboard so I can view new, active, and completed jobs. | &check; |
| As a Manager | I can create, update and delete users so I can manage access and permissions. | &check; |
| As a Manager | I can assign jobs to employees so I can plan what each employee will work on. | &check; |
| As a Manager | I can mark jobs as complete so I can review any feedback before closing the job. | &check; |
| As a Manager | I can approve job deletion request so I can verify the actual necessity of the job. | &check; |
| As a Manager | I can reopen jobs so that I can move them from the completed to the active jobs list. | &check; |
| As a Manager | I can reassign a job so that I can assign it to a different employee. | &check; |

[Back to top](#table-of-content)

### Client site user
|   |   |   |
|--------|--------|--------|
| As a Client | I can view the home page with a menu so I can navigate to different pages. | &check; |
| As a Client | I can access the dashboard so I can view new, active and completed jobs information. | &check; |
| As a Client | I can add a new job so I can communicate the relevant maintenance needs. | &check; |
| As a Client | I can edit a job so I can update relevant information for that job. | &check; |
| As a Client | I can request that a job be deleted so I can remove it from the active list. | &check; |
| As a Client | I can send a message so I can communicate with the company.| &check; |
| As a Client | I can add / edit categories so that I can organize equipments in them. | &check; |
| As a Client | I can add an equipment so that I can create a job for it. | &check; |
| As a Client | I can edit / delete and equipment so that I can organize the equipment list. | &check; |
| As a User | I can filter the jobs so that I can search for the relevant ones. | &check; |

[Back to top](#table-of-content)

### Employee site user
|   |   |   |
|--------|--------|--------|
| As an Employee | I can access the employee dashboard so I can view jobs that have been assigned to me. | &check; |
| As an Employee | I can add feedback to jobs so I can communicate any extra needs. | &check; |
| As an Employee | I can mark jobs as done so I they can be moved to the completed list. | &check; |

[Back to top](#table-of-content)

## Site Structure
TheMaintenanceCo is divided in four parts: **home page, manager dashboard, client dashboard and employee dashboard**. When a user logs in it check the user type and redirect the user to the correct dashbaord. All views have relevant permissions so user cannot access a page that is not allowed by their user type, if they try to access something outside of the user permission it will redirect them to a 404 page not found.
The home page has a basic structure with a landing, about, contact and login page or logout if the user is already loggedin.
In the manager dashboard the user can view, edit and delete all jobs, add, edit and delete users. For this project the manager has to approve the user signup in order for it to become active and grant the user access to the dashboard. This is because of the way the company's bussiness model works. The logic is that after a user signs all relevant contracts and paperworks he them receives access to the dashboard.
In the client dashboard the user can view, edit and delete only jobs from his username. The user can also add, edit and delete categories and equipments. There is also a message page where the client can send an email and some fields are prepopuplated with user data.
In the employee dashboard the user can view all jobs that have been assigned to him, add feedback and mark jobs as done.

You can see all features in detail in the [Features](<#features>) section.

[Back to top](#table-of-content)

## Design Choices

- ### Color Scheme
TheMaintenanceCo is built on minimalist design choice, so the color palette select for this project reflects this intention. All caolors are mainly monochromatic shades of black and grey and only the buttons and some link have either a True Blue or Dodger Blue.

![Color](readme/assets/images/colors.png)

- ### Typography
The fonts used for the site are the standard Bootstrap 5 native fonts stack. This system selects the best user firendly font depending on the os the user is using:

- Safari for macOS and iOS: -apple-system;
- Windows: Segoe UI;
- Android: Roboto;
- Linux: Noto Sans, Liberation Sans;
- Fallback fonts: Helvetica Neue, Arial and Sans serif.

To find out more about these Bootstrap option please read the documentation [here](https://getbootstrap.com/docs/5.0/content/reboot/#native-font-stack).

[Back to top](#table-of-content)

# **Features**
All the project features are detailed and listed bellow:

## Home page

### Home
This is the main ladning page with a top navigation menu with link to all pages, a hero image with a call to action button that takes the user to the contact page and a footer.

<details><summary><b>Home page</b></summary>

![Home page](readme/assets/images/home_page.png)
</details><br/>

### Navigation
The main navigation menu has a black background with a brand text on the left and navigation link to the right, which are all offwhite. The visible links change depending if a user is looged in or not:

- If the user is logged out he can view: *home*, *about*, *contact* and *login*.
- If the user is logged in he can view: *home*, *about*, *contact*, *dashboard* and *logout*.
- In the dashboard all user view: *logout* and the *user name* that is currently logged in.

<details><summary><b>Top menu logged out</b></summary>

![Top menu](readme/assets/images/top_menu.png)
</details><br/>

<details><summary><b>Top menu logged in</b></summary>

![Top menu logged](readme/assets/images/top_menu_logged.png)
</details><br/>

<details><summary><b>Top menu in the dashboard</b></summary>

![Top menu dash](readme/assets/images/top_menu_dash.png)
</details><br/>

[Back to top](#table-of-content)

### About
The About page is very simple, it only contains some introduction information about the company's service and a link so the user can go to the contact page and send a message for more information.

<details><summary><b>About page</b></summary>

![About](readme/assets/images/about_page.png)
</details><br/>

[Back to top](#table-of-content)

### Contact
The contact page has a form where the sire user can send a message to the company. The message is sent using [EmailJS](https://www.emailjs.com/) api to deliver to the company's email.

<details><summary><b>Contact page</b></summary>

![Contact](readme/assets/images/contact_page.png)
</details><br/>

[Back to top](#table-of-content)

### Account
The account page is only accessible for users that are logged in. In this page the user can edit his *name, username* and *email address* and also *change his password*.

<details><summary><b>Account page</b></summary>

![Account](readme/assets/images/account_page.png)
</details><br/>

<details><summary><b>Change password</b></summary>

![Change password](readme/assets/images/change_password.png)
</details><br/>

[Back to top](#table-of-content)

### Sign up
In the sign up page the user can register for an account. However every new user has to be approved by a manager, until a manager has reviewd the registraion the user cannot access the dashboard and instead, is presented with a message that the aplication is awaiting approval.

<details><summary><b>Sign up page</b></summary>

![Signup](readme/assets/images/signup_page.png)
</details><br/>

<details><summary><b>Awaiting approval message</b></summary>

![Awaiting approval](readme/assets/images/awaiting_approval.png)
</details><br/>

[Back to top](#table-of-content)

### Login
In the login page the user can enter the username and password, it then validades the user and check which user type it is to redirect the user to the correct dashboard.

<details><summary><b>Login page</b></summary>

![Login](readme/assets/images/login.png)
</details><br/>

[Back to top](#table-of-content)

## Manager Dashboard

### Manager menu
The manager dashbaord has it's own sub navigation menu underneath the top navigation. It has links to the internal pages of the dashboard: *jobs, add user* and *users*.

<details><summary><b>Manager dashboard menu</b></summary>

![Manager dashboard menu](readme/assets/images/dash_manager_menu.png)
</details><br/>

[Back to top](#table-of-content)

### New jobs
The new jobs page is the landing page for the dashboard, this is where the user can see all newly created jobs. They have a status of new until the job is assigned to an employee, then it is update with an active status and moves to the active jobs list. In the open accordion the manager can view all relevant information for the job and can *edit, delete* or *assign a job*.

<details><summary><b>New jobs</b></summary>

![New jobs](readme/assets/images/dash_new_jobs.png)
</details><br/>

<details><summary><b>New jobs accordion details</b></summary>

![New jobs accordion details](readme/assets/images/dash_new_jobs_info.png)
</details><br/>

[Back to top](#table-of-content)

### Active jobs
In the active jobs page the user can view all jobs that are active, meaning, they have an employee asigned to them. In this page the user can: *edit, delete, close* or *reassign a job*.

Another feature of this page is if the client has request that a job be deleted it then gives the manager an option to *approve deletion* or *cancel deleteion* at the top of the accordion. It also shows a message in the title saying that the job is *Awaiting deletion*.

<details><summary><b>Active jobs</b></summary>

![Active jobs](readme/assets/images/dash_active_jobs.png)
</details><br/>

[Back to top](#table-of-content)

### Completed jobs
The completed jobs page lists all jobs that are marked as done. The manager can view the information for each job and also still *delete, edit* or *reopen a job* so it can move bacj to the active jobs.

<details><summary><b>Completed jobs</b></summary>

![Completed jobs](readme/assets/images/dash_completed_jobs.png)
</details><br/>

[Back to top](#table-of-content)

### Filter
All the jobs page has a folter button in the toop right corner that open a filter field. In it the user can filter for specific jobs by their *id, title, descriptopn* and *user*. The filter is also availabre in the show users page.

<details><summary><b>Filter</b></summary>

![Filter](readme/assets/images/dash_filter.png)
</details><br/>

[Back to top](#table-of-content)

### Users
The users page displays a list of all users registered in the website. At the top there's a list of the users awaiting for approval and bellow that list an accordion with all active users. This page gives the user the ability to *edit, delete* and *approve users*.

<details><summary><b>Users</b></summary>

![Users](readme/assets/images/dash_users.png)
</details><br/>

<details><summary><b>User info</b></summary>

![Users info](readme/assets/images/dash_users_open.png)
</details><br/>

<details><summary><b>Edit user</b></summary>

![Edit user](readme/assets/images/dash_edit_user.png)
</details><br/>

[Back to top](#table-of-content)

## Client Dashboard

### Client menu
The client dashbaord has it's own sub navigation menu underneath the top navigation. It has links to the internal pages of the dashboard: *jobs, settings* and *send message*.

<details><summary><b>Client dashboard menu</b></summary>

![Client dashboard menu](readme/assets/images/dash_client_menu.png)
</details><br/>

[Back to top](#table-of-content)

### Jobs
In the clients jobs page he has access to all *new, active* and *completed jobs* related to the loggedin user. The information and logic is exactly the same as with the manager dashboard. The only difference is that when a job has a status of active the client cannot directly delete a job, because it has already been assigned to en employee, therefor he has to request a job deletion that appear in the managers dashboard for approval. If the manager approves the deletion then the job is deleted for all users. If a job has already been request for deletion, the client user can still cancel the job deletion request.

<details><summary><b>Client dashboard menu</b></summary>

![Jobs](readme/assets/images/dash_client.png)
</details><br/>

[Back to top](#table-of-content)

### Categories
The categories page inside the settings link shows all created categories for the user. There is also a field where the suer can type a new category name and add it to the database. The user can also *edit* or *delete* each individual category. Every deletion option in the project brings up a modal confirmation as a safeguard to avoi unintentional deletion of data. When a category is deleted it dletes all equipments and jobs related to that category.

<details><summary><b>Categories</b></summary>

![Categories](readme/assets/images/dash_categories.png)
</details><br/>

<details><summary><b>Deletion modal</b></summary>

![Deletion modal](readme/assets/images/dash_delete.png)
</details><br/>

[Back to top](#table-of-content)

### Equipments
Af with the categories the equipmenrs are also inside the settings link and follow the same logic as the categories. The equipmenrs, however, have a Many to One relationship with the categories, meaning there are many equipments to one category. When an equipments is deleted it also deletes all related jobs for that equipment.

<details><summary><b>Equipments</b></summary>

![Equipments](readme/assets/images/dash_equipments.png)
</details><br/>

[Back to top](#table-of-content)

### Add job
The add job page is where the user can create a new job. He first has to select a category for the job, that them fetches all related equipments that beleng to the select category. The user then enters the description for the job. Once the job is created it goes tot he new jobs list and awaits for a manager to assign an employee to it. After the job creating the category and equipmenrs cannot be changes, so the user must create a new job if it is related to a different equipment or cetegory.

<details><summary><b>Add job page</b></summary>

![Add job](readme/assets/images/dash_add_job.png)
</details><br/>

[Back to top](#table-of-content)

### Send message
This page is exactly the same as the contact page in the home page, it uses the same form. The only difference is that it populates the form with the user email it there is one registered.

<details><summary><b>Send message</b></summary>

![Send message](readme/assets/images/dash_contact.png)
</details><br/>

[Back to top](#table-of-content)

## Employee Dashboard

### Jobs
The employee dashboard shows only the jobs that have been assigned to user by a manager. He then access all the information regarding that job and also add feedback. Once a job is complete the user can mark a job as done, which then moves it to the completed list for all users. The employee still has access to the accounts, where the user can *edit* and *change the password* if needed.

<details><summary><b>Employee dashboard</b></summary>

![Employee dashboard](readme/assets/images/dash_employee.png)
</details><br/>

<details><summary><b>Feedback</b></summary>

![Feedback](readme/assets/images/dash_feedback.png)
</details><br/>

[Back to top](#table-of-content)

# **Future Features**

- Add an urgency status option to jobs;
- Add an internal messaging page;
- Add a password reset page with email confirmation;
- Add more automated testing;

[Back to top](#table-of-content)

 # **Technologies used**

 ## Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the site.

[Back to top](#table-of-content)

## Frameworks & Software
- [Bootstrap](https://getbootstrap.com/) - A CSS framework that helps building solid, responsive, mobile-first sites
- [Django](https://www.djangoproject.com/) - A model-view-template framework used to create the Review | Alliance site
- [Balsamiq](https://balsamiq.com/) - Used to create the wireframe.
- [Numbers](https://www.apple.com/uk/numbers/) - Used to create ERD models.
- [Github](https://github.com/) - Used to host and edit the website.
- [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal in [Gitpod](https://www.gitpod.io) used to push changes to the GitHub repository.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used to test performance of site.
- [Responsive Design Checker](https://www.responsivedesignchecker.com/) - Used for responsiveness check.
- [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/) - Used to validate the sites accessibility.
- [a11y Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/) - Used to test color contrast on the site
- [Real Favicon Generator](https://realfavicongenerator.net/) - Used to create the favicon.
- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to debug and test responsiveness.
- [Cloudinary](https://cloudinary.com/) - A service that hosts all static files in the project.
- [HTML Validation](https://validator.w3.org/) - Used to validate HTML code
- [CSS Validation](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
- [PEP8 Validation](http://pep8online.com/) - At the time for deploying this project the PEP8 Online Validaton service was offline, therefore not used.
- [JSHint Validation](https://jshint.com/) - Used to validate JavaScript code

[Back to top](#table-of-content)

## Libraries

In the list below are all the libraries used in the project, these are located in *requirements.txt*:

- [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI;
- [cloudinary](https://pypi.org/project/cloudinary/) - The Cloudinary Python SDK allows you to quickly and easily integrate your application with Cloudinary. Effortlessly optimize, transform, upload and manage your cloud's assets;
- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) - Bootstrap 5 template pack for django crispy forms;
- [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) - Django Cloudinary Storage is a Django package that facilitates integration with Cloudinary by implementing Django Storage API.
- [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) - Used to integrate Django DRY forms in the project.
- [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn ???Green Unicorn??? is a Python WSGI HTTP Server for UNIX. It???s a pre-fork worker model ported from Ruby???s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.
- [oauthlib](https://pypi.org/project/oauthlib/) - OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
- [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
- [PyJWT](https://pypi.org/project/PyJWT/) - A Python implementation of RFC 7519.
- [python3-openid](https://pypi.org/project/python3-openid/) - OpenID support for modern servers and consumers.
- [pytz](https://pypi.org/project/pytz/) - This is a set of Python packages to support use of the OpenID decentralized identity system in your application, update to Python 3
- [requests-oauhlib](https://pypi.org/project/requests-oauthlib/) - Provides first-class OAuth library support for Requests.
- [sqlparse](https://pypi.org/project/sqlparse/) - sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.

[Back to top](#table-of-content)

# **Testing**

Please refer to the [Testing](TESTING.md) file for more information about the testing of theMaintenanceCo.

[Back to top](#table-of-content)

# **Deployment**

## Deployment To Heroku

The project was deployed to [Heroku](https://www.heroku.com). To deploy, please follow the process below:

1. To begin with we need to create a GitHub repository from the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) by following the link and then click 'Use this template'.

2. Fill in the needed details as stated in the screenshot below and then click 'Create Repository From Template'.

3. When the repository creation is done click 'Gitpod' to open the repository in the gitpod IDE.

4. Now it's time to install Django and the supporting libraries that are needed. Type the commands below to do this.

- ```pip3 install 'django<4' gunicorn```
- ```pip3 install 'dj_database_url psycopg2```
- ```pip3 install 'dj3-cloudinary-storage```

5. When Django and the libraries are installed we need to create a requirements file.

- ```pip3 freeze --local > requirements.txt``` - This will create and add required libraries to requirements.txt

6. Now it's time to create the project.

- ```django-admin startproject YOUR_PROJECT_NAME .``` - This will create your project

7. When the project is created we can now create the application.

- ```python3 manage.py startapp APP_NAME``` - This will create your application

8. Add the application to settings.py

9. Now it is time to do our first migration and run the server to test that everything works as expected. This is done by writing the commands below.

- ```python3 manage.py migrate``` - This will migrate the changes
- ```python3 manage.py runserver``` - This runs the server. To test it, click the open browser button that will be visible after the command is run.

10. Now it is time to create our application on Heroku, attach a database, prepare our environment and settings.py file and setup the Cloudinary storage for our static and media files.

- Head on to [Heroku](https://www.heroku.com/) and sign in (or create an account if needed).

- In the top right corner there is a button that is labeled 'New'. Click that and then select 'Create new app'.

11. Now it's time to enter an application name that needs to be unique. When you have chosen the name, choose your region and click 'Create app".

12. To add a database to the app you need to go to the resources tab ->> add-ons, search for 'Heroku Postgres' and add it.

13. Go to the settings tab and click on the reveal Config Vars button. Copy the text from DATABASE_URL (because we are going to need it in the next step).

14. Go back to GitPod and create a new env.py in the top level directory. Then add these rows.

- ```import os``` - This imports the os library
- ```os.environ["DATABASE_URL_FROM HEROKU"]``` - This sets the environment variables.
- ```os.environ["SECRET_KEY"]``` - Here you can choose whatever secret key you want.

15. Now we are going to head back to Heroku to add our secret key to config vars. See screenshot below.

16. Now we have some preparations to do connected to our environment and settings.py file. In the settings.py, add the following code:

```import os```

```import dj_database_url```

```if os.path.isfile("env.py"):```

```import env```

17. In the settings file, remove the insecure secret key and replace it with:

```SECRET_KEY = os.environ.get('SECRET_KEY')```

18. Now we need to comment out the old database setting in the settings.py file (this is because we are going to use the postgres database instead of the sqlite3 database).

Now, add the link to the DATABASE_URL that we added to the environment file earlier.

19. Save all your fields and migrate the changes.

```python3 manage.py migrate```

20. Now we are going to get our connection to Cloudinary connection working (this is were we will store our static files). First you need to create a Cloudinary account and from the Cloudinary dashboard copy the API Environment Variable.

21. Go back to the env.py file in Gitpod and add the Cloudinary url (it's very important that the url is correct):

```os.environ["CLOUDINARY_URL"] = "cloudinary://************************"```

22. Go back to Heroku and add the Cloudinary url in Config Vars. We also need to add a disable collectstatic variable to get our first deployment to Heroku to work.

23. In the settings.py file on Gitpod. We now need to add our Cloudinary Libraries we installed earlier to the installed apps. Here it is important to get the order correct.

24. For Django to be able to understand how to use and where to store static files we need to add some extra rows to the settings.py file.

25. Now it's time to link the file to the Heroku templates directory.

26. Let's change the templates directory to TEMPLATES_DIR in the teamplates array.

27. To be able to get the application to work through Heroku we also need to add our Heroku app and localhost to which hosts that are allowed.

28. Now we just need to add some files to Gitpod.

- Create 3 folders in the top level directory: **media**, **static**, **templates**
- Create a file called **Procfile* and add the following line of code to it: ```web: gunicorn PROJ_NAME.wsgi?```

29. Now you can save all the files and prepare for the first commit and push to Github by writing the lines below.

- ```git add .```
- ```git commit -m "Deployment Commit```
- ```git push```

30. Before moving on to the Heroku deployment we just need to add one more thing in the config vars. We need to add "PORT" in the KEY input field and "8000" in the VALUE field. If we don't add this there might be problems with the deployment.

31. Now it's time for deployment. Scroll to the top of the settings page in Heroku and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

32. Scroll down to the manual deployment section and click 'Deploy Branch'. Hopefully the deployment is successful!

The link to the live theMaintenanceCo website on Heroku can be found [here](https://the-maintenance-co.herokuapp.com/). And the Github repository can be found [here](https://github.com/andrebraga7/the-maintenance-co).

[Back to top](#table-of-content)

## How To Fork The Repository On GitHub

It is possible to do a independent copy of a GitHub Repository by forking the GitHub account. The copy can then be viewed and it is also possible to do changes in the copy without affecting the original repository. To fork the repository, take these steps:

1. After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.

[Back to top](#table-of-content)

## Cloning The Project

To clone and set up this project you need to follow the steps below.

1. When you are in the repository, find the code tab and click it.
2. To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
3. Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
4. Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.
5. To be able to get the project to work you need to install the requirements. This can be done by using the command below:

* ```pip3 install -r requirements.txt``` - This command downloads and install all required dependencies that is stated in the requirements file.

6. The next step is to set up the environment file so that the project knows what variables that needs to be used for it to work. Environment variables are usually hidden due to sensitive information. It's very important that you don't push the env.py file to Github (this can be secured by adding env.py to the .gitignore-file). The variables that are declared in the env.py file needs to be added to the Heroku config vars. Don't forget to do necessary migrations before trying to run the server.

* ```python3 manage.py migrate``` - This will do the necessary migrations.
* ```python3 manage.py runserver``` - If everything i setup correctly the project is now live locally.

[Back to top](#table-of-content)

# **Credits**

## Content

- All text content was written by Andre Braga;

- The hero image in the landing page was generated by [Midjourney's](https://midjourney.com/home/?callbackUrl=%2Fapp%2F) AI;

- Template for read.me provided by Code Institute (*with some additional changes that my mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/))* suggested;

## Technical

- I used the django documentation to help me understand the framework and python concepts [Django Documentation](https://docs.djangoproject.com/en/4.1/);

- The Django Allauth documentation was really helpfull to help with the User models and login, signup pages. [Django Allauth documentation](https://django-allauth.readthedocs.io/en/latest/);

- [Stackoverflow](https://stackoverflow.com/), as always, was really helpfull with small helps and concepts explanation.

[Back to top](#table-of-content)

# Acknowledgements
TheMaintenanceCo was creates as the fourth portfolio project for the Full Stack Software Developer course from [**Code Institute**](https://codeinstitute.net). I would like to thank my mentor, [**Precious Ijege**](https://www.linkedin.com/in/precious-ijege-908a00168/) for his guidance and support throught this project and the Code Institute team.

[**Andre Braga**](https://www.linkedin.com/in/andrestrevisan/) 2023

[Back to top](#table-of-content)