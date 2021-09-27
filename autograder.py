	# Autograder

# This will attempt to perform intended tasks for SortedList, using Sortables.
# For each task, the autograder will:
#  - Define some expected behavior for some use case
#  - Perform the use case
#  - Award "points" if the result is as expected
#  - Either not award points (not too bad) or cause an error (pretty bad) if the result is not as expected
#    NOTE: Exception handling here could manage these errors, but it can be helpful to see them as well!

# This is a script to do the tests and print out what's happening
def singleTest(desc, target, val, pts):
	print("AUTOGRADER: " + desc)
	print(" - Expected Value: " + str(target))
	print(" - Observed Value: " + str(val))
	score = 0
	if (val == target):
		score = 5
		pts = pts + 5
	print("POINTS: This section: " + str(score).zfill(2) + "/05 Total: " + str(pts).zfill(3) + "/100\n")	
	return pts

points = 0

print("\n --- AUTOGRADER: SORTEDNATLIST ---\n")
from sortedNatList import SortedNatList
l = SortedNatList(5)

print("\nAUTOGRADER: Singleton List Testing: 30 pts\n")
points = singleTest("Checking SortedNatList(5).size()", 1, l.size(), points)
points = singleTest("Checking SortedNatList(5).head()", 5, l.head(), points)
points = singleTest("Checking SortedNatList(5).tail()", 5, l.tail(), points)
ltest = l.insert(-1)
points = singleTest("Checking SortedNatList(5).insert(-1) == SortedNatList(5)", True, l == ltest, points)
ltest = l.insert("some string")
points = singleTest("Checking SortedNatList(5).insert(\"some string\") == SortedNatList(5)", True, l == ltest, points)
ltest = l.insert(3)
points = singleTest("Checking SortedNatList(5).insert(3) != SortedNatList(5)", False, l == ltest, points)

print("\nAUTOGRADER: Doubleton List Testing: 30 pts\n")
l = ltest
points = singleTest("Checking SortedNatList((3)->(5)).size()", 2, l.size(), points)
points = singleTest("Checking SortedNatList((3)->(5)).head()", 3, l.head(), points)
points = singleTest("Checking SortedNatList((3)->(5)).tail()", 5, l.tail(), points)
points = singleTest("Checking SortedNatList((3)->(5)).contains(3)", True, l.contains(3), points)
points = singleTest("Checking SortedNatList((3)->(5)).contains(4)", False, l.contains(4), points)
points = singleTest("Checking SortedNatList((3)->(5)).contains(5)", True, l.contains(5), points)

print("\nAUTOGRADER: Remove/Insert Doubleton Testing: 20 pts\n")
l = l.remove(5)
points = singleTest("Checking that .head == .tail after .remove(5)", True, l.head() == l.tail(), points)
l = l.insert(4)
points = singleTest("Checking that .tail == 4 after .insert(4)", 4, l.tail(), points)
points = singleTest("Checking that .head == 3 still", 3, l.head(), points)
l = l.remove(3)
points = singleTest("Checking that .head == 4 after .remove(3)", 4, l.head(), points)

print("\nAUTOGRADER: Remove/Insert General Testing: 20 pts\n")
l = SortedNatList(5)
l = l.insert(3)
l = l.insert(7)
points = singleTest("For SNL(3->5->7) .head == 3 and .tail == 7 and .contains(5)", True, l.head() == 3 and l.tail() == 7 and l.contains(5), points)
l = l.remove(5)
points = singleTest("Checking internal removal with SNL(3->5->7).remove(5).contains(5)", False, l.contains(5), points)
l = l.insert(5)
points = singleTest("Checking internal re-insertion preserves head, tail, contains", True, l.head() == 3 and l.tail() == 7 and l.contains(5), points)
l = l.remove(3)
l = l.remove(5)
l = l.remove(7)
points = singleTest("Removing all elements should give None", None, l, points)
