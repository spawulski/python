"""Context Manager."""

"""Easy file manipulation."""


class OpenFile:
    """Class that will function as a Context Manager."""

    def __init__(self, filename, mode):
        """Initialize OpenFile class."""
        self.filename = filename
        self.mode = mode

    def __enter__(self, content):
        """Manipulate content of file."""
        self.filename = open(self.filename, self.mode)
        self.filename.write(content)

    def __exit__(self):
        """Close file."""
        self.filename.close()

    def context(n, content):
        """Open, Write, and Close a file."""
        file = OpenFile(n, "w")
        file.__enter__(content)
        file.__exit__()


newFile = OpenFile("text.txt", "w")

newFile.__enter__("This is a test.")

newFile.__exit__()

OpenFile.context("test.py", "This is the content of the test.")
