# https://www.codewars.com/kata/608cc9666513cc00192a67a9

class Node:
    def __init__(self, _range):
        self.range = _range
        self.value = 0
        self.left = None
        self.right = None

def build_tree(_node):
    delta = _node.range[1] - _node.range[0]
    if delta == 1:
        pass
    elif delta == 2:
        _node.left = Node([_node.range[0],_node.range[0]+1])
        _node.right = Node([_node.range[0]+1, _node.range[0]+2])
    else:
        mid = (_node.range[1] - _node.range[0]) // 2 + _node.range[0]
        _node.left = Node( [_node.range[0] , mid] )
        build_tree(_node.left)
        _node.right = Node( [mid , _node.range[1]] )
        build_tree(_node.right)

def eval_tree(_node,arr,op):
    if _node.range[1] - _node.range[0] == 1:
        _node.value = arr[_node.range[0]]
    else:
        _node.value = op(eval_tree(_node.left,arr,op), eval_tree(_node.right,arr,op))
    return _node.value

def eval_range(_node,_range,op):
    if _node.range == _range:
        return _node.value
    else:
        mid = _node.left.range[1]  # equal to _node.right[0]
        if _range[0] < mid and _range[1] > mid:
            return op(
                eval_range(_node.left, [_range[0], mid], op ),
                eval_range(_node.right, [mid,_range[1]], op )
            )
        elif _range[0] >= mid:
            return eval_range(_node.right, _range, op)
        else:
            return eval_range(_node.left, _range, op)
    


def compute_ranges(arr, op, rs):
    root = Node([0,len(arr)])
    build_tree(root)
    eval_tree(root, arr, op)
    return [eval_range(root, r,op) for r in rs]

def _sum(a,b): 
    return a+b
def _max(a,b): 
    return a if a > b else b
def _min(a,b): 
    return a if a < b else b
def _gcd(a,b): 
    return a if b == 0 else _gcd(b, a%b) 
def _lcm(a,b): 
    if a == 0: return b
    if b == 0: return a
    return a*b / _gcd(a,b)
def mod_sum(n): return lambda a,b:  (a+b)%n


print( compute_ranges([1, 5, 8, 5, 1, 8], _sum, [[0, 4], [0, 6], [2, 4], [1, 4]]) )
compute_ranges([0, 0, 4, 75, 12, 0, 16, 5], _gcd, [[1, 4], [2, 6], [0, 1], [1, 4], [4, 7]])


# The following function is the naive version, that has no optimization. It does the sample tests, but cannot finish the real tests without timing out
def compute_ranges_naive(arr, op, rs):
    result = []
    for r in rs:
        start = r[0]
        end = r[1]
        ans = arr[start]
        for i in range(start+1,end):
            ans = op(ans, arr[i])
        result.append(ans)
    return result

#print(compute_ranges_naive([1, 5, 8, 5, 1, 8], _sum, [[0, 4], [0, 6], [2, 4], [1, 4]]))
print(compute_ranges_naive([0, 0, 4, 75, 12, 0, 16, 5], _gcd, [[1, 4], [2, 6], [0, 1], [1, 4], [4, 7],[0,7]]) )