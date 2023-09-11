#========================= INTERMEDIATE PROBLEMS ===============================#
#
#----------------------------- Tower Of Hanoi ----------------------------------#
def TowerOfHanoi(n, src, hel, des):
    if(n == 1):
        print("Transfer disk ", n, " from ",src, " to ",des)
        return
    else:
        TowerOfHanoi(n-1,src, des,hel)
        print("Transfer disk ", n, " from ",src, " to ",des)
        TowerOfHanoi(n-1,hel,src,des)
TowerOfHanoi(3,"S","H", "D")