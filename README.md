# Example of Manual Use of PBP with Python

This example uses kernel0d.py as a microkernel to enact mevent-sending between two spreadsheet cells which depend upon one another. 

This example shows how to construct this test manually, using only Python code and not requiring the use of the DPL (Diagrammatic Programming Language). Hopefully, doing this manually will make it obvious why drawing diagrams is preferred over writing Python code manually - text is useful, but, has its limitations. We need to use both, text and diagrams.

Look at the diagram `cells.drawio` using the [drawio](https://app.diagrams.net) editor.

![test](cells.drawio.svg)

The program uses two kinds of parts 
1. Cell
2. Print.

The program instantiates 2 copies of Cell and 2 copies of Print. [Aside: we don't need to invent names for these instances, the system uses (X,Y) information to know which one is which].

The program has 2 input gates (the white rhombuses) "edit1" and "edit2". [Aside: these names come from the idea that we would want to hook up GUI widgets that send "edit" mevents in whenever a user edits the text in the widget. To keep this example simple, we don't bother to implement GUI widgets and just build the controller logic in Cell components.]

When a mevent [Aside: a mevent is just a pair of strings - a port name plus a payload string] is sent into the "edit1" gate, the mevent is sent "down" to the first Cell component on the diagram to its "edit" port [Aside: all components have ports. I use the word "Gate" to mean ports that "interface with something outside of the given diagram". Usually the things "outside" are other parts, but, at the very top level, "outside" is some other code not written in PBP form ("main.py" in this example)]. The Cell component creates 2 new mevents and shoots them out of its "display" and "edit" ports. The payload is the same in each case - it is a copy of the payload string sent in on the "edit" input port.

When the first Cell receives an "edit" input, it reacts by sending the input to 2 places: to it "display" port and to its "edit" output port. [Aside: it's OK to use the same name for an input port as for an output port, these ports are in separate namespaces - the system knows which one you mean (a part reacts to an input and sends to an output)].

The top level diagram wires up the "display" output port of the first Cell to 2 places - the "display" input port of the first Print part and to the output gate "" [aside: the empty string is the default name of a port].

So every time a mevent is first into the "edit" port of the first Cell, it gets printed on sys.stderr (see pr.py) and it gets queued up on the output gate of the top level AND, it gets sent to the "update" input port of the 2nd Cell part. The 2nd Cell reacts - at some time in the future - to the fact that it has an input on its "update" port. Looking at the code in Cell.py, we see that the reaction to an "update" mevent is to send the mevent to the "display" port (but, NOT to the "edit" port). The top level diagram wires up the "display" port to 2 places - the 2nd Print part and the output gate.

Hence, for every "edit1" mevent, we see the payload get printed twice and queued up twice on the output. Note that inputs on the "edit" port are sent to two outputs ("display" and "edit") while inputs to the "update" port are sent to only one place ("display").

Likewise, the same kind of reactions happen for every "edit2" input.

The actual mevents on "edit1" and "edit2" are injected from "the outside" in main.py.

The outputs are formatted as JSON pairs - the port name and the payload. Each part has only ONE output queue, so we need to differentiate mevents on the queue. Using only one output queue lets us store mevents in order of arrival, and, doesn't cause deadlock issues (the deadlock problem doesn't go away in general, but PBP can't trip over deadlock at a low level - the Software Architect(s) must deal with deadlock explicitly (this is a good thing - explicit is good, implicit appears to be initially easier but always causes some kind of headache, workaround, epicycle later on).

[Aside: in this simple example, the outputs at the top level just pile up, in order, since nothing is peeling outputs out of the output queue. We see this piling-up in the JSON output on the console].

[Aside: JSON output has an interesting, useful property. You can build per-project REPLs that display any (or all) of the outputs of a system, without hard-wiring this informatin into a project. FP-based outputs have no name - there is only one output in a function making it harder to figure what it means when you're poking around at the innards of a system]].

[Aside: looking at the JSON output of this test, we see `{ "" : "hello" }` which means `"hello"` sent to the default port `""`].

[Aside: the really interesting part in this test is the Cell part. The Print part was invented to help watch what is going on inside the test. Print is a throw-away part. It contains so little code that it doesn't hurt our feelings to simply toss it away when we're done with the test.]

[Aside: the system invents numeric IDs for the parts. These are arbitrary, but must be used consistently within the same Container].

# Usage
`$ make`

# Further
Even this tiny tester contains 4 part instances (2 Cells and 2 Prints) and 12 wires.

When you get tired of wiring this stuff up by hand using raw Python, explore how to generate Container parts using draw.io and das2json.

