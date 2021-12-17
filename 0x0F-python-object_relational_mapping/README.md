# 0x0F. Python - Object-relational mapping

## Tasks:

### 0. Get all states
Write a script that lists all states from the database hbtn_0e_0_usa.
* File: 0-select_states.py

### 1. Filter states
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
* File: 1-filter_states.py

### 2. File: 1-filter_states.py
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
* File: 2-my_filter_states.py

### 3. SQL Injection...
Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
* File: 3-my_safe_filter_states.py

### 4. Cities by states
Write a script that lists all cities from the database hbtn_0e_4_usa
* Write a script that lists all cities from the database hbtn_0e_4_usa

### 5. All cities by state
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
* File: 5-filter_cities.py

### 6. First state model
Write a python file that contains the class definition of a State and an instance Base = declarative_base():
* File: model_state.py

### 7. All states via SQLAlchemy
Write a script that lists all State objects from the database hbtn_0e_6_usa
* File: 7-model_state_fetch_all.py

### 8. First state
Write a script that prints the first State object from the database hbtn_0e_6_usa
* File: 8-model_state_fetch_first.py

### 9. Contains `a`
Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
* File: 9-model_state_filter_a.py

### 10. Get a state
Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
* File: 10-model_state_my_get.py

### 11. Add a new state
Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
* File: 11-model_state_insert.py

### 12. Update a state
Write a script that changes the name of a State object from the database hbtn_0e_6_usa
* File: 12-model_state_update_id_2.py

### 13. Delete states
Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
* File: 13-model_state_delete_a.py

### 14. Cities in state
Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.
* File: model_city.py, 14-model_city_fetch_by_state.py
