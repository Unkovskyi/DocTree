import os
import os.path as path

def parse_dir(in_path, level=1):
    result = []

    for i in os.listdir(in_path):
        p_path = path.join(in_path, i)

        if path.isdir(p_path):

            path_info = (i,i.split('.')[-1],level, False)
            result.append(path_info)
            tmp_result = parse_dir(p_path, level=level+1)
            result.extend(tmp_result)

        else:
            path_info = (i,(True if i.split('.')[-1]=='py' else False),level, True)
            result.append(path_info)

    return result


class DirTree:
    def __init__(self, dir_path):
        assert path.isdir(dir_path), 'dir path must be a path to dir'
        self.dir_path = dir_path

    def list_dir(self):
        tree = parse_dir(self.dir_path)

        def map_tree_elem(elem):
            elem_str = '{shift}[{prefix} {PyM}] {name}'.format(
                shift='\t' * elem[2],
                prefix=('F' if elem[3] else 'D' ),
                name=elem[0],
                PyM=('PyM' if elem[1]==True else '')
            )

            return elem_str

        result = map(map_tree_elem, tree)
        result = '\n'.join(result)


        return result

dir_tree = DirTree('C:\HP_LaserJet_400_MFP_M425')
dir_structure = dir_tree.list_dir()
print(dir_structure)