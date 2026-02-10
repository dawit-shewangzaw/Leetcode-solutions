class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]

        transformations = set()

        for word in words:
            code = ""

            for ch in word:
                index = ord(ch) - ord('a')
                code += morse[index]

            transformations.add(code)

        return len(transformations)
