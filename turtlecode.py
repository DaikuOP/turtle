from turtle import *
def poli2(lado, ang, ang_total):
    ang_recorrido = 0
    while ang_recorrido < ang_total:
        t.fd(lado)
        t.lt(ang)
        ang_recorrido += ang

def poli(lado, ang, ang_recorrido, ang_total):
    if ang_recorrido+ang > ang_total:
        ...
    else:
        t.fd(lado)
        t.lt(ang)
        poli(lado, ang, ang_recorrido+ang, ang_total)



def polispi(lado, ang, ang_recorrido, ang_total):
        if ang_recorrido+ang > ang_total:
            ...
        else:
            t.fd(lado)
            t.lt(ang)
            polispi(lado+20, ang, ang_recorrido+ang, ang_total)
    
def inspi(lado, ang, ang_recorrido, ang_total, inc):
    if ang_recorrido + ang > ang_total:
        ...
    else:
        t.fd(lado)
        t.lt(ang)
        inspi(lado, ang+inc, ang_recorrido+ang, ang_total, inc)

def arco_circular(r, ang):
    poli(r, 1, ang)

def doble_poli(lado1, lado2, ang, ang_recorrido, ang_total):
    if ang_recorrido+ang > ang_total:
        ...
    else:
        t.fd(lado1)
        t.lt(ang)
        t.fd(lado2)
        t.lt(ang)
        doble_poli(lado1, lado2, ang, ang_recorrido+ang, ang_total)

def mcm(n,m):
    if n==0:
        return m
    else:
        return mcm(m%n, n)

def lcm(n,m):
    return n*m/mcm(n,m)

print(lcm(40, 30))

#inspi(20, 20, 0, 300000, 30)
#inspi(20, 120, 0, 300000, 90)
#inspi(20, 80, 0, 300000, 60)


if __name__ == "__main__":
    t = Turtle()
    screen = t.getscreen()
    screen.tracer(0)
    inspi(20, 20, 0, 300000, 30)
    screen.update()
    screen.mainloop()


