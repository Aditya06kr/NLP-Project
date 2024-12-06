from textblob import TextBlob
from language_tool_python import LanguageTool

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = LanguageTool('en-US')

    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        matches = self.grammar_check.check(text)

        found_mistakes = []
        corrected_text = text  # Start with the original text
        for mistake in matches:
            # Extract details of the mistake
            start = mistake.offset
            end = start + mistake.errorLength
            error_text = corrected_text[start:end]

            # Apply suggestions if available
            if mistake.replacements:
                suggestion = mistake.replacements[0]  # Take the first suggestion
                corrected_text = (
                    corrected_text[:start] + suggestion + corrected_text[end:]
                )
                # Adjust subsequent offsets due to text length changes
                for m in matches:
                    if m.offset > start:
                        m.offset += len(suggestion) - len(error_text)

            found_mistakes.append({
                'mistake': error_text,
                'rule': mistake.ruleId
            })

        found_mistakes_count = len(found_mistakes)
        return corrected_text, found_mistakes, found_mistakes_count

    def correct_text(self, text):
        # First apply spell check
        spell_corrected = self.correct_spell(text)
        # Then apply grammar correction
        grammar_corrected, mistakes, _ = self.correct_grammar(spell_corrected)
        return grammar_corrected, mistakes
