CREATE SCHEMA IF NOT EXISTS homework;
CREATE TABLE IF NOT EXISTS homework.brawl_stats
(
    player_tag VARCHAR(20)     NOT NULL,
    trophies     INTEGER NOT NULL,
    date     DATE           NOT NULL,
    UNIQUE (player_tag, date)
);
