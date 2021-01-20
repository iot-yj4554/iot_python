DROP TABLE if EXISTS addressbook;

CREATE TABLE addressbook(
	num INT AUTO_INCREMENT PRIMARY KEY,
	NAME VARCHAR(30) NOT NULL,
	phone VARCHAR(16),
	email VARCHAR(30),
	addr VARCHAR(80)
);

INSERT INTO addressbook(NAME, phone, email, addr)
SELECT CONCAT(first_name,' ',last_name), CONCAT('010-', YEAR(birth_date), '-', DATE_FORMAT(birth_date, '%m'), DATE_FORMAT(birth_date, '%d')), CONCAT(last_name, '@gmail.com'), '서울'
FROM employees;

SELECT * FROM addressbook ORDER BY NAME
LIMIT 120,20;


SELECT COUNT(*) FROM addressbook;