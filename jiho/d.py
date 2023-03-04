b = int(input( ))

a = []
for i in range(b) :
    d = []
    h= input( )
    v = h.split()
    d.append(v)
    a.append(d)

def preorder(x) :
    if x == -1 :
        return
    print(chr(x+65))
    preorder(a[x][0])
    preorder(a[x][1])

def inorder(x) :
    if x== -1:
        return
    inorder(a[x][0])
    print(chr(x+65))
    inorder(a[x][1])

def postorder(x) :
    if x== -1 :
        return
    postorder(a[x][0])
    postorder(a[x][1])
    print(chr(x+65))