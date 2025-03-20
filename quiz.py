"""
Create a Python quiz program with 5 questions and
multiple-choice answers. Display the score at the end."""


quiz_questions = [
    {"question": "What is the capital of India?", "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"], "answer": "B"},
    {"question": "Who was the first Prime Minister of India?", "options": ["A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Sardar Patel", "D. Dr. B.R. Ambedkar"], "answer": "A"},
    {"question": "Which is the national animal of India?", "options": ["A. Lion", "B. Elephant", "C. Tiger", "D. Leopard"], "answer": "C"},
    {"question": "What is the national sport of India?", "options": ["A. Cricket", "B. Hockey", "C. Kabaddi", "D. Football"], "answer": "B"},
    {"question": "Which river is considered the holiest in India?", "options": ["A. Yamuna", "B. Brahmaputra", "C. Ganges", "D. Godavari"], "answer": "C"}
]

score = 0

for index, quiz in enumerate(quiz_questions, start=1):
    print(f"\nQuestion {index}: {quiz['question']}")
    for option in quiz['options']:
        print(option)
    
    user_answer = input("Your answer (A, B, C, D): ").strip().upper()
    if user_answer == quiz['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {quiz['answer']}")

print("\nQuiz Completed!")
print(f"Your final score: {score}/5")
