import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    #employees_first_3 = employees.head(3)
    #print(employees_first_3)
    return employees.head(3)