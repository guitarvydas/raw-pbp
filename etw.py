import sys
sys.path.insert(0, 'pbp/kernel')
import kernel0d as zd
import editabletextwidget as etw

# Editable Text Widget Part: install, instantiator, handler

def install (reg):
    # install this Leaf component template - an Editable Text Widget - into the palette of templates that could be instantiated
    zd.register_component (reg, zd.mkTemplate ( "Editable Text Widget", None, instantiator))

def instantiator (reg, owner, name, template_data, arg):
    # instantiate one, unique Editable Text Widget
    # each separate instance of Editable Text Widgets in a system will call this instantiator once to create a unique widget
    name_with_id = zd.gensymbol ("Editable Text Widget")
    widget = etw.EditableTextWidget(title=name_with_id)
    widget.display (name_with_id)
    widget.run ()
    return zd.make_leaf ( name_with_id, owner, widget, arg, handler)

def handler (eh, msg):
    # the mevent handler for Editable Text Widgets
    # the unique instance for a given widget is given by the "eh" data structure (like "self" in OO)
    if msg.port == "display":
        widget = eh.instance_data
        widget.display (msg.datum.v)
    else:
        # sending a mevent causes the mevent to be queued at on the output queue of the topmost Part that contains
        # this widget
        # in this particular case, we want to send a mevent that says that this widget was sent a mevent to a pin
        # that is undeifned and that can't be handled (we don't expect this to fire after testing, but it might fire
        # during initial design and debug, if the programmer hooked up something incorrectly)
        zd.send (eh, "#", f"{eh.name}: unrecognized mevent {zd.format_mevent (msg)}", msg)
