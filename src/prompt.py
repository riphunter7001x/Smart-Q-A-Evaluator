# Prompt template for generating a question and answer
prompt_template_for_qa = """
Generate a simple one Random question related to the topic {topic} in dictionary format. Each dictionary should contain two keys:

"question": A question text related to the topic.
"answer": A one-word or one-liner answer to the question.

Ensure that the question covers various aspects of the topic. Example topics to include might vary based on the subject but should cover a wide range of related subtopics.
"""

# Prompt template for the evaluator
prompt_template_for_eval = """
You are an expert evaluator. Below, you will find a reference question with its correct answer, as well as the user's answer. Your task is to evaluate the user's answer based on the provided criteria.

Reference Question and Answer:
Question and answer: {qa}

User's Answer:
{userAnswer}

Evaluation Criteria:
Incorrect: The answer is incorrect or unrelated to the reference.
Correct: The answer is correct and aligns with the reference, including minor misspellings.

Please provide your evaluation based on the criteria above in the following format:
Result: [Correct ✅/Incorrect ❌]

"""
# Reason: [Explanation for your evaluation in short if answer is correct/incorrect then give some short explanation]