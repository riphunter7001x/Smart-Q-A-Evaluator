from langchain_core.output_parsers import BaseOutputParser
from typing import Dict

class dictOutput(BaseOutputParser):
    def parse(self, text: str) -> Dict[str, str]:
        # Extracting the JSON part from the text
        import re
        match = re.search(r'\{[^}]+\}', text)
        if match:
            json_text = match.group(0)

            # Load the JSON data
            import json
            data = json.loads(json_text)

            # Extract the question and answer
            question = data["question"]
            answer = data["answer"]

            return {
                "question": question,
                "answer": answer
            }
        else:
            raise ValueError("No JSON object found in the input text.")
