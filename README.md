## Project chronology

- make a project directory
- git init
- create a gitignore file
- create a README.md file
- git commit "git commit -m "chore: initialize git and add .gitignore"
- STEP 2 — Virtual Environment (Local Dev Ready)
  python -m venv venv

# Windows

venv\Scripts\activate

# Linux / Mac

source venv/bin/activate

- install dependencies requirements.txt
- git add requirements.txt
- git commit -m "build: add initial project dependencies"

#### STEP 3 — Project Folder Structure

```plaintext
mkdir app
cd app
mkdir core api models schemas services repositories utils tests
mkdir api/v1
cd ..
```

```plaintext
git commit 
git add app
git commit -m "chore: create base project structure"
```

#### STEP 4 — Environment Config (.env)

```plaintext
PROJECT_NAME=University Management System
DATABASE_URL=postgresql://postgres:password@localhost:5432/university_db
SECRET_KEY=supersecretkey
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

#### STEP 5 — Core Config (config.py)

```plaintext
app/core/config.py
```

```python
- git commit 
```

#### STEP 6 — Database Setup (Atomicity Foundation)

```plaintext
app/core/database.py
```

```python
- git commit 
```

#### STEP 7 — Base Model (Soft Delete Ready)

```plaintext
📄 app/models/base.py
```

```python
- git commit 
```

#### STEP 8 — Global Exception Handling

```plaintext
app/core/exceptions.py
```

```python
- git commit 
```

#### STEP 9 — FastAPI App Bootstrap

```plaintext
📄 app/main.py
```

```python
- git commit 
```

#### Server Run

```plaintext
uvicorn app.main:app --reload
```

#### STEP 2.4 — Repository Layer (DB Access Only)



API end points


# post method

/api/v1/attendance/mark

# get method

/api/v1/attendance/my

# get method

/api/v1/attendance/percentage/course_id

# get method

/api/v1/attendance/course-report/course_id

# get method

/api/v1/attendance/faculty-dashboard

# post method

/api/v1/auth/change-password

# post method

/api/v1/auth/login

# post method

/api/v1/auth/forgot-password

# get courses

/api/v1/courses/

# create courses

/api/v1/courses/

# create enrollment

api/v1/enrollments

# get enrollments

api/v1/enrollments/my-courses

# create user

api/v1/users

# get user

api/v1/users/admin-only

# get user

api/v1/users/teacher-area

# get user

api/v1/users/student-area
