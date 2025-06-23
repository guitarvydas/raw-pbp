# Example of Manual Use of PBP with Python

This example uses kernel0d.py as a microkernel to enact mevent-sending between two spreadsheet cells which depend upon one another. 

unfinished. For now, only guicell.py has been tested.

$ python3 guicell.py

type in a number and hit ENTER
type in another number and click to focus elsewhere.
In both cases, the dummy `send (x)` function is called. This is meant to be replaced by a `send` call to kernel0d.py.

See PBP.drawio for a rough sketch of what is intended to happen.
