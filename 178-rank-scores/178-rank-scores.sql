/* Write your T-SQL query statement below */
SELECT score,
dense_rank() over (order by score DESC) as rank
from Scores;