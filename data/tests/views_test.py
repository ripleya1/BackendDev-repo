import pytest
import requests
from os import system
import platform

# to be run at the beginning of each class
def startup():
    system("python manage.py makemigrations")
    system("python manage.py migrate --database=testing")
    system("python manage.py runserver")

# to be run at the end of each class
def end():
    try:
        if(platform.system() == "Windows"):
            system("del databases/testing.sqlite3")
        else:
            system("rm databases/testing.sqlite3")
    except Exception as e:
        print("Exception: " + e)

# NOTE: make sure the server is running before running tests!
# these tests assume that there is nothing in the database beforehand and you are running them in order
class TestDepartmentViewSet:
    startup()
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
    
    end()

class TestMajorViewSet():
    startup()

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
    
    end()