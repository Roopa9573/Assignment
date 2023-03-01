# Data for students in different colleges
college_data = {
    "college1": {
        "state": "state1",
        "city": "city1",
        "campus": "campus1",
        "section1": [
            {"id": 1, "name": "John"},
            {"id": 2, "name": "Jane"}
        ],
        "section2": [
            {"id": 3, "name": "Bob"},
            {"id": 4, "name": "Alice"}
        ]
    },
    "college2": {
        "state": "state2",
        "city": "city2",
        "campus": "campus2",
        "section1": [
            {"id": 5, "name": "Mike"},
            {"id": 6, "name": "Sara"}
        ],
        "section2": [
            {"id": 7, "name": "Kate"},
            {"id": 8, "name": "Tom"}
        ]
    }
}

# Data level access implementation
class DataLevelAccess:
    def __init__(self, role, college=None, section=None):
        self.role = role
        self.college = college
        self.section = section

    def get_data(self):
        if self.role == "superadmin":
            # Super Admin can see the data of all colleges (i.e., all students)
            return college_data
        elif self.role == "admin":
            # Admin can see the data of 1 college (i.e., students data of 1 college)
            if self.college is None:
                return {}
            else:
                return college_data.get(self.college, {})
        elif self.role == "teacher":
            # Teacher can see all the students data of particular section
            if self.college is None or self.section is None:
                return {}
            else:
                college = college_data.get(self.college, {})
                section_data = college.get(self.section, [])
                return section_data
        elif self.role == "student":
            # Student can see only his/her data
            if self.college is None or self.section is None:
                return {}
            else:
                college = college_data.get(self.college, {})
                section_data = college.get(self.section, [])
                student_data = [s for s in section_data if s["id"] == self.id]
                return student_data
        else:
            # Invalid role
            return {}

# Example usage
# Super Admin can see the data of all colleges (i.e., all students)
superadmin_access = DataLevelAccess(role="superadmin")
print(superadmin_access.get_data())

# Admin can see the data of 1 college (i.e., students data of 1 college)
admin_access = DataLevelAccess(role="admin", college="college1")
print(admin_access.get_data())

# Teacher can see all the students data of particular section
teacher_access = DataLevelAccess(role="teacher", college="college1", section="section1")
print(teacher_access.get_data())

# Student can see only his/her data
student_access = DataLevelAccess(role="student", college="college1", section="section1", id=1)
print(student_access.get_data())
