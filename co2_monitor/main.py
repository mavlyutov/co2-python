import sys
import usb.core

VENDOR_ID = 0x04d9
PRODUCT_ID = 0xa052

dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
if dev is None:
    raise ValueError('Device not found')

result = dev.ctrl_transfer(0xC0, CTRL_LOOPBACK_READ, 0, 0, len(msg))

print result

