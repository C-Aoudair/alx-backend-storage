-- This script creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    UPDATE users
    JOIN (
	SELECT corrections.user_id,
            SUM(score * weight) / SUM(weight) AS weighted_avg
	FROM corrections
	JOIN projects ON corrections.project_id = projects.id
	GROUP BY corrections.user_id
    ) AS avg_scores ON users.id = avg_scores.user_id
    SET users.average_score = avg_scores.weighted_avg;
END//

DELIMITER ;
