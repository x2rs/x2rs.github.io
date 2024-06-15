# 5 相对论

<!--引用kumikosjtu.github.io开始-->

## 经典力学的困难

在 $S$ 系中空间各点放置无穷系列的时钟，这些时钟与该惯性系保持相对静止、彼此同步。一个事件的时空坐标 $(x,y,z,t)$ 由该事件发生的地点及该处的时钟记录下来。

### 同时性和时间间隔的绝对性

**同时性**

$t_2=t_1$, $t_2'=t_1'$.

**时间间隔**
$$
\Delta t=t_2-t_1\\
\Delta t'=t_2'-t_1'=\Delta t
$$

### 空间间隔的绝对性

在 $S$ 系中 $P_1:(x_1,y_1,t_1)$，$P_2:(x_2,y_2,t_2)$ 推出 $L=x_2-x_1$。（同时测量）

在 $S'$ 系中 $P_1:(x_1',y_1',t_1')$，$P_2:(x_2',y_2',t_2')$。

得到 $L'=x_2'-x_1'=(x_2-ut_2)-(x_1-ut_1)=x_2-x_1$.

牛顿：时间和空间是与物质的存在和 **运动** 无关的，是绝对不变的。考虑物体的运动，得出了 **狭义相对论 *Special Relativity***。

### 牛顿牛顿的绝对时空观

$$
\left\{
\begin{matrix}
x_2'-x_1'=x_2-x_1\\
t_2'-t_1'=t_2-t_1\\
\end{matrix}
\right.
$$

$$
\left\{
\begin{matrix}
v_x'=v_x-u\\
v_y'=v_y\\
v_z'=v_z
\end{matrix}
\right.
$$

$$
\left\{
\begin{matrix}
a_x'=a_x-\dfrac{\mathrm d u}{\mathrm d t}\\
a_y'=a_y\\
a_z'=a_z
\end{matrix}
\right.
$$

宏观低速物体的力学规律在任何惯性系中形式相同。力学的基本运动规律在所有惯性系中可以表示为相同形式。

### 伽利略变换的局限性

一维电磁波动方程：
$$
\frac{\partial ^2}{\partial x^2}\Phi(x,t)-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}\Phi(x,t)=0
$$
利用 $x'=x-ut$ 进行变换，发现形式上不相同。
$$
\frac{\partial^2}{\partial x'^2}\Phi-\frac{1}{c^2}\frac{\partial ^2}{\partial t'^2} \Phi+\frac{2u}{c^2}\frac{\partial ^2}{\partial x '\partial t'}-\frac{u^2}{c^2} \frac{\partial ^2}{\partial x'^2}\Phi=0
$$
光速是否符合伽利略速度变换。

**掷球实验**

$t=t_{10}=0$ 时刻 A 加速球，$t=t_1$ 时刻球出手。

$t=t_{20}=L/c$ 时刻，B 看到 A 开始投球的动作。$t=t_2=t_1+L/(c+u)$ 时刻，B 看到球离开 A 手的情况。

但是如果 $L$ 很大，得到 $L/c>t_1+L/(c+u)$，因果律被破坏。

## 狭义相对论的基本假设

1. 狭义相对性原理：一切物理规律在任何惯性系中形式相同。
2. 光速不变原理：在所有惯性系中，真空中的光速相同为 $c$，与光源和观测者的运动无关。

## 狭义相对论的时空观

### 同时性的相对性

$S$ 地面参考系。在火车上 $A',B'$ 放置信号接收器

### 时间间隔的相对性

相对于 $S'$ 系静止：
$$
\Delta t_0'=\frac{2d}{c}
$$
$\Delta t_0'$ 称为固有时或者本征时。

如果在 $S$ 系中观察，得到
$$
l=\sqrt{d^2+\left(\frac{u\Delta t}{2}\right)^2}\\
\Rightarrow \Delta t =\frac{2d}{c}\frac{1}{\sqrt{1-\frac{u^2}{c^2}}}=\frac{\Delta t_0'}{\sqrt{1-\frac{u^2}{c^2}}}
$$


![image-20230504081156375](https://notes.sjtu.edu.cn/uploads/upload_7f79d834997db918307770efa9a6ce30.png)

### 洛伦兹长度收缩

如果在 $S$ 系中尺的长度是 $L$，那么在 $S'$ 系中的观测者测量为
$$
L'=L\sqrt{1-\frac{u^2}{c^2}}
$$
![image-20230504223856808](https://notes.sjtu.edu.cn/uploads/upload_3bf10c1b5ea51c7d47362e94cf04d050.png)

![image-20230504082311480](https://notes.sjtu.edu.cn/uploads/upload_bee8e18da07414286b69cd742c0c3b29.png)

 宇宙射线进入大气层时与大气微粒碰撞形成 $\mu^-$ 介子。

如果没有时间膨胀：
$$
s_0=u\tau\approx644\mathrm{~m}
$$
时间膨胀：
$$
\Delta t=\frac{\tau}{\sqrt{1-\frac{u^2}{c^2}}}
$$

$$
s=u\Delta t\approx 1.02\times 10^4\mathrm{~m}
$$

如果在 $\mu^-$ 子上看：大气层的厚度变短了。尺缩效应。

<!--引用kumikosjtu.github.io结束-->

## 洛伦兹坐标变换

设有两个惯性参考系 $S$ 和 $S'$，$x$ 轴和 $x'$ 轴方向相同而且重合，$S'$ 系相对于 $S$ 系以速度 $\boldsymbol u$ 沿 $x$ 轴正方向运动。两个惯性系分别有自己的计时系统。

$$
\gamma = \frac{1}{\sqrt{1-\dfrac{u^2}{c^2}}}
$$

正变换

$$
\begin{cases}
x'=\gamma(x-ut) \newline
y'=y \newline
z'=z \newline
t'=\gamma\left(t-\dfrac{u}{c^2}x\right)
\end{cases}
$$

逆变换

$$
\begin{cases}
x=\gamma(x'+ut') \newline
y=y' \newline
z=z' \newline
t=\gamma\left(t'+\dfrac{u}{c^2}x'\right)
\end{cases}
$$


## 洛伦兹速度变换

正变换

$$
\begin{cases}
v_x' = \dfrac{v_x - u}{1-\dfrac{u}{c^2} v_x} \newline\newline
v_y' = \dfrac{v_y}{1-\dfrac{u}{c^2}v_x}\sqrt{1-\dfrac{u^2}{c^2}} \newline\newline
v_z' = \dfrac{v_z}{1-\dfrac{u}{c^2}v_x}\sqrt{1-\dfrac{u^2}{c^2}}
\end{cases}
$$

逆变换

$$
\begin{cases}
v_x = \dfrac{v_x' + u}{1+\dfrac{u}{c^2} v_x'} \newline\newline
v_y = \dfrac{v_y'}{1+\dfrac{u}{c^2}v_x'}\sqrt{1-\dfrac{u^2}{c^2}} \newline\newline
v_z = \dfrac{v_z'}{1+\dfrac{u}{c^2}v_x'}\sqrt{1-\dfrac{u^2}{c^2}}
\end{cases}
$$

## References
[kumikosjtu.github.io](https://kumikosjtu.github.io/%E5%A4%A7%E5%AD%A6%E7%89%A9%E7%90%86I/)