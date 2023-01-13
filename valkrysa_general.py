from dragonfly import (MappingRule, BringApp, Key, Function, Grammar, Playback,
                       IntegerRef, Dictation, Choice, WaitWindow)

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.actions import Key, Text, Mouse
from castervoice.lib.merge.state.short import R

class ValkrysaGeneral(MappingRule):

    mapping = {
    "pop": R(Mouse("left")),
    "select address bar": R(Key("ctrl:down") + Key("l") + Key("ctrl:up"))
    }

def get_rule():
    return ValkrysaGeneral, RuleDetails(name="valkrysa general")
