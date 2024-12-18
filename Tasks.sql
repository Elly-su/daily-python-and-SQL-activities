SELECT d.department_name, SUM(e.salary) AS total_payroll
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;
