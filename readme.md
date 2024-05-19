## Smart Q&A Evaluator

### Description
The Smart Q&A Evaluator is a web application that leverages generative AI to create an interactive question-and-answer experience. Users can select a topic from a dropdown menu (Geography, Health, or Sports), and the application generates a random question related to the chosen topic. Users can then input their answers, which are evaluated in real-time by the AI for accuracy and relevance.

### Features
- **Topic Selection:** Choose from three topics: Geography, Health, or Sports.
- **Dynamic Question Generation:** Generate random questions based on the selected topic using a large language model (LLM).
- **Real-time Answer Evaluation:** Evaluate user answers for correctness and relevance against model-generated answers.
- **Interactive UI:** User-friendly interface built with Streamlit.

### Technology Stack
- **Front-end:** Streamlit
- **Back-end:** Python, Large Language Model (LLM)
- **Deployment:** [Link to deployed app](https://smart-queation-answer-evaluator.streamlit.app/)



### Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/riphunter7001x/Smart-Q-A-Evaluator.git
   cd Smart-Q-A-Evaluator
   ```

2. **Create and activate a Conda environment:**
   ```sh
   conda create --name smart-q-a-evaluator python=3.10
   conda activate smart-q-a-evaluator
   ```

3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root and add your environment variables:
   ```makefile
   GROQ_API_KEY=your_groq_api_key
   ```

5. **Run the Streamlit application:**
   ```sh
   streamlit run app.py
   ```
