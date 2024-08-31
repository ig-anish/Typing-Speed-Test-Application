import random
import time

sentences = [
    "The cat slept peacefully on the windowsill as the rain pattered against the glass.",
    "Walking through the forest, she stumbled upon an ancient, hidden temple covered in moss.",
    "Every morning, he enjoys a cup of freshly brewed coffee while reading the newspaper.",
    "The artist captured the essence of the sunset with bold, vibrant strokes of orange and pink.",
    "Despite the chaos around him, he remained calm and focused, solving the problem with ease.",
    "The melody of the song brought back memories of summer days spent by the beach.",
    "She opened the old book, and the smell of aged paper filled the room.",
    "The children laughed and played in the park, their joy infectious to all who watched.",
    "In the distance, the mountains stood tall, their peaks covered in a blanket of snow.",
    "He whispered a secret to his friend, knowing it would be safe with him."
]

best_score = []

def run_test(sentences):
    random.shuffle(sentences)
    start_time = time.time()
    score=0
    word_count = 0

    for sentence in sentences:
        print(sentence)
        typed_sentence= input()
        words = sentence.split()
        word_count += len(words)

        if typed_sentence == sentence:
            score +=1
            print("\033[92mCorrect!\003[0m")
        else:
            print("\033[91mIncorrect.\003[0m")
    elapsed_time = time.time() - start_time
    wpm = word_count / (elapsed_time/60)
    print(f"You scored {score} out of {len(sentences)} in {elapsed_time:.2f} seconds!")
    print(f"Your WPM is {wpm:.2f}")
    best_score.append(score)

run_test(sentences)
print("\n Best scores:")
for score in best_score:
    print(score)