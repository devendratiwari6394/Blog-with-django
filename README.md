# Django Blog Website

A simple **Blog Web Application built with Django** where users can read blog posts and view full blog details.
This project demonstrates the basic concepts of **Django such as Models, Views, Templates, and URL routing**.

## 🚀 Live Demo

https://blog-with-django-1.onrender.com/

---

## 📌 Features

* View all blog posts
* Read full blog details
* Admin panel to manage blog posts
* Publish / Unpublish blog functionality
* Blog posts stored in database
* Responsive UI

---

## 🛠️ Tech Stack

**Backend**

* Python
* Django

**Frontend**

* HTML
* CSS
* Bootstrap

**Database**

* SQLite

**Deployment**

* Render

**Version Control**

* Git & GitHub

---

## 📂 Project Structure

```
blog_project/
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│
├── templates/
├── static/
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/blog-django.git
cd blog-django
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate virtual environment

**Windows**

```
venv\Scripts\activate
```

**Mac / Linux**

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```
python manage.py migrate
```

---

### 5️⃣ Create Superuser

```
python manage.py createsuperuser
```

---

### 6️⃣ Run Development Server

```
python manage.py runserver
```

Open in browser

```
http://127.0.0.1:8000/
```

---

## 🧠 Blog Model Example

```python
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

---

## 🌐 Deployment

This project is deployed on **Render**

Live URL:

https://blog-with-django-1.onrender.com/

---

## 📚 Learning Objectives

This project helps to understand:

* Django project structure
* Django models
* Template rendering
* URL routing
* CRUD operations
* Deployment on cloud platforms

---

## 👨‍💻 Author

**Devendra Tiwari**

---

⭐ If you like this project, please consider giving it a **star on GitHub**.
