select r."State", count(*) from registrants r 
group by r."State" 
order by count desc