import os

ignored = [
    "index.md",
    ".ini",
    ".yml",
    "build.py",
    ".git",
    "compile",
    "makenew"]


def list_files(startpath):
    with open(os.path.join(startpath, "index.md"), "w", encoding="utf-8")\
            as file:
        segs = startpath.split(os.path.sep)
        file.write("# " + (segs[-1] if segs[-1] != "." else "Home") + "\n")
        file.write("#### ")
        list = []
        for i in range(len(segs)):
            temp = ""
            temp += "[" + (segs[i] if segs[i] != "." else "Home") + "]"
            path_str = os.path.sep.join(
                [".." for j in range(len(segs) - i - 1)])
            temp += "(" + path_str + ")"
            list.append(temp)
        file.write(
            ("\\" +
             os.path.sep).join(list))
        file.write("\n")
        for root, dirs, files in os.walk(startpath):
            if root.find(".git") >= 0:
                pass
            else:
                level = root.replace(startpath, '').count(os.sep) - 1
                if level != -1:
                    if level <= 1:
                        indent = ' ' * 4 * (level)
                        file.write(
                            '{}- {}\n'.format(
                                indent,
                                "[" + os.path.basename(root) + "]" +
                                "(" + os.path.relpath(root, startpath)
                                .replace(" ", "%20") + ")"
                            )
                        )
                if level <= 0:
                    subindent = ' ' * 4 * (level + 1)
                    for f in files:
                        if(all(filepart not in f for filepart in ignored)):
                            file.write(subindent + "- ")
                            file.write("[_" + os.path.basename(f) + "_]")
                            path_str = os.path.relpath(
                                os.path.join(root, f), startpath)
                            file.write(
                                "(" + path_str.replace(" ", "%20") + ")")
                            file.write("\n")
                else:
                    pass


for root, dirs, files in os.walk("."):
    list_files(root)
