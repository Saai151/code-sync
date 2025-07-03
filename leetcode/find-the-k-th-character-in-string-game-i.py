class Solution:
    def kthCharacter(self, k: int) -> str:

        word = "a"
        alphabet = "abcdefghijklmnopqrstuvwxyz"


        while (len(word) <= k):
            newWord = ""
            for char in word:
                if word.index(char) == 25:
                    newWord += "a"
                newWord += alphabet[alphabet.index(char) + 1]
            word += newWord
            print(word)
        return word[k - 1]