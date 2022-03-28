# Write your MySQL query statement below


select  distinct u.name ,  ifnull( sum(r.distance) over(partition by user_id ),0 )  as travelled_distance  from rides r right join users u
on u.id = r.user_id 
order by travelled_distance desc , name 