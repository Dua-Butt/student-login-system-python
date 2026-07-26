# Student Login System (Python)

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
