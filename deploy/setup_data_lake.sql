DROP SCHEMA IF EXISTS algorand;
CREATE SCHEMA algorand;
DROP TABLE IF EXISTS algorand_data;

CREATE TABLE algorand_data (
    id SERIAL PRIMARY KEY NOT NULL,
    data JSON NOT NULL,
);
