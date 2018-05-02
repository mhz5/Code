class Solution(object):
    morse_letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        a_ascii = ord('a')
        representations = set()

        for word in words:
            rep = ''
            for c in word:
                idx = ord(c) - a_ascii
                rep += Solution.morse_letters[idx]
            representations.add(rep)

        return len(representations)

