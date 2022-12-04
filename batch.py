import os
def get_file_name(root_dir):
    """
    获取文件名称
    """
    summary_content = ""
    for parent, _, file_names in os.walk(root_dir):
        is_cat = 1
        file_list = []
        od = 1
        for full_name in file_names:
            parent_name = parent.rsplit("\\", 1)[1]
            # fp = open(root_dir + "\\" + parent_name +
            #           ".md", 'w', encoding="utf-8")
            # fp.write("# " + parent_name)
            # fp.close()

            if is_cat:
                summary_content += '- [%s]($%s)' % (parent_name,
                                                    parent_name) + "\n"
            # 完整路径
            file_path = os.path.join(parent, full_name)
            file_srouce_name = full_name.rsplit(".", 1)[0]

            with open(file_path, "r+", encoding='utf-8') as file:
                file_content = file.readlines()

                if file_content[0].startswith("---"):
                    title = file_content[1][7:-1]
                    order = file_content[2][7:-1]
                    file_list.append([order, title, file_srouce_name])
                    file_content = file_content[6:]

                    file.seek(0)
                    file.truncate()
                    file.write("# " + title + "\n" + "".join(file_content))
                else:

                    title = file_content[1][7:-1]
                    order = file_content[2][7:-1]
                    print(title)
                    file_list.append([od, file_srouce_name, file_srouce_name])

            is_cat = 0
            od += 1
        if not file_list:
            continue
        print(file_list)
        file_list.sort(key=lambda x: int(x[0]))

        for file_child in file_list:

            # print(file_child)
            summary_content += '\t- [%s.md]($%s.md)' % (file_child[1], parent_name + "-" +
                                                  file_child[2]) + "\n"
    with open(root_dir + "/summary.md", mode='w', encoding='utf-8') as f:
        f.write(summary_content)


ROOT_DIR_TEST = r"H:\\Scripting\\Vue Projects\\docs2_yuelili_com\\AE\\expression"
ROOT_DIR2 = r"H:\\Scripting\\Vue Projects\\docs2_yuelili_com\\AE\\expression"
get_file_name(ROOT_DIR_TEST)