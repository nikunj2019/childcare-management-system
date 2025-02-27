CREATE TABLE children (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    enrolled BOOLEAN DEFAULT FALSE,
    classroom VARCHAR(50)
);