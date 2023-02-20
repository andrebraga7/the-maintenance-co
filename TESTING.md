- [**Testing**](<#testing>)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
    - [Additional Testing]()
    - [Known Bugs]()




## Testing User Stories

- As a Manager I can access the managers dashboard so I can view new, active, and completed jobs.
    - When the user signs in to the website it redirects to the dashboard where the user is presented with new, active and completed jobs.

- As a Manager I can create, update and delete users so I can manage access and permissions.
    - In the manager dashbaord thje user has access to the sign up page and user editing page, to create, edit or delete users.

- As a Manager I can assign jobs to employees so I can plan what each employee will work on.
    - In the new jobs accordion the user can click on assign job and select an employee to assign to.

- As a Manager I can mark jobs as complete so I can review any feedback before closing the job.
    - In the active jobs accordion the user can mark a job as done.

- As a Manager I can approve job deletion request so I can verify the actual necessity of the job.
    - When a client user request a job deletion an option becomes available in the active jobs accordion so the user can approva the job deletion.

- As a Manager I can reopen jobs so that I can move them from the completed to the active jobs list.
    - In the completed jobs list the user can select to reopen a job as required.

- As a Manager I can reassign a job so that I can assign it to a different employee.
    - In the active jobs accordion the manager can reassign a job to a different employee.

- As a Client I can view the home page with a menu so I can navigate to different pages.
    - On the top of the home page there is a menu with links to all the different pages.

- As a Client I can access the dashboard so I can view new, active and completed jobs information.
    - When the user signs in to the website it redirects to the dashboard where the user is presented with new, active and completed jobs.

- As a Client I can add a new job so I can communicate the relevant maintenance needs.
    - In the client dashboard the user can click on add new job where the he can add the job details and save.

- As a Client I can edit a job so I can update relevant information for that job.
    - In the new and active jobs list, the user can click on edit job to edit any relevant information.

- As a Client - I can request that a job be deleted so I can remove it from the active list.
    - When a job is in the active jobs list the user can click on request job deletion so a manager can approve the deletion.

- As a Client  I can send a message so I can communicate with the company.
    - In the dashboard the client can click on send message and a contact forms loads with the user email prepopulated.

- As a Client - I can add / edit categories so that I can organize equipments in them.
    - In the settings page the user can add, edit or delete categories as required.

- As a Client - I can add an equipment so that I can create a job for it.
    - In the settings page the user can add equipments as required.

- As a Client - I can edit / delete and equipment so that I can organize the equipment list.
    - In the settings page the user can edit or delete equipments as required.

- As a User - I can filter the jobs so that I can search for the relevant ones.
    - In the jobs list pages the user has a filter button that opens an input field that will filter throught the jobs id, title and description.

- As an Employee I can access the employee dashboard so I can view jobs that have been assigned to me.
    - When the user signs in to the website it redirects to the dashboard where the user is presented with active and completed jobs.

- As an Employee I can add feedback to jobs so I can communicate any extra needs.
    - In the active jobs accordion the user can click on add feedback to add any relevant information.

- As an Employee I can mark jobs as done so I they can be moved to the completed list.
    - In the active jobs accordion the user can click on mark job as done to move it to the completed list.

## Code Validation
The website's code has been tested using the W3C Markup Validator and JSHint. Some error were found regarding button elements being descendents of anchors and some form placeholder attributes now being allowed for select elements, this however is generated throught crispy forms automatic forms. The button elements was a quick fix, I just removed the button and styled the links as I wanted.
Some other error are apearing in the W3C validator regarding script element havind unecessary type=text/javascript attribute, however, this is now normal practices.
Another issue was some id and aria-label repetition errors, this is to do with the use of boostrap accordions and Jinja2 for loops.
Some other aria-labelledby error where caught and fixed.












### Markup Validation
After fixing the inital errors that W3C Markup Validation Service reported, no errors were returned.

<details><summary><b>HTML Validation Result</b></summary>

![HTML Result Home Page](readme/assets/images/html_validation_no_error.png)
</details><br/>

[Back to top](<#table-of-content>)

### CSS Validaton
When validating my own code the W3C CSS Validator reports no errors.

<details><summary><b>CSS Validation Result</b></summary>

![CSS Result](readme/assets/images/css_validation_no_error.png)
</details><br/>

[Back to top](<#table-of-content>)

### PEP Validation
At the time of this project the website [pep8online](http://pep8online.com/) is currently offline. Usually I'm using that site to validate my Python code. Due to the site being offline I have followed Code Institutes workaround to add the PEP8 validator 'pycodestyle' to the Gitpod Workspace. I have tested the following Python files:

* admin.py - No errors or warnings reported
* forms.py - No errors or warnings reported
* models.py - No errors or warnings reported
* test_forms.py - No errors or warnings reported
* urls.py - No errors or warnings reported
* views.py - No errors or warnings reported

[Back to top](<#table-of-content>)

### JavaScript Validation
The JSHint validator results can be seen below:

No errors were returned when passing through JSHint (script.js) but the test reported one undefined variable connected to Bootstrap which is no problem.

<details><summary><b>JSHint Validation Result</b></summary>

![JSHint Validation](readme/assets/images/js_hint_validation.png)
</details><br/>

[Back to top](<#table-of-content>)

## Additional Testing

### Manual Testing

In addition to tests stated above I have performed a series of manual tests. Below the list of tests that has been conducted can be found.

| Status | **Main Website - User Logged Out**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication loads a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all reviews
| &check; | Clicking the All button on the nav bar lists all reviews
| &check; | Clicking the Albums button on the nav bar lists all album reviews
| &check; | Clicking the Concert button on the nav bar lists all concert reviews
| &check; | Clicking the Log In / Sign Up loads the sign up page
| &check; | 6 Reviews are rendered for the user on all / albums / concert page before pagination kicks in
| &check; | Clicking the Read More button on the a review card loads the review detail page
| &check; | In the details view the user cannot create a comment
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the YouTube link in the footer area opens YouTube in a new window
| &check; | Clicking the LinkedInlink in the footer area opens LinkedIN in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window

| Status | **Main Website - User Logged In**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication loads a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all reviews
| &check; | Clicking the All button on the nav bar lists all reviews
| &check; | Clicking the Albums button on the nav bar lists all album reviews
| &check; | Clicking the Concert button on the nav bar lists all concert reviews
| &check; | 6 Reviews are rendered for the user on all / albums / concert page before pagination kicks in
| &check; | Clicking the Read More button on the a review card loads the review detail page
| &check; | In the detail view the logged in user can comment a review
| &check; | When user submits a comment a message with approval information is being showed on the page
| &check; | In the detail view the logged in user can update/delete the comments written by themselves
| &check; | Clicking the update button loads the update comment page
| &check; | Clicking the delete button loads the delete comment page
| &check; | In the detail view the logged in user can like/unlike reviews
| &check; | In the detail view the logged in user can update/delete the reviews written by themselves
| &check; | Clicking the update button in the detail view loads the update review page
| &check; | Clicking the delete button in the detail view loads the delete review page
| &check; | Clicking the My Reviews button in the logged in user menu lists the logged in users reviews
| &check; | Clicking the update button in the My Reviews view loads the update review page
| &check; | Clicking the delete button in the My Reviews view loads the delete review page
| &check; | In the My Reviews view the information about the review status is correct
| &check; | In the logged in user menu the Admin Area is not visible
| &check; | Clicking the Show Profile Page button in the logged in user menu loads the My Profile page
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the YouTube link in the footer area opens YouTube in a new window
| &check; | Clicking the LinkedInlink in the footer area opens LinkedIN in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window

| Status | **Main Website - Admin Logged In**
|:-------:|:--------|
| &check; | Clicking the Admin Area button in the logged in user menu loads the Admin Area Page
| &check; | In the review section. Clicking the approve / unapprove / publish / unpublish toggles the approve and status signs
| &check; | The view button is only visible if a review is published
| &check; | In the comment section. Clicking the approve / unapprove toggles the approve and status signs
| &cross; | When clicking delete / add genre the appropiate page loads and shows success page after submit
| &check; | Total Users shows correct number of total users
| &check; | Total Reviews shows the correct number of total reviews
| &check; | Total Comments shows the correct number of total comments
| &check; | Reviews that need approval shows the correct numer of reviews that need approval
| &check; | Comments that need approval shows the correct numer of comments that need approval

 Status | **Create A Review - User Logged In**
|:-------:|:--------|
| &check; | Title field is required
| &check; | Title field does not accept empty field
| &check; | Title field does not accept just spaces
| &check; | Artist field is required
| &check; | Artist field does not accept empty field
| &check; | Artist field does not accept just spaces
| &check; | Featured Image is not required
| &check; | Fragment field is required
| &check; | Fragment field does not accept empty field
| &check; | Body field is required
| &check; | Body field does not accept empty field
| &check; | Category field defaults to Uncategorized
| &check; | Fragment field is required
| &check; | Fragment field does not accept empty field
| &check; | Record Label is not required
| &check; | Venue is not required
| &check; | Genre field defaults to Uncategorized
| &check; | Rating field defaults to 3
| &check; | Status field defaults to Draft
| &check; | Posting as shows name of logged in user
| &check; | Review Success Page is displayed when the user submits the review and the form validation is ok.

Status | **Create A New User - User Logged Out**
|:-------:|:--------|
| &check; | Username field is required
| &check; | Username field does not accept empty field
| &check; | Email field does not accept just spaces
| &check; | Email field is optional
| &check; | Password field does not accept empty field
| &check; | Success flash message is displayed when the user submits the create a new user form
| &check; | Default biography is visible in about page (with i.e default featured image)

Status | **Create A Profile Page - User Logged In**
|:-------:|:--------|
| &check; | Default featured image is visible the first time a user opens the 'my profile' page
| &check; | First Name field is required
| &check; | First Name field does not accept empty field
| &check; | First Name field does not accept just spaces
| &check; | Last Name field is required
| &check; | Last Name field does not accept empty field
| &check; | Last Name field does not accept just spaces
| &check; | Update profile success Page is displayed when the user submits the profile form

### Automated Testing
Some automated testing has been done during this project. Due to prioritization of other tasks I only could provide 34% coverage. See screenshot below. Automated tests can be run by typing the command - *python3 manage.py test*

<details><summary><b>Automated Testing</b></summary>

![Automated Testing](readme/assets/images/test_coverage_report.png)
</details><br/>

### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

| Desktop    | Display <1280px       | Display >1280px    |
|------------|-----------------------|--------------------|
| Render     | pass                  | pass               |
| Images     | pass                  | pass               |
| Links      | pass                  | pass               |

| Tablet     | Samsung Galaxy Tab 10 | Amazon Kindle Fire | iPad Mini | iPad Pro |
|------------|-----------------------|--------------------|-----------|----------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

| Phone      | Galaxy S5/S6/S7       | iPhone 6/7/8       | iPhone 12pro         |
|------------|-----------------------|--------------------|----------------------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

[Back to top](<#table-of-content>)

### Browser Compatibility
* Google Chrome Version (106.0.5249.119)
* Mozilla Firefox (version 105.0.3)
* Min (version 1.26.0)
* Apple Safari (version 16.0)
* Microsoft Edge (version 106.0.1370.47)

[Back to top](<#table-of-content>)

### Lighthouse
Google Lighthouse in Chrome Developer Tools was used to test the application within the areas of *Performance*, *Accessibility*, *Best Practices* and *SEO*. I tested the *index page*, *review details page*, *the admin area* and *the about page*. The testing showed the following:

* Index Page - Performance: 75, Accessibility: 100, Best Practises: 100, SEO: 92
* Review Details Page - Performance: 81, Accessibility: 98, Best Practises: 100, SEO: 92
* Admin Area - Performance: 85, Accessibility: 97, Best Practises: 100, SEO: 100
* About page - Performance: 73, Accessibility: 98, Best Practises: 100, SEO: 100

In general this is OK results. The performance is affected in a negative way by external scripts (connected to i.e. Bootstrap) and the lower result on SEO on the Index page and Admin Area Page is i.e. connected to the 'read more' links that is not a 100% optimal description from a SEO point of view. The lower accessibility result on the review details page is connected to the heading elements not being in sequentially-descending order, but this is an active design choice and not a big issue (but I thought it would be proper to highlight it here so that it's clear I'm aware of it).

<details><summary><b>Lighthouse Index Result</b></summary>

![Lighthouse Index Result](readme/assets/images/lighthouse_index.png)
</details><br/>

<details><summary><b>Lighthouse Review Details Page Result</b></summary>

![Lighthouse Review Details Page](readme/assets/images/lighthouse_review_details_page.png)
</details><br/>

<details><summary><b>Lighthouse Admin Area Result</b></summary>


![Lighthouse Admin Area Result](readme/assets/images/lighthouse_admin_area.png)
</details><br/>

<details><summary><b>Lighthouse About Page Result</b></summary>

![Lighthouse About Page Result](readme/assets/images/lighthouse_about.png)
</details><br/>


### WAVE
[WAVE](https://wave.webaim.org/) was used to check accessibility. 0 errors were found.

<details><summary><b>WAVE Result</b></summary>

![WAVE Result](readme/assets/images/wave_result.png)
</details><br/>

### a11y Color Contrast Accessibility Validator
[a11y](https://color.a11y.com/Contrast/) was used to check the color contrast accessibility. 0 errors were found.

<details><summary><b>a11y Result</b></summary>

![a11y Result](readme/assets/images/a11y_contrast_test.png)
</details><br/>

[Back to top](<#table-of-content>)

### Peer Review
Additional testing of the application was conducted by people outside of the software development field. Some smaller spelling and grammar errors were found and corrected. No issues connected to design or handling of the site.

## Known bugs
No known bugs besides those in the fixed / unfixed bugs section.

### Fixed Bugs
**2022-10-10**
* Bug: When updating a review or comment the approved variable did not get updated to 'False'. This is is now handled and fixed.

**2022-10-11**
* Bug: When updating a review the slug did not change. I chose to fix this bug so that the slug updates when a review is updated but one 'school' within this area says that a slug never should be changed (due to problems with urls / linking in the future). This functionality is an easy fix to remove if necessary but I chose to keep it for now.

**2022-10-14**
* Bug: When the Markup Validation was done there was initially quite a lot of errors. The debugging process was very straight forward and the errors could easily be fixed.

<details><summary><b>HTML Validation</b></summary>

![HTML Validation](readme/assets/images/html_validation_error.png)
</details><br />

**2022-10-17**
* Bug: The CSS Validation reported an error that is connected to Font Awesome. When I validate my own CSS code there are no errors at all. So this might be a Font Awesome bug that is out of my control. But I thought it would be proper to highlight the error here in the bugs section.

<details><summary><b>CSS Validation</b></summary>

![CSS Validation](readme/assets/images/css_validaton_error.png)
</details><br />

### Unfixed Bugs

**2022-10-14**
* Bug: Summernote is not working 100% properly. I have debugged and sweeped the Internet for solutions. The issue is that when a user creates a review it's not possible to overide the choices the user makes when writing the review (i.e. font-size and font). I tried to handle this by setting rules of what tools to show in the Summernote editor without success. One workaround could of course be to remove the Summernote functionality but I did not want to do that in this project at least. This bug is still unfixed and I haven't found a solution to it yet.

**2022-10-15**
* Bug: 2 warning / issues reported in the Google Chrome DevTools console. The first one is connected to a navigator.userAgent issue and the second to usage of a deprecated feature. I have done some digging and it seems that these issues have been reported within different forums on the web. I have checked other browsers (i.e. Firefox, Min and Edge) and the issue does not show up there.

<details><summary><b>Warnings from Google Chrome DevTools</b></summary>

![HTML Validation](readme/assets/images/google_chrome_warning.png)
</details><br />





Back to [**README file.**](README.md)