# Django Blogs Application

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2-brightgreen.svg)](https://djangoproject.com)

This blogs project allows the user to publish their blogs in the application.
In this Django App, user initially need to register in and login to post their blogs. There are different features added in this application. Users can update their profile, can search through the blogs based on title of the post, Shows latest posts in the sidebar. The comments features allows a reader to post their comment for a post, can also remove, approve and edit it.

![Django Blogs Application](https://github.com/jissmonjose/project-blog-app/blob/master/screenshot/Screenshot1.png)



## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/jissmonjose/project-blog-app.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.