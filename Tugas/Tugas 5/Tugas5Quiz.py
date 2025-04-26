import random

# Base Class: Game
class Game:
    def start(self):
        raise NotImplementedError("Subclass must implement start method")

# Parent Class: CodeCracker
class CodeCracker(Game):
    def __init__(self, name, length=3, max_attempts=6):
        self.name = name
        self.length = length
        self.max_attempts = max_attempts
        self.code = self.generate_code()
        self.attempts = 0
        self.won = False

    def generate_code(self):
        return [str(random.randint(0, 9)) for _ in range(self.length)]

    def get_feedback(self, guess):
        feedback = []
        for i in range(self.length):
            if guess[i] == self.code[i]:
                feedback.append("✔️")  # Benar posisi & angka
            elif guess[i] in self.code:
                feedback.append("~")   # Benar angka, salah posisi
            else:
                feedback.append("x")   # Salah
        return " ".join(feedback)

    def display_keypad(self):
        print("""
       ___________
      | 7 | 8 | 9 |
      | 4 | 5 | 6 |
      | 1 | 2 | 3 |
      |     0     |
       ___________
        """)

    def start(self):
        print(f"\n🕵️‍♂️ Welcome, Agent {self.name}! Crack the {self.length}-digit code!")
        print(f"You have {self.max_attempts} attempts.\n")
        self.display_keypad()

        while self.attempts < self.max_attempts and not self.won:
            guess = input(f"Attempt {self.attempts+1}: Enter your {self.length}-digit guess: ")
            if len(guess) != self.length or not guess.isdigit():
                print("❗Invalid input. Try again.\n")
                continue

            self.attempts += 1
            feedback = self.get_feedback(guess)
            print(f"🔍 Feedback: {feedback}\n")

            if list(guess) == self.code:
                self.won = True
                print(f"🎉 Code cracked in {self.attempts} attempts. Well done, Agent {self.name}!")
                break

        if not self.won:
            print(f"💣 You failed! The correct code was: {''.join(self.code)}")

# Child Class: Hard Mode
class HardMode(CodeCracker):
    def generate_code(self):
        # Unique digits only
        digits = list('0123456789')
        return random.sample(digits, self.length)

    def get_feedback(self, guess):
        # Override with more dramatic feedback
        base_feedback = super().get_feedback(guess)
        return "🧠 AI Response: " + base_feedback

# Game Menu
def menu(name):
    while True:
        print("""
    === CODE CRACKER ===
    1. Easy Mode (3-digit)
    2. Medium Mode (4-digit)
    3. Hard Mode (5-digit, no duplicate)
    """)
        choice = input("Select mode [1-3]: ")

        if choice == '1':
            game = CodeCracker(name, length=3, max_attempts=6)
        elif choice == '2':
            game = CodeCracker(name, length=4, max_attempts=7)
        elif choice == '3':
            game = HardMode(name, length=5, max_attempts=8)
        else:
            print("❗Invalid choice.")
            continue

        game.start()

        again = input("\nPlay again? (y/n): ")
        if again.lower() != 'y':
            print("👋 Thanks for playing, Agent!")
            break

# Start the game properly
name = input("Enter your agent codename: ")
print(f'hello {name}, welcome to secret code crakcer mission😎')
menu(name)

