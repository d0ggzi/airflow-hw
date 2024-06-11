INSERT INTO homework.brawl_stats
VALUES ('{{ params.player_tag }}', {{ ti.xcom_pull(task_ids="get_trophies") }},
        '{{ execution_date.strftime("%Y-%m-%d") }}')
ON CONFLICT (player_tag, date) DO
    UPDATE
        SET trophies = excluded.trophies;
