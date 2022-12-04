import pytest
import requests

# NOTE: make sure you run the migrate-and-setup script with the testing flag in order to create the clean database:
# python manage.py migrate-and-setup --testing
# NOTE: make sure the server is running on the clean database:
# python manage.py runserver --settings=BackendDev.testSettings
# NOTE: stop the server and remove the database file when the test is done:
# rm databases/testing.sqlite3
class TestDepartmentViewSet:
    def testGetOnNothing(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/")
            assert req.text == "[]"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))
    
    def testPostOnNothing(self):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Departments/", data = {"name":"Test Department 1"})
            getReq = requests.get("http://127.0.0.1:8000/api/Departments/1/")
            assert getReq.text == "{\"name\":\"Test Department 1\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testGetOnElement(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/1/")
            assert req.text == "{\"name\":\"Test Department 1\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testPut(self):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Departments/1/", data = {"name":"Test Department 2"})
            getReq = requests.get("http://127.0.0.1:8000/api/Departments/1/")
            assert getReq.text == "{\"name\":\"Test Department 2\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testGetOnElementAfterPut(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/1/")
            assert req.text == "{\"name\":\"Test Department 2\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testPatch(self):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Departments/1/", data = {"name":"Test Department 3"})
            getReq = requests.get("http://127.0.0.1:8000/api/Departments/1/")
            assert getReq.text == "{\"name\":\"Test Department 3\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))
    
    def testGetOnElementAfterPatch(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/1/")
            assert req.text == "{\"name\":\"Test Department 3\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testPost(self):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Departments/", data = {"name":"Test Department 2"})
            getReq = requests.get("http://127.0.0.1:8000/api/Departments/2/")
            assert getReq.text == "{\"name\":\"Test Department 2\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testGetOnAllElements(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/")
            assert req.text == "[{\"name\":\"Test Department 3\"},{\"name\":\"Test Department 2\"}]"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testDelete(self):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Departments/1/")
            getReq = requests.get("http://127.0.0.1:8000/api/Departments/1/")
            assert getReq.text == "{\"detail\":\"Not found.\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testGetOnAllElementsAfterDeleting(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Departments/")
            assert req.text == "[{\"name\":\"Test Department 2\"}]"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

class TestMajorViewSet():
    def testGetOnNothing(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Majors/")
            assert req.text == "[]"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))
    
    def testPostOnNothing(self):
        try:
            createDeptReq = requests.post("http://127.0.0.1:8000/api/Departments/", data = {"name":"Test Department 1"})            
            req = requests.post("http://127.0.0.1:8000/api/Majors/", data = {"name":"Test Major 1","subject":"http://127.0.0.1:8000/api/Departments/3/"})
            getReq = requests.get("http://127.0.0.1:8000/api/Majors/1/")
            assert getReq.text == "{\"name\":\"Test Major 1\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testGetOnElement(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Majors/1/")
            assert req.text == "{\"name\":\"Test Major 1\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testPut(self):
        try:
            req = requests.put("http://127.0.0.1:8000/api/Majors/1/", data = {"name":"Test Major 2", "subject":"http://127.0.0.1:8000/api/Departments/3/"})
            getReq = requests.get("http://127.0.0.1:8000/api/Majors/1/")
            assert getReq.text == "{\"name\":\"Test Major 2\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testGetOnElementAfterPut(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Majors/1/")
            assert req.text == "{\"name\":\"Test Major 2\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testPatch(self):
        try:
            req = requests.patch("http://127.0.0.1:8000/api/Majors/1/", data = {"name":"Test Major 1"})
            getReq = requests.get("http://127.0.0.1:8000/api/Majors/1/")
            assert getReq.text == "{\"name\":\"Test Major 1\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))
    
    def testGetOnElementAfterPatch(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Majors/1/")
            assert req.text == "{\"name\":\"Test Major 1\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testPost(self):
        try:
            req = requests.post("http://127.0.0.1:8000/api/Majors/", data = {"name":"Test Major 2", "subject":"http://127.0.0.1:8000/api/Departments/3/"})
            getReq = requests.get("http://127.0.0.1:8000/api/Majors/2/")
            assert getReq.text == "{\"name\":\"Test Major 2\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testGetOnAllElements(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Majors/")
            assert req.text == "[{\"name\":\"Test Major 1\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"},{\"name\":\"Test Major 2\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}]"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testDelete(self):
        try:
            req = requests.delete("http://127.0.0.1:8000/api/Majors/1/")
            getReq = requests.get("http://127.0.0.1:8000/api/Majors/1/")
            assert getReq.text == "{\"detail\":\"Not found.\"}"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))

    def testGetOnAllElementsAfterDeleting(self):
        try:
            req = requests.get("http://127.0.0.1:8000/api/Majors/")
            assert req.text == "[{\"name\":\"Test Major 2\",\"subject\":\"http://127.0.0.1:8000/api/Departments/3/\"}]"
        except Exception as e:
            if req.status_code != requests.codes.ok:
                pytest.fail("Request failed with code " + str(req.status_code))
            pytest.fail("Exception: " + str(e))