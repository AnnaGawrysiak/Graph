

class VertexAlreadyExists(Exception):
    """Raised when the vertex label is already a neighbour"""
    def __init__(self, message):
        super().__init__(message)