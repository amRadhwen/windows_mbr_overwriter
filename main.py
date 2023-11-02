from WindowsMBROverwriter import WindowsMBROverwriter

if __name__ == "__main__":
    # Example MBR data, replace this with your desired MBR content.
    mbr_data = b'\x00' * 512

    overwriter = WindowsMBROverwriter()
    overwriter.overwrite_mbr(mbr_data)