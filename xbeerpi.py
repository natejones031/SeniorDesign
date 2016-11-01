#########################################
# Opens communication with USB port and #
# writes/reads to/from port             #
#########################################

# To list connections with USB ports, use:
# $ lsusb

import serial

# Connects to USB port on RPI #
ser = serial.Serial('/dev/ttyUSB0',9600)
str = 'Hello from RPI'     # string to send
print 'Sending "%s"' % str # print to console on RPI
ser.write('%s\n' % str)    # writes to connected USB port

# Writes/reads to and from port #
while True:
  incoming = ser.readline().strip()
  print 'Received %s' % incoming
  ser.write('RPI Received: %s\n' % incoming)