import pandas as pd

data = {
    "Name": [
        "Data Scientist",
        "Data Analyst",
        "Data Engineer",
        "Machine Learning Engineer",
        "Business Analyst",
        "Data Scientist",
        "Data Analyst",
        "Data Engineer",
        "Machine Learning Engineer",
        "Business Analyst",
    ],
    "Age": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    "City": [
        "New York",
        "Chicago",
        "San Francisco",
        "Los Angeles",
        "Seattle",
        "New York",
        "Chicago",
        "San Francisco",
        "Los Angeles",
        "Seattle",
    ],
}

df = pd.DataFrame(data)
