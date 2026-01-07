def study_assistant():
    print("AI Personalized Study Assistant\n")

    subject = input("Enter subject: ")
    topic = input("Enter topic: ")
    level = input("Difficulty level (easy / medium / hard): ")
    time = input("Available study time (hours): ")

    print("\n--- Personalized Study Plan ---")
    print(f"Subject: {subject}")
    print(f"Focus Topic: {topic}")
    print(f"Difficulty Level: {level}")
    print(f"Study Time: {time} hours\n")

    print("Recommended Strategy:")
    print(f"- Review core concepts of {topic}")
    print("- Use short notes and diagrams")
    print("- Practice 5–10 questions")
    print("- Revise and self-test")

if __name__ == "__main__":
    study_assistant()
