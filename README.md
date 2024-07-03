### PYTHON PDF HIGHLIGHTER SCRIPT

#### Keywords: 
The keywords list now contains the exact strings to search for, maintaining case sensitivity.
#### Search Logic: 
Directly checks if each keyword is present in the text span without converting to lowercase.
#### Highlighting Logic:
- Identifies columns to highlight (columns_to_highlight) based on the exact keyword matches.
- Identifies rows to highlight (rows_to_highlight) based on the exact keyword matches.
- Highlights rows and columns accordingly using highlight_area() function.


```
This script will  perform a case-sensitive search for the specified keywords in the PDF document. Adjustments like these ensure that the script respects the original case of each keyword as it appears in the document. Replace "your_password_here" with the actual password if the PDF is encrypted.
```
