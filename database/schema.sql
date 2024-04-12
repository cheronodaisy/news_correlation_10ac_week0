CREATE TABLE "domain" (
  "SourceCommonName" varchar PRIMARY KEY,
  "location" varchar,
  "Country" varchar
);

CREATE TABLE "articles" (
  "article_id" varchar PRIMARY KEY,
  "source_id" varchar,
  "source_name" varchar,
  "author" varchar,
  "title" varchar,
  "description" text,
  "url"  varchar,
  "url_to_image" varchar,
  "published_at" timestamp,
  "content" text,
  "category" varchar,
  "article" text,
  "title_sentiment" varchar
);

CREATE TABLE "traffic" (
  "GlobalRank" integer PRIMARY KEY,
  "domain" varchar
);

ALTER TABLE "traffic" ADD FOREIGN KEY ("domain") REFERENCES "domain" ("SourceCommonName");

ALTER TABLE "domain" ADD FOREIGN KEY ("SourceCommonName") REFERENCES "articles" ("source_name");
