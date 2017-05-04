#!/usr/bin/env python3

# Wesley Stutzman
# 3/8/2017
# Algorithams in python
# Double Linked List


# This calss is designed to handle the nodes inside the linked list
class Node:
  # Default constructor fot the link nodes
  # Set link data on call or leave it all empty
  def __init__(self, in_head = None, in_tail = None, in_data = None):
    self.head = in_head
    self.tail = in_tail
    self.data = in_data

  # The folowing methods are used to set node data
  def set_head(self, in_head):
    self.head = in_head
  def set_tail(self, in_tain):
    self.tail = in_tail
  def set_data(self, in_data):
    self.data = in_data
  # The folowing functions are used to get node data
  def get_head(self):
    return self.head
  def get_tail(self):
    return self.tail
  def get_data(self):
    return self.data
  def __str__(self):
    return str(self.data)

# The folowing calss is used to handle creating the linked list
class Dll:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = int(0)
  # Add items to the front of the list
  def add_front(self, data):
    # Default set next node to nothing
    next_node = None
    # If there is a head set it to your next node
    if self.head != None:
      next_node = self.head
    # Create a new head with the current data and the last head as next node
    self.head = Node(None, next_node, data)
    # If there was no head then there is no tail so set one
    # Set the newly created head to the tail as well
    if next_node != None:
      self.tail = self.head
    # Always add one to the seize
    self.size = self.size + 1
  # Same as adding to head but with the tail
  def add_rear(self, data):
    next_node = None
    if self.tail != None:
      next_none = self.tail
    self.tail = Node(next_node, None, data)
    if next_node != None:
      self.head = self.tail
    self.size = self.size + 1
  # Remove a the front of the list
  # Save the value in the node to return at the end
  # Set the head to the node behind it with the tail
  # Decrease the size by 1
  # Return the data pulled from the node
  def remove_front(self):
    return_value = self.head.get_data()
    self.head = self.head.get_tail()
    self.size = self.size - 1
    return return_value
  # Same as above
  def remove_rear(self):
    return_value = self.tail.get_data()
    self.tail = self.tail.get_head()
    self.size = self.size - 1
    return return_value
  # If the size is 0 return true else false
  def is_empty(self):
    return self.size == 0
  # Return the current size of the list
  def size(self):
    return self.size
  # Return the data from the front of the list
  def peek_front(self):
    return self.head.get_data()
  # Return the data from the end of the list
  def peek_rear(self):
    return self.tail.get_data()

if __name__ == "__main__":
  link = Dll()
  link.add_front(5)
  link.add_front(10)
  link.add_rear(12)
  print(link.peek_rear())
  print(link.peek_front())
  link.remove_front()
  link.remove_rear()
  print(link.peek_front()) 
