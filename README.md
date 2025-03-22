# Python Text Correction Tool

This project implements a text correction tool in Python that utilizes the Levenshtein distance algorithm to suggest the most accurate corrections for misspelled words by comparing them against a dictionary of valid words.

## Features

- **Levenshtein Distance Calculation**: Measures the minimum number of single-character edits (insertions, deletions, or substitutions) required to transform one word into another. citeturn0search5

- **Dictionary-Based Correction**: Compares input words against a predefined dictionary to suggest the closest valid word based on the calculated edit distance.

## How It Works

1. **Levenshtein Distance Algorithm**: The core of the tool is the `StringEdit` class, which computes the Levenshtein distance between two strings. This algorithm determines how similar two words are by counting the minimum number of operations needed to convert one word into another.

2. **Correction Suggestion**: For a given input word, the tool calculates the edit distance to each word in the dictionary. The word with the smallest edit distance is suggested as the correct spelling.

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/surenkumard/Python-Text-Correction-Tool.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd Python-Text-Correction-Tool
   ```

3. **Install Dependencies**:

   Ensure you have `numpy` installed:

   ```bash
   pip install numpy
   ```

4. **Prepare the Dictionary**:

   The `dictionary.txt` file contains a list of valid words. You can customize this file by adding or removing words as needed.

5. **Run the Application**:

   Execute the `app.py` script to start the text correction tool:

   ```bash
   python app.py
   ```

6. **Input Text**:

   Enter the text you want to check. The tool will process each word, compare it against the dictionary, and suggest corrections for any misspelled words.

## Example

Suppose you input the word "exampel". The tool will calculate the edit distance between "exampel" and each word in the dictionary. If "example" has the smallest edit distance, it will be suggested as the correct spelling.

## References

- **Levenshtein Distance**: A metric for measuring the difference between two sequences. citeturn0search5

- **Python-Levenshtein Module**: A Python extension for computing string edit distances and similarities. citeturn0search3
