from typing import Union
from class_data import class_database
from fastapi import FastAPI, HTTPException, Query
from collections import defaultdict

app = FastAPI()

# GET /professor: Fetches the name of the class professor
@app.get("/professor")
def fetch_professor():
    for person, data in class_database.items():
        if data.role == 'professor':
            return {"professsor": person}

## GET /students: Fetches a full list of students in GBA6270
@app.get("/students")
def fetch_list_of_students():
    students = []
    for person, data in class_database.items():
        if data.role == "student":
            students.append(person)
    
    return {"students": students}


## GET /student?name={student name}: Fetches information on specific student. Mandatory query.
@app.get("/student")
def fetch_student_information(name: str = Query(..., description="Student full name, as seen in list of students, with spaces")):
    try:
        student_data = class_database[name.upper()]
        
        # If person is found in the database, but they are a professor, throw error
        if student_data.role != "student":
            raise HTTPException(status_code=404, detail="Student not found in database")
        
        return {
			name.upper():
			{
				"role": student_data.role,
				"Network Security Analysis Log Group": student_data.net_sec_log_analysis_group,
				"Network Security Monitoring Tool Group": student_data.net_sec_monitoring_tool_group,
				"Final Project Group": student_data.final_project_group
			}
		}
    except:
        # If person is not found in the database, throw error.
        raise HTTPException(status_code=404, detail="Student not found in database")
    
    
##### DATABASE FOR MONTIORING TOOL MIGHT BE INCORRECT? FIX?
@app.get("/groups")
def fetch_class_groups(name: str | None = Query(None, description="Group name query to see students in specified group")):
    if name == None:
        return {
			"Network Security Analysis Log", 
			"Network Security Monitoring Tool",
			"Final Project"
		}
    elif name.upper() == "NETWORK SECURITY ANALYSIS LOG":
        analysis_log_groups = defaultdict(list)
        
        for person, data in class_database.items():
            if data.role == "student":
                analysis_log_groups[data.net_sec_log_analysis_group].append(person)
        
        return {
			"Network Security Analysis Log Groups": dict(sorted(analysis_log_groups.items()))
		}
        
    elif name.upper() == "NETWORK SECURITY MONITORING TOOL":
        monitoring_tool_groups = defaultdict(list)
        
        for person, data in class_database.items():
            if data.role == "student":
                monitoring_tool_groups[data.net_sec_monitoring_tool_group].append(person)
                
        return {
            "Network Security Monitoring Tool Groups": dict(sorted(monitoring_tool_groups.items()))
		}
    
    elif name.upper() == "FINAL PROJECT":
        final_project_groups = defaultdict(list)
        
        for person, data in class_database.items():
            if data.role == "student":
                final_project_groups[data.final_project_group].append(person)
                
        return {
			"Final Project Groups": dict(sorted(final_project_groups.items()))
		}
   
    else:
        raise HTTPException(status_code=404, detail="Specified group name does not exist")
        
            