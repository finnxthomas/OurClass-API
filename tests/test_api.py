from fastapi.testclient import TestClient
from api.class_api import app
from tests.golden_data import golden_students

# Start the Test client for FastAPI
client = TestClient(app)

##
## Test that list of students can be retrieved and is correct
##
def test_fetch_list_of_students():

    # Call the endpoint 
    response = client.get("/students")
    
    # Assert that we received a response and data
    assert response.status_code == 200    
    student_list = response.json()
    
    # Check if response contains "students". This confirms that the proper
    # response was given
    assert "students" in student_list
    
    # Ensure list of students is as expected.
    assert student_list["students"] == golden_students
    
##
## Test that the professor name can be fetched
##
def test_fetch_professor():
    response = client.get("/professor")
    assert response.status_code == 200
    data = response.json()
    
    assert data["professor"] == "FAHEEM AHMED SHAIKH"
    
##
## Test that student data retrieved with GET /student?name={student name} is correct
##
def test_fetch_student_data():
    # Test Student Data for Finn Thomas
    response = client.get("/student?name=Finn%20Thomas")
    assert response.status_code == 200
    student_data = response.json()
    
    assert "FINN THOMAS" in student_data
    assert student_data["FINN THOMAS"]["role"] == "student"
    assert student_data["FINN THOMAS"]["Network Security Analysis Log Group"] == 6
    assert student_data["FINN THOMAS"]["Network Security Monitoring Tool Group"] == 1
    assert student_data["FINN THOMAS"]["Final Project Group"] ==  1
    
    # Test Student Data for Hugo Rosales
    response = client.get("/student?name=Hugo%20Rosales")
    assert response.status_code == 200
    student_data = response.json()
    
    assert "HUGO ROSALES" in student_data
    assert student_data["HUGO ROSALES"]["role"] == "student"
    assert student_data["HUGO ROSALES"]["Network Security Analysis Log Group"] == 6
    assert student_data["HUGO ROSALES"]["Network Security Monitoring Tool Group"] == 1
    assert student_data["HUGO ROSALES"]["Final Project Group"] ==  1
    
    
##
## Test that Group names can be fetched
##
def test_fetch_group_names():
    response = client.get("/groups")
    assert response.status_code == 200
    
    groups = response.json()
    assert "Final Project" in groups
    assert "Network Security Analysis Log" in groups
    assert "Network Security Monitoring Tool" in groups
    

##
## Test that group data with members can be fetched 
##
def test_fetch_group_data():
    
    # Test final project query
    response = client.get("groups?name=Final%20Project")
    assert response.status_code == 200
    final_group_data = response.json()
    
    assert final_group_data["Final Project Groups"]["1"] == [
		"HUGO ROSALES",
		"FINN THOMAS"
	]
    
    # Test Monitoring Tool query
    response = client.get("groups?name=Network%20Security%20Monitoring%20Tool")
    assert response.status_code == 200
    monitoring_tool_group_data = response.json()
    assert monitoring_tool_group_data["Network Security Monitoring Tool Groups"]["1"] == [
		"LUIS CEBALLOS",
		"HUGO ROSALES",
		"FINN THOMAS",
		"KEITH WALCOTT"
	]
    
    # Test Analysis Log Query
    response = client.get("groups?name=Network%20Security%20Analysis%20Log")
    assert response.status_code == 200
    analysis_log_group_data = response.json()
    assert analysis_log_group_data["Network Security Analysis Log Groups"]["6"] == [
		"HUMNA MURSALIN",
		"HUGO ROSALES",
		"FINN THOMAS"
	]
    

##
## Test Error Handing for Students
##
def test_unknown_student():
    response = client.get("/student?name=Willy Wonka")
    assert response.status_code == 404
    error = response.json()
    
    assert error["detail"] == "Student not found in database"


##
## Test Error Handing for Groups
##
def test_unknown_group():
    response = client.get("/groups?name=Midterm Group")
    assert response.status_code == 404
    error = response.json()
    
    assert error["detail"] == "Specified group name does not exist"
    