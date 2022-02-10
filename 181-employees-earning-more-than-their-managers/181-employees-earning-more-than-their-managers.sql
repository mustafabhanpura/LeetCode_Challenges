# Write your MySQL query statement below

SELECT t.name as Employee
from
(
SELECT a.id,a.name as name,a.salary as emp_salary,a.managerId,b.salary as manager_salary
from Employee a,Employee b 
where a.ManagerId = b.id) t
where t.emp_salary> t.manager_salary