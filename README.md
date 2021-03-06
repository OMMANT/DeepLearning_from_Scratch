# 밑바닥부터 시작하는 딥러닝


## CHAPTER 2. 퍼셉트론
**퍼셉트론**(perceptron)은 프랑크 로젠블라트가 1957년에 고안한 알고리즘  
퍼셉트론이란?  
다수의 신호를 입력으로 받아 하나의 신호를 출력하는 '인공 뉴런'을 뜻함. 신호의 출력은 흐른다 / 안흐른다 (1 / 0) 이 두 가지 값을 갖는다. $x_1$와 $x_2$ 는 입력 신호, $y$는 출력 신호, $w_1$과 $w_2$는 가중치이다. 뉴런에서 보내온 신호의 총합이 임계치를 넘어서면 1을 출력하고 그렇지 않다면 0을 출력한다. 이를 수식으로 표현하면 아래와 같다.

$$ y = \begin{cases} 0\; (w_1 x_1 + w_2 x_2 \leq \theta) \\ 1\; (w_1 x_1 + w_2 x_2 > \theta) \end{cases} $$

이렇게 구현한 AND게이트는 직관적이고 알기 쉽지만 앞으로를 생각해 다른 방식으로 수정할 수 있다. 위의 식에서 $\theta$를 $-b$로 치환하면 아래와 같다.
$$ y =
\begin{cases}
0\; (b + w_1 x_1 + w_2 x_2  \leq 0) \\
1\; (b + w_1 x_1 + w_2 x_2 > 0) 
\end{cases} $$

여기서 $b$를 편향(bias)라 부르기로 한다.
