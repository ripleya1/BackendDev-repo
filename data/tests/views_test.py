import pytest
import requests

# NOTE: make sure you run the migrate-and-setup script with the testing flag in order to create the clean database:
# python manage.py migrate-and-setup --testing
# NOTE: make sure the server is running on the clean database:
# python manage.py runserver --settings=BackendDev.testSettings
# run tests using:
# pytest data/tests
# NOTE: stop the server and remove the database file when the test is done:
# rm databases/testing.sqlite3

@pytest.fixture(scope="session")
def superuser_credentials():
    return ("superuser", "xu261backend_su")

@pytest.fixture(scope="session")
def professor_credentials():
    return ("mikeyg", "mikey_scotch")

@pytest.fixture(scope="session")
def adminassistant_credentials():
    return ("donnaw", "donna_pw")

@pytest.fixture(scope="session")
def student_credentials():
    return ("aaronr", "test_ar_pw")

# tuples are (username, password)
@pytest.fixture(scope="session")
def credentials(superuser_credentials, professor_credentials, adminassistant_credentials, student_credentials):
    return {"superuser": superuser_credentials, "professor": professor_credentials, "adminassistant": adminassistant_credentials, "student": student_credentials}

#TODO: FIX DEFAULT FIXTURES (SHOULD INCLUDE FULL RESPONSE NOT JUST RESULTS FIELD)
# list, retrieve, create, update, partial update, delete

