file = open('tree.txt', 'r')
list = file.readlines()
text = list[0]
tree_list = []

def separate(list):
   current_word = ''
   for char in list:
      if char != ' ':
         current_word += char
      else:
         if current_word:
            tree_list.append(current_word)
            current_word = ''

   if current_word:
      tree_list.append(current_word)

   print(tree_list)
   
separate(text)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree(node, prefix="", is_last=True, is_root=True, side=""):
    if node is None:
        return

    if is_root:
        print(node.value)
    else:
        branch = "└── " if is_last else "├── "
        print(f"{prefix}{branch}{side}{node.value}")

    children = []

    if getattr(node, 'right', None) is not None:
        children.append((node.right, "R "))

    if getattr(node, 'left', None) is not None:
        children.append((node.left, "L "))

    for i, (child, child_side) in enumerate(children):
        is_last_child = (i == len(children) - 1)
        new_prefix = prefix + ("    " if is_last else "│   ") if not is_root else ""
        print_tree(child, new_prefix, is_last_child, False, child_side)


def build_tree(elements):
    if not elements:
        return None
    
    mid_index = len(elements) // 2
    
    root = Node(elements[mid_index])
    
    root.left = build_tree(elements[:mid_index])
    
    root.right = build_tree(elements[mid_index + 1:])
    
    return root

tree1 = build_tree(tree_list)
print_tree(tree1)

