# # Write your MySQL query statement below
SELECT d.name as Department,f.name as Employee,f.salary as Salary
from
(SELECT e.name as name,e.salary as salary,t.departmentId as dept_id from
(SELECT departmentId,
MAX(salary) as highest_salary
from Employee 
Group by 1) t,Employee as e
where t.highest_salary = e.salary and t.departmentId= e.departmentId 
) f,Department d
where d.id = f.dept_id
