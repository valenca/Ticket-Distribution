-- -----------------------------------------------------
-- TICKETS
-- -----------------------------------------------------

-- Número de bilhetes vendidos por ano e por tipo
SELECT
	YEAR(t_date) AS 'Year',
	t_type AS 'Ticket Type',
	COUNT(*) AS 'Number of Sales'
FROM
	tickets
GROUP BY
	1,
	2
ORDER BY
	1,
	2
;

-- Listagem das lojas mais usadas na venda de bilhetes
SELECT
	t_store AS 'Store',
	COUNT(*) AS 'Number of Sales'
FROM
	tickets
GROUP BY
	1
ORDER BY
	2 DESC,
	1
;

-- -----------------------------------------------------
-- DEPOSITS
-- -----------------------------------------------------

-- Quanto dinheiro fizeram por mês em depósitos
SELECT
	CONCAT(YEAR(d_date), ' - ', MONTHNAME(d_date)) AS 'Date',
	ROUND(SUM(d_value),2) AS 'Gain in Deposits'
FROM
	deposits
GROUP BY
	1
ORDER BY
	1
;

-- Quantos depósitos foram feitos por mês
SELECT
	CONCAT(YEAR(d_date), ' - ', MONTHNAME(d_date)) AS 'Date',
	COUNT(*) AS 'Number of Deposits'
FROM
	deposits
GROUP BY
	1
ORDER BY
	1
;

-- Listagem das lojas e máquinas mais usadas no depósito de viagens
SELECT
	d_location AS 'Location',
	COUNT(*) AS 'Number of Deposits'
FROM
	deposits
GROUP BY
	1
ORDER BY
	2 DESC,
	1
;

-- -----------------------------------------------------
-- VALIDATIONS
-- -----------------------------------------------------

-- Percentagem de validações por tipo de transporte
SELECT
	totals.type AS 'Transport Type',
	CONCAT(ROUND(totals.total/total.total*100,2),' %') AS 'Validations Percentage'
FROM
	(SELECT
		COUNT(*) AS total
	FROM
		validations
	) AS total,
	(SELECT
		v_company AS type,
		COUNT(*) AS total
	FROM
		validations
	GROUP BY
		1
	ORDER BY
		2 DESC
	) AS totals
;

-- Número de validações por dia
SELECT
	CONCAT(DATE(v_date), ' - ', DAYNAME(DATE(v_date))) as 'Day',
	COUNT(*) AS 'Number of Validations'
FROM
	validations
GROUP BY
	1
ORDER BY
	1,
	2
;

-- Listagem dos transportes mais usados
SELECT
	v_transport AS 'Transport',
	COUNT(*) AS 'Number of Validations'
FROM
	validations
GROUP BY
	1
ORDER BY
	2 DESC,
	1
;

-- -----------------------------------------------------
-- TICKETS & DEPOSITS
-- -----------------------------------------------------

-- Número total de viagens carregadas, lozalização mais usada e tipo de bilhete por pessoa
SELECT
	t_person AS 'Person',
	t_type AS 'Ticket Type',
	SUM(d_trips) AS 'Total Trips',
	frequencies.location AS 'Most Used Location'
FROM
	tickets,
	deposits,
	(SELECT
		locations.id AS id,
		locations.location AS location
	FROM
		(SELECT
			d_t_id AS id,
			d_location AS location,
			count(d_location)
		FROM
			deposits
		GROUP BY
			1,2
		ORDER BY
			3 DESC
		) AS locations
	GROUP BY
		1
	ORDER BY
		1
	) AS frequencies
WHERE
	t_id = d_t_id AND
	t_id = frequencies.id
GROUP BY
	t_id
ORDER BY
	t_id
;

-- -----------------------------------------------------
-- TICKETS & VALIDATIONS
-- -----------------------------------------------------

-- Percentagem de validações por tipo de transporte e por tipo de bilhete
SELECT
	totals.type AS 'Ticket Type',
	totals.company AS 'Transport Type',
	CONCAT(ROUND(totals.total/total.total*100,2),' %') AS 'Validations Percentage per Ticket Type'
FROM
	(SELECT
		types.type,
		COUNT(*) AS total
	FROM
		(SELECT
			t_type AS type,
			v_company AS company
		FROM
			tickets JOIN validations
		WHERE
			t_id = v_t_id
		) AS types
	GROUP BY
		1
	) AS total,
	(SELECT
		types.type,
		types.company,
		COUNT(*) AS total
	FROM
		(SELECT
			t_type AS type,
			v_company AS company
		FROM
			tickets JOIN validations
		WHERE
			t_id = v_t_id
		) AS types
	GROUP BY
		1,
		2
	) AS totals
WHERE
	total.type = totals.type
GROUP BY
	1,
	2
ORDER BY
	1,
	2,
	3
;

-- -----------------------------------------------------
-- DEPOSITS & VALIDATIONS
-- -----------------------------------------------------

-- Número de validações por depósito por pessoa
SELECT
	d_t_id AS 'Person',
	ROUND(validation.total/deposit.total,2) AS 'Validations per Deposit'
FROM
	deposits,
	(SELECT
		d_t_id AS id,
		count(*) AS total
	FROM
		deposits
	GROUP BY
		1
	) AS deposit,
	(SELECT
		v_t_id AS id,
		count(*) AS total
	FROM
		validations
	GROUP BY
		1
	) AS validation
WHERE
	d_t_id = deposit.id AND
	d_t_id = validation.id
GROUP BY
	1
ORDER BY
	1
;

-- -----------------------------------------------------
-- TICKETS & DEPOSITS & VALIDATIONS
-- -----------------------------------------------------

-- Toda a informação relativa a uma pessoa
SELECT
	tickets.person AS 'Person',
	tickets.type AS 'Ticket Type',
	tickets.trips AS 'Trips Left',
	deposits.total AS 'Total Deposits',
	deposits.sum_trips AS 'Total Trips Deposited',
	deposits.sum_value AS 'Total Money Deposited',
	IFNULL(validations.total,0) AS 'Total Validations',
	CONCAT(IFNULL(validations.bus,0.00), ' %') AS 'Bus Usage',
	CONCAT(IFNULL(validations.subway,0.00), ' %') AS 'Subway Usage',
	CONCAT(IFNULL(validations.train,0.00), ' %') AS 'Train Usage'
FROM
	(SELECT
		t_id AS id,
		t_person AS person,
		t_type AS type,
		t_trips AS trips
	FROM
		tickets
	) AS tickets LEFT JOIN
	(SELECT
		d_t_id AS id,
		COUNT(*) AS total,
		SUM(d_trips) AS sum_trips,
		ROUND(SUM(d_value),2) AS sum_value
	FROM
		deposits
	GROUP BY
		1
	) AS deposits ON tickets.id = deposits.id LEFT JOIN
	(SELECT 
		v_t_id AS id, 
		COUNT(*) AS total,
		ROUND(AVG(v_company = 'bus')*100,2) AS bus,
		ROUND(AVG(v_company = 'subway')*100,2) AS subway,
		ROUND(AVG(v_company = 'train')*100,2) AS train
	FROM 
		validations
	GROUP BY
		1
	) AS validations ON tickets.id = validations.id
ORDER BY
	tickets.id
;
