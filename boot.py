import storage
storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "SKELL"
storage.remount("/", readonly=True)
storage.enable_usb_drive()
