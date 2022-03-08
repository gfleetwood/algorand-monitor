DROP SCHEMA IF EXISTS data_lake;
CREATE SCHEMA data_lake;
DROP TABLE IF EXISTS algorand_data;

CREATE TABLE algorand_data (
    id SERIAL PRIMARY KEY NOT NULL,
    data JSON NOT NULL,
);
