#  File: TestLinkedList.py

#  Description: write helper methods for LinkedList

#  Student's Name: Eun Seo

#  Student's UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 04/02/2016

#  Date Last Modified: 04/02/2016


class Link(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    # initialize
    def __init__(self):
        self.first = None

    # make sure that there is __str__() function for LinkedList class
    # there should be 10 data items to a line with 2 spaces between data values
    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        st = ""
        current = self.first

        items = 0

        while (current != None):
            # add two spaces to st
            st += str(current.data) + "  "
            current = current.next
            # increment by 1 # of items
            items += 1

            # if there are 10 items, start a new line
            if (items == 10):
                # start a new line as you are done with 10 items
                st += "\n"
                # initialize # of items
                items = 0

            # return final st
        return st[0:-2]

    # get number of links
    def getNumLinks(self):
        current = self.first
        if (current == None):
            return 0
        count = 1

        while (current.next != None):
            current = current.next
            # increment count
            count = count + 1
        return count

    # Add data at the beginning of the list
    def addFirst(self, data):
        newLink = Link(data)

        newLink.next = self.first
        self.first = newLink

    # Add data at the end of a list
    def addLast(self, data):
        newLink = Link(data)

        current = self.first

        if (current == None):
            self.first = newLink
            return

        while (current.next != None):
            current = current.next
        current.next = newLink

    # Add data in an ordered list in ascending order
    # Adds new link to already sorted LinkedList in its proper place
    def addInOrder(self, data):
        newLink = Link(data)

        current = self.first

        previous = self.first

        if (current == None) or (current.data >= data):
            newLink.next = self.first
            self.first = newLink
            return

        while (current.next != None):
            if (current.data <= data):
                previous = current
                current = current.next
            else:
                newLink.next = previous.next
                previous.next = newLink
                return

        if (current.data <= data):
            current.next = newLink
        else:
            newLink.next = previous.next
            previous.next = newLink
        return

    # Search in an unordered list, return None if not found
    def findUnordered(self, data):
        current = self.first

        if (current == None):
            return None

        while (data != current.data):
            if (current.next == None):
                return None
            else:
                current = current.next

            return current

    # Search in an ordered list, return None if not found
    def findOrdered(self, data):
        current = self.first

        if (current == None):
            return None

        while (current.data != None):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    # Delete and return Link from an unordered list or None if not found
    def delete(self, data):
        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

            if (current == self.first):
                self.first = self.first.next
            else:
                previous.next = current.next

            return current

    # Copy the contents of a list and return new list
    def copyList(self):
        newList = LinkedList()
        current = self.first

        # start copying from end of the list so that when complete is a copy in the correct order
        while (current != None):
            newList.addLast(current.data)
            current = current.next

        return newList

    # Reverse the contents of a list and return new list
    def reverseList(self):
        newList = LinkedList()
        current = self.first

        # start adding data from beg of the list, so that when it reaches the end it is a reverse copy
        while (current != None):
            newList.addFirst(current.data)
            current = current.next

        return newList

    # Sort the contents of a list in ascending order and return new list
    # sorts the LINKED LIST
    def sortList(self):
        newList = LinkedList()
        current = self.first

        while (current != None):
            # add in ascending order
            newList.addInOrder(current.data)
            if (current.next != None):
                current = current.next
            else:
                break  # break out of loop when (current.next == None)

        return newList

    # Return True if a list is sorted in ascending order or False otherwise
    def isSorted(self):
        newList = LinkedList()
        current = self.first

        while (current.next != None):
            # test that list sorted in ascending order
            # test current data to next data
            if (current.data <= current.next.data):
                # if it is in order, then continue to next
                current = current.next
            # if NOT in ascending order, break out, return False
            else:
                return False

        # safe, finished traversing list and confirmed that it is in ascneding order
        # thus return True
        return True

    # Return True if a list is empty or False otherwise
    # CHECK: is list empty?
    def isEmpty(self):
        # return True if list is empty
        if (self.first == None):
            return True
        # return False if list NOT empty
        else:
            return False

    # Merge two sorted lists and return new list in ascending order
    def mergeList(self, b):
        # check if list empty
        if (self.isEmpty() == True):
            return b
        elif (b.isEmpty() == True):
            return self
        # else:
        # create a new linked list
        ll = LinkedList()

        ss = self.first
        bb = b.first
        # while both lists have not yet reached the end
        while ((ss != None) and (bb != None)):
            if (ss.data <= bb.data):
                # add self
                ll.addLast(ss.data)
                ss = ss.next
            else:  # if ss.data > bb.data
                # add b
                ll.addLast(bb.next)
                bb = bb.next

        # sort list self
        if (ss == None):
            while (bb != None):
                ll.addLast(bb.data)

                if (bb.next == None):
                    break
                # go to next link
                else:
                    bb = bb.next

        # sort list b
        if (bb == None):
            while (ss != None):
                ll.addLast(ss.data)

                if (ss.next == None):
                    break
                # go to next link
                else:
                    ss = ss.next

        # return new list in ascending order, string format
        st = ""

        # set first link as current
        current = ll.first
        while (ll != None):
            # add two spaces to st between each number
            st = st + str(current.data) + "  "
            if (current.next == None):
                break
            else:
                current = current.next  # break out of loop
        # when (ll == None), or reaches end
        # return the string
        return st[0:-2]

    # Test if two lists are equal, item by item and return True
    def isEqual(self, b):
        ss = self.first
        bb = b.first

        if ((ss == None) and (bb == None)):
            return True

        elif ((ss == None) or (bb == None)):
            return False

        else:
            while (ss.next != None) and (bb.next != None):
                if (ss.data == bb.data):
                    ss = ss.next
                    bb = bb.next
                if (ss.data != bb.data):
                    return False
                else:
                    ss = ss.next
                    bb = bb.next

            if ((ss.next != None) or (bb.next != None)):
                return False
            if (ss.data != bb.data):
                return False
            else:
                return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def removeDuplicates(self):
        newList = LinkedList()
        current = self.first

        # As you go through the old list keep a set or
        # list of all the values you meet.

        noDuplicateList = []

        # When you visit a Link check if its value exists
        # in this set or list, if it does not then
        # create a new Link with that value and
        # add it to the new LinkedList and then
        # add that value to the set or list.
        # If the value is there in the set or list then
        # go to the next Link.
        while (current != None):
            # check if value exists
            if (current.data in noDuplicateList):
                pass
            else:
                # if it does not exist, create a new link w that value
                # add this new link to the new linked list (duplicatesList)
                noDuplicateList.append(current.data)
                # then add that value to the 'old' list
                newList.addLast(current.data)
            # if current.data IN noDuplicateList
            # don't do anything

            current = current.next

        return newList


def main():
    # Test methods addFirst() and __str__() by adding more than
    # 10 items to a list and printing it.

    # ******this is Mitra's test case, block out after finished
    # testList = [56, 84, 32, 91, 27, 45, 88, 36, 19, 23, 48, 54]

    testList = [75, 23, 90, 14, 68, 12, 54, 37, 21, 88, 84, 31]
    mergeList = [13, 78, 90, 43, 48]

    testList1 = [13, 78, 90, 43, 48]
    testList2 = [75, 23, 90, 14, 68, 12, 54, 37, 21, 89, 84, 31]

    # Test method addFirst()
    print("Test method addFirst")
    list1 = LinkedList()

    for item in testList:
        list1.addFirst(item)
    print(list1)
    print()

    # Test method addLast()
    print("Test method addLast")
    # create new LinkedList object
    list2 = LinkedList()

    for item in testList:
        list2.addLast(item)
    print(list2)
    print()

    # Test method addInOrder()
    print("Test method addInOrder")

    # create new LinkedList object
    list3 = LinkedList()

    for item in testList:
        list3.addInOrder(item)
    print(list3)
    print()

    # Test method getNumLinks()
    print("Test method getNumLinks")

    list4 = LinkedList()

    for item in testList:
        list4.addLast(item)

    print(list4.getNumLinks())
    print()

    #####

    # Test method findUnordered(95)
    # Consider two cases - item is there, item is not there
    # item not there
    list5 = LinkedList()

    print("Test method findUnordered")
    print(list5.findUnordered(95) != None)
    # item there
    print(list5.findUnordered(95) == None)
    print()

    #####

    list6 = LinkedList()

    # Test method findOrdered(23) return T/F
    # Consider two cases - item is there, item is not there
    # item not there
    print("Test method findOrdered")
    print(list6.findOrdered(23) != None)
    # item there
    print(list6.findOrdered(23) == None)
    print()
    #####

    list7 = LinkedList()

    for item in testList:
        list7.addLast(item)

    print("Test method delete")
    # Consider two cases - item is there, item is not there
    # item not there
    # print("Current list")
    # print(list7)
    # print("Test method delete")
    # print("Can delete 23?")
    print(list7.delete(23) != None)
    # print(list7)
    # item thre
    # print("Can delete 23?")
    print(list7.delete(23) == None)
    # print("No, can't delete 23 b/c 23 has been deleted and it does not exist")
    # print(list7)
    print()

    #####

    list8 = LinkedList()

    for item in testList:
        list8.addInOrder(item)

    # Test method copyList()
    print("Test method copyList")
    print(list8.copyList())
    print()

    #####

    list9 = LinkedList()

    for item in testList:
        list9.addInOrder(item)

    # Test method reverseList()
    print("Test method reverseList")
    print(list9.reverseList())
    print()

    #####

    list10 = LinkedList()

    for item in testList:
        list10.addInOrder(item)

    # Test method sortList()
    print("Test method sortList")
    print(list10.sortList())
    print()

    #####

    # Test method isSorted()
    print("Test method isSorted")

    list11 = LinkedList()
    for item in testList:
        list11.addInOrder(item)
    # Consider two cases - list is sorted, list is not sorted

    print(list11.isSorted() == True)

    # print(list11)
    print(list11.isSorted() != True)
    print()

    #####

    # Test method isEmpty()
    print("Test method isEmpty")

    list12 = LinkedList()
    for item in testList:
        list12.addInOrder(item)

    print(list12.isEmpty())
    print()

    #####
    # NEED TO GO OVER MERGELIST, ISEQUAL, REMOVEDUPLICATES

    # Test method mergeList()

    list13 = LinkedList()
    for item in testList:
        list13.addInOrder(item)

    merge = LinkedList()
    for item2 in mergeList:
        merge.addInOrder(item2)

    print("Test method mergeList")
    print(list13.mergeList(merge))
    print()

    #####
    list14 = LinkedList()
    for item in testList1:
        list14.addInOrder(item)

    list15 = LinkedList()
    for item in testList2:
        list15.addInOrder(item)

    # Test method isEqual()
    print("Test method isEqual")
    # print(list14)
    # print(list15)
    # Consider two cases - lists are equal, lists are not equal
    print(list14.isEqual(list15))
    print()

    #####
    list16 = LinkedList()
    for item in testList1:
        list16.addInOrder(item)
    # print(list16)

    list16.addFirst(90)
    # print(list16)

    # Test removeDuplicates()
    print("Test removeDuplicates")
    print(list16.removeDuplicates())
    # print(list16)
    print()


main()