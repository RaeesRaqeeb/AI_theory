import pandas as pd
from pandas_profiling import ProfileReport


# Sample DataFrame
data = {
'A': [1, 2, 3, 4, None],
'B': [10.5, 20.5, None, 40.5, 50.5],
'C': ['apple', 'banana', 'apple', 'orange', 'banana']
}

df = pd.DataFrame(data)

# Generate the profile report
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

# Save the report to an HTsML file
profile.to_file("report.html")

# To display the report in a Jupyter Notebook (if you're using one)
# profile.to_notebook_iframe()
