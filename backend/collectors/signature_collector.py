import win32api


def get_company_name(path):
    if not path:
        return "Unknown"

    try:
        info = win32api.GetFileVersionInfo(path, "\\")

        ms = info["FileVersionMS"]
        ls = info["FileVersionLS"]

        language = win32api.VerQueryValue(
            info,
            r"\VarFileInfo\Translation"
        )[0]

        string = "\\StringFileInfo\\%04X%04X\\CompanyName" % (
            language[0],
            language[1],
        )

        return win32api.VerQueryValue(info, string)

    except:
        return "Unknown"