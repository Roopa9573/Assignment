from flask import Flask, request, jsonify, abort
import sqlite3

# Define the Flask app and database connection
app = Flask(__name__)
db_conn = sqlite3.connect("data.db")

# Define the data tables in the database
db_conn.execute("CREATE TABLE IF NOT EXISTS colleges (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")
db_conn.execute("CREATE TABLE IF NOT EXISTS sections (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, college_id INTEGER NOT NULL, FOREIGN KEY(college_id) REFERENCES colleges(id))")
db_conn.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, section_id INTEGER NOT NULL, FOREIGN KEY(section_id) REFERENCES sections(id))")
db_conn.execute("CREATE TABLE IF NOT EXISTS marks (id INTEGER PRIMARY KEY AUTOINCREMENT, subject TEXT NOT NULL, marks INTEGER NOT NULL, student_id INTEGER NOT NULL, FOREIGN KEY(student_id) REFERENCES students(id))")

# Define the data level access rules for the different roles
data_rules = {
    "superadmin": {
        "read": True,
        "write": True,
        "update": True,
        "delete": True
    },
    "admin": {
        "read": True,
        "write": True,
        "update": True,
        "delete": True
    },
    "teacher": {
        "read": True,
        "write": False,
        "update": True,
        "delete": False
    },
    "student": {
        "read": True,
        "write": False,
        "update": True,
        "delete": False
    }
}

# Define helper functions to check data level access based on the user's role
def check_read_access(role):
    return data_rules[role]["read"]

def check_write_access(role):
    return data_rules[role]["write"]

def check_update_access(role):
    return data_rules[role]["update"]

def check_delete_access(role):
    return data_rules[role]["delete"]

# Define the API endpoints for manipulating data
# READ data
@app.route("/api/<role>/colleges")
def get_colleges(role):
    if not check_read_access(role):
        abort(403, description="You do not have permission to perform this action.")
    cursor = db_conn.execute("SELECT * FROM colleges")
    colleges = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
    return jsonify(colleges)

@app.route("/api/<role>/colleges/<int:college_id>/sections")
def get_sections(role, college_id):
    if not check_read_access(role):
        abort(403, description="You do not have permission to perform this action")
    cursor = db_conn.execute("SELECT * FROM sections WHERE college_id = ?", (college_id,))
    sections = [{"id": row[0], "name": row[1], "college_id": row[2]} for row in cursor.fetchall()]
    return jsonify(sections)

@app.route("/api/<role>/sections/<int:section_id>/students")
def get_students(role, section_id):
    if not check_read_access(role):
        abort(403, description="You do not have permission to perform this action")
    cursor = db_conn.execute("SELECT * FROM students WHERE section_id = ?", (section_id,))
    students = [{"id": row[0], "name": row[1], "section_id": row[2]} for row in cursor.fetchall()]
    return jsonify(students)

@app.route("/api/<role>/students/<int:student_id>/marks.")
 if not check_read_access(role):
        abort(403, description="You do not have permission to perform this action")
    cursor = db_conn.execute("SELECT * FROM students WHERE section_id = ?", (section_id,))
    marks = [{"id": row[0], "subject": row[1], "marks":row[2], "section_id": row[3]} for row in cursor.fetchall()]
    return jsonify(students)                                                                                          
    
