# A program that runs a quiz for different european capitals. 

def european_capitals_quiz():
    # Dictionary of countries and capitals
    countries = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United Kingdom": "London",
        "Portugal": "Lisbon",
        "Netherlands": "Amsterdam",
        "Belgium": "Brussels",
        "Sweden": "Stockholm",
        "Poland": "Warsaw"
    }

    score = 0
    total_questions = len(countries)

    print("European Capitals Quiz!")
    print(f"Answer the following Capitals of {total_questions} European countries:\n")

    # Ask each question
    for country, capital in countries.items():
        user_answer = input(f"What is the capital of {country}? ")
        
        # Checks the answer 
        if user_answer.strip().lower() == capital.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The capital of {country} is {capital}.\n")

    # Displays the final results
    print("=" * 40)
    print(f"Quiz Completed!")
    print(f"Your score: {score} out of {total_questions}")
    print(f"Your percentage: {score / total_questions * 100:.1f}%")

# Run the quiz
european_capitals_quiz()

        
