marks=[85,72,90,68,95]
print("ORIGINAL LISTS : ",marks)
print("\n--indexing---")

print("first mark: ",marks[0])
print ("third mark: ",marks[1])
print("last mark :",marks[-1])

print("\n---update---")
marks[1]=75
print("after changing sec mark : ",marks)

print("\n---add---")
marks.append(88)
print("after append: ",marks)

marks.insert(2,91)
print("after insert : ",marks)

print("\n---remove---")

marks.remove(68)
print("after remove (68)",marks)

removed_mark=marks.pop(2)
print("removed element : ",removed_mark)
print("after pop(2): ",marks)

print("\n--legth---")
print("no of elements : ",len(marks))

print("\n--string--")
marks.sort()
print("ascending order: ",marks)


