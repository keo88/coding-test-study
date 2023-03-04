WITH t0 as (
    SELECT home_id, sum(home_goal) - sum(away_goal) s
    FROM match_results
    GROUP BY home_id
), t1 as (
    SELECT away_id, sum(away_goal) - sum(home_goal) s
    FROM match_results
    GROUP BY away_id
), t2 as(
    SELECT home_id id, s goal_difference
    FROM t0
    UNION ALL
    SELECT *
    FROM t1
)
SELECT name, sum(goal_difference) goal_difference
FROM t2 natural join football_teams
GROUP BY name
ORDER BY goal_difference desc, name