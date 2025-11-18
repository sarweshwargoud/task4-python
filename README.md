📘 Flask User Management API

A simple REST API built using Flask that allows you to manage users using GET, POST, PUT, DELETE requests.
This project demonstrates basic API development concepts such as routing, JSON handling, and HTTP methods.

🚀 Features

Add new users

Get all users

Get a single user by ID

Update user details

Delete a user

In-memory storage (Dictionary/List)

🛠 Technologies Used

Python

Flask

Postman (for testing)

▶️ How to Run the App
1. Create and activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Run the Flask app
python app.py


The API will start at:
👉 http://127.0.0.1:5000/

📌 API Endpoints
✔ 1. GET all users

URL: GET /users
Returns list of all users.

✔ 2. POST add user

URL: POST /users
Body (JSON):

{
  "name": "Ravi Kumar",
  "email": "ravi@example.com"
}


Response:

{
  "id": 1,
  "name": "Ravi Kumar",
  "email": "ravi@example.com"
}

✔ 3. GET user by ID

GET /users/<id>

✔ 4. PUT update user

PUT /users/<id>
Body:

{
  "name": "Updated Name",
  "email": "updated@example.com"
}

✔ 5. DELETE user

DELETE /users/<id>

✔ Sample Postman Usage
🔹 For POST /users

Select: POST

URL: http://127.0.0.1:5000/users

Go to Body → raw → JSON

Enter:

{
  "name": "Ravi Kumar",
  "email": "ravi@example.com"
}


Click Send

If the API is correct, you will see:

{
  "id": 1,
  "name": "Ravi Kumar",
  "email": "ravi@example.com"
}
