SELECT username
FROM users
LEFT JOIN photos
ON users.id = photos.user_id
WHERE photos.user_id is NULL;