class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        x = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                x += "G"
                i += 1
            elif command[i:i+2] == "()":
                
                i += 2
                x += "o"
            else:
                x += "al"
                i += 4
        return x
