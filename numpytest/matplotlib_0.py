"""
import matplotlib.pyplot as plt

선 그래프
    plt.plot([x,] y [,fmt])
        x,y = 배열
        (x,y) 좌표로 입력을 받아 연결하여 그래프로 보여줌
        ex)
            x = numpy.arange(-4.5,5,0.5)
            y1 = 2*x**2
            plt.plot(x,y)

    plt.show()
        그래프를 보여준다.

    plt.figure()
        여러개의 그래프를 한페이지가 아닌 페이지를 나누어 보여준다.
        ex)
            plt.plot(x,y)
            plt.figure()
            plt.plot(x,y1)
            plt.show()

    plt.clf()
        지정한 창에있는 그래프를 모두 지운다.
        ex)
            plt.figure(1) # 그래프 창을 지정
            plt.plot(x,y) # 그래프 생성
            plt.clf() # 그래프 삭제

    plt.subplot(m,n,p)
        하나의 창에 m*n개의 창을 띄워서 그래프를 보여준다.
        ex)











"""