import tkinter as tk
from tkinter import messagebox
import random
import winsound
import threading


class NumberGuessingGame:

    def __init__(self, root):

        self.root = root

        # ================= WINDOW =================

        self.root.title("Number Guessing Game")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#0f172a")

        # ESC = Exit Fullscreen
        self.root.bind(
            "<Escape>",
            self.exit_fullscreen
        )

        # ================= SETTINGS =================

        self.difficulties = {
            "Easy": {
                "max_number": 50,
                "attempts": 10,
                "time": 60
            },

            "Medium": {
                "max_number": 100,
                "attempts": 7,
                "time": 45
            },

            "Hard": {
                "max_number": 500,
                "attempts": 5,
                "time": 30
            }
        }

        self.high_score = 0
        self.timer_id = None

        # ================= VARIABLES =================

        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 7
        self.time_left = 45
        self.score = 100
        self.hint_used = False
        self.game_over = False

        # ================= GUI =================

        self.create_gui()

        self.new_game()

    # ==================================================
    # FULLSCREEN
    # ==================================================

    def exit_fullscreen(self, event=None):

        self.root.attributes(
            "-fullscreen",
            False
        )

        try:
            self.root.state("zoomed")
        except:
            pass

    # ==================================================
    # SOUND SYSTEM
    # ==================================================

    def beep(self, frequency, duration):

        """
        Windows built-in sound.
        Runs in separate thread so GUI doesn't freeze.
        """

        def sound():

            try:
                winsound.Beep(
                    frequency,
                    duration
                )
            except:
                pass

        threading.Thread(
            target=sound,
            daemon=True
        ).start()

    # ==================================================
    # CLICK SOUND
    # ==================================================

    def sound_click(self):

        self.beep(
            700,
            100
        )

    # ==================================================
    # WRONG SOUND
    # ==================================================

    def sound_wrong(self):

        def sound():

            try:
                winsound.Beep(
                    350,
                    120
                )

                winsound.Beep(
                    250,
                    150
                )

            except:
                pass

        threading.Thread(
            target=sound,
            daemon=True
        ).start()

    # ==================================================
    # HINT SOUND
    # ==================================================

    def sound_hint(self):

        def sound():

            try:
                winsound.Beep(
                    700,
                    100
                )

                winsound.Beep(
                    900,
                    120
                )

            except:
                pass

        threading.Thread(
            target=sound,
            daemon=True
        ).start()

    # ==================================================
    # WIN SOUND
    # ==================================================

    def sound_win(self):

        def sound():

            try:

                winsound.Beep(
                    700,
                    120
                )

                winsound.Beep(
                    900,
                    120
                )

                winsound.Beep(
                    1100,
                    120
                )

                winsound.Beep(
                    1400,
                    250
                )

            except:
                pass

        threading.Thread(
            target=sound,
            daemon=True
        ).start()

    # ==================================================
    # GAME OVER SOUND
    # ==================================================

    def sound_gameover(self):

        def sound():

            try:

                winsound.Beep(
                    500,
                    180
                )

                winsound.Beep(
                    400,
                    180
                )

                winsound.Beep(
                    300,
                    300
                )

            except:
                pass

        threading.Thread(
            target=sound,
            daemon=True
        ).start()

    # ==================================================
    # COUNTDOWN SOUND
    # ==================================================

    def sound_countdown(self):

        self.beep(
            1000,
            120
        )

    # ==================================================
    # CREATE GUI
    # ==================================================

    def create_gui(self):

        # ================= MAIN =================

        main = tk.Frame(
            self.root,
            bg="#0f172a"
        )

        main.pack(
            fill="both",
            expand=True
        )

        # ================= TITLE =================

        tk.Label(
            main,
            text="🎯 NUMBER GUESSING GAME",
            font=("Segoe UI", 34, "bold"),
            fg="#38bdf8",
            bg="#0f172a"
        ).pack(
            pady=(40, 5)
        )

        tk.Label(
            main,
            text="Guess the secret number before your time runs out!",
            font=("Segoe UI", 13),
            fg="#94a3b8",
            bg="#0f172a"
        ).pack()

        # ================= DIFFICULTY =================

        top = tk.Frame(
            main,
            bg="#0f172a"
        )

        top.pack(
            pady=20
        )

        tk.Label(
            top,
            text="Difficulty:",
            font=("Segoe UI", 12, "bold"),
            fg="#cbd5e1",
            bg="#0f172a"
        ).pack(
            side="left"
        )

        self.difficulty = tk.StringVar(
            value="Medium"
        )

        self.difficulty_menu = tk.OptionMenu(
            top,
            self.difficulty,
            "Easy",
            "Medium",
            "Hard",
            command=self.change_difficulty
        )

        self.difficulty_menu.config(
            bg="#334155",
            fg="white",
            activebackground="#475569",
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            width=12,
            relief="flat"
        )

        self.difficulty_menu.pack(
            side="left",
            padx=10
        )

        # ================= CARD =================

        self.card = tk.Frame(
            main,
            bg="#1e293b",
            width=680,
            height=610
        )

        self.card.pack()

        self.card.pack_propagate(
            False
        )

        # ================= RANGE =================

        self.range_label = tk.Label(
            self.card,
            text="",
            font=("Segoe UI", 16, "bold"),
            fg="#e2e8f0",
            bg="#1e293b"
        )

        self.range_label.pack(
            pady=(30, 20)
        )

        # ================= STATS =================

        stats = tk.Frame(
            self.card,
            bg="#1e293b"
        )

        stats.pack()

        # Attempts

        self.attempt_box = self.create_stat_box(
            stats,
            "ATTEMPTS",
            "#38bdf8"
        )

        self.attempt_box.pack(
            side="left",
            padx=8
        )

        # Timer

        self.timer_box = self.create_stat_box(
            stats,
            "TIME",
            "#22c55e"
        )

        self.timer_box.pack(
            side="left",
            padx=8
        )

        # Score

        self.score_box = self.create_stat_box(
            stats,
            "HIGH SCORE",
            "#facc15"
        )

        self.score_box.pack(
            side="left",
            padx=8
        )

        # ================= PROGRESS =================

        self.progress = tk.Canvas(
            self.card,
            width=530,
            height=14,
            bg="#334155",
            highlightthickness=0
        )

        self.progress.pack(
            pady=25
        )

        # ================= INPUT LABEL =================

        tk.Label(
            self.card,
            text="ENTER YOUR GUESS",
            font=("Segoe UI", 10, "bold"),
            fg="#94a3b8",
            bg="#1e293b"
        ).pack()

        # ================= INPUT =================

        self.entry = tk.Entry(
            self.card,
            font=("Segoe UI", 24, "bold"),
            justify="center",
            width=12,
            bg="#0f172a",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.entry.pack(
            pady=12,
            ipady=8
        )

        self.entry.focus()

        # ================= BUTTONS =================

        buttons = tk.Frame(
            self.card,
            bg="#1e293b"
        )

        buttons.pack()

        # Guess

        self.guess_button = tk.Button(
            buttons,
            text="🎯 GUESS",
            font=("Segoe UI", 12, "bold"),
            bg="#0284c7",
            fg="white",
            activebackground="#0369a1",
            relief="flat",
            cursor="hand2",
            width=16,
            command=self.check_guess
        )

        self.guess_button.pack(
            side="left",
            padx=6,
            ipady=8
        )

        # Hint

        self.hint_button = tk.Button(
            buttons,
            text="💡 HINT",
            font=("Segoe UI", 12, "bold"),
            bg="#7c3aed",
            fg="white",
            activebackground="#6d28d9",
            relief="flat",
            cursor="hand2",
            width=16,
            command=self.show_hint
        )

        self.hint_button.pack(
            side="left",
            padx=6,
            ipady=8
        )

        # ================= RESULT =================

        self.result_label = tk.Label(
            self.card,
            text="",
            font=("Segoe UI", 13, "bold"),
            fg="white",
            bg="#1e293b",
            wraplength=500,
            justify="center"
        )

        self.result_label.pack(
            pady=20
        )

        # ================= NEW GAME =================

        tk.Button(
            self.card,
            text="🔄 NEW GAME",
            font=("Segoe UI", 11, "bold"),
            bg="#475569",
            fg="white",
            activebackground="#64748b",
            relief="flat",
            cursor="hand2",
            width=34,
            command=self.new_game
        ).pack(
            ipady=7
        )

        # ================= FOOTER =================

        tk.Label(
            main,
            text="Press ESC to exit fullscreen",
            font=("Segoe UI", 9),
            fg="#64748b",
            bg="#0f172a"
        ).pack(
            pady=12
        )

        # Enter key

        self.root.bind(
            "<Return>",
            lambda event: self.check_guess()
        )

    # ==================================================
    # STAT BOX
    # ==================================================

    def create_stat_box(
        self,
        parent,
        title,
        text_color
    ):

        box = tk.Frame(
            parent,
            bg="#334155",
            width=160,
            height=80
        )

        box.pack_propagate(
            False
        )

        tk.Label(
            box,
            text=title,
            font=("Segoe UI", 9, "bold"),
            fg="#94a3b8",
            bg="#334155"
        ).pack(
            pady=(10, 0)
        )

        label = tk.Label(
            box,
            text="0",
            font=("Segoe UI", 17, "bold"),
            fg=text_color,
            bg="#334155"
        )

        label.pack()

        # Save reference

        if title == "ATTEMPTS":

            self.attempt_label = label

        elif title == "TIME":

            self.timer_label = label

        elif title == "HIGH SCORE":

            self.score_label = label

        return box

    # ==================================================
    # DIFFICULTY
    # ==================================================

    def change_difficulty(self, value):

        self.sound_click()

        if self.timer_id:

            try:
                self.root.after_cancel(
                    self.timer_id
                )
            except:
                pass

        self.new_game()

    # ==================================================
    # NEW GAME
    # ==================================================

    def new_game(self):

        settings = self.difficulties[
            self.difficulty.get()
        ]

        self.max_number = settings[
            "max_number"
        ]

        self.max_attempts = settings[
            "attempts"
        ]

        self.time_left = settings[
            "time"
        ]

        self.secret_number = random.randint(
            1,
            self.max_number
        )

        self.attempts = 0
        self.score = 100
        self.hint_used = False
        self.game_over = False

        self.range_label.config(
            text=f"🔢 Guess a number between 1 and {self.max_number}"
        )

        self.attempt_label.config(
            text=f"0 / {self.max_attempts}"
        )

        self.timer_label.config(
            text=f"{self.time_left}s",
            fg="#22c55e"
        )

        self.score_label.config(
            text=str(self.high_score)
        )

        self.result_label.config(
            text="🚀 Make your first guess!",
            fg="white"
        )

        self.guess_button.config(
            state=tk.NORMAL
        )

        self.hint_button.config(
            state=tk.NORMAL
        )

        self.entry.config(
            state=tk.NORMAL
        )

        self.entry.delete(
            0,
            tk.END
        )

        self.entry.focus()

        self.update_progress()

        if self.timer_id:

            try:
                self.root.after_cancel(
                    self.timer_id
                )
            except:
                pass

        self.timer()

    # ==================================================
    # TIMER
    # ==================================================

    def timer(self):

        if self.game_over:
            return

        self.timer_label.config(
            text=f"{self.time_left}s"
        )

        # Last 10 seconds

        if self.time_left <= 10:

            self.timer_label.config(
                fg="#ef4444"
            )

            self.sound_countdown()

        # Last 20 seconds

        elif self.time_left <= 20:

            self.timer_label.config(
                fg="#f59e0b"
            )

        else:

            self.timer_label.config(
                fg="#22c55e"
            )

        # Time over

        if self.time_left <= 0:

            self.game_over = True

            self.guess_button.config(
                state=tk.DISABLED
            )

            self.hint_button.config(
                state=tk.DISABLED
            )

            self.entry.config(
                state=tk.DISABLED
            )

            self.result_label.config(
                text=f"⏰ TIME'S UP!\n"
                     f"The number was {self.secret_number}",
                fg="#ef4444"
            )

            self.sound_gameover()

            messagebox.showinfo(
                "TIME'S UP",
                f"Time's Up!\n\n"
                f"The number was "
                f"{self.secret_number}"
            )

            return

        self.time_left -= 1

        self.timer_id = self.root.after(
            1000,
            self.timer
        )

    # ==================================================
    # CHECK GUESS
    # ==================================================

    def check_guess(self):

        if self.game_over:
            return

        value = self.entry.get().strip()

        # Empty

        if value == "":

            self.result_label.config(
                text="❌ Enter a number!",
                fg="#f87171"
            )

            self.sound_wrong()

            return

        # Invalid

        try:

            guess = int(value)

        except ValueError:

            self.result_label.config(
                text="❌ Please enter a valid number!",
                fg="#f87171"
            )

            self.sound_wrong()

            self.entry.delete(
                0,
                tk.END
            )

            return

        # Range

        if guess < 1 or guess > self.max_number:

            self.result_label.config(
                text=f"⚠️ Enter number between "
                     f"1 and {self.max_number}!",
                fg="#fbbf24"
            )

            self.sound_wrong()

            return

        # Click sound

        self.sound_click()

        self.attempts += 1

        # Score

        self.score = max(
            0,
            100 - (self.attempts - 1) * 10
        )

        self.attempt_label.config(
            text=f"{self.attempts} / {self.max_attempts}"
        )

        self.update_progress()

        # ================= CORRECT =================

        if guess == self.secret_number:

            self.game_over = True

            final_score = (
                self.score +
                self.time_left
            )

            if self.hint_used:

                final_score -= 15

            final_score = max(
                0,
                final_score
            )

            if final_score > self.high_score:

                self.high_score = final_score

            self.score_label.config(
                text=str(self.high_score)
            )

            self.result_label.config(
                text=f"🎉 PERFECT!\n"
                     f"You found {self.secret_number}!\n"
                     f"🏆 Score: {final_score}",
                fg="#4ade80"
            )

            self.guess_button.config(
                state=tk.DISABLED
            )

            self.hint_button.config(
                state=tk.DISABLED
            )

            self.entry.config(
                state=tk.DISABLED
            )

            if self.timer_id:

                try:
                    self.root.after_cancel(
                        self.timer_id
                    )
                except:
                    pass

            self.sound_win()

            messagebox.showinfo(
                "🏆 YOU WON!",
                f"Congratulations!\n\n"
                f"Number: {self.secret_number}\n"
                f"Attempts: {self.attempts}\n"
                f"Time left: {self.time_left}s\n"
                f"Score: {final_score}"
            )

            return

        # ================= LOW =================

        if guess < self.secret_number:

            self.result_label.config(
                text="📉 TOO LOW!\n"
                     "Try a higher number.",
                fg="#38bdf8"
            )

        # ================= HIGH =================

        else:

            self.result_label.config(
                text="📈 TOO HIGH!\n"
                     "Try a lower number.",
                fg="#fb923c"
            )

        self.sound_wrong()

        # ================= GAME OVER =================

        if self.attempts >= self.max_attempts:

            self.game_over = True

            self.guess_button.config(
                state=tk.DISABLED
            )

            self.hint_button.config(
                state=tk.DISABLED
            )

            self.entry.config(
                state=tk.DISABLED
            )

            if self.timer_id:

                try:
                    self.root.after_cancel(
                        self.timer_id
                    )
                except:
                    pass

            self.result_label.config(
                text=f"😔 GAME OVER!\n"
                     f"The number was {self.secret_number}",
                fg="#ef4444"
            )

            self.sound_gameover()

            messagebox.showinfo(
                "😔 GAME OVER",
                f"Game Over!\n\n"
                f"The correct number was "
                f"{self.secret_number}"
            )

            return

        self.entry.delete(
            0,
            tk.END
        )

        self.entry.focus()

    # ==================================================
    # HINT
    # ==================================================

    def show_hint(self):

        if self.game_over:
            return

        if self.hint_used:
            return

        self.hint_used = True

        self.sound_hint()

        if self.secret_number % 2 == 0:

            parity = "EVEN"

        else:

            parity = "ODD"

        if self.secret_number <= self.max_number // 2:

            position = "FIRST HALF"

        else:

            position = "SECOND HALF"

        self.result_label.config(
            text=f"💡 HINT\n"
                 f"The number is {parity}\n"
                 f"and is in the {position}.",
            fg="#c084fc"
        )

        self.hint_button.config(
            state=tk.DISABLED
        )

    # ==================================================
    # PROGRESS
    # ==================================================

    def update_progress(self):

        self.progress.delete(
            "all"
        )

        width = 530
        height = 14

        percentage = (
            self.attempts /
            self.max_attempts
        )

        filled = int(
            width * percentage
        )

        self.progress.create_rectangle(
            0,
            0,
            filled,
            height,
            fill="#38bdf8",
            outline=""
        )


# ======================================================
# MAIN
# ======================================================

root = tk.Tk()

game = NumberGuessingGame(
    root
)

root.mainloop()
