# Flashy - French to English Flashcards

## Description
Flashy is a Python-based flashcard application for learning French vocabulary. The app displays French words on the front of the card and their English translations on the back. Users can indicate whether they got the word right or wrong, and the program saves progress for future review.

## Features
- Displays flashcards with French words and their English translations.
- Automatically flips cards after 3 seconds to show the English translation.
- Tracks words the user has learned and saves unlearned words for future review in `words_to_learn.csv`.
- Uses a graphical interface powered by Tkinter.
- Includes appealing visual elements like card images and buttons.

## How to Use
1. Run the `main.py` file in your terminal or Python IDE.
2. The app will display a French word on the front of the flashcard.
3. After 3 seconds, the card flips to reveal the English translation.
4. Use the buttons:
   - ✅ to mark the word as "known" (it will be removed from future reviews).
   - ❌ to skip the word (it will remain in future reviews).
5. Progress is saved automatically in `words_to_learn.csv`.

## Requirements
- Python 3.7 or higher
- Required Libraries:
  - pandas
  - tkinter
- Ensure the following files are in the correct directories:
  - `data/french_words.csv`
  - `data/words_to_learn.csv`
  - `images/card_front.png`
  - `images/card_back.png`
  - `images/right.png`
  - `images/wrong.png`

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Zar1717/flashy.git
2. Navigate to the project folder:
   ```bash
   cd flashy
3. Install required libraries:
   ```bash
   pip install pandas
4. Run the program:
   ```bash
   python main.py



Notes:

- The app uses french_words.csv for the initial vocabulary and updates words_to_learn.csv dynamically as the user progresses.
- Ensure all images are in the images/ folder for the app to display correctly.

Future Improvements:

- Add support for additional languages.
- Include audio pronunciation for each word.
- Allow users to customize flashcards by uploading their own word lists.
