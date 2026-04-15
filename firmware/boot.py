import usb_hid

# Add CONSUMER_CONTROL to the list of enabled devices
usb_hid.enable((
    usb_hid.Device.KEYBOARD,
    usb_hid.Device.MOUSE,
    usb_hid.Device.CONSUMER_CONTROL
))
