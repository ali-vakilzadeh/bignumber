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
        for i in range(len(value), 0, -self.chunk_size):
            start = max(0, i - self.chunk_size)
            chunks.insert(0, int(value[start:i]))
        return chunks

    def display(self, group_size: int = 0, separator: str = ' ') -> str:
        """Returns the number as a formatted string with optional grouping and custom separator."""
        raw_number = ''.join(f'{chunk:09}' for chunk in self.chunks).lstrip('0') or '0'
        if group_size > 0:
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

    # Custom arithmetic operations without external dependencies
    def add(self, other: 'BigNumber') -> 'BigNumber':
        max_len = max(len(self.chunks), len(other.chunks))
        self_chunks = [0] * (max_len - len(self.chunks)) + self.chunks
        other_chunks = [0] * (max_len - len(other.chunks)) + other.chunks
        result_chunks = []
        carry = 0
        for a, b in zip(reversed(self_chunks), reversed(other_chunks)):
            total = a + b + carry
            carry = total // self.base
            result_chunks.insert(0, total % self.base)
        if carry > 0:
            result_chunks.insert(0, carry)
        return BigNumber(''.join(f'{chunk:09}' for chunk in result_chunks).lstrip('0'))

    def subtract(self, other: 'BigNumber') -> 'BigNumber':
        if self.display() < other.display():
            raise ValueError("Subtraction would result in a negative value")
        self_chunks = self.chunks[:]
        other_chunks = [0] * (len(self_chunks) - len(other.chunks)) + other.chunks
        result_chunks = []
        borrow = 0
        for a, b in zip(reversed(self_chunks), reversed(other_chunks)):
            total = a - b - borrow
            if total < 0:
                total += self.base
                borrow = 1
            else:
                borrow = 0
            result_chunks.insert(0, total)
        return BigNumber(''.join(f'{chunk:09}' for chunk in result_chunks).lstrip('0'))

    def multiply(self, other: 'BigNumber') -> 'BigNumber':
        result = BigNumber("0")
        for i, b in enumerate(reversed(other.chunks)):
            temp = [0] * i
            carry = 0
            for a in reversed(self.chunks):
                product = a * b + carry
                carry = product // self.base
                temp.insert(0, product % self.base)
            if carry > 0:
                temp.insert(0, carry)
            result = result.add(BigNumber(''.join(f'{chunk:09}' for chunk in temp).lstrip('0')))
        return result

    def divide(self, other: 'BigNumber') -> 'BigNumber':
        if other.display() == '0':
            raise ValueError("Cannot divide by zero")
        dividend = int(self.display())
        divisor = int(other.display())
        quotient = dividend // divisor
        return BigNumber(str(quotient))


