import datetime
import winshell

def get_recycle_bin_metadata(date_format):
    file_metadata_list = []
    recycle_bin = winshell.recycle_bin()

    for item in recycle_bin:
        created = item.getctime().strftime(date_format) if item.getctime() else ""
        modified = item.getmtime().strftime(date_format) if item.getmtime() else ""
        accessed = item.getatime().strftime(date_format) if item.getatime() else ""

        file_data = {
            "file": item.name,
            "name": item.name,
            "type": "", # parse from item.name if needed
            "location": item.original_filename,
            "size (bytes)": item.size,
            "created": created,
            "modified": modified,
            "accessed": accessed
        }
        file_metadata_list.append(file_data)

    return file_metadata_list