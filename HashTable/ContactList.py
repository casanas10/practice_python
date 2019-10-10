'''
Design a hashable class that represents contacts
- Assume each contact is a string and must be in a list
- Possible that contacts are duplicates.
'''

class ContactList:
    def __init__(self, names):
        '''
        list of strings
        :param names:
        '''
        self.names = names

    def __hash__(self):
        '''
        Conceptually we want to hash the set of names. Since the set type is mutable, it cannot be hashed
        Therefore we use frozenset. A frozen set is just an immutable version of a python set. Elements cannot be changed
        :return:
        '''
        return hash(frozenset(self.names))

    def __eq__(self, other):
        '''
        check if equal
        :param other:
        :return:
        '''
        return set(self.names) == set(other.names)

    def merge_contact_list(self, contacts):
        '''
        list of contact list
        :param contacts:
        :return:
        '''
        return list(set(contacts))

'''
Time Complexity for computing the Hash is O(n) where n is the number of strings in the contact list 
'''

