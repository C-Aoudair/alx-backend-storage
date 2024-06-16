-- This script creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE average FLOAT;
    
    SELECT SUM(score*weight)/SUM(weight) INTO average FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    UPDATE users SET average_score = average
    WHERE id = user_id;
END//

DELIMITER ;
