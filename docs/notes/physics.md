# 大物补天

## 8 平衡态

### 8.1 平衡态

无外界影响，宏观量保持不变，动态平衡

没有宏观量的流

热平衡，热力学第零定律

### 理想气体状态方程

$$
pV=\nu RT
$$

玻尔兹曼常数

$$
k_B=\frac{R}{N_A}=1.38 \times 10^{-23}J/K
$$

所以

$$
pV=\nu k_B N_A T=Nk_BT
$$

$N$ 为总分子数

$$
p=\frac{N}{V} k_B T = n k_B T
$$

$n$ 为单位体积内的分子数

<!--这是正确的吗？？？-->

定义：$m_{all}$为气体总质量，$M$为气体摩尔质量，有：

$$
pV=\frac{m}{M} R T
$$

上式中两边除以 $V$，

$$
p = \frac{\rho}{M} R T = \frac{\rho}{M} k_B N_A T = ???
$$
<!--这是正确的吗？？？-->

### 关于 dN dV


### 对大量分子组成的气体系统的统计假设

（1）气体处在平衡态时，分子在容器中的空间分布，平均来说是均匀的 （不考虑重力影响）

$$
n = \frac{dN}{dV}=\frac{N}{V}
$$

dV——体积元
（宏观小，微观大）
“非常大的小”

dN, dV 宏观小，微观大

dN, dV 不是无穷小

### 理想气体速度分布各向同性(isotropic)

$$\overline{v_x^2}=\overline{v_y^2}=\overline{v_z^2}=\frac{1}{3} \overline{v^2}$$

气体在平衡态时，具有相同速率的分子向各个方向运动的平均分子数是相同的（速度分布的各向同性）若定义

$$
\overline{v_x}=\frac{\sum_i v_{xi}}{N}
$$

$$
\overline{v_x^2}=\frac{\sum_i v_{xi}^2}{N}
$$

则显然有

$$
\overline{v_x}=\overline{v_y}=\overline{v_z}=0
$$

$$
\overline{v_x^2}=\overline{v_y^2}=\overline{v_z^2}=\frac{1}{3}\overline{v^2}
$$

因为

$$
\overline{v^2}=\overline{v_x^2}+\overline{v_y^2}+\overline{v_z^2}
$$

设第 $i$ 组分子的速度在 $\overline{v_i}\sim\overline{v_i}+\mathrm d \overline{v_i}$ 区间内，以 $n_i$ 表示单位体积内第 $i$ 组分子的数量。$m$：分子质量，$n=\sum n_i$

一次碰撞分子动量变化 $2mv_{ix}$，完全弹性碰撞，在 $\mathrm d t$ 时间内与 $\mathrm d A$ 碰撞的分子数 $n_i \underbrace{v_{ix}\mathrm d t}_{能碰到容器壁对应的距离}\underbrace{\mathrm d S}_{面元}$。

他们给容器壁的总冲量：
$$
2mn_iv_{ix}^2 \mathrm d t\mathrm d S
$$
考虑不同速度分子，一半朝左一半朝右，朝左碰右壁，朝右碰左壁：
$$
\mathrm d I=\sum_{i,v_{ix}>0 朝左} 2mn_i v_{ix}^2 \mathrm d t\mathrm d S=\sum_i m n_iv_{ix}^2 \mathrm d t\mathrm d S
$$
得到
$$
p=\frac{\mathrm d F}{\mathrm d S}=\frac{\mathrm d I/\mathrm d t}{\mathrm d S}=\sum_i mn_iv_{ix}^2 =nm\frac{\sum_i n_i v_{xi}^2}{\underbrace{\sum_i n_i}_{n}}=nm\overline{v_x^2}=\frac{1}{3}nm\overline{v^2}
$$
代入平均分子动能 $\overline{\varepsilon _t}=\frac{1}{2}m\overline{v^2}$，得到 $p=\frac{2}{3}n\overline{\varepsilon_t}$。

代入 $p=nkT$，结论 $\overline{\varepsilon_t}=\frac{3}{2}kT$， 温度标志着物体内部分子热运动的剧烈程度，它是大量分子热运动的平均平动动能 $\overline{\varepsilon_t}$ 的统计平均值的量度。

均方根速率：$\overline{\varepsilon_t}=\frac{1}{2}m\overline{v^2}=\frac{3}{2}kT$，得到
$$
\sqrt{\overline{v^2}}=\sqrt{\frac{3kT}{m}}\overset{\times N_A}{=}\sqrt{\frac{3RT}{M}}
$$

## 速率分布函数

阿巴阿巴阿巴

阿巴阿巴阿巴

阿巴阿巴阿巴

阿巴阿巴阿巴

阿巴阿巴阿巴

不会！

我觉得就是概统的概率密度吧qwq

## 速度分布函数

速度范围：

$$
v_x \to v_x+dv_x
$$

$$
v_y \to v_y+dv_y
$$

$$
v_z \to v_z+dv_z
$$

设取在该速度范围的分子数为dN，则速度分布函数定义为

$$
F(v_x,v_y,v_z)=\frac{1}{N}\frac{dN}{dv_xdv_ydv_z}
$$

### 麦克斯韦速度分布函数

麦克斯韦证明了，处于平衡态的理想气体系统，满足：

$$
F(v_x,v_y,v_z)=(\frac{m}{2\pi k_B T})^{\frac{3}{2}}e^{\frac{m}{2k_B T}(v_x^2+v_y^2+v_z^2)}
$$

### 麦克斯韦速率分布函数

$$
f(v)=4\pi(\frac{m}{2\pi k_B T})^{\frac{3}{2}}e^{\frac{m}{2k_B T}v^2}v^2
$$

证明：利用速度分布律可以导出速率分布律

分子速率处于$v$和$v+dv$间的几率是分子速度矢量端点落在以$v$和$v+dv$为内外半径球壳内的几率。

$$
f(v)dv = F(v_x,v_y,v_z) \cdot 4 \pi v^2 dv
$$

*我感觉就是表面积*

**注意到**，令

$$
\frac{k_B T}{m} = \sigma^2
$$

即

$$
\frac{m}{k_B T} = \frac{1}{\sigma^2}
$$

则上面两个分布函数变为：

$$
F(v_x,v_y,v_z)=(\frac{1}{2\pi \sigma^2})^{\frac{3}{2}}e^{\frac{1}{2 \sigma^2}(v_x^2+v_y^2+v_z^2)}
$$

$$
f(v)=4\pi(\frac{1}{2\pi \sigma^2})^{\frac{3}{2}}e^{\frac{1}{2 \sigma^2}v^2}v^2
$$


芝士正态分布！！！！！$\sigma$是速度分量的标准差！！！

### 三个重要的速率

最可几速率
$$
v_p=\sqrt{\frac{2k_B T}{m}}=\sqrt{2}\sigma
$$

平均速率
$$
\overline{v}=\sqrt{\frac{8k_B T}{\pi m}}=\sqrt{\frac{8}{\pi}}\sigma
$$

均方根速率
$$
v=\sqrt{\frac{3k_B T}{m}}=\sqrt{3}\sigma
$$

$$
\varepsilon _t
$$

$$
p=\frac{2}{3}
$$