from openpyxl import load_workbook
import webbrowser


workbook = load_workbook(filename = 'comprehensive-list.xlsx')
sheet = workbook['Sheet1']

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Suppose your URLs are in column 5, rows 2 to 30

url_column = "H"
for row in range(1, 3):
    string = url_column + str(row)
    url = sheet[string].value
    webbrowser.get(chrome_path).open(url)
