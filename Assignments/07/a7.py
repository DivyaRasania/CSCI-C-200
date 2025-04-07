import matplotlib.pyplot as plt

########################
# PROBLEM 1
########################
def encode(msg, shift):
    """
    Encode a message using Caesar Cipher with extended alphabet including space.
    
    Args:
    msg (str): The message to encode (lowercase)
    shift (int): Number of positions to shift
    
    Returns:
    str: Encoded message
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz{'
    encoded_msg = ''
    msg = msg.replace(' ', '{')
    
    for char in msg:
        idx = alphabet.index(char)
        new_idx = (idx + shift) % len(alphabet)
        encoded_msg += alphabet[new_idx]
    
    return encoded_msg

def decode(msg, shift):
    """
    Decode a message using Caesar Cipher with extended alphabet including space.
    
    Args:
    msg (str): The message to decode (lowercase)
    shift (int): Number of positions to shift
    
    Returns:
    str: Decoded message
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz{'
    decoded_msg = ''
    
    for char in msg:
        idx = alphabet.index(char)
        new_idx = (idx - shift) % len(alphabet)
        if alphabet[new_idx] == '{':
            decoded_msg += ' '
            continue
        decoded_msg += alphabet[new_idx]

    return decoded_msg

########################
# PROBLEM 2
########################
def tiles(n, v, lst):
    """
    Find all possible combinations of tiles that sum to n.
    
    Args:
        n (int): Target sum
        v (list): List of available tile values
        lst (list): Initial combinations to start with
    
    Returns:
        list: List of all possible combinations that sum to n
    """
    result = []
    
    for combo in lst:
        if sum(combo) == n:
            result.append(combo)
    
    new_lst = []
    for combo in lst:
        if sum(combo) < n:
            for val in v:
                new_combo = combo + [val]
                if sum(new_combo) <= n:
                    new_lst.append(new_combo)
    
    if new_lst:
        result.extend(tiles(n, v, new_lst))
    
    return result

########################
# PROBLEM 3
########################
def secdec_dec(n):
    """
    Convert a base-17 number (string) to decimal.

    Args:
        n (str): The base-17 number as a string

    Returns:
        int: The decimal equivalent of the base-17 number
    """
    base = 17
    result = 0
    
    for char in n:
        value = int(char) if char.isdigit() else ord(char.upper()) - ord('A') + 10
        result = result * base + value
    
    return result

########################
# PROBLEM 4
########################
def intersection(x,y):
    """
    Returns the intersection of two lists x and y.

    Args:
        x (list): First list
        y (list): Second list
    
    Returns:
        list: List of points that are in both x and y
    """
    return [point for point in x if point in y]
 
def block_distance(p0,p1):
    """
    Returns the city block distance between two points p0 and p1.

    Args:
        p0 (tuple): First point (x,y)
        p1 (tuple): Second point (x,y)

    Returns:
        int: The city block distance between p0 and p1
    """
    return abs(p0[0]-p1[0]) + abs(p0[1]-p1[1])
 
 
def get_points(center,bd):
    """
    Returns a list of points within a city block distance bd from the center point.
    
    Args:
        center (tuple): The center point (x,y)
        bd (int): The block distance

    Returns:
        list: List of points within the block distance from the center
    """
    points = []
    for x in range(center[0] - bd, center[0] + bd + 1):
        for y in range(center[1] - bd, center[1] + bd + 1):
            if block_distance(center, (x, y)) <= bd:
                points.append((x, y))
    return points

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file,
    please put any print statements you want to try in
    this if statement.
    """

    # Problem 1
    # data = ["abc xyz","the cat", "i love ctwohundred"]
    # for i,j in enumerate(data,start=2):
    #     print(f"original msg {j}")
    #     print(f"encoded  msg {encode(j,i)}")
    #     print(f"decoded  msg {decode(encode(j,i),i)}")

    # secret_msg = encode("the quick brown fox jumps over the lazy dog", 24)
    # print(secret_msg)
    # print(decode(secret_msg,24))

    # Problem 2
    # n = 6
    # v = [1,2,3]
    # print(tiles(n,v,[[i] for i in v]))
    # for i in tiles(n,v,[[i] for i in v]):
    #     print(sum(i), end="")

    # n = 4
    # v = [1,2]
    # print(tiles(n,v,[[i] for i in v]))
    # for i in tiles(n,v,[[i] for i in v]):
    #     print(sum(i), end="")

    # Problem 3
    # data4 = ["G2","100","10","GA3","G","E2"]
    # for d in data4:
    #     print(secdec_dec(d), int(d,17))

    # Problem 4 
    # A = ((0,-1),2)
    # B = ((0,1),1)
    # C = ((4,4),1)
    # p = get_points(*A)
    # q = get_points(*B)
    # r = intersection(p,q)
    # s = get_points(*C)
    # t = intersection(s,q)

    # for points in p,q,r,s:
    #     print(points)

    # # uncomment to see visualization
    # color = 'rgbmy'

    # for i,pts in enumerate([p,q,r,s,t]):
    #     plt.plot([x for x,_ in pts],[y for _,y in pts],color[i] + 'o')

    # plt.gca().legend(("A: ((0,-1),2)", "B: ((0,1),1)", r"$\mathsf{A}\cap\mathsf{B}$","C: ((4,4),1)", r"$\mathsf{B}\cap\mathsf{C}$"))
    # plt.axis([-7, 7, -7, 7])
    # plt.grid()
    # plt.gca().set_aspect("equal")

    # plt.grid(True)
    # plt.title("City with square streets.")
    # plt.show()

    print()