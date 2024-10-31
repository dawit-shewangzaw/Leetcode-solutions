class Solution:
    def countValidWords(self, sentence: str) -> int:
        # Split the sentence by spaces and filter out empty tokens
        tokens = sentence.split()
        valid_count = 0

        for token in tokens:
            if self.isValidWord(token):
                valid_count += 1

        return valid_count

    def isValidWord(self, token: str) -> bool:
        has_hyphen = False
        has_punctuation = False

        for i, ch in enumerate(token):
            if ch.isdigit():
                return False  # Invalid if it contains digits
            
            if ch == '-':
                # Invalid if there is more than one hyphen or if it is not surrounded by letters
                if has_hyphen or i == 0 or i == len(token) - 1 or not (token[i - 1].isalpha() and token[i + 1].isalpha()):
                    return False
                has_hyphen = True
            
            elif ch in "!.,":  
                # Invalid if there is more than one punctuation or if it's not at the end
                if has_punctuation or i != len(token) - 1:
                    return False
                has_punctuation = True

            elif not ch.isalpha():
                return False  # Invalid if contains other characters

        return True