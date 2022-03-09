DROP SCHEMA IF EXISTS warehouse;
CREATE SCHEMA warehouse;
DROP TABLE IF EXISTS algorand_price_data;

CREATE TABLE algorand_price_data (
    id SERIAL PRIMARY KEY NOT NULL,
    price NUMERIC NOT NULL,
    updated_utc TIMESTAMP NOT NULL
);
