import pytest
import requests

# NOTE: make sure you run the migrate-and-setup script with the testing flag in order to create the clean database:
# python manage.py migrate-and-setup --testing
# NOTE: make sure the server is running on the clean database:
# python manage.py runserver --settings=BackendDev.testSettings
# NOTE: stop the server and remove the database file when the test is done:
# rm databases/testing.sqlite3

@pytest.fixture
def superuser_credentials():
    return ("superuser", "xu261backend_su")

@pytest.fixture
def professor_credentials():
    return ("mikeyg", "mikey_scotch")

@pytest.fixture
def adminassistant_credentials():
    return ("donnaw", "donna_pw")

@pytest.fixture
def student_credentials():
    return ("aaronr", "test_ar_pw")

@pytest.fixture(autouse=True, scope="session")
def credentials(superuser_credentials, professor_credentials, adminassistant_credentials, student_credentials):
    return {"superuser": superuser_credentials, "professor": professor_credentials, "adminassistant": adminassistant_credentials, "student": student_credentials}

class TestDepartments:
    @pytest.fixture(scope="class")
    def default_departments():
        return "{{\"id\":1,\"name\":\"Mathematics\"},{\"id\":2,\"name\":\"Biology\"},{\"id\":3,\"name\":\"Psychology\"},{\"id\":4,\"name\":\"Computer Science\"},{\"id\":5,\"name\":\"Art\"},{\"id\":6,\"name\":\"Business\"}}"

class TestMajor:
    @pytest.fixture(scope="class")
    def default_major():
        return "{{\"id\":1,\"name\":\"BS in Computer Science\",\"subject\":\"Computer Science\"},{\"id\":2,\"name\":\"BA in Computer Science\",\"subject\":\"Computer Science\"},{\"id\":3,\"name\":\"Fine Arts\",\"subject\":\"Art\"},{\"id\":4,\"name\":\"Art Education\",\"subject\":\"Art\"},{\"id\":5,\"name\":\"Finance\",\"subject\":\"Business\"},{\"id\":6,\"name\":\"Accounting\",\"subject\":\"Business\"},{\"id\":7,\"name\":\"Mathematics\",\"subject\":\"Mathematics\"},{\"id\":8,\"name\":\"Actuarial Science\",\"subject\":\"Mathematics\"}}"

class TestMinor:
    @pytest.fixture(scope="class")
    def default_minor():
        return "{{\"id\":1,\"name\":\"Mathematics\",\"subject\":\"Mathematics\"},{\"id\":2,\"name\":\"Statistics\",\"subject\":\"Mathematics\"},{\"id\":3,\"name\":\"Applied Mathematics\",\"subject\":\"Mathematics\"},{\"id\":4,\"name\":\"Computer Science\",\"subject\":\"Computer Science\"},{\"id\":5,\"name\":\"Cybersecurity\",\"subject\":\"Computer Science\"},{\"id\":6,\"name\":\"Finance\",\"subject\":\"Business\"}}"

class TestCourses:
    @pytest.fixture(scope="class")
    def default_courses():
        return "[]"

class TestHighimpactexperiences:
    # TODO: do not check creation date field
    @pytest.fixture(scope="class")
    def default_highimpactexperiences():
        return "{{\"id\":1,\"name\":\"Immersive and Service Learning Courses\",\"RTX_name\":\"Immersive Learning\",\"area\":null,\"advisor\":null,\"Freshman_desc\":\"Watch reflections of Xavier students who have participated in immersive and service learning academic experiences.Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration.\",\"Sophomore_desc\":\"Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration. ILE and SERL courses are available in the Core, as electives, and within many majors\",\"Junior_desc\":\"Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration. ILE and SERL courses are available in the Core, as electives, and within many majors\",\"Senior_desc\":\"Many ILE and SERL Attributed Courses are integrated into Capstone and Community Engaged Research experiences in your major. Ask your advisor, or use an Advanced Search to explore these integrated experiences.\",\"creation_date\":\"2022-12-04T17:22:51.250266Z\"}}"

class TestEvents:
    @pytest.fixture(scope="class")
    def default_events():
        return "[]"

class TestStudent:
    @pytest.fixture(scope="class")
    def default_student_list():
        return "{{\"id\":1,\"prof\":{\"user\":{\"username\":\"kolleng\",\"email\":\"gruizengak@xavier.edu\",\"first_name\":\"Kollen\",\"last_name\":\"Gruizenga\"},\"prefix\":\"\",\"suffix\":\"II\",\"role\":\"ST\"},\"major\":[1,5],\"minor\":[1],\"schoolyear\":\"SR\"},{\"id\":2,\"prof\":{\"user\":{\"username\":\"aaronr\",\"email\":\"ripleya@xavier.edu\",\"first_name\":\"Aaron\",\"last_name\":\"Ripley\"},\"prefix\":\"Mr.\",\"suffix\":\"\",\"role\":\"ST\"},\"major\":[1],\"minor\":[],\"schoolyear\":\"JR\"}}"

class TestProfessor:
    @pytest.fixture(scope="class")
    def default_professor_list():
        return "{{\"id\":1,\"prof\":{\"user\":{\"username\":\"mikeyg\",\"email\":\"goldweber@xavier.edu\",\"first_name\":\"Michael\",\"last_name\":\"Goldweber\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":4,\"degree_desc\":\"PhD in Computer Science, University of Michigan 1969\"}}"

class TestAdminassistant:
    @pytest.fixture(scope="class")
    def default_adminassistant_list():
        return"{{\"id\":1,\"prof\":{\"user\":{\"username\":\"donnaw\",\"email\":\"wallace@xavier.edu\",\"first_name\":\"Donna\",\"last_name\":\"Wallace\"},\"prefix\":\"\",\"suffix\":\"\",\"role\":\"AA\"},\"department\":4}}"

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