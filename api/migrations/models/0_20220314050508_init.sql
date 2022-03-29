-- upgrade --
CREATE TABLE IF NOT EXISTS "activities" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(225) NOT NULL,
    "created_on" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "time_of" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "time_spent_min" SMALLINT NOT NULL  DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "journalentry" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(225) NOT NULL,
    "created_on" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "entry" TEXT NOT NULL,
    "health_rating" SMALLINT NOT NULL  DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "events" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(225) NOT NULL,
    "created_on" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "description" TEXT NOT NULL,
    "journal_entry_id" INT NOT NULL REFERENCES "journalentry" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "meals" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(225) NOT NULL,
    "created_on" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "nutriments" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(225) NOT NULL,
    "created_on" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "nutriment_type" VARCHAR(6) NOT NULL  DEFAULT 'Food',
    "carbs_gm" INT,
    "protein_gm" INT,
    "calories" INT,
    "sugar_gm" INT,
    "ounces" INT
);
COMMENT ON COLUMN "nutriments"."nutriment_type" IS 'Liquid: Liquid\nFood: Food';
CREATE TABLE IF NOT EXISTS "symptoms" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(225) NOT NULL,
    "created_on" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "symptoms_in_journal" (
    "journalentry_id" INT NOT NULL REFERENCES "journalentry" ("id") ON DELETE CASCADE,
    "symptoms_id" INT NOT NULL REFERENCES "symptoms" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "nutriments_in_meal" (
    "meals_id" INT NOT NULL REFERENCES "meals" ("id") ON DELETE CASCADE,
    "nutriments_id" INT NOT NULL REFERENCES "nutriments" ("id") ON DELETE CASCADE
);
