# These lines that start with the # are called comments. They don't affect the way the code runs.
# In this tutorial file, I put comments above the relevant lines.

# You can skip down to the next comment, for now this is not important...

from dragonfly import (MappingRule, BringApp, Key, Function, Grammar, Playback,
                       IntegerRef, Dictation, Choice, WaitWindow)

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.actions import Key, Text, Mouse

class ValkrysaSQL(MappingRule):

    mapping = {
    "new query": Text("SELECT * ") + Key("enter") + Text("FROM ddc2_edw. ") + Key("enter") + Text("LIMIT 499; ") + Key("home,left,left"),
    'new temporary table': Text("DROP TABLE IF EXISTS ") + Key("enter") + Text("; ") + Key("enter") + Text("CREATE TEMPORARY TABLE temp_ar_ AS ") + Key("enter") + Text("; ") + Key("left,left,left,left,left,left,left"),
    'new subquery': Text(",  AS (") + Key("left,left,left,left,left"),
    'add comment': Text("/*  */") + Key("left,left,left"),
    'encode standard': Text(" ENCODE ZSTD"),
    'encode numeric': Text(" ENCODE AZ64"),
    'encode raw': Text(" ENCODE RAW"),
    'left join': Text("LEFT JOIN  ON ") + Key("left,left,left,left"),
    'right join': Text("RIGHT JOIN  ON ") + Key("left,left,left,left"),
    'inner join': Text("INNER JOIN  ON ") + Key("left,left,left,left"),
    'fun some': Text("SUM() ") + Key("left,left"),
    'fun count': Text("COUNT() ") + Key("left,left"),
    'fun count distinct': Text("COUNT(DISTINCT ) ") + Key("left,left"),
    'fun min': Text("MIN() ") + Key("left,left"),
    'fun max': Text("MAX() ") + Key("left,left"),
    'fun coalesce': Text("COALESCE(, ) ") + Key("left,left,left,left"),
    'fun greatest': Text("GREATEST(, ) ") + Key("left,left,left,left"),
    'fun least': Text("LEAST(, ) ") + Key("left,left,left,left"),
    "fun average": Text("AVG() ") + Key("left/5:2"),
    'in': Text("IN () ") + Key("left,left"),
    'not in': Text("NOT IN () ") + Key("left,left"),
    'i like': Text("ILIKE '%%' ") + Key("left,left,left"),
    'not i like': Text("NOT ILIKE '%%' ") + Key("left,left,left"),
    'from': Text("FROM "),
    'union': Text("UNION ") + Key("enter"),
    'where': Text("WHERE "),
    'lodge and': Text("AND "),
    'lodge or': Text("OR "),
    'group by': Text("GROUP BY "),
    'having': Text("HAVING  > 1 ") + Key("left,left,left,left,left"),
    'order by': Text("ORDER BY "),
    'descending': Text(" DESC "),
    'ascending': Text(" ASC "),
    'alias as': Text(" AS "),
    'limit': Text("LIMIT 499;"),
    'case statement': Text("CASE ") + Key("enter,tab") + Text("WHEN  THEN ") + Key("enter") + Text("ELSE ") + Key("enter,backspace") + Text("END AS "),
    'date key': Text("date_key"),
    'date time key': Text("date_time_key"),
    'is not null': Text(" IS NOT NULL"),
    'is null': Text(" IS NULL"),
    'distribution key': Text("DISTKEY"),
    'sort key': Text("SORTKEY()") + Key("left"),
    'variable character': Text("VARCHAR()") + Key("left")
    }

# This stuff is required too -- However you will learn more about how to change the rule types and contexts later.
def get_rule():
    return ValkrysaSQL, RuleDetails(name="valkrysa sequel")
