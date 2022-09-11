from dragonfly import (MappingRule, BringApp, Key, Function, Grammar, Playback,
                       IntegerRef, Dictation, Choice, WaitWindow)

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.actions import Key, Text, Mouse
from castervoice.lib.merge.state.short import R

class ValkrysaUnity(MappingRule):

    mapping = {
        "unity play": R(Key("ctrl:down") + Key("p") + Key("ctrl:up")), 
        "unity hand": Key("q"), 
        "unity move": Key("w"), 
        "unity rotate": Key("e"), 
        "unity scale": Key("r"), 
        "unity save": R(Key("ctrl:down") + Key("s") + Key("ctrl:up")),
        "unity vector": Text("Vector3"),
        "create awake function": R(Text("private void Awake(){}") + Key("up") + Key("enter")),
        "create start function": R(Text("private void Start(){}") + Key("up") + Key("enter")),
        "create update function": R(Text("private void Update(){}") + Key("up") + Key("enter"))
    }

def get_rule():
    return ValkrysaUnity, RuleDetails(name="valkrysa unity")
