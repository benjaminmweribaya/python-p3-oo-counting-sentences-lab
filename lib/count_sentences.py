class MyString:
    def __init__(self, value=''):
        # Ensure value is a string
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Value must be a string.")
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print ("The value must be a string.")

    def is_sentence(self):
        # Check if the string ends with a period
        return self._value.endswith('.')
    
    def is_question(self):
        # Check if the string ends with a question mark
        return self._value.endswith('?')

    def is_exclamation(self):
        # Check if the string ends with an exclamation mark
        return self._value.endswith('!')
    
    def count_sentences(self):
        # Normalize the string by replacing multiple punctuation marks with single periods
        import re
        # Replace `!` and `?` with `.`
        normalized = re.sub(r'[!?]', '.', self._value)
        # Split on `.`
        sentences = [sentence.strip() for sentence in normalized.split('.') if sentence.strip()]
        return len(sentences)

# Testing the class
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence())  # False
print(string.is_question())  # False
print(string.is_exclamation())  # False
print(string.count_sentences())  # 3
