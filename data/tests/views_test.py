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


class TestMajor:
    @pytest.fixture(scope="class")
    def default_major(self):
        return "{\"count\":8,\"next\":null,\"previous\":null,\"results\":[{\"id\":1,\"name\":\"BS in Computer Science\",\"subject\":\"Computer Science\"},{\"id\":2,\"name\":\"BA in Computer Science\",\"subject\":\"Computer Science\"},{\"id\":3,\"name\":\"Fine Arts\",\"subject\":\"Art\"},{\"id\":4,\"name\":\"Art Education\",\"subject\":\"Art\"},{\"id\":5,\"name\":\"Finance\",\"subject\":\"Business\"},{\"id\":6,\"name\":\"Accounting\",\"subject\":\"Business\"},{\"id\":7,\"name\":\"Mathematics\",\"subject\":\"Mathematics\"},{\"id\":8,\"name\":\"Actuarial Science\",\"subject\":\"Mathematics\"}]}"

    def testListAsStudent(self, credentials, default_major):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Major/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == default_major
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsProfessor(self, credentials, default_major):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Major/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == default_major
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsAdminassistant(self, credentials, default_major):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Major/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == default_major
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsSuperuser(self, credentials, default_major):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Major/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == default_major
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testRetrieveAsStudent(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Major/1/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == "{\"id\":1,\"name\":\"BS in Computer Science\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsProfessor(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Major/1/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == "{\"id\":1,\"name\":\"BS in Computer Science\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsAdminassistant(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Major/1/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == "{\"id\":1,\"name\":\"BS in Computer Science\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsSuperuser(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Major/1/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == "{\"id\":1,\"name\":\"BS in Computer Science\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testCreateAsStudent(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Major/", data={"name":"Test Major 1", "subject":"Computer Science"}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsProfessor(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Major/", data={"name":"Test Major 1", "subject":"Computer Science"}, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsAdminassistant(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Major/", data={"name":"Test Major 1", "subject":"Computer Science"}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Major/9/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":9,\"name\":\"Test Major 1\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsSuperuser(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Major/", data={"name":"Test Major 2", "subject":"Computer Science"}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Major/10/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":10,\"name\":\"Test Major 2\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    
    def testUpdateAsStudent(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Major/9/", data={"name":"Test Major 2", "subject":"Computer Science"}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsProfessor(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Major/9/", data={"name":"Test Major 2", "subject":"Computer Science"}, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsAdminassistant(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Major/9/", data={"name":"Test Major 12", "subject":"Computer Science"}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Major/9/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":9,\"name\":\"Test Major 12\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsSuperuser(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Major/10/", data={"name":"Test Major 22", "subject":"Computer Science"}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Major/10/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":10,\"name\":\"Test Major 22\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testPartialUpdateAsStudent(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Major/9/", data={"name":"Test Major 3"}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsProfessor(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Major/9/", data={"name":"Test Major 3"}, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsAdminassistant(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Major/9/", data={"name":"Test Major 3"}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Major/9/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":9,\"name\":\"Test Major 3\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsSuperuser(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Major/10/", data={"name":"Test Major 33"}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Major/10/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":10,\"name\":\"Test Major 33\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testDeleteAsStudent(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Major/9/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsProfessor(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Major/9/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsAdminassistant(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Major/9/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Major/9/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsSuperuser(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Major/10/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Major/10/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))


class TestMinor:
    @pytest.fixture(scope="class")
    def default_minor(self):
        return "{\"count\":6,\"next\":null,\"previous\":null,\"results\":[{\"id\":1,\"name\":\"Mathematics\",\"subject\":\"Mathematics\"},{\"id\":2,\"name\":\"Statistics\",\"subject\":\"Mathematics\"},{\"id\":3,\"name\":\"Applied Mathematics\",\"subject\":\"Mathematics\"},{\"id\":4,\"name\":\"Computer Science\",\"subject\":\"Computer Science\"},{\"id\":5,\"name\":\"Cybersecurity\",\"subject\":\"Computer Science\"},{\"id\":6,\"name\":\"Finance\",\"subject\":\"Business\"}]}"

    def testListAsStudent(self, credentials, default_minor):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Minor/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == default_minor
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsProfessor(self, credentials, default_minor):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Minor/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == default_minor
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsAdminassistant(self, credentials, default_minor):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Minor/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == default_minor
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsSuperuser(self, credentials, default_minor):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Minor/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == default_minor
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testRetrieveAsStudent(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Minor/1/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == "{\"id\":1,\"name\":\"Mathematics\",\"subject\":\"Mathematics\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsProfessor(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Minor/1/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == "{\"id\":1,\"name\":\"Mathematics\",\"subject\":\"Mathematics\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsAdminassistant(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Minor/1/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == "{\"id\":1,\"name\":\"Mathematics\",\"subject\":\"Mathematics\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsSuperuser(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Minor/1/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == "{\"id\":1,\"name\":\"Mathematics\",\"subject\":\"Mathematics\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testCreateAsStudent(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Minor/", data={"name":"Test Minor 1", "subject":"Computer Science"}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsProfessor(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Minor/", data={"name":"Test Minor 1", "subject":"Computer Science"}, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsAdminassistant(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Minor/", data={"name":"Test Minor 1", "subject":"Computer Science"}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Minor/7/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":7,\"name\":\"Test Minor 1\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsSuperuser(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Minor/", data={"name":"Test Minor 2", "subject":"Computer Science"}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Minor/8/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":8,\"name\":\"Test Minor 2\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    
    def testUpdateAsStudent(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Minor/7/", data={"name":"Test Minor 2", "subject":"Computer Science"}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsProfessor(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Minor/7/", data={"name":"Test Minor 2", "subject":"Computer Science"}, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsAdminassistant(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Minor/7/", data={"name":"Test Minor 12", "subject":"Computer Science"}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Minor/7/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":7,\"name\":\"Test Minor 12\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsSuperuser(self, credentials):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Minor/8/", data={"name":"Test Minor 22", "subject":"Computer Science"}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Minor/8/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":8,\"name\":\"Test Minor 22\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testPartialUpdateAsStudent(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Minor/7/", data={"name":"Test Minor 3"}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsProfessor(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Minor/7/", data={"name":"Test Minor 3"}, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsAdminassistant(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Minor/7/", data={"name":"Test Minor 3"}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Minor/7/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":7,\"name\":\"Test Minor 3\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsSuperuser(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Minor/8/", data={"name":"Test Minor 33"}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Minor/8/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":8,\"name\":\"Test Minor 33\",\"subject\":\"Computer Science\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testDeleteAsStudent(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Minor/7/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsProfessor(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Minor/7/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsAdminassistant(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Minor/7/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Minor/7/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsSuperuser(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Minor/8/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Minor/8/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))


class TestCourses:
    @pytest.fixture(scope="class")
    def default_courses(self):
        return "[]"

    def testCreateAsStudent(self, credentials):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Courses/", data={"name":"Test Department 1"}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsProfessor(self, credentials):
        try:
            jsonData = { 
                "crn":54341, 
                "title":"Test Course", 
                "course_num":100, 
                "subject":1, 
                "instructor":1, 
                "credit_hours":3, 
                "desc_text":"Test course description" 
            }
            req = requests.post("http://127.0.0.1:8000/api/Courses/", json=jsonData, auth=(credentials["professor"][0], credentials["professor"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/54341/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"crn\":54341,\"title\":\"Test Course\",\"course_num\":100,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsAdminassistant(self, credentials):
        try:
            jsonData = { 
                "crn":12345, 
                "title":"Test Course", 
                "course_num":101, 
                "subject":1, 
                "instructor":1, 
                "credit_hours":3, 
                "desc_text":"Test course description" 
            }
            req = requests.post("http://127.0.0.1:8000/api/Courses/", json=jsonData, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/12345/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"crn\":12345,\"title\":\"Test Course\",\"course_num\":101,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsSuperuser(self, credentials):
        try:
            jsonData = { 
                "crn":11111, 
                "title":"Test Course 2", 
                "course_num":102, 
                "subject":1, 
                "instructor":1, 
                "credit_hours":3, 
                "desc_text":"Test course description" 
            }
            req = requests.post("http://127.0.0.1:8000/api/Courses/", json=jsonData, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/11111/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"crn\":11111,\"title\":\"Test Course 2\",\"course_num\":102,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testListAsStudent(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Courses/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == "{\"count\":3,\"next\":null,\"previous\":null,\"results\":[{\"crn\":54341,\"title\":\"Test Course\",\"course_num\":100,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"},{\"crn\":12345,\"title\":\"Test Course\",\"course_num\":101,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"},{\"crn\":11111,\"title\":\"Test Course 2\",\"course_num\":102,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}]}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsProfessor(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Courses/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == "{\"count\":3,\"next\":null,\"previous\":null,\"results\":[{\"crn\":54341,\"title\":\"Test Course\",\"course_num\":100,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"},{\"crn\":12345,\"title\":\"Test Course\",\"course_num\":101,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"},{\"crn\":11111,\"title\":\"Test Course 2\",\"course_num\":102,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}]}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsAdminassistant(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Courses/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == "{\"count\":3,\"next\":null,\"previous\":null,\"results\":[{\"crn\":54341,\"title\":\"Test Course\",\"course_num\":100,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"},{\"crn\":12345,\"title\":\"Test Course\",\"course_num\":101,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"},{\"crn\":11111,\"title\":\"Test Course 2\",\"course_num\":102,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}]}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsSuperuser(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Courses/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == "{\"count\":3,\"next\":null,\"previous\":null,\"results\":[{\"crn\":54341,\"title\":\"Test Course\",\"course_num\":100,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"},{\"crn\":12345,\"title\":\"Test Course\",\"course_num\":101,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"},{\"crn\":11111,\"title\":\"Test Course 2\",\"course_num\":102,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}]}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testRetrieveAsStudent(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Courses/12345/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == "{\"crn\":12345,\"title\":\"Test Course\",\"course_num\":101,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsProfessor(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Courses/12345/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == "{\"crn\":12345,\"title\":\"Test Course\",\"course_num\":101,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsAdminassistant(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Courses/12345/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == "{\"crn\":12345,\"title\":\"Test Course\",\"course_num\":101,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsSuperuser(self, credentials):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Courses/12345/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == "{\"crn\":12345,\"title\":\"Test Course\",\"course_num\":101,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
  
    def testUpdateAsStudent(self, credentials):
        try:
            jsonData = { 
                "crn":11111, 
                "title":"Test Course 21", 
                "course_num":102, 
                "subject":1, 
                "instructor":1, 
                "credit_hours":3, 
                "desc_text":"Test course description" 
            }
            req = requests.put("http://127.0.0.1:8000/api/Courses/11111/", json=jsonData, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsProfessor(self, credentials):
        jsonData = { 
                "crn":11111, 
                "title":"Test Course 21", 
                "course_num":102, 
                "subject":1, 
                "instructor":1, 
                "credit_hours":3, 
                "desc_text":"Test course description" 
            }
        try:
            req = requests.put("http://127.0.0.1:8000/api/Courses/11111/", json=jsonData, auth=(credentials["professor"][0], credentials["professor"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/11111/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"crn\":11111,\"title\":\"Test Course 21\",\"course_num\":102,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsAdminassistant(self, credentials):
        jsonData = { 
                "crn":11111, 
                "title":"Test Course 211", 
                "course_num":102, 
                "subject":1, 
                "instructor":1, 
                "credit_hours":3, 
                "desc_text":"Test course description" 
            }
        try:
            req = requests.put("http://127.0.0.1:8000/api/Courses/11111/", json=jsonData, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/11111/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"crn\":11111,\"title\":\"Test Course 211\",\"course_num\":102,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsSuperuser(self, credentials):
        jsonData = { 
                "crn":11111, 
                "title":"Test Course 2111", 
                "course_num":102, 
                "subject":1, 
                "instructor":1, 
                "credit_hours":3, 
                "desc_text":"Test course description" 
            }
        try:
            req = requests.put("http://127.0.0.1:8000/api/Courses/11111/", json=jsonData, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/11111/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"crn\":11111,\"title\":\"Test Course 2111\",\"course_num\":102,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testPartialUpdateAsStudent(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Courses/11111/", data={"course_num":103}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsProfessor(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Courses/11111/", data={"course_num":103}, auth=(credentials["professor"][0], credentials["professor"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/11111/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"crn\":11111,\"title\":\"Test Course 2111\",\"course_num\":103,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsAdminassistant(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Courses/11111/", data={"course_num":104}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/11111/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"crn\":11111,\"title\":\"Test Course 2111\",\"course_num\":104,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsSuperuser(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Courses/11111/", data={"course_num":105}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/11111/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"crn\":11111,\"title\":\"Test Course 2111\",\"course_num\":105,\"subject\":1,\"instructor\":1,\"credit_hours\":3,\"desc_text\":\"Test course description\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testDeleteAsStudent(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Courses/11111/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsProfessor(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Courses/11111/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/11111/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsAdminassistant(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Courses/54341/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/54341/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsSuperuser(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Courses/12345/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Courses/12345/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))


class TestHighimpactexperiences:
    # TODO: do not check creation date field, use .contains instead of ==
    # might need to make an edited version that doesnt include the creation date field
    # the default strings are edited to not include the creation_date field as it will not be checked
    @pytest.fixture(scope="class")
    def default_highimpactexperiences(self):
        return "{\"count\":1,\"next\":null,\"previous\":null,\"results\":[{\"id\":1,\"name\":\"Immersive and Service Learning Courses\",\"RTX_name\":\"Immersive Learning\",\"area\":null,\"advisor\":null,\"Freshman_desc\":\"Watch reflections of Xavier students who have participated in immersive and service learning academic experiences.Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration.\",\"Sophomore_desc\":\"Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration. ILE and SERL courses are available in the Core, as electives, and within many majors\",\"Junior_desc\":\"Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration. ILE and SERL courses are available in the Core, as electives, and within many majors\",\"Senior_desc\":\"Many ILE and SERL Attributed Courses are integrated into Capstone and Community Engaged Research experiences in your major. Ask your advisor, or use an Advanced Search to explore these integrated experiences.\","
    def testListAsStudent(self, credentials, default_highimpactexperiences):
        try:
            req = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text.__contains__(default_highimpactexperiences)
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsProfessor(self, credentials, default_highimpactexperiences):
        try:
            req = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text.__contains__(default_highimpactexperiences)
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsAdminassistant(self, credentials, default_highimpactexperiences):
        try:
            req = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text.__contains__(default_highimpactexperiences)
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsSuperuser(self, credentials, default_highimpactexperiences):
        try:
            req = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text.__contains__(default_highimpactexperiences)
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    @pytest.fixture(scope="class")
    def default_retrieve_highimpactexperiences(self):
        return "{\"id\":1,\"name\":\"Immersive and Service Learning Courses\",\"RTX_name\":\"Immersive Learning\",\"area\":null,\"advisor\":null,\"Freshman_desc\":\"Watch reflections of Xavier students who have participated in immersive and service learning academic experiences.Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration.\",\"Sophomore_desc\":\"Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration. ILE and SERL courses are available in the Core, as electives, and within many majors\",\"Junior_desc\":\"Use an Advanced Search in Self Service to explore Immersive and Service Learning Attributed Courses during registration. ILE and SERL courses are available in the Core, as electives, and within many majors\",\"Senior_desc\":\"Many ILE and SERL Attributed Courses are integrated into Capstone and Community Engaged Research experiences in your major. Ask your advisor, or use an Advanced Search to explore these integrated experiences.\","
    def testRetrieveAsStudent(self, credentials, default_retrieve_highimpactexperiences):
        try:
            req = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/1/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text.__contains__(default_retrieve_highimpactexperiences)
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsProfessor(self, credentials, default_retrieve_highimpactexperiences):
        try:
            req = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/1/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text.__contains__(default_retrieve_highimpactexperiences)
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsAdminassistant(self, credentials, default_retrieve_highimpactexperiences):
        try:
            req = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/1/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text.__contains__(default_retrieve_highimpactexperiences)
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsSuperuser(self, credentials, default_retrieve_highimpactexperiences):
        try:
            req = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/1/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text.__contains__(default_retrieve_highimpactexperiences)
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testCreateAsStudent(self, credentials):
        jsonData = {
            "name":"Test HIE", 
            "RTX_name":"test-hie", 
            "area":4, 
            "advisor":1, 
            "Freshman_desc":"desc1", 
            "Sophomore_desc":"desc2", 
            "Junior_desc":"desc3", 
            "Senior_desc":"desc4" 
        }
        try:
            req = requests.post("http://127.0.0.1:8000/api/HighImpactExperiences/", json=jsonData, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsProfessor(self, credentials):
        jsonData = {
            "name":"Test HIE", 
            "RTX_name":"test-hie", 
            "area":4, 
            "advisor":1, 
            "Freshman_desc":"desc1", 
            "Sophomore_desc":"desc2", 
            "Junior_desc":"desc3", 
            "Senior_desc":"desc4" 
        }
        try:
            req = requests.post("http://127.0.0.1:8000/api/HighImpactExperiences/", json=jsonData, auth=(credentials["professor"][0], credentials["professor"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text.__contains__("{\"id\":2,\"name\":\"Test HIE\",\"RTX_name\":\"test-hie\",\"area\":4,\"advisor\":1,\"Freshman_desc\":\"desc1\",\"Sophomore_desc\":\"desc2\",\"Junior_desc\":\"desc3\",\"Senior_desc\":\"desc4\",")
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsAdminassistant(self, credentials):
        jsonData = {
            "name":"Test HIE 2", 
            "RTX_name":"test-hie2", 
            "area":4, 
            "advisor":1, 
            "Freshman_desc":"desc1", 
            "Sophomore_desc":"desc2", 
            "Junior_desc":"desc3", 
            "Senior_desc":"desc4" 
        }
        try:
            req = requests.post("http://127.0.0.1:8000/api/HighImpactExperiences/", json=jsonData, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text.__contains__("{\"id\":3,\"name\":\"Test HIE 2\",\"RTX_name\":\"test-hie2\",\"area\":4,\"advisor\":1,\"Freshman_desc\":\"desc1\",\"Sophomore_desc\":\"desc2\",\"Junior_desc\":\"desc3\",\"Senior_desc\":\"desc4\",")
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testCreateAsSuperuser(self, credentials):
        jsonData = {
            "name":"Test HIE 3", 
            "RTX_name":"test-hie3", 
            "area":4, 
            "advisor":1, 
            "Freshman_desc":"desc1", 
            "Sophomore_desc":"desc2", 
            "Junior_desc":"desc3", 
            "Senior_desc":"desc4" 
        }
        try:
            req = requests.post("http://127.0.0.1:8000/api/HighImpactExperiences/", json=jsonData, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/4/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text.__contains__("{\"id\":4,\"name\":\"Test HIE 3\",\"RTX_name\":\"test-hie3\",\"area\":4,\"advisor\":1,\"Freshman_desc\":\"desc1\",\"Sophomore_desc\":\"desc2\",\"Junior_desc\":\"desc3\",\"Senior_desc\":\"desc4\",")
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    
    def testUpdateAsStudent(self, credentials):
        jsonData = {
            "name":"Test HIE 3", 
            "RTX_name":"test-hie", 
            "area":4, 
            "advisor":1, 
            "Freshman_desc":"desc1", 
            "Sophomore_desc":"desc2", 
            "Junior_desc":"desc3", 
            "Senior_desc":"desc4" 
        }
        try:
            req = requests.put("http://127.0.0.1:8000/api/HighImpactExperiences/2/", json=jsonData, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsProfessor(self, credentials):
        jsonData = {
            "name":"Test HIE 11", 
            "RTX_name":"test-hie", 
            "area":4, 
            "advisor":1, 
            "Freshman_desc":"desc1", 
            "Sophomore_desc":"desc2", 
            "Junior_desc":"desc3", 
            "Senior_desc":"desc4" 
        }
        try:
            req = requests.put("http://127.0.0.1:8000/api/HighImpactExperiences/2/", json=jsonData, auth=(credentials["professor"][0], credentials["professor"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text.__contains__("{\"id\":2,\"name\":\"Test HIE 11\",\"RTX_name\":\"test-hie\",\"area\":4,\"advisor\":1,\"Freshman_desc\":\"desc1\",\"Sophomore_desc\":\"desc2\",\"Junior_desc\":\"desc3\",\"Senior_desc\":\"desc4\",")
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsAdminassistant(self, credentials):
        jsonData = {
            "name":"Test HIE 21", 
            "RTX_name":"test-hie2", 
            "area":4, 
            "advisor":1, 
            "Freshman_desc":"desc1", 
            "Sophomore_desc":"desc2", 
            "Junior_desc":"desc3", 
            "Senior_desc":"desc4" 
        }
        try:
            req = requests.put("http://127.0.0.1:8000/api/HighImpactExperiences/3/", json=jsonData, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text.__contains__("{\"id\":3,\"name\":\"Test HIE 21\",\"RTX_name\":\"test-hie2\",\"area\":4,\"advisor\":1,\"Freshman_desc\":\"desc1\",\"Sophomore_desc\":\"desc2\",\"Junior_desc\":\"desc3\",\"Senior_desc\":\"desc4\",")
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsSuperuser(self, credentials):
        jsonData = {
            "name":"Test HIE 31", 
            "RTX_name":"test-hie3", 
            "area":4, 
            "advisor":1, 
            "Freshman_desc":"desc1", 
            "Sophomore_desc":"desc2", 
            "Junior_desc":"desc3", 
            "Senior_desc":"desc4" 
        }
        try:
            req = requests.put("http://127.0.0.1:8000/api/HighImpactExperiences/4/", json=jsonData, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/4/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text.__contains__("{\"id\":4,\"name\":\"Test HIE 31\",\"RTX_name\":\"test-hie3\",\"area\":4,\"advisor\":1,\"Freshman_desc\":\"desc1\",\"Sophomore_desc\":\"desc2\",\"Junior_desc\":\"desc3\",\"Senior_desc\":\"desc4\",")
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testPartialUpdateAsStudent(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/HighImpactExperiences/2/", data={"name":"Test HIE 211"}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsProfessor(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/HighImpactExperiences/2/", data={"name":"Test HIE 211"}, auth=(credentials["professor"][0], credentials["professor"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text.__contains__("{\"id\":2,\"name\":\"Test HIE 211\",\"RTX_name\":\"test-hie\",\"area\":4,\"advisor\":1,\"Freshman_desc\":\"desc1\",\"Sophomore_desc\":\"desc2\",\"Junior_desc\":\"desc3\",\"Senior_desc\":\"desc4\",")
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsAdminassistant(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/HighImpactExperiences/3/", data={"name":"Test HIE 311"}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text.__contains__("{\"id\":3,\"name\":\"Test HIE 311\",\"RTX_name\":\"test-hie2\",\"area\":4,\"advisor\":1,\"Freshman_desc\":\"desc1\",\"Sophomore_desc\":\"desc2\",\"Junior_desc\":\"desc3\",\"Senior_desc\":\"desc4\",")
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsSuperuser(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/HighImpactExperiences/4/", data={"name":"Test HIE 411"}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/4/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text.__contains__("{\"id\":4,\"name\":\"Test HIE 411\",\"RTX_name\":\"test-hie3\",\"area\":4,\"advisor\":1,\"Freshman_desc\":\"desc1\",\"Sophomore_desc\":\"desc2\",\"Junior_desc\":\"desc3\",\"Senior_desc\":\"desc4\",")
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testDeleteAsStudent(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/HighImpactExperiences/2/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsProfessor(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/HighImpactExperiences/2/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsAdminassistant(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/HighImpactExperiences/3/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsSuperuser(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/HighImpactExperiences/4/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/HighImpactExperiences/4/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))


# class TestEvents:
#     @pytest.fixture(scope="class")
#     def default_events(self):
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


class TestProfessor:
    @pytest.fixture(scope="class")
    def default_professor_list(self):
        return "{\"count\":1,\"next\":null,\"previous\":null,\"results\":[{\"id\":1,\"prof\":{\"user\":{\"username\":\"mikeyg\",\"email\":\"goldweber@xavier.edu\",\"first_name\":\"Michael\",\"last_name\":\"Goldweber\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":4,\"degree_desc\":\"PhD in Computer Science, University of Michigan 1969\"}]}"

    def testListAsStudent(self, credentials, default_professor_list):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Professor/list/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == default_professor_list
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsProfessor(self, credentials, default_professor_list):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Professor/list/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == default_professor_list
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsAdminassistant(self, credentials, default_professor_list):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Professor/list/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == default_professor_list
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsSuperuser(self, credentials, default_professor_list):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Professor/list/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == default_professor_list
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    
    @pytest.fixture(scope="class")
    def default_professor_retrieve(self):
        return "{\"id\":1,\"prof\":{\"user\":{\"username\":\"mikeyg\",\"email\":\"goldweber@xavier.edu\",\"first_name\":\"Michael\",\"last_name\":\"Goldweber\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":4,\"degree_desc\":\"PhD in Computer Science, University of Michigan 1969\"}"
    def testRetrieveAsStudent(self, credentials, default_professor_retrieve):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Professor/1/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.text == default_professor_retrieve
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsProfessor(self, credentials, default_professor_retrieve):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Professor/1/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == default_professor_retrieve
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsAdminassistant(self, credentials, default_professor_retrieve):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Professor/1/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == default_professor_retrieve
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsSuperuser(self, credentials, default_professor_retrieve):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Professor/1/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == default_professor_retrieve
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
                        "username":"TestProf1", 
                        "email":"testprof@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Prof", 
                        "password":"test_pw" 
                    },  
                    "prefix":"Dr." 
                }, 
                "department":4,
                "degree_desc":"Test degree_desc"
            }
            req = requests.post("http://127.0.0.1:8000/api/Professor/register/", json=jsonData, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403        
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
                        "username":"TestProf1", 
                        "email":"testprof@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Prof", 
                        "password":"test_pw" 
                    },  
                    "prefix":"Dr." 
                }, 
                "department":4,
                "degree_desc":"Test degree_desc"
            }
            req = requests.post("http://127.0.0.1:8000/api/Professor/register/", json=jsonData, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
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
                        "username":"TestProf1", 
                        "email":"testprof@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Prof", 
                        "password":"test_pw" 
                    },  
                    "prefix":"Dr." 
                }, 
                "department":4,
                "degree_desc":"Test degree_desc"
            }
            req = requests.post("http://127.0.0.1:8000/api/Professor/register/", json=jsonData, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Professor/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":2,\"prof\":{\"user\":{\"username\":\"TestProf1\",\"email\":\"testprof@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Prof\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":4,\"degree_desc\":\"Test degree_desc\"}"
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
                        "username":"TestProf2", 
                        "email":"testprof@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Prof", 
                        "password":"test_pw" 
                    },  
                    "prefix":"Dr." 
                }, 
                "department":4,
                "degree_desc":"Test degree_desc"
            }
            req = requests.post("http://127.0.0.1:8000/api/Professor/register/", json=jsonData, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Professor/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":3,\"prof\":{\"user\":{\"username\":\"TestProf2\",\"email\":\"testprof@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Prof\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":4,\"degree_desc\":\"Test degree_desc\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    
    def testUpdateAsStudent(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestProf11", 
                        "email":"testprof@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Prof", 
                        "password":"test_pw" 
                    },  
                    "prefix":"Dr." 
                }, 
                "department":4,
                "degree_desc":"Test degree_desc"
            }
            req = requests.put("http://127.0.0.1:8000/api/Professor/2/", json=jsonData, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsProfessorSameProfessor(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestProf11", 
                        "email":"testprof@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Prof", 
                        "password":"test_pw" 
                    },  
                    "prefix":"Dr." 
                }, 
                "department":4,
                "degree_desc":"Test degree_desc"
            }
            req = requests.put("http://127.0.0.1:8000/api/Professor/2/", json=jsonData, auth=("TestProf1", "test_pw"))
            getReq = requests.get("http://127.0.0.1:8000/api/Professor/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":2,\"prof\":{\"user\":{\"username\":\"TestProf11\",\"email\":\"testprof@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Prof\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":4,\"degree_desc\":\"Test degree_desc\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsProfessorDifferentProfessor(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestProf12", 
                        "email":"testprof@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Prof", 
                        "password":"test_pw" 
                    },  
                    "prefix":"Dr." 
                }, 
                "department":4,
                "degree_desc":"Test degree_desc"
            }
            req = requests.put("http://127.0.0.1:8000/api/Professor/2/", json=jsonData, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsAdminassistant(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestProf21", 
                        "email":"testprof@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Prof", 
                        "password":"test_pw" 
                    },  
                    "prefix":"Dr." 
                }, 
                "department":4,
                "degree_desc":"Test degree_desc"
            }
            req = requests.put("http://127.0.0.1:8000/api/Professor/3/", json=jsonData, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Professor/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":3,\"prof\":{\"user\":{\"username\":\"TestProf21\",\"email\":\"testprof@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Prof\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":4,\"degree_desc\":\"Test degree_desc\"}"
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
                        "username":"TestProf1", 
                        "email":"testprof@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Prof", 
                        "password":"test_pw" 
                    },  
                    "prefix":"Dr." 
                }, 
                "department":4,
                "degree_desc":"Test degree_desc"
            }
            req = requests.put("http://127.0.0.1:8000/api/Professor/2/", json=jsonData, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Professor/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":2,\"prof\":{\"user\":{\"username\":\"TestProf1\",\"email\":\"testprof@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Prof\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":4,\"degree_desc\":\"Test degree_desc\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    @pytest.fixture(scope="class")
    def default_partial_update_professor(self):
        return {"department":3}
    def testPartialUpdateAsStudent(self, credentials, default_partial_update_professor):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Professor/2/", data=default_partial_update_professor, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsProfessorSameProfessor(self, credentials, default_partial_update_professor):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Professor/2/", data=default_partial_update_professor, auth=("TestProf1", "test_pw"))
            getReq = requests.get("http://127.0.0.1:8000/api/Professor/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":2,\"prof\":{\"user\":{\"username\":\"TestProf1\",\"email\":\"testprof@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Prof\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":3,\"degree_desc\":\"Test degree_desc\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsProfessorDifferentProfessor(self, credentials, default_partial_update_professor):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Professor/3/", data=default_partial_update_professor, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsAdminassistant(self, credentials, default_partial_update_professor):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Professor/3/", data=default_partial_update_professor, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Professor/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":3,\"prof\":{\"user\":{\"username\":\"TestProf21\",\"email\":\"testprof@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Prof\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":3,\"degree_desc\":\"Test degree_desc\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsSuperuser(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Professor/3/", data={"department":4}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/Professor/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":3,\"prof\":{\"user\":{\"username\":\"TestProf21\",\"email\":\"testprof@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Prof\"},\"prefix\":\"Dr.\",\"suffix\":\"\",\"role\":\"PR\"},\"department\":4,\"degree_desc\":\"Test degree_desc\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testDeleteAsStudent(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Professor/1/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsProfessorSameProfessor(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Professor/3/", auth=("TestProf21", "test_pw"))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Professor/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsProfessorDifferentProfessor(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Professor/2/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsAdminassistant(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Professor/2/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Professor/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsSuperuser(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestProf1", 
                        "email":"testprof@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Prof", 
                        "password":"test_pw" 
                    },  
                    "prefix":"Dr." 
                }, 
                "department":4,
                "degree_desc":"Test degree_desc"
            }
            createReq = requests.post("http://127.0.0.1:8000/api/Professor/register/", json=jsonData, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert createReq.status_code == 201
            req = requests.delete("http://127.0.0.1:8000/api/Professor/4/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/Professor/4/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))


class TestAdminassistant:
    @pytest.fixture(scope="class")
    def default_adminassistant_list(self):
        return"{\"count\":1,\"next\":null,\"previous\":null,\"results\":[{\"id\":1,\"prof\":{\"user\":{\"username\":\"donnaw\",\"email\":\"wallace@xavier.edu\",\"first_name\":\"Donna\",\"last_name\":\"Wallace\"},\"prefix\":\"\",\"suffix\":\"\",\"role\":\"AA\"},\"department\":4}]}"
    def testListAsStudent(self, credentials, default_adminassistant_list):
        try:
            req = requests.get("http://127.0.0.1:8000/api/AdminAssistant/list/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsProfessor(self, credentials, default_adminassistant_list):
        try:
            req = requests.get("http://127.0.0.1:8000/api/AdminAssistant/list/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == default_adminassistant_list
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsAdminassistant(self, credentials, default_adminassistant_list):
        try:
            req = requests.get("http://127.0.0.1:8000/api/AdminAssistant/list/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == default_adminassistant_list
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testListAsSuperuser(self, credentials, default_adminassistant_list):
        try:
            req = requests.get("http://127.0.0.1:8000/api/AdminAssistant/list/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == default_adminassistant_list
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    
    @pytest.fixture(scope="class")
    def default_adminassistant_retrieve(self):
        return "{\"id\":1,\"prof\":{\"user\":{\"username\":\"donnaw\",\"email\":\"wallace@xavier.edu\",\"first_name\":\"Donna\",\"last_name\":\"Wallace\"},\"prefix\":\"\",\"suffix\":\"\",\"role\":\"AA\"},\"department\":4}"
    def testRetrieveAsStudent(self, credentials, default_adminassistant_retrieve):
        try:
            req = requests.get("http://127.0.0.1:8000/api/AdminAssistant/1/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsProfessor(self, credentials, default_adminassistant_retrieve):
        try:
            req = requests.get("http://127.0.0.1:8000/api/AdminAssistant/1/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.text == default_adminassistant_retrieve
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsAdminassistant(self, credentials, default_adminassistant_retrieve):
        try:
            req = requests.get("http://127.0.0.1:8000/api/AdminAssistant/1/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.text == default_adminassistant_retrieve
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testRetrieveAsSuperuser(self, credentials, default_adminassistant_retrieve):
        try:
            req = requests.get("http://127.0.0.1:8000/api/AdminAssistant/1/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.text == default_adminassistant_retrieve
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
                        "username":"TestAdmin1", 
                        "email":"testadmin@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Admin", 
                        "password":"test_pw" 
                    }
                }, 
                "department":4
            }
            req = requests.post("http://127.0.0.1:8000/api/AdminAssistant/register/", json=jsonData, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403        
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
                        "username":"TestAdmin1", 
                        "email":"testadmin@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Admin", 
                        "password":"test_pw" 
                    }
                }, 
                "department":4
            }
            req = requests.post("http://127.0.0.1:8000/api/AdminAssistant/register/", json=jsonData, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
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
                        "username":"TestAdmin1", 
                        "email":"testadmin@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Admin", 
                        "password":"test_pw" 
                    }
                }, 
                "department":4
            }
            req = requests.post("http://127.0.0.1:8000/api/AdminAssistant/register/", json=jsonData, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/AdminAssistant/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":2,\"prof\":{\"user\":{\"username\":\"TestAdmin1\",\"email\":\"testadmin@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Admin\"},\"prefix\":\"\",\"suffix\":\"\",\"role\":\"AA\"},\"department\":4}"
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
                        "username":"TestAdmin2", 
                        "email":"testadmin@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Admin", 
                        "password":"test_pw" 
                    }
                }, 
                "department":4
            }
            req = requests.post("http://127.0.0.1:8000/api/AdminAssistant/register/", json=jsonData, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/AdminAssistant/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":3,\"prof\":{\"user\":{\"username\":\"TestAdmin2\",\"email\":\"testadmin@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Admin\"},\"prefix\":\"\",\"suffix\":\"\",\"role\":\"AA\"},\"department\":4}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    
    def testUpdateAsStudent(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestAdmin1", 
                        "email":"testadmin@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Admin", 
                        "password":"test_pw" 
                    }
                }, 
                "department":4
            }
            req = requests.put("http://127.0.0.1:8000/api/AdminAssistant/2/", json=jsonData, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsAdminassistantSameAdminassistant(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestAdmin11", 
                        "email":"testadmin@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Admin", 
                        "password":"test_pw" 
                    }
                }, 
                "department":4
            }
            req = requests.put("http://127.0.0.1:8000/api/AdminAssistant/2/", json=jsonData, auth=("TestAdmin1", "test_pw"))
            getReq = requests.get("http://127.0.0.1:8000/api/AdminAssistant/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":2,\"prof\":{\"user\":{\"username\":\"TestAdmin11\",\"email\":\"testadmin@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Admin\"},\"prefix\":\"\",\"suffix\":\"\",\"role\":\"AA\"},\"department\":4}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsAdminassistantDifferentAdminassistant(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestAdmin21", 
                        "email":"testadmin@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Admin", 
                        "password":"test_pw" 
                    }
                }, 
                "department":4
            }
            req = requests.put("http://127.0.0.1:8000/api/AdminAssistant/3/", json=jsonData, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testUpdateAsProfessor(self, credentials):
        try:
            jsonData = { 
                "prof":{ 
                    "user":{ 
                        "username":"TestAdmin21", 
                        "email":"testadmin@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Admin", 
                        "password":"test_pw" 
                    }
                }, 
                "department":4
            }
            req = requests.put("http://127.0.0.1:8000/api/AdminAssistant/3/", json=jsonData, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
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
                        "username":"TestAdmin21", 
                        "email":"testadmin@xavier.edu", 
                        "first_name":"Test", 
                        "last_name":"Admin", 
                        "password":"test_pw" 
                    }
                }, 
                "department":4
            }
            req = requests.put("http://127.0.0.1:8000/api/AdminAssistant/3/", json=jsonData, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/AdminAssistant/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":3,\"prof\":{\"user\":{\"username\":\"TestAdmin21\",\"email\":\"testadmin@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Admin\"},\"prefix\":\"\",\"suffix\":\"\",\"role\":\"AA\"},\"department\":4}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testPartialUpdateAsStudent(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/AdminAssistant/2/", data={"department":3}, auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsAdminassistantSameAdminassistant(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/AdminAssistant/2/", data={"department":3}, auth=("TestAdmin11", "test_pw"))
            getReq = requests.get("http://127.0.0.1:8000/api/AdminAssistant/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":2,\"prof\":{\"user\":{\"username\":\"TestAdmin11\",\"email\":\"testadmin@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Admin\"},\"prefix\":\"\",\"suffix\":\"\",\"role\":\"AA\"},\"department\":3}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsAdminassistantDifferentAdminassistant(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/AdminAssistant/3/", data={"department":3}, auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsProfessor(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/AdminAssistant/3/", data={"department":3}, auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testPartialUpdateAsSuperuser(self, credentials):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/AdminAssistant/3/", data={"department":4}, auth=(credentials["superuser"][0], credentials["superuser"][1]))
            getReq = requests.get("http://127.0.0.1:8000/api/AdminAssistant/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.text == "{\"id\":3,\"prof\":{\"user\":{\"username\":\"TestAdmin21\",\"email\":\"testadmin@xavier.edu\",\"first_name\":\"Test\",\"last_name\":\"Admin\"},\"prefix\":\"\",\"suffix\":\"\",\"role\":\"AA\"},\"department\":4}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))

    def testDeleteAsStudent(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/AdminAssistant/3/", auth=(credentials["student"][0], credentials["student"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsAdminassistantSameAdminassistant(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/AdminAssistant/3/", auth=("TestAdmin21", "test_pw"))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/AdminAssistant/3/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsAdminassistantDifferentAdminassistant(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/AdminAssistant/2/", auth=(credentials["adminassistant"][0], credentials["adminassistant"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsProfessor(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/AdminAssistant/2/", auth=(credentials["professor"][0], credentials["professor"][1]))
            assert req.status_code == 403
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))
    def testDeleteAsSuperuser(self, credentials):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/AdminAssistant/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert req.status_code == 204
            getReq = requests.get("http://127.0.0.1:8000/api/AdminAssistant/2/", auth=(credentials["superuser"][0], credentials["superuser"][1]))
            assert getReq.status_code == 404
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            else:
                pytest.fail("Exception: " + str(e))