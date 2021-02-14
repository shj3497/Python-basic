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
            plt.subplot(2,2,1) # p=1 인 곳에 아래 그래프를 보여준다.
            plt.plot(x, y1)
            ...
            plt.subplot(2,2,4) # p=4 인 곳에 아래 그래프를 보여준다.
            plt.plot(x, y4)


    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
        x,y 의 범위를 지정해준다.


    fmt = '[color][line_style][marker]'
        color:
            b,g,r.. 등
        line_style:
            -   : 실선
            --  : 파선
            :   : 점선
            -.  : 파선 점선 혼합선
        marker:
            o   : 원모양
            ^,v,<,> : 화살표 방향
            s   : 사각형
            등...
    ex)
        plt.plot(x,y1,color="b", linestyle="-")


    xlabel, ylabel
        x축과 y축에 라벨로 문자열을 입력해준다.
        ex)
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
    title
        그래프 제목을 추가
        ex)
            plt.title('Graph Title')
    grid
        그래프 격자 표시
        ex)
            plt.grid(True)
    legend([], loc="")
        그래프 구분?
        ex)
            plt.legend(['data1','data2',...'data4']) # default 왼쪽 상단
            plt.legend(['data1','data2',...'data4'], loc='lower right') # 우측 하단
            or loc=1,2,3,4 : 각각 사분면으로 생각하면 좋을듯
    ex)
        x = numpy.arange(0,5,1)
        y1 = x
        y2 = x+1
        y3 = x+2
        y4 = x+3

        plt.plot(x,y1,'>-r', x,y2,'s-g', x,y3,'d:b', x,y4,'-.Xc') # '>-r' marker, line_style, color
        plt.legend(['data1','data2','data3','data4']) # 그래프 구분
        plt.show()

# 만약 그래프에서 한글을 표시하고 싶다면 matplotlib 에서 사용하는 폰트를 한글 폰트로 지정해야한다.
    matplotlib.rcParams['font.family'] >> default : sans-serif 이다. >> 한글 깨짐

    matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 맑은 고딕으로 설정
    matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 폰트가 깨지는것을 막아준다.


# 산점도
    plt.scatter(x,y [,s=size_n, c=colors, marker='marker_string', alpha=alpha_f])












"""