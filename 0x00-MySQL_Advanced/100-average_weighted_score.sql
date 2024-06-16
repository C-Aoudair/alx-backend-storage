-- This script creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(score * weight) / SUM(weight)
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id
    )
    WHERE id = user_id;
END//

DELIMITER ;
