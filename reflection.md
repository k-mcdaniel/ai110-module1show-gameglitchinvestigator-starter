# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The number was not between 1-100 and when guessing 99 it told me to go higher, but when I went to 100 it said to go lower.
  2. If I guess over 100, the hint tells me to go higher
  3. It looks like the logic is missing the Less than or Greater than check when submitting a guess
  4. If you select a New game, it does not refresh and the prompt that says you won or the game is over does not go away
  5. How the game is scored, it shouldn't be negative points, somehow the

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used Claude Code as my AI assistant
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). Claude correctly identified that the hint messages were swapped, would say Go Higher instead of Go Lower and vice versa.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). Claude listed 8 bugs total, including minor issues like the "Attempts left" counter being off by one and the info text hardcoding "1 and 100." While technically correct, this was misleading because it buried the 3 game-breaking bugs in a long list. I had to decide myself which ones actually prevented the game from working. I verified by asking Claude which bugs were game-breaking, and then focused my fixes on those first.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I used two methods: running pytest to check that automated tests passed, and verifying in the live game with streamlit run app.py. A fix wasn't considered done until both confirmed the behavior was correct.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code. I ran python -m pytest tests/test_game_logic.py -v which ran 6 tests and all passed. The most targeted was test_secret_always_compared_as_int, which called check_guess(9, 47) and expected "Too Low". The broken code would have returned "Too High" because "9" > "47" alphabetically, so this test would have failed before the fix — confirming the bug was genuinely resolved.
- Did AI help you design or understand any tests? How? Yes, Claude Code wrote the tests and explained that the existing starter tests were already broken because they compared result == "Win" directly, but check_guess returns a tuple. Claude fixed them to unpack both values first (outcome, message = check_guess(...)) so the assertions could work correctly.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
