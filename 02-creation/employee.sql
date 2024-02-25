CREATE TABLE IF NOT EXISTS department(
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS employee(
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	chief INTEGER REFERENCES additional.employee(id)
);

CREATE TABLE IF NOT EXISTS EmployeeDepartment(
	employee_id INTEGER REFERENCES additional.employee(id),
	department_id INTEGER REFERENCES additional.department(id),
	CONSTRAINT pk PRIMARY KEY (employee_id, department_id)
);