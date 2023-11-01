class Piece:
    def __init__(self, color):
        self.color = color

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "K"

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "Q"

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "B"

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "N"

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "R"

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "P"