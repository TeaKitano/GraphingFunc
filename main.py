import sympy
import math
from sympy import sympify
import numpy
import matplotlib.pyplot as plt
import streamlit as st

def ReadFanc(s):
    print(s)
    l=["1","2","3","4","5","6","7","8","9","0"]
    k=s[0]
    for i in range(len(s)-1):
        if s[i+1]=="x":
            if s[i] in l:
                k=k+"*"
        k=k+s[i+1]
            
    x=sympy.Symbol('x')
    print(k)
    y=sympify(k)

    if type(y.subs(x,8).evalf())==type(sympy.sin(6).evalf()):
        args=(x)
        return sympy.lambdify(args,y,"numpy")
    else:
        print("error")
        return False

def mkFuncPlot(mn,mx,f):
    x=sympy.Symbol("x")
    y=ReadFanc(f)
    xl=numpy.linspace(mn,mx,1000)
    print(xl)
    yl=y(xl)
    print(xl,yl)
    return [xl,yl]

def main():
    fig=plt.figure()
    ax=fig.add_subplot()

    check=st.checkbox("範囲指定")
    if check:
        xmn=st.number_input(label="x最小値",value=-10)
        xmx=st.number_input(label="x最大値",value=10)
        ymn=st.number_input(label="y最小値",value=-10)
        ymx=st.number_input(label="y最大値",value=10)
        plt.xlim(xmn,xmx)
        plt.ylim(ymn,ymx)
    else:
        xmn=-10
        xmx=10
    
    s1=st.text_input(label="一つ目の関数",value="x+5")
    s2=st.text_input(label="二つ目の関数",value="x+2")

    start=st.button("描画")
    
    if start:
        l1=mkFuncPlot(xmn,xmx,s1)
        ax.plot(l1[0],l1[1])
        l2=mkFuncPlot(xmn,xmx,s2)
        ax.plot(l2[0],l2[1])
        st.pyplot(fig)


if __name__=="__main__":
    main()
