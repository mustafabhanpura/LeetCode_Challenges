# Write your MySQL query statement below

SELECT d.name as Department,
e.name as Employee,
e.salary as Salary

from Employee e, Department d

where e.departmentId = d.id
and (e.departmentId,e.salary) in
(
SELECT 
a.departmentId,
a.salary
from
(
SELECT departmentId,
salary,
DENSE_RANK() over (partition by departmentId order by salary DESC) as 
'rank'
from Employee) a
where a.rank<=3)