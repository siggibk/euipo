CREATE TABLE trademark (
	application_number VARCHAR(50) PRIMARY KEY,
	name VARCHAR(1024) DEFAULT NULL,
	type VARCHAR(20) DEFAULT NULL,
	application_language VARCHAR(2) DEFAULT NULL,
	second_language VARCHAR(2) DEFAULT NULL,
	nature VARCHAR(100) DEFAULT NULL,
	status VARCHAR(100),
	status_date TIMESTAMP,
	status_milestone INT,
	expiry_date TIMESTAMP DEFAULT NULL,
	application_date TIMESTAMP DEFAULT NULL,
	registration_date TIMESTAMP DEFAULT NULL,
	applicant_identifier VARCHAR(50) DEFAULT NULL,
	representative_identifier VARCHAR(50) DEFAULT NULL
);

CREATE TABLE design (
	design_identifier VARCHAR(50) PRIMARY KEY,
	application_number VARCHAR(50),
	indication VARCHAR(1024) DEFAULT NULL,
	original_indication VARCHAR(1024) DEFAULT NULL,
	application_language VARCHAR(2) DEFAULT NULL,
	second_language VARCHAR(2) DEFAULT NULL,
	status VARCHAR(100) DEFAULT NULL,
	renewal_status VARCHAR(100) DEFAULT NULL,
	status_date TIMESTAMP DEFAULT NULL,
	effective_date TIMESTAMP DEFAULT NULL,
	expiry_date TIMESTAMP DEFAULT NULL,
	registration_date TIMESTAMP DEFAULT NULL,
	application_date TIMESTAMP DEFAULT NULL,
	applicant_identifier VARCHAR(50) DEFAULT NULL,
	representative_identifier VARCHAR(50) DEFAULT NULL
);

CREATE TABLE trademark_class (
	id SERIAL PRIMARY KEY,
	number INT NOT NULL,
	application_number VARCHAR(50) NOT NULL,
	FOREIGN KEY (application_number)
		REFERENCES trademark (application_number)
);

CREATE TABLE trademarkclass_description (
	id SERIAL PRIMARY KEY,
	trademark_class_id INT NOT NULL,
	language VARCHAR (2),
	description TEXT,
	FOREIGN KEY (trademark_class_id)
		REFERENCES trademark_class (id)
);

CREATE INDEX ON trademark_class (application_number);

CREATE INDEX ON trademarkclass_description (trademark_class_id);
