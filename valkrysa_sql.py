from dragonfly import (MappingRule, BringApp, Key, Function, Grammar, Playback,
                       IntegerRef, Dictation, Choice, WaitWindow)

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.actions import Key, Text, Mouse
from castervoice.lib.merge.state.short import R

class ValkrysaSQL(MappingRule):

    mapping = {
    "add kick": R(Key("shift:down") + Key("alt:down") + Mouse("left") + Key("shift:up") + Key("alt:up")),
    "new query":
        Text("SELECT * ") + Key("enter")
        + Text("FROM ddc2_edw. ") + Key("enter")
        + Text("LIMIT 499;")
        + Key("home,left,left"),
    'new temporary table':
        Text("DROP TABLE IF EXISTS ") + Key("enter") + Text("; ") + Key("enter")
        + Text("CREATE TEMPORARY TABLE temp_ar_ AS ") + Key("enter") + Text("; ")
        + Key("left,left,left,left,left,left,left"),
    'new table':
        Text("DROP TABLE IF EXISTS ") + Key("enter") + Text("; ") + Key("enter")
        + Text("CREATE TABLE ddc2_edw.") + Key("enter") + Text("(") + Key("enter,right,right,enter")
        + Text("SORTKEY()") + Key("enter") + Text(";")
        + Key("up,up,up,up,up,end"),
    'drop table': Text("DROP TABLE IF EXISTS ddc2_edw.") + Key("enter") + Text(";") + Key("left,left"),
    'new subquery': Text(",  AS (") + Key("left,left,left,left,left"),
    'new comment': Text("/*  */") + Key("left,left,left"),
    'new multi-line comment': Text("/*") + Key("enter"),
    'new delete': Text("DELETE FROM ") + Key("enter") + Text("WHERE  = ''") + Key("enter") + Text(";") + Key("up,up,end"),
    'encode standard': Text(" ENCODE ZSTD"),
    'encode numeric': Text(" ENCODE AZ64"),
    'encode raw': Text(" ENCODE RAW"),
    'left join': Text("LEFT JOIN  ON ") + Key("left,left,left,left"),
    'right join': Text("RIGHT JOIN  ON ") + Key("left,left,left,left"),
    'inner join': Text("INNER JOIN  ON ") + Key("left,left,left,left"),
    'fun some': Text("SUM()") + Key("left"),
    'fun count': Text("COUNT()") + Key("left"),
    'fun count distinct': Text("COUNT(DISTINCT )") + Key("left"),
    'fun len': Text("LEN()") + Key("left"),
    'fun min': Text("MIN()") + Key("left"),
    'fun max': Text("MAX()") + Key("left"),
    'fun coalesce': Text("COALESCE(, )") + Key("left,left,left"),
    'fun greatest': Text("GREATEST(, )") + Key("left,left,left"),
    'fun least': Text("LEAST(, )") + Key("left,left,left"),
    "fun average": Text("AVG()") + Key("left/5"),
    'in': Text(" IN ()") + Key("left"),
    'not in': Text(" NOT IN ()") + Key("left"),
    'i like': Text(" ILIKE '%%'") + Key("left,left"),
    'not i like': Text(" NOT ILIKE '%%'") + Key("left,left"),
    'from': Text("FROM "),
    'union': Text("UNION ") + Key("enter"),
    'where': Text("WHERE "),
    'group by': Text("GROUP BY "),
    'group by one': Text("GROUP BY 1"),
    'group by two': Text("GROUP BY 1, 2"),
    'group by three': Text("GROUP BY 1, 2, 3"),
    'group by four': Text("GROUP BY 1, 2, 3, 4"),
    'group by five': Text("GROUP BY 1, 2, 3, 4, 5"),
    'group by six': Text("GROUP BY 1, 2, 3, 4, 5, 6"),
    'group by seven': Text("GROUP BY 1, 2, 3, 4, 5, 6, 7"),
    'group by eight': Text("GROUP BY 1, 2, 3, 4, 5, 6, 7, 8"),
    'group by nine': Text("GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9"),
    'group by ten': Text("GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"),
    'having': Text("HAVING  > 1 ") + Key("left,left,left,left,left"),
    'order by': Text("ORDER BY "),
    'order by one': Text("ORDER BY 1"),
    'order by two': Text("ORDER BY 1, 2"),
    'order by three': Text("ORDER BY 1, 2, 3"),
    'order by four': Text("ORDER BY 1, 2, 3, 4"),
    'order by five': Text("ORDER BY 1, 2, 3, 4, 5"),
    'order by six': Text("ORDER BY 1, 2, 3, 4, 5, 6"),
    'order by seven': Text("ORDER BY 1, 2, 3, 4, 5, 6, 7"),
    'order by eight': Text("ORDER BY 1, 2, 3, 4, 5, 6, 7, 8"),
    'order by nine': Text("ORDER BY 1, 2, 3, 4, 5, 6, 7, 8, 9"),
    'order by ten': Text("ORDER BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"),
    'descending': Text(" DESC"),
    'ascending': Text(" ASC"),
    'alias as': Text(" AS "),
    'limit': Text("LIMIT 499;"),
    'case statement': Text("CASE ") + Key("enter,tab") + Text("WHEN  THEN ") + Key("enter") + Text("ELSE ") + Key("enter,backspace") + Text("END AS "),
    'inline case statement': Text("CASE WHEN  =  THEN  END") + Key("left:13"),
    'date key': Text("date_key"),
    'date time key': Text("date_time_key"),
    'is not null': Text(" IS NOT NULL"),
    'is null': Text(" IS NULL"),
    'between dates': Text(" BETWEEN '202--' AND '202--'") + Key("left:8"),
    'distribution key': Text("DISTKEY"),
    'sort key': Text("SORTKEY()") + Key("left"),
    'variable character': Text("VARCHAR()") + Key("left"),
    'new cte': Text("WITH  AS (") + Key("enter") + Key("left,left,left,left,left,left"),
    'another cte': Text(", (") + Key("enter") + Key("left,left,left"),
    'equals blank': Text(" = ''") + Key("left"),
    'not equals blank': Text(" != ''") + Key("left"),
    'greater than blank': Text(" > ''") + Key("left"),
    'greater than equals blank': Text(" >= ''") + Key("left"),
    'less than blank': Text(" < ''") + Key("left"),
    'less than equals blank': Text(" <= ''") + Key("left")
    }

def get_rule():
    return ValkrysaSQL, RuleDetails(name="valkrysa sequel")
