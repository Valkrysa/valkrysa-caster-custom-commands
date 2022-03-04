from dragonfly import (MappingRule, BringApp, Key, Function, Grammar, Playback,
                       IntegerRef, Dictation, Choice, WaitWindow)

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.actions import Key, Text, Mouse
from castervoice.lib.merge.state.short import R

class ValkrysaGeneral(MappingRule):

    mapping = {
    "add kick": R(Key("shift:down") + Key("alt:down") + Mouse("left") + Key("shift:up") + Key("alt:up")),
    "kicker": R(Mouse("left"))
    }

def get_rule():
    return ValkrysaGeneral, RuleDetails(name="valkrysa general")
