class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Check if the first and last characters of the sentence match
        if sentence[0] != sentence[-1]:
            return False
        
        # Iterate through the string to check word boundaries (spaces)
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                # The end of the previous word must match the start of the next word
                if sentence[i - 1] != sentence[i + 1]:
                    return False
                    
        return True