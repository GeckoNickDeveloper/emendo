# Imports

# Implementation
class Color:
    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self.r = 0 if r < 0 else 255 if r > 255 else r
        self.g = 0 if g < 0 else 255 if g > 255 else g
        self.b = 0 if b < 0 else 255 if b > 255 else b
        
    @classmethod
    def hex(cls, hex_str: str):
        # Hex String correctness
        if hex_str.startswith("#"):
            hex_str = hex_str[1:]

        if len(hex_str) != 6:
            raise ValueError("Invalid hex color string length")

        for c in hex_str:
            if not (
                "0" <= c <= "9" or
                "a" <= c.lower() <= "f"
            ):
                raise ValueError("Invalid hex color string")
        
        # Parsing
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)
                
        return cls(r, g, b)
    
    @classmethod
    def rgb(cls, r: int, g: int, b: int):
        return cls(r, g, b)
    
    
    def stringify(self):
        r = hex(self.r)[2:].upper()
        g = hex(self.g)[2:].upper()
        b = hex(self.b)[2:].upper()
        
        return f"#{r}{g}{b}"
    
    