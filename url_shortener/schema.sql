DROP TABLE IF EXISTS word;
DROP TABLE IF EXISTS post;

CREATE TABLE word (
  word TEXT PRIMARY KEY,
  used INTEGER NOT NULL,
  for_url TEXT NULL
);

CREATE INDEX idx_for_url ON word (for_url);