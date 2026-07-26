# Student Login System - Python

## Description
This project validates login using data from a text file.

## Skills Used
Python, File Handling, Functions, Manual Test Cases

## Test Cases
TC_01: Valid Login - Pass
TC_02: Invalid Password - Pass  
TC_03: User Not Found - Pass

 #With txt file 
## Project Workflow
1. Open the file.
2. Take the username from the user.
3. Take the password from the user.
4. Read each record from the file.
5. Separate the username and password.
6. Compare the entered credentials with the file data.
7. If a match is found, display **"Login Successful"**.
8. Otherwise, continue checking the remaining records.
9. If no match is found after checking all records, display **"Login Failed"**.

## Workflow Diagram

```text
Start
  │
  ▼
Open File
  │
  ▼
Get Username & Password
  │
  ▼
Read Next Record
  │
  ▼
Split Username & Password
  │
  ▼
Credentials Match?
 ┌───────┴────────┐
 │                │
Yes              No
 │                │
 ▼                ▼
Login        More Records?
Successful    ┌─────┴─────┐
              │           │
             Yes         No
              │           │
              ▼           ▼
      Read Next Record  Login Failed
```

# Student Login System (CSV)

## Project Workflow

1. Open the CSV file.
2. Create a CSV reader.
3. Skip the header row.
4. Take the username from the user.
5. Take the password from the user.
6. Read each row from the CSV file.
7. Separate the username and password.
8. Compare the entered credentials with the CSV data.
9. If a match is found, display **"Login Successful"**.
10. Otherwise, continue checking the remaining rows.
11. If no match is found after checking all rows, display **"Login Failed"**.

## Workflow Diagram

```text
Start
  │
  ▼
Open CSV File
  │
  ▼
Create CSV Reader
  │
  ▼
Skip Header Row
  │
  ▼
Get Username & Password
  │
  ▼
Read Next Row
  │
  ▼
Separate Username & Password
  │
  ▼
Credentials Match?
 ┌───────┴────────┐
 │                │
Yes              No
 │                │
 ▼                ▼
Login        More Rows?
Successful    ┌─────┴─────┐
              │           │
             Yes         No
              │           │
              ▼           ▼
       Read Next Row   Login Failed
```
