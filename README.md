# T-shirt-store---An-LLM-project
T-shirt store is a data retrieval project where the user can retrieve data  from the t-shirt database by just passing a simple question like query. It uses LLM technology.
![Screenshot 2024-06-28 110208](https://github.com/ArjunMadhyastha/T-shirt-store---An-LLM-project/assets/120244775/141bff8d-b131-43de-8f17-3b064cd79b5f)
# Steps to run the project
1. Install all the packages given in the requirements.txt file
2. Go the the terminal and navigate to the project directory
3. Use the command 'streamlit run main.py' to run the project
4. The project page will open in your favourite browser.
5. Enter any query regarding the t-shirts database to get the required output.
# Sample Questions
1.How many total t shirts are left in total in stock?
2.How many t-shirts do we have left for Nike in XS size and white color?
3.How much is the total price of the inventory for all S-size t-shirts?
4.How much sales amount will be generated if we sell all small size adidas shirts today after discounts?
# Project Structure
1.main.py: The main Streamlit application script.
2.langchain_helper.py: This has all the langchain code
3.requirements.txt: A list of required Python packages for the project.
4.few_shots.py: Contains few shot prompts
5..env: Configuration file for storing your Google API key.
