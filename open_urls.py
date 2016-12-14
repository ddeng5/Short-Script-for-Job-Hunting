from openpyxl import load_workbook
import webbrowser
import sys

workbook = load_workbook(filename = sys.argv[1])
sheet = workbook['Sheet1']

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Suppose your URLs are in column 5, rows 2 to 30

url_column = "H"
for row in range(int(sys.argv[2]), int(sys.argv[3])):
    string = url_column + str(row)
    url = sheet[string].value
    webbrowser.get(chrome_path).open(url)
