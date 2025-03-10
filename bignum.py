class BigNumber:
    def __init__(self, value: str):
        """Initializes the BigNumber with a string representation."""
        self.chunk_size = 9  # Each chunk can hold up to 10^9 digits
        self.base = 10 ** self.chunk_size
        self.chunks = self._parse_value(value)

    def _parse_value(self, value: str) -> list:
        """Parses the input string and stores it as chunks of digits."""
        value = value.lstrip('0') or '0'  # Remove leading zeros
        chunks = []
        # Process the value in reverse to split into chunk_size pieces
        for i in range(len(value), 0, -self.chunk_size):
            start = max(0, i - self.chunk_size)
            chunks.insert(0, int(value[start:i]))
        return chunks

    def display(self, group_size: int = 0, separator: str = ' ') -> str:
        """Returns the number as a formatted string with optional grouping and custom separator."""
        raw_number = ''.join(f'{chunk:09}' for chunk in self.chunks).lstrip('0') or '0'
        if group_size > 0:
            # Correctly group digits from left to right
            return separator.join([raw_number[i:i + group_size] for i in range(0, len(raw_number), group_size)])
        return raw_number

    def to_scientific(self) -> str:
        """Returns the number in scientific notation X E Y format."""
        raw_number = self.display()
        exponent = len(raw_number) - 1
        mantissa = f'{raw_number[0]}.{raw_number[1:10]}'
        return f'{mantissa} E {exponent}'

    def length(self) -> int:
        """Returns the number of digits in the BigNumber."""
        return len(self.display())

    # Basic arithmetic operations
    def add(self, other: 'BigNumber') -> 'BigNumber':
        result = int(self.display()) + int(other.display())
        return BigNumber(str(result))

    def subtract(self, other: 'BigNumber') -> 'BigNumber':
        result = int(self.display()) - int(other.display())
        return BigNumber(str(result))

    def multiply(self, other: 'BigNumber') -> 'BigNumber':
        result = int(self.display()) * int(other.display())
        return BigNumber(str(result))

    def divide(self, other: 'BigNumber') -> 'BigNumber':
        if int(other.display()) == 0:
            raise ValueError("Cannot divide by zero")
        result = int(self.display()) // int(other.display())
        return BigNumber(str(result))
