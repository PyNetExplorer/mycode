#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=3&category=17&difficulty=easy&type=multiple"

def print_questions_and_choices(data):
    for idx, result in enumerate(data.get('results', []), start=1):
        print(f"Question {idx}: {result['question']}")
        choices = result['incorrect_answers'] + [result['correct_answer']]
        print("Choices:")
        for choice_idx, choice in enumerate(choices, start=1):
            print(f"{choice_idx}. {choice}")
        print()

def main():

       response = requests.get(URL)  # Fetch data from the API
       if response.status_code == 200:  # Check if request is successful
          data = response.json()  # Convert JSON response to Python dictionary
          print_questions_and_choices(data)  # Print questions and choices
       else:
          print("Failed to fetch data from the API.")

if __name__ == "__main__":
    main()
