# Advanced Quiz Game in Python
import random

questions = [
	{
		"question": "What is the capital of France?",
		"options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
		"answer": "A"
	},
	{
		"question": "Which planet is known as the Red Planet?",
		"options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
		"answer": "B"
	},
	{
		"question": "Who wrote 'Hamlet'?",
		"options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
		"answer": "B"
	},
	{
		"question": "What is the largest ocean on Earth?",
		"options": ["A) Atlantic", "B) Indian", "C) Pacific", "D) Arctic"],
		"answer": "C"
	},
	{
		"question": "What is the chemical symbol for gold?",
		"options": ["A) Au", "B) Ag", "C) Gd", "D) Go"],
		"answer": "A"
	}
]

def run_quiz():
	print("\n--- Advanced Quiz Game ---")
	random.shuffle(questions)
	score = 0
	for idx, q in enumerate(questions, 1):
		print(f"\nQ{idx}: {q['question']}")
		for opt in q['options']:
			print(opt)
		user_ans = input("Your answer (A/B/C/D): ").strip().upper()
		if user_ans == q['answer']:
			print("Correct!")
			score += 1
		else:
			print(f"Wrong! The correct answer was {q['answer']}.")
	print(f"\nQuiz Over! Your score: {score}/{len(questions)}")
	if score == len(questions):
		print("Excellent! Perfect score!")
	elif score >= len(questions) // 2:
		print("Good job! You passed.")
	else:
		print("Better luck next time.")

if __name__ == "__main__":
	run_quiz()
