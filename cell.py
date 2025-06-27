import sys
sys.path.insert(0, 'pbp/kernel')
import kernel0d as zd

def install (reg):
    # install this Leaf component template into the palette of templates that could be instantiated
    zd.register_component (reg, zd.mkTemplate ( "Cell", None, instantiator))

def instantiator (reg, owner, name, template_data, arg):
    # instantiate one, unique Cell
    # each separate instance of Cells in a system will call this instantiator once to create a unique Cell part
    name_with_id = zd.gensymbol ("Cell")
    return zd.make_leaf ( name_with_id, owner, None, arg, handler)

def handler (eh, msg):
    # the mevent handler for Cells
    # the unique instance for a given Cell is given by the "eh" data structure (like "self" in OO)
    if msg.port == "begin":
        pass
    elif msg.port == "edit":
        zd.send (eh, "display", msg.datum.v, msg)
    else:
        # sending a mevent causes the mevent to be queued at on the output queue of the topmost Part that contains
        # this widget
        # in this particular case, we want to send a mevent that says that this widget was sent a mevent to a pin
        # that is undeifned and that can't be handled (we don't expect this to fire after testing, but it might fire
        # during initial design and debug, if the programmer hooked up something incorrectly)
        zd.send (eh, "#", f"{eh.name}: unrecognized mevent {zd.format_mevent (msg)}", msg)
