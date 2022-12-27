# Schedulr
&lt;br> Schedulr.

Schedulr is a project that creates periods of time to study based on your courses for the semester. Based off of Utm Computer Science Courses and created with 3 other students at the University of Toronto.

## Setup:
  ### 1. Make sure Node.js and npm are installed on your computer
   If you don't have Node.js and npm installed, you can download and install them from the official Node.js [website](https://nodejs.org/en/)
  ### 2. Use npm to install react if it is not already installed
   ```bash
   npm install react react-dom
   ```
   Depending on your installation, you might have to run the following command
   ```bash
   cd frontend
   npm i react
   ```
   
  ### 3. Setup the virtual environment. 
  To set up and activate a Python virtual environment on Windows and Mac OS, you can follow these steps:
  Open a new terminal at the directory schedulr/backend
  
  ### Windows
  Use the following command to create a virtual environment with the name "myenv":
  
  ```python
  python -m venv myenv
  ```
  To activate the virtual environment run this command
  ```python
  myenv\Scripts\activate
  ```
  Your command prompt should now have "(myenv)" at the beginning, indicating that the virtual environment is active.
  
  ### Mac OS
  Use the following command to create a virtual environment with the name "myenv":
  
  ```python
  python3 -m venv myenv
  ```

  To activate the virtual environment, use the following command:
  ```python
  source myenv/bin/activate
  ```
  Your command prompt should now have "(myenv)" at the beginning, indicating that the virtual environment is active.

  ### Installing Libraries
  Inorder to get all the required libraries, run
  ```bash
  pip install -r requirements.txt
  ```
  
  Now, both the front end and backend should be set up and ready to go

## Deployment

In order to have the project running, there are two sets of commands which you need to run, given the installation was done properly

On the first terminal, make sure it is on schedulr/frontend and then run 
```bash
npm start
```

On the second terminal, make sure the virtual environment is activated and terminal is on schedulr/backend, if not, look at installation again , then run
```python	
python manage.py runserver
```

  
##  User Manual
In order to use the app
  1. Open http://localhost:3000/ on your web-browser
  2. At first you will be redirected to the login page, if it is your first time using the app, click on register on the navigation bar
  3. After registering you should be navigated to the login page, where you can type in your credentials to login 
  4. Click on user-form on the header
  5. Here fill out which courses you have and your preferences, and after submitting you will be navigated back to the home page
  6. DISCLAIMER: if it is your first time using the app, you need to wait a few minutes for the calendar events to show up
  7. Now you can navigate throughout the calendar and see which study blocks have been assigned to your custom need
  8. If you wish to logout, click on the logout button on the left navigation bar

