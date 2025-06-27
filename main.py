import sys
sys.path.insert(0, 'pbp/kernel')
import kernel0d as zd
import etw
import cell


# The Part palette contains templates for Parts. There are Container Parts and Leaf Parts.
# Leaf Parts contain code in the host language (Python in this case).
# Container Parts contain a list of Part instances plus a list of connections. Part instances are created by
# calling the *_instantiate methods on templates. Connections are down/across/up/through wires between ports on Part
# instances. Usually we create Container Parts using diagrams and distill the diagrams down to JSON. Container Parts
# can also be built by hand, mimicing the JSON structure, as seen below.
#
# Every system must contain at least one top level Container that wires up the Parts making up the system. Often,
# there are many layers of Containers. Building a layered system of Containers is "easier" when done using diagrams,
# but it's possible to write the necessary JSON by hand.
#
# At the moment, down/across/up/through connection directions are encoded using integers.
# 0 => down
# 1 => up
# 2 => across
# 3 => through
# "down" means a connection from an input gate (a port on the Container) to an input port of an child part
# "up" means a connection from an output port of a child part to an output gate of its enclosing Container
# "across" means a connection from an output port of a child part to an input port of some other child part (or
#   an input port of itself (this is called feedback, which works differently than recursion, because inputs are
#   queued)
# "through" means a connection from an input gate to an output gate of of the same Container part (useful for
#   stubbing out Container parts during design and development)
# multiple connections, i.e. fan-out and fan-in, are created by adding more 1:1 connections to the list. The
# whole list of connections must be processed atomically to block other mevents from sneaking in. Atomic
# processing is straight-forward in any of the common programming languages. The only time this actually matters
# is when writing machine code on bare hardware, since CPUs allow sequencing of opcodes to be interrupted
# by sequencing of other opcodes (IRQs (not NMIs) - low-level interrupts, not Non-Maskable Interrupts). I.E. if
# you're using a standard programming language, like Python, feel free to simply ignore this issue - Python handles
# this automatically by its design.





# Top Level Container part for this project - manual version
# (this is usually built by using the diagram compiler 'das2json' and loading the .json into the kernel)
reg = zd.make_component_registry () # make an empty template palette ("registry")
top_level_container =  {
    "name": "main",
    "children": [
        {
            "name": "Editable Text Widget",
            "id": 5
        },
        {
            "name": "Cell",
            "id": 9
        }
    ],
    "connections": [
        {
            "dir": 0,
            "source_port": "",
            "target_port": "begin",
            "target": {
                "name": "Cell",
                "id": 9
            }
        },
        {
            "dir": 1,
            "source_port": "display",
            "target_port": "display",
            "source": {
                "name": "Cell",
                "id": 9
            },
            "target": {
                "name": "Editable Text Widget",
                "id": 5
            }
        },
        {
            "dir": 1,
            "source_port": "edit",
            "target_port": "edit",
            "source": {
                "name": "Editable Text Widget",
                "id": 5
            },
            "target": {
                "name": "Cell",
                "id": 9
            }
        },
        {
            "dir": 2,
            "source_port": "#",
            "target_port": "#",
            "source": {
                "name": "Editable Text Widget",
                "id": 5
            }
        },
        {
            "dir": 2,
            "source_port": "display",
            "target_port": "",
            "source": {
                "name": "Cell",
                "id": 9
            }
        },
        {
            "dir": 2,
            "source_port": "#",
            "target_port": "#",
            "source": {
                "name": "Cell",
                "id": 9
            }
        }
    ],
    "file": "etw-tester.drawio"
}

projectPath = "."
diagrams = []
[palette, env] = zd.initialize_from_files (projectPath, diagrams)
# then insert the top level Part into the palette ("registry") 
zd.register_component ( palette, zd.mkTemplate ( top_level_container ["name"], top_level_container, zd.container_instantiator))
# install widget comopnent
etw.install (palette)
cell.install (palette)
print (palette.templates.keys ())
zd.start (arg='', Part_name='main', palette=palette, env=env)

