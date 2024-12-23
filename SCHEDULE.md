# 30-Day Schedule for Method Library Website Application

This document outlines a 30-day schedule for setting up a method library website application tailored for coaches and scrum masters.

## Week 1: Project Planning and Setup

### Day 1: Project Planning
- Define project scope and requirements.
- Identify user roles: visitors, users, and admin.
- Draft wireframes for the application layout.
- draw ERD for database

### Day 2: Environment Setup
- Create a Gitpod workspace.
- Set up a PostgreSQL database in your preferred environment (e.g., Heroku).
- Initialize a Django project and configure settings for PostgreSQL.

### Day 3: Version Control
- Set up Git for version control.
- Create a repository on GitHub or another platform
- Commit initial project setup files

### Day 4: Basic Django Configuration
- Set up Django apps (e.g., methods, users).
- Configure URLs and basic views.
- Test Django installation by running the server.
- Create a Procfile for Heroku.
- Ensure all dependencies are listed in `requirements.txt`.
- Create a Heroku app and link to GitHub repository
- Set up PostgreSQL on Heroku.
- Initial Deployment

### Day 5: User Authentication
- Implement user registration and login using Django's built-in authentication system.
- Create templates for login and registration pages.

### Day 6: User Profile Management
- Allow users to create and update profiles.
- Implement user authentication checks for accessing methods.

### Day 7: Review and Refactor
- Review code and structure.
- Refactor any redundant code or improve organization.

## Week 2: Method CRUD Functionality

### Day 8: Database Models
- Define models for Methods (title, description, created_by, etc.).
- Create migrations and apply them to PostgreSQL. --> python3 manage.py makemigrations, migrate

### Day 9: Method Creation
- Implement functionality for users to create methods.
- Create a form for method submission and a corresponding view.

### Day 10: Method Listing
- Develop a view to list all methods.
- Implement pagination and search functionality.

### Day 11: Method Detail View
- Create a detail view for each method.
- Include options for users to edit or delete their methods.

### Day 12: Method Update Functionality
- Implement editing functionality for methods.
- Ensure only the method creator can edit.

### Day 13: Method Deletion Functionality
- Implement deletion for methods.
- Create confirmation dialogs for deletions.

### Day 14: Admin Functionality
- Create an admin interface for managing all methods.
- Implement delete options for admins only.

## Week 3: Frontend Development

### Day 15: Bootstrap Integration
- Integrate Bootstrap for styling.
- Apply Bootstrap classes to improve UI.

### Day 16: Create Base Templates
- Create a base template to maintain consistent layout.
- Include navigation, footer, and header sections.

### Day 17: Method Form Styling
- Style method creation and update forms using CSS and Bootstrap.

### Day 18: Responsiveness
- Ensure the site is responsive and mobile-friendly.
- Test across various devices and screen sizes.

### Day 19: User Experience Enhancements
- Add notifications for successful actions (e.g., method created, updated).

### Day 20: Testing User Flows
- Test user flows from registration to method management.
- Gather feedback from potential users.

### Day 21: Bug Fixes, Improvements and content maintenacne 
- Address any bugs discovered during user flow testing.
- Implement suggested improvements.
- add users, methods and comments to the database

## Week 4: Final Touches and Deployment

### Day 22-25: Prepare for Deployment
- Finalize any configurations for deployment.
- Set environment variables for production settings.
- Deploy the application to Heroku.
- Test the deployed app thoroughly.

### Day 26-29: Final Testing, Documentation
- Perform end-to-end testing on the live application.
- Check user registrations, logins, method creation, and admin functions.
- Write documentation for users and developers.
- Include setup instructions, usage guidelines, and API references if applicable.

### Day 30: Post-Launch Review
- Review feedback and plan for future improvements.
- Set up a maintenance schedule for updates and bug fixes.
