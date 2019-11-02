import re

def strip(string, chr = '\s'):
  """ 
        Implementation of Python's Strip Method.
  
        Parameters: 
            string (String): Target string.
            chr (String): Character(s) to strip. Defaults to whitespace character.
          
        Returns: 
            String: A string with the characters stripped away. 
        """
  
  pattern = re.compile(f'(^[{chr}]*)(.+?)([{chr}]*$)')
  ret = pattern.sub(r'\2', string)
  return ret
