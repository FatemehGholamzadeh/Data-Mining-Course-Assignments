from __future__ import print_function
from cubes import Workspace, Cell, PointCut

# 1. Create a workspace
workspace = Workspace()
workspace.register_default_store("sql", url="mysql://root@localhost/olapdb")
workspace.import_model("model.json")

# 2. Get a browser
browser = workspace.browser("irbd_balance")

# 3. Play with aggregates
result = browser.aggregate()

print("Total\n"
      "----------------------")

print("Record count : %8d" % result.summary["record_count"])
print("Total amount : %8d" % result.summary["amount_sum"])
print("Average amount: %8d" % result.summary["amount_avg"])
print("Standard Deviation: %8d" % result.summary["amount_std"])

#
# 4. Drill-down through a dimension
#

print("####################################################################")

print("\n"
      "Drill Down by Category (top-level Item hierarchy)\n"
      "======================================================================")

result = browser.aggregate(drilldown=["item"])
print(("%-20s%10s%10s%10s%10s\n"+"-"*70) % ("Category", "Count", "Total", "Standard Deviation", "Average"))
for row in result.table_rows("item"):
    print("%-20s%10d%10d%10d%10d" % (
                              row.record["item.category"],
                              row.record["record_count"],
                              row.record["amount_sum"],
                              row.record["amount_std"],
                              row.record["amount_avg"])
                              )


print("####################################################################")

print("\n"
      "Slice where Category = Equity\n"
      "======================================================================")

cut = PointCut("item", ["e"])
cell = Cell(browser.cube, cuts = [cut])
result = browser.aggregate(cell, drilldown=["item"])

print(("%-20s%10s%10s%10s%20s\n"+"-"*70) % ("Sub-category", "Count", "Sum", "Average", "Standard Deviation"))

for row in result.table_rows("item"):
    print("%-20s%10d%10d%10d%10d" % (
                              row.record["item.subcategory"],
                              row.record["record_count"],
                              row.record["amount_sum"],
                              row.record["amount_avg"],
                              row.record["amount_std"]
                              ))