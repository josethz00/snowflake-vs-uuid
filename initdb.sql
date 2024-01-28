-- POSTGRES

CREATE TABLE IF NOT EXISTS tests_uuid (
  id UUID NOT NULL PRIMARY KEY,
  name varchar(255) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS tests_snowflake (
  id BIGINT NOT NULL PRIMARY KEY,
  name varchar(255) NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);