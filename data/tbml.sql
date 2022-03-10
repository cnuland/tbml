CREATE TABLE meals (
	meal_id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
);

CREATE TYPE nutriment_type AS ENUM ('food', 'liquid');

CREATE TABLE nutriments (
	nutriment_id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
    type nutriment_type NOT NULL,
    carbs_gm NUMERIC,
    protein_gm NUMERIC,
    calories NUMERIC,
    sugar_gm NUMERIC,
    ounces NUMERIC,
);

CREATE TABLE nutriments_in_meals (
  meal_id INT NOT NULL,
  nutriment_id INT NOT NULL,
  PRIMARY KEY (meal_id, nutriment_id),
  FOREIGN KEY (meal_id)
      REFERENCES meals (meal_id),
  FOREIGN KEY (nutriment_id)
      REFERENCES nutriments (nutriment_id)
);

CREATE TABLE journal_entry (
	journal_id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
    journal_entry TEXT NOT NULL,
    health_rating SMALLINT NOT NULL,
);

CREATE TABLE events (
	event_id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
    description TEXT NOT NULL,
    journal_id INT NOT NULL,
    FOREIGN KEY (journal_id)
      REFERENCES journal_entry (journal_id),
);

CREATE TABLE symptoms (
	symptom_id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
);

CREATE TABLE symptoms_in_journal (
  journal_id INT NOT NULL,
  symptom_id INT NOT NULL,
  PRIMARY KEY (journal_id, symptom_id),
  FOREIGN KEY (journal_id)
      REFERENCES journal_entry (journal_id),
  FOREIGN KEY (symptom_id)
      REFERENCES symptoms (symptom_id)
);

CREATE TABLE activities (
	activity_id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	time_of TIMESTAMP NOT NULL,
    time_spent BIGINT NOT NULL,
    calories_burned BIGINT NOT NULL,
);