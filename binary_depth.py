import json
# import sys


class Node:
    # Binary Node structure.
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def parse_tree_from_json(json_data):
    """
     Read json structure and create a binary tree
     @params:
        {"tree": {"nodes": [{"id": "1", "left": "2", "right": "3", "value": 1},..], "root": "1"}
    """
    if not json_data or "tree" not in json_data:
        return Node(-1)
    tree = json_data["tree"]
    if not tree.get("root") or not tree.get("nodes"):
        return Node(-1)
    print(" Info of the given tree : root id [{}] \
            No. of nodes in tree : [{}]".format(tree["root"], len(tree["nodes"])))
    node_map = {}
    # first pass at the nodes assuming the order is not guaranteed
    # also node entry can be missing
    root_id = tree["root"]
    for node in tree["nodes"]:
        n = Node(node["value"])
        if node.get("left"):
            n.left = node["left"]
        if node.get("right"):
            n.right = node["right"]
        node_map[node["id"]] = n

    if root_id not in node_map:
        return Node(-1)
    root = node_map[root_id]
    for node_id in node_map:
        node = node_map[node_id]
        if node.left and node.left in node_map:
            node.left = node_map[node.left]
        else:
            node.left = None
        if node.right and node.right in node_map:
            node.right = node_map[node.right]
        else:
            node.right = None
    return root


def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(str(node.value) + ' ')
        print_tree(node.right)


def BinaryTreeNodeDepthSum(root):
    """
     Given a root of a binary tree find the sum of nodes depth.
    """
    def calculate_depth(node, level, depth):
        # base case to exit.
        if not node:
            return 0
        if node.value:
            depth["depth"] += level
        if node.left:
           calculate_depth(node.left, level+1, depth)
        if node.right:
           calculate_depth(node.right, level+1, depth)
        return depth
    # keeping a global map to track the sum.
    depth = {"depth": 0}
    level = 0
    calculate_depth(root, level=level, depth=depth)
    return depth


if __name__ == "__main__":
    # json_data = json.load(sys.stdin)
    json_data = ["""{
    "tree": {
        "nodes": [
        {"id": "1", "left": "2", "right": null, "value": 1},
        {"id": "2", "left": null, "right": null, "value": 2}
    ],
        "root": "1"
    }
    }""",
                 """{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": null, "right": null, "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3}
    ],
    "root": "1"
  }
}""",

                 """ 
{
  "tree": {
    "nodes": [{"id": "1", "left": null, "right": null, "value": 1}],
    "root": "1"
  }
}""",
                 """
{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": null, "right": null, "value": 2},
      {"id": "3", "left": null, "right": null, "value": 3}
    ],
    "root": "1"
  }
}"""]
    root = parse_tree_from_json(json.loads(json_data[3]))
    print_tree(root)
    depth = BinaryTreeNodeDepthSum(root)
    print("Total Depth of tree is : {} ".format(depth))
