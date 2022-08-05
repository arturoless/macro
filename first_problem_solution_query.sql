SELECT reviewers.`name`, books.title, ratings.rating, ratings.rating_date FROM ratings INNER JOIN reviewers INNER JOIN books ON
ratings.book_id = books.id AND ratings.reviewer_id = reviewers.id;