DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS city;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE country (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  description TEXT
);

CREATE TABLE city (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  description TEXT,
  country_id INTEGER NOT NULL,
  FOREIGN KEY (country_id) REFERENCES country (id)
);

INSERT INTO user (username, password) VALUES ('admin', 'admin');

INSERT INTO country (name, description) VALUES (
  'United Kingdom',
  'The United Kingdom of Great Britain and Northern Ireland, commonly known as the United Kingdom (UK) or Britain, is a sovereign state in Europe.'
);
INSERT INTO country (name, description) VALUES (
  'France',
  'France, officially the French Republic, is a unitary sovereign state comprising territory in western Europe and several overseas regions and territories.'
);
INSERT INTO country (name, description) VALUES (
  'Spain',
  'Spain, officially the Kingdom of Spain, is a sovereign state located on the Iberian Peninsula in southwestern Europe.'
); 
INSERT INTO country (name, description) VALUES (
  'Germany',
  'Germany, officially the Federal Republic of Germany (German:
Bundesrepublik Deutschland), is a federal parliamentary republic in western-central Europe.'
);

INSERT INTO city (name, description, country_id)  VALUES ('London', NULL, 1);
INSERT INTO city (name, description, country_id) VALUES ('Liverpool', NULL, 1);
INSERT INTO city (name, description, country_id) VALUES ('Paris', NULL, 2);
INSERT INTO city (name, description, country_id) VALUES ('Madrid', NULL, 3);
INSERT INTO city (name, description, country_id) VALUES ('Berlin', NULL, 4);
INSERT INTO city (name, description, country_id) VALUES ('Munich', NULL, 4);
INSERT INTO city (name, description, country_id) VALUES ('Hamburg', NULL, 4);

