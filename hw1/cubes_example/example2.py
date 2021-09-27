from __future__ import print_function
from cubes import Workspace, Cell, PointCut
import time


# 1. Create a workspace
workspace = Workspace()
workspace.register_default_store("sql", url="mysql://root@localhost/olapdb")
workspace.import_model("model.json")

# 2. Get a browser
browser = workspace.browser("irbd_balance")

# 3. Play with aggregates
result = browser.aggregate()



#
# 4. Drill-down through two dimensions
#

print("\n"
      "Drill Down by two attributes (Sub-category and year)\n"
      "======================================================================")

result = browser.aggregate(drilldown=[("item", None, "subcategory"), ("year", None, "year")])
#
print(("%-30s%10s%10s%10s%10s\n"+"-"*70) % ("Sub-Category", "year", "Count", "Total", "Averageَ"))
#
for row in result.table_rows("item"):
    print("%-30s%10d%10d%10d%10d" % (row.record["item.subcategory_label"],
                                 row.record["year"],
                                 row.record["record_count"],
                                 row.record["amount_sum"],
                                 row.record["amount_avg"])
                              )


cut1 = PointCut("item", ["e", "cs"])
cut2 = PointCut("year", [2010])

cell = Cell(browser.cube, cuts = [cut1, cut2])

result = browser.aggregate(cell, drilldown=["item"])

print("####################################################################")

print("\n"
      "Dice by two attributes and drill down item\n"
      "============================================================")

print(("%-30s%10s%10s%10s\n"+"-"*60) % ("Line Item", "Count", "Total", "Average"))

for row in result.table_rows("item"):
    print("%-30s%10d%10d%10d" % ( row.record["item.line_item"],
                              row.record["record_count"],
                              row.record["amount_sum"],
                              row.record["amount_avg"],
                              ))


