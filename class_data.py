class Data:
    def __init__(self, 
                 role, 
                 net_sec_log_analysis_group=0, 
                 net_sec_monitoring_tool_group=0,
                 final_project_group=0):
        self.role = role
        self.net_sec_log_analysis_group = net_sec_log_analysis_group
        self.net_sec_monitoring_tool_group = net_sec_monitoring_tool_group
        self.final_project_group = final_project_group
    
class_database = {
    "FAHEEM AHMED SHAIKH": Data("professor"),
    "KATE BARRETT": Data("student", 7, 4, 3),
    "ANNA BETOVA": Data("student", 1, 2, 2),
    "KENNETH CARBONELL": Data("student", 3, 5, 4),
    "LUIS CEBALLOS": Data("student", 8, 1, 8),
    "AMANDA CLARK": Data("student", 8, 3, 5),
    "JACOB COOPER": Data("student", 2, 6, 7),
    "CHANTREL DAULTON": Data("student", 4, 5, 6),
    "ROY ESEYAN": Data("student", 3, 6, 4),
    "STACY HOLMES": Data("student", 5, 3, 5),
    "ABBAS HOSSEINI": Data("student", 2, 5, 9),
    "DANIEL LEE": Data("student", 4, 3, 8),
    "BILL LUONG": Data("student", 5, 4, 3),
    "ASHWEEN MANIMARAN": Data("student", 8, 3, 9),
    "HUMNA MURSALIN": Data("student", 6, 5, 8),
    "THONG NGUYEN": Data("student", 1, 2, 2),
    "SKYE OWENS": Data("student", 2, 6, 7),
    "CAMDEN PHAM": Data("student", 5, 2, 7),
    "LUISA ROSA SILVA": Data("student", 7, 6, 6),
    "HUGO ROSALES": Data("student", 6, 1, 1),
    "TUAN CRAINE SALLY": Data("student", 7, 4, 3),
    "ANGEL SANTOYO": Data("student", 1, 2, 2),
    "FINN THOMAS": Data("student", 6, 1, 1),
    "DARREN VAN ORDT": Data("student", 4, 6, 9),
    "KEITH WALCOTT": Data("student", 3, 1, 4),
    "DANIEL ZAMUDIO": Data("student", 9, 4, 5)
}
