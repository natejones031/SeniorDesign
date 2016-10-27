################################################
# Author:         Nathan Jones                 #
# Last Modified:  10/24/16                     #
# This code initializes a connection with pixy #
# and reads blocks of data and prints it.      #
# To access the fields of the struct, use the  #
# convention: blocks[index].field_name         #
# where: blocks is the pixy data,              #
# index is the block number to access,         #
# and field_name is the field to access.       #
################################################

from pixy import *
from ctypes import *

# TODO: #

# Modifies: frame
# Effects: prints block parameters to screen
def printParams():
  print 'frame %3d:' % (frame)
  frame = frame + 1
  for index in range (0,count)
    print '[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].type, blocks[index].signature, blocks[index].x, blocks[index].y, blocks[index].width, blocks[index].height)
  return;	

# initialize Pixy Interpreter thread #
pixy_init()

# Create Blocks to store pixy data # 
# c_unit represents the C unsigned int datatype #
class Blocks (Structure):
  _fields_ = [ ("type", c_uint),
    ("signature", c_uint), # color signature (0-9)
    ("x", c_uint),         # relative x coordinate
    ("y", c_uint),         # relative y coordinate
    ("width", c_uint),     # width of block detected
    ("height", c_uint),    # heighth of block detected
    ("angle", c_uint) ]    # angle of block detected
			   
number_of_blocks = 100 # number of block to read from pixy
blocks = BlockArray(number_of_blocks)
frame = 0

while 1:
  # Grab pixy dara and store in blocks) #
  count = pixy_get_blocks(100, blocks)
  if count > 0:
  # Pixy data is Found #
    printParams()
