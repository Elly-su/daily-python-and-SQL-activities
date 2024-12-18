CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    manager_id INT,
    FOREIGN KEY (manager_id)
        REFERENCES employees (employee_id)
);

INSERT INTO departments (department_name, location, manager_id)
VALUES
('Human Resources', 'Building A', 1),  -- Assuming employee with ID 1 is the HR manager
('IT', 'Building B', 2),               -- Assuming employee with ID 2 is the IT manager
('Sales', 'Building C', 3),            -- Assuming employee with ID 3 is the Sales manager
('Marketing', 'Building D', 4),        -- Assuming employee with ID 4 is the Marketing manager
('Finance', 'Building E', 5);          -- Assuming employee with ID 5 is the Finance manager

SELECT * FROM departments;