class TestDepartments:
    @pytest.fixture(scope="class")
    def default_departments(self):
        return "{\"count\":6,\"next\":null,\"previous\":null,\"results\":[{\"id\":1,\"name\":\"Mathematics\"},{\"id\":2,\"name\":\"Biology\"},{\"id\":3,\"name\":\"Psychology\"},{\"id\":4,\"name\":\"Computer Science\"},{\"id\":5,\"name\":\"Art\"},{\"id\":6,\"name\":\"Business\"}]}"
    
    def testListAsStudent(self, credentials, default_departments):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == default_departments
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsProfessor(self, credentials, default_departments):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == default_departments
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsAdminassistant(self, credentials, default_departments):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == default_departments
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsSuperuser(self, credentials, default_departments):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == default_departments
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testRetrieveAsStudent(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/1/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == "{\"id\":1,\"name\":\"Mathematics\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsProfessor(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/1/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == "{\"id\":1,\"name\":\"Mathematics\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsAdminassistant(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/1/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == "{\"id\":1,\"name\":\"Mathematics\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsSuperuser(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/1/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == "{\"id\":1,\"name\":\"Mathematics\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testCreateAsStudent(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Departments/", data={"name":"Test Department 1"}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsProfessor(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Departments/", data={"name":"Test Department 1"}, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsAdminassistant(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Departments/", data={"name":"Test Department 1"}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsSuperuser(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Departments/", data={"name":"Test Department 1"}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Departments/7/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":7,\"name\":\"Test Department 1\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    
    def testUpdateAsStudent(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Departments/7/", data={"name":"Test Department 2"}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsProfessor(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Departments/7/", data={"name":"Test Department 2"}, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsAdminassistant(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Departments/7/", data={"name":"Test Department 2"}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsSuperuser(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Departments/7/", data={"name":"Test Department 2"}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Departments/7/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":7,\"name\":\"Test Department 2\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testPartialUpdateAsStudent(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Departments/7/", data={"name":"Test Department 3"}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsProfessor(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Departments/7/", data={"name":"Test Department 3"}, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsAdminassistant(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Departments/7/", data={"name":"Test Department 3"}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsSuperuser(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Departments/7/", data={"name":"Test Department 3"}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Departments/7/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":7,\"name\":\"Test Department 3\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testDeleteAsStudent(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Departments/7/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsProfessor(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Departments/7/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsAdminassistant(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Departments/7/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsSuperuser(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Departments/7/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Departments/7/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))


# class TestMajor:
#     @pytest.fixture(scope="class")
#     def default_major():
#         return "{\"count\":8,\"next\":null,\"previous\":null,\"results\":[{\"id\":1,\"name\":\"BS in Computer Science\",\"subject\":\"Computer Science\"},{\"id\":2,\"name\":\"BA in Computer Science\",\"subject\":\"Computer Science\"},{\"id\":3,\"name\":\"Fine Arts\",\"subject\":\"Art\"},{\"id\":4,\"name\":\"Art Education\",\"subject\":\"Art\"},{\"id\":5,\"name\":\"Finance\",\"subject\":\"Business\"},{\"id\":6,\"name\":\"Accounting\",\"subject\":\"Business\"},{\"id\":7,\"name\":\"Mathematics\",\"subject\":\"Mathematics\"},{\"id\":8,\"name\":\"Actuarial Science\",\"subject\":\"Mathematics\"}]}"

# class TestMinor:
#     @pytest.fixture(scope="class")
#     def default_minor():
#         return "{\"count\":6,\"next\":null,\"previous\":null,\"results\":[{\"id\":1,\"name\":\"Mathematics\",\"subject\":\"Mathematics\"},{\"id\":2,\"name\":\"Statistics\",\"subject\":\"Mathematics\"},{\"id\":3,\"name\":\"Applied Mathematics\",\"subject\":\"Mathematics\"},{\"id\":4,\"name\":\"Computer Science\",\"subject\":\"Computer Science\"},{\"id\":5,\"name\":\"Cybersecurity\",\"subject\":\"Computer Science\"},{\"id\":6,\"name\":\"Finance\",\"subject\":\"Business\"}]}"

# class TestCourses:
#     @pytest.fixture(scope="class")
#     def default_courses():
#         return "[]"

# class TestHighimpactexperiences:
#     # TODO: do not check creation date field, use .contains instead of ==
#     @pytest.fixture(scope="class")
#     def default_highimpactexperiences():
#         return "{"count":1,"next":null,"previous":null,"results":[{"id":1,"name":"Immersive and Service Learning Courses","RTX_name":"Immersive Learning","area":null,"advisor":null,"Freshman_desc":"Watch reflections of Xavier students who have participated in immersive and service learning academic experiences.Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration.","Sophomore_desc":"Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration. ILE and SERL courses are available in the Core, as electives, and within many majors","Junior_desc":"Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration. ILE and SERL courses are available in the Core, as electives, and within many majors","Senior_desc":"Many ILE and SERL Attributed Courses are integrated into Capstone and Community Engaged Research experiences in your major. Ask your advisor, or use an Advanced Search to explore these integrated experiences.","creation_date":"2022-12-05T20:13:41.663049Z"}]}"

# class TestEvents:
#     @pytest.fixture(scope="class")
#     def default_events():
#         return "[]"

class TestStudent:
    @pytest.fixture(scope="class")
    def default_student_list(self):
        return "{\"count\":2,\"next\":null,\"previous\":null,\"results\":[{\"id\":1,\"prof\":{\"user\":{\"username\":\"kolleng\",\"email\":\"gruizengak@xavier.edu\",\"first_name\":\"Kollen\",\"last_name\":\"Gruizenga\"},\"prefix\":\"\",\"suffix\":\"II\",\"role\":\"ST\"},\"major\":[1,5],\"minor\":[1],\"schoolyear\":\"SR\"},{\"id\":2,\"prof\":{\"user\":{\"username\":\"aaronr\",\"email\":\"ripleya@xavier.edu\",\"first_name\":\"Aaron\",\"last_name\":\"Ripley\"},\"prefix\":\"Mr.\",\"suffix\":\"\",\"role\":\"ST\"},\"major\":[1],\"minor\":[],\"schoolyear\":\"JR\"}]}"

    def testListAsStudent(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Student/list/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == "{\"count\":1,\"next\":null,\"previous\":null,\"results\":[{\"id\":2,\"prof\":{\"user\":{\"username\":\"aaronr\",\"email\":\"ripleya@xavier.edu\",\"first_name\":\"Aaron\",\"last_name\":\"Ripley\"},\"prefix\":\"Mr.\",\"suffix\":\"\",\"role\":\"ST\"},\"major\":[1],\"minor\":[],\"schoolyear\":\"JR\"}]}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsProfessor(self, credentials, default_student_list):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Student/list/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == default_student_list
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsAdminassistant(self, credentials, default_student_list):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Student/list/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == default_student_list
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsSuperuser(self, credentials, default_student_list):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Student/list/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == default_student_list
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testRetrieveAsStudentSameStudent(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Student/2/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == "{\"id\":2,\"prof\":{\"user\":{\"username\":\"aaronr\",\"email\":\"ripleya@xavier.edu\",\"first_name\":\"Aaron\",\"last_name\":\"Ripley\"},\"prefix\":\"Mr.\",\"suffix\":\"\",\"role\":\"ST\"},\"major\":[1],\"minor\":[],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsStudentDifferentStudent(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Student/1/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsProfessor(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Student/1/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == "{\"id\":1,\"prof\":{\"user\":{\"username\":\"kolleng\",\"email\":\"gruizengak@xavier.edu\",\"first_name\":\"Kollen\",\"last_name\":\"Gruizenga\"},\"prefix\":\"\",\"suffix\":\"II\",\"role\":\"ST\"},\"major\":[1,5],\"minor\":[1],\"schoolyear\":\"SR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsAdminassistant(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Student/1/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == "{\"id\":1,\"prof\":{\"user\":{\"username\":\"kolleng\",\"email\":\"gruizengak@xavier.edu\",\"first_name\":\"Kollen\",\"last_name\":\"Gruizenga\"},\"prefix\":\"\",\"suffix\":\"II\",\"role\":\"ST\"},\"major\":[1,5],\"minor\":[1],\"schoolyear\":\"SR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsSuperuser(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Student/1/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == "{\"id\":1,\"prof\":{\"user\":{\"username\":\"kolleng\",\"email\":\"gruizengak@xavier.edu\",\"first_name\":\"Kollen\",\"last_name\":\"Gruizenga\"},\"prefix\":\"\",\"suffix\":\"II\",\"role\":\"ST\"},\"major\":[1,5],\"minor\":[1],\"schoolyear\":\"SR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testCreateAsStudent(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestUser1", 
                        "email":"testuser@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"User", 
                        "password":"test_pw" 
                    },  
                    "suffix":"III" 
                }, 
                "major":[1, 4], 
                "minor":[1], 
                "schoolyear":"JR" 
            }
            req = requests.post("http://127.0.0.1:8000/api/Student/register/", json=jsonData, auth=(credentials["student"][0], credentials["student"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Student/3/", auth=("TestUser1", "test_pw"))
            assert getReq.text == "{\"id\":3,\"prof\":{\"user\":{\"username\":\"TestUser1\",\"email\":\"testuser@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"User\"},\"prefix\":\"\",\"suffix\":\"III\",\"role\":\"ST\"},\"major\":[1,4],\"minor\":[1],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsProfessor(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestUser2", 
                        "email":"testuser@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"User", 
                        "password":"test_pw" 
                    },  
                    "suffix":"III" 
                }, 
                "major":[1, 4], 
                "minor":[1], 
                "schoolyear":"JR" 
            }
            req = requests.post("http://127.0.0.1:8000/api/Student/register/", json=jsonData, auth=(credentials["professor"][0], credentials["professor"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Student/4/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert getReq.text == "{\"id\":4,\"prof\":{\"user\":{\"username\":\"TestUser2\",\"email\":\"testuser@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"User\"},\"prefix\":\"\",\"suffix\":\"III\",\"role\":\"ST\"},\"major\":[1,4],\"minor\":[1],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsAdminassistant(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestUser3", 
                        "email":"testuser@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"User", 
                        "password":"test_pw" 
                    },  
                    "suffix":"III" 
                }, 
                "major":[1, 4], 
                "minor":[1], 
                "schoolyear":"JR" 
            }
            req = requests.post("http://127.0.0.1:8000/api/Student/register/", json=jsonData, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Student/5/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert getReq.text == "{\"id\":5,\"prof\":{\"user\":{\"username\":\"TestUser3\",\"email\":\"testuser@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"User\"},\"prefix\":\"\",\"suffix\":\"III\",\"role\":\"ST\"},\"major\":[1,4],\"minor\":[1],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsSuperuser(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestUser4", 
                        "email":"testuser@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"User", 
                        "password":"test_pw" 
                    },  
                    "suffix":"III" 
                }, 
                "major":[1, 4], 
                "minor":[1], 
                "schoolyear":"JR" 
            }
            req = requests.post("http://127.0.0.1:8000/api/Student/register/", json=jsonData, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Student/6/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":6,\"prof\":{\"user\":{\"username\":\"TestUser4\",\"email\":\"testuser@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"User\"},\"prefix\":\"\",\"suffix\":\"III\",\"role\":\"ST\"},\"major\":[1,4],\"minor\":[1],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsNotLoggedIn(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestUser5", 
                        "email":"testuser@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"User", 
                        "password":"test_pw" 
                    },  
                    "suffix":"III" 
                }, 
                "major":[1, 4], 
                "minor":[1], 
                "schoolyear":"JR" 
            }
            req = requests.post("http://127.0.0.1:8000/api/Student/register/", json=jsonData)
            # using newly created username and password
            getReq = requests.get("http://127.0.0.1:8000/api/Student/7/", auth=("TestUser5", "test_pw"))
            assert getReq.text == "{\"id\":7,\"prof\":{\"user\":{\"username\":\"TestUser5\",\"email\":\"testuser@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"User\"},\"prefix\":\"\",\"suffix\":\"III\",\"role\":\"ST\"},\"major\":[1,4],\"minor\":[1],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    
    def testUpdateAsStudentSameStudent(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestUser11", 
                        "email":"testuser@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"User", 
                        "password":"test_pw" 
                    },  
                    "suffix":"III" 
                }, 
                "major":[1, 4], 
                "minor":[1], 
                "schoolyear":"JR" 
            }
            req = requests.put("http://127.0.0.1:8000/api/Student/3/", json=jsonData, auth=("TestUser1", "test_pw"))
            getReq = requests.get("http://127.0.0.1:8000/api/Student/3/", auth=("TestUser11", "test_pw"))
            assert getReq.text == "{\"id\":3,\"prof\":{\"user\":{\"username\":\"TestUser11\",\"email\":\"testuser@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"User\"},\"prefix\":\"\",\"suffix\":\"III\",\"role\":\"ST\"},\"major\":[1,4],\"minor\":[1],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsStudentDifferentStudent(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestUser111", 
                        "email":"testuser@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"User", 
                        "password":"test_pw" 
                    },  
                    "suffix":"III" 
                }, 
                "major":[1, 4], 
                "minor":[1], 
                "schoolyear":"JR" 
            }
            req = requests.put("http://127.0.0.1:8000/api/Student/3/", json=jsonData, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsProfessor(self, credentials):
        jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestUser21", 
                        "email":"testuser@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"User", 
                        "password":"test_pw" 
                    },  
                    "suffix":"III" 
                }, 
                "major":[1, 4], 
                "minor":[1], 
                "schoolyear":"JR" 
            }
        try:
            req = requests.put("http://127.0.0.1:8000/api/Student/4/", json=jsonData, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsAdminassistant(self, credentials):
        jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestUser31", 
                        "email":"testuser@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"User", 
                        "password":"test_pw" 
                    },  
                    "suffix":"III" 
                }, 
                "major":[1, 4], 
                "minor":[1], 
                "schoolyear":"JR" 
            }
        try:
            req = requests.put("http://127.0.0.1:8000/api/Student/5/", json=jsonData, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Student/5/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert getReq.text == "{\"id\":5,\"prof\":{\"user\":{\"username\":\"TestUser31\",\"email\":\"testuser@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"User\"},\"prefix\":\"\",\"suffix\":\"III\",\"role\":\"ST\"},\"major\":[1,4],\"minor\":[1],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsSuperuser(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestUser41", 
                        "email":"testuser@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"User", 
                        "password":"test_pw" 
                    },  
                    "suffix":"III" 
                }, 
                "major":[1, 4], 
                "minor":[1], 
                "schoolyear":"JR" 
            }
            req = requests.put("http://127.0.0.1:8000/api/Student/6/", json=jsonData, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Student/6/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":6,\"prof\":{\"user\":{\"username\":\"TestUser41\",\"email\":\"testuser@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"User\"},\"prefix\":\"\",\"suffix\":\"III\",\"role\":\"ST\"},\"major\":[1,4],\"minor\":[1],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    @pytest.fixture(scope="class")
    def default_partial_update_student(self):
        return {"major":[2,3]}
    def testPartialUpdateAsStudentSameStudent(self, credentials, default_partial_update_student):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Student/3/", data=default_partial_update_student, auth=("TestUser11", "test_pw"))
            getReq = requests.get("http://127.0.0.1:8000/api/Student/3/", auth=("TestUser11", "test_pw"))
            assert getReq.text == "{\"id\":3,\"prof\":{\"user\":{\"username\":\"TestUser11\",\"email\":\"testuser@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"User\"},\"prefix\":\"\",\"suffix\":\"III\",\"role\":\"ST\"},\"major\":[2,3],\"minor\":[1],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsStudentDifferentStudent(self, credentials, default_partial_update_student):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Student/3/", data=default_partial_update_student, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsProfessor(self, credentials, default_partial_update_student):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Student/4/", data=default_partial_update_student, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsAdminassistant(self, credentials, default_partial_update_student):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Student/5/", data=default_partial_update_student, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Student/5/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert getReq.text == "{\"id\":5,\"prof\":{\"user\":{\"username\":\"TestUser31\",\"email\":\"testuser@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"User\"},\"prefix\":\"\",\"suffix\":\"III\",\"role\":\"ST\"},\"major\":[2,3],\"minor\":[1],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsSuperuser(self, credentials, default_partial_update_student):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Student/6/", data=default_partial_update_student, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Student/6/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":6,\"prof\":{\"user\":{\"username\":\"TestUser41\",\"email\":\"testuser@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"User\"},\"prefix\":\"\",\"suffix\":\"III\",\"role\":\"ST\"},\"major\":[2,3],\"minor\":[1],\"schoolyear\":\"JR\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testDeleteAsStudentSameStudent(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Student/3/", auth=("TestUser11", "test_pw"))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Student/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsStudentDifferentStudent(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Student/1/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsProfessor(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Student/4/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsAdminassistant(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Student/5/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Student/5/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsSuperuser(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Student/6/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Student/6/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

# class TestProfessor:
#     @pytest.fixture(scope="class")
#     def default_professor_list():
#         return "{\"count\":1,\"next\":null,\"previous\":null,\"results\":[{\"id\":1,\"prof\":{\"user\":{\"username\":\"mikeyg\",\"email\":\"goldweber@xavier.edu\",\"first_name\":\"Michael\",\"last_name\":\"Goldweber\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":4,\"degree_desc\":\"PhD in Computer Science, University of Michigan 1969\"}]}"

# class TestAdminassistant:
#     @pytest.fixture(scope="class")
#     def default_adminassistant_list():
#         return"{\"count\":1,\"next\":null,\"previous\":null,\"results\":[{\"id\":1,\"prof\":{\"user\":{\"username\":\"donnaw\",\"email\":\"wallace@xavier.edu\",\"first_name\":\"Donna\",\"last_name\":\"Wallace\"},\"prefix\":\"\",\"suffix\":\"\",\"role\":\"AA\"},\"department\":4}]}"




# OLD:
# class TestDepartmentViewSet:
#     def testGetOnNothing(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Departments/")
#             assert req.text == "[]"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))
    
#     def testPostOnNothing(self):
#         try:
#             req = requests.post("http://127.0.0.1:8000/api/Departments/", data = {"name":"Test Department 1"})
#             getReq = requests.get("http://127.0.0.1:8000/api/Departments/1/")
#             assert getReq.text == "{\"name\":\"Test Department 1\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testGetOnElement(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Departments/1/")
#             assert req.text == "{\"name\":\"Test Department 1\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testPut(self):
#         try:
#             req = requests.put("http://127.0.0.1:8000/api/Departments/1/", data = {"name":"Test Department 2"})
#             getReq = requests.get("http://127.0.0.1:8000/api/Departments/1/")
#             assert getReq.text == "{\"name\":\"Test Department 2\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testGetOnElementAfterPut(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Departments/1/")
#             assert req.text == "{\"name\":\"Test Department 2\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testPatch(self):
#         try:
#             req = requests.patch("http://127.0.0.1:8000/api/Departments/1/", data = {"name":"Test Department 3"})
#             getReq = requests.get("http://127.0.0.1:8000/api/Departments/1/")
#             assert getReq.text == "{\"name\":\"Test Department 3\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))
    
#     def testGetOnElementAfterPatch(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Departments/1/")
#             assert req.text == "{\"name\":\"Test Department 3\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testPost(self):
#         try:
#             req = requests.post("http://127.0.0.1:8000/api/Departments/", data = {"name":"Test Department 2"})
#             getReq = requests.get("http://127.0.0.1:8000/api/Departments/2/")
#             assert getReq.text == "{\"name\":\"Test Department 2\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testGetOnAllElements(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Departments/")
#             assert req.text == "[{\"name\":\"Test Department 3\"},{\"name\":\"Test Department 2\"}]"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testDelete(self):
#         try:
#             req = requests.delete("http://127.0.0.1:8000/api/Departments/1/")
#             getReq = requests.get("http://127.0.0.1:8000/api/Departments/1/")
#             assert getReq.text == "{\"detail\":\"Not found.\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testGetOnAllElementsAfterDeleting(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Departments/")
#             assert req.text == "[{\"name\":\"Test Department 2\"}]"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

# class TestMajorViewSet():
#     def testGetOnNothing(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Majors/")
#             assert req.text == "[]"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))
    
#     def testPostOnNothing(self):
#         try:
#             createDeptReq = requests.post("http://127.0.0.1:8000/api/Departments/", data = {"name":"Test Department 1"})            
#             req = requests.post("http://127.0.0.1:8000/api/Majors/", data = {"name":"Test Major 1","subject":"http://127.0.0.1:8000/api/Departments/3/"})
#             getReq = requests.get("http://127.0.0.1:8000/api/Majors/1/")
#             assert getReq.text == "{\"name\":\"Test Major 1\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testGetOnElement(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Majors/1/")
#             assert req.text == "{\"name\":\"Test Major 1\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testPut(self):
#         try:
#             req = requests.put("http://127.0.0.1:8000/api/Majors/1/", data = {"name":"Test Major 2", "subject":"http://127.0.0.1:8000/api/Departments/3/"})
#             getReq = requests.get("http://127.0.0.1:8000/api/Majors/1/")
#             assert getReq.text == "{\"name\":\"Test Major 2\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testGetOnElementAfterPut(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Majors/1/")
#             assert req.text == "{\"name\":\"Test Major 2\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testPatch(self):
#         try:
#             req = requests.patch("http://127.0.0.1:8000/api/Majors/1/", data = {"name":"Test Major 1"})
#             getReq = requests.get("http://127.0.0.1:8000/api/Majors/1/")
#             assert getReq.text == "{\"name\":\"Test Major 1\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))
    
#     def testGetOnElementAfterPatch(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Majors/1/")
#             assert req.text == "{\"name\":\"Test Major 1\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testPost(self):
#         try:
#             req = requests.post("http://127.0.0.1:8000/api/Majors/", data = {"name":"Test Major 2", "subject":"http://127.0.0.1:8000/api/Departments/3/"})
#             getReq = requests.get("http://127.0.0.1:8000/api/Majors/2/")
#             assert getReq.text == "{\"name\":\"Test Major 2\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testGetOnAllElements(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Majors/")
#             assert req.text == "[{\"name\":\"Test Major 1\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"},{\"name\":\"Test Major 2\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}]"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testDelete(self):
#         try:
#             req = requests.delete("http://127.0.0.1:8000/api/Majors/1/")
#             getReq = requests.get("http://127.0.0.1:8000/api/Majors/1/")
#             assert getReq.text == "{\"detail\":\"Not found.\"}"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))

#     def testGetOnAllElementsAfterDeleting(self):
#         try:
#             req = requests.get("http://127.0.0.1:8000/api/Majors/")
#             assert req.text == "[{\"name\":\"Test Major 2\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}]"
#         except Exception as e:
#             if req.status_code != requests.codes.ok:
#                 pytest.fail("Request failed with code " + str(req.status_code))
#             pytest.fail("Exception: " + str(e))