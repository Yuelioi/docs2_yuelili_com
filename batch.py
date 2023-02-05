import os

summary_content = ""


def generate_summary(path, parent="", level=0):
    if level == 3:  # 限制递归深度
        return
    global summary_content
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            summary_content += f"""{' ' * level *4}- [{child}](${child})\n"""
            generate_summary(child_path, parent + "-" + child, level + 1)
        else:

            summary_content += f"{' ' * level *4}- [{child.replace('.md','')}](${(parent + '-')[1:] +child})\n"


root_dir = r"H:\Scripting\Vue Projects\docs2_yuelili_com\AE\scripting"
generate_summary(root_dir)

print(summary_content)
with open(root_dir + "\\summary.md", "w+", encoding="utf-8")as f:
    f.write(summary_content)
