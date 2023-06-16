SELECT DAYNAME(created_at) as day_of_week, COUNT(*) as sum
FROM users
GROUP BY day_of_week
ORDER BY sum DESC;