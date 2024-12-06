from textblob import TextBlob
from language_tool_python import LanguageTool

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = LanguageTool('en-US')

    def correct_spell(self, text):
        # Correct spelling for each word in the text
        words = text.split()
        corrected_words = []
        spelling_mistakes = []  # To track spelling mistakes
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            if corrected_word != word:
                spelling_mistakes.append(word)  # Track the original misspelled word
            corrected_words.append(corrected_word)
        corrected_text = " ".join(corrected_words)
        return corrected_text, spelling_mistakes

    def correct_grammar(self, text):
        # Capitalize the first letter of the sentence if it's lowercase
        corrected_text = text[0].upper() + text[1:] if text else text
        
        # Then pass to LanguageTool for further grammar checking
        matches = self.grammar_check.check(corrected_text)
        print("Grammar Matches:", matches)  # Debugging line to show all grammar matches
        
        grammar_mistakes = []
        
        # Apply each grammar fix carefully
        for mistake in matches:
            if mistake.replacements:
                suggestion = mistake.replacements[0]
                grammar_mistakes.append({
                    'mistake': mistake.context,
                    'suggestion': suggestion
                })
                # Replace only the specific mistake part
                start_index = mistake.offset
                end_index = start_index + mistake.errorLength
                corrected_text = corrected_text[:start_index] + suggestion + corrected_text[end_index:]
        
        # Manually fix common grammar issues that might not be caught by LanguageTool
        corrected_text = corrected_text.replace(" wants", " want")  # Handling verb agreement
        
        # You can add other manual replacements or checks here if needed, like "I" at the start of the sentence
        # or any other common error patterns

        return corrected_text, grammar_mistakes


    def process_text(self, text):
        # First, correct spelling
        corrected_text, spelling_mistakes = self.correct_spell(text)
        print("After spelling correction:", corrected_text)  # Debugging line
        
        # Then, correct grammar in the corrected text
        corrected_grammar_text, grammar_mistakes = self.correct_grammar(corrected_text)
        print("After grammar correction:", corrected_grammar_text)  # Debugging line
        
        return corrected_grammar_text, grammar_mistakes, spelling_mistakes

