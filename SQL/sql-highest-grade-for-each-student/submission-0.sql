WITH highest_scores AS (
    SELECT
        student_id,
        exam_id,
        score,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY score DESC, exam_id ASC
        ) AS ranking
    FROM exam_results
)
SELECT
    student_id,
    exam_id,
    score
FROM highest_scores
WHERE ranking = 1
ORDER BY student_id ASC;