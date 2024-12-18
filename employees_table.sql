SHOW DATABASES;
USE hr_database;
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    hire_date DATE NOT NULL,
    job_id INT NOT NULL,
    salary DECIMAL(10 , 2 ),
    manager_id INT,
    department_id INT,
    status ENUM('Active', 'Inactive') DEFAULT 'Active',
    date_of_birth DATE
);
INSERT INTO employees (first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id, status, date_of_birth)
VALUES
('Timothy', 'Kamau', 'tkamau@example.com', '123-456-7890', '2021-03-15', 1, 60000.00, NULL, 1, 'Active', '1990-05-10'),
('Jane', 'Kanana', 'jkanana@example.com', '234-567-8901', '2020-07-23', 2, 75000.00, 1, 2, 'Active', '1988-08-22'),
('Emily', 'Atieno', 'eatieno@example.com', '345-678-9012', '2019-11-02', 3, 50000.00, 2, 1, 'Active', '1992-02-14'),
('Michael', 'J', 'mj@example.com', '456-789-0123', '2018-06-17', 1, 67000.00, NULL, 3, 'Active', '1985-06-06'),
('Sarah', 'Rono', 'srono@example.com', '567-890-1234', '2022-01-08', 2, 52000.00, 4, 2, 'Active', '1994-09-25'),
('David', 'Martinez', 'dmartinez@example.com', '678-901-2345', '2021-10-01', 4, 80000.00, NULL, 4, 'Active', '1987-03-11'),
('Laura', 'Kerubo', 'lkerubo@example.com', '789-012-3456', '2017-09-21', 3, 58000.00, 1, 1, 'Inactive', '1989-11-03'),
('James', 'Wilson', 'jwilson@example.com', '890-123-4567', '2019-12-19', 5, 55000.00, 6, 3, 'Active', '1991-07-29'),
('Anna', 'Williams', 'awilliams@example.com', '901-234-5678', '2022-03-30', 4, 72000.00, NULL, 2, 'Active', '1993-01-18'),
('Robert', 'Taylor', 'rtaylor@example.com', '012-345-6789', '2020-04-11', 5, 63000.00, 3, 4, 'Active', '1995-10-12');

UPDATE employees
SET email = REPLACE(email, '@example.com', '@gmail.com')
WHERE email LIKE '%@example.com';

