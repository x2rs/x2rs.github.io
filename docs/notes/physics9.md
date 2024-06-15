# 9 热力学定律

## 9.1 热力学第一定律

### 9.1.1 准静态过程
之前所讲的物理规律都是在静态的状态成立的，但是系统的状态一旦发生改变，系统就会处于非平衡态。非平衡态到平衡态的过渡时间就是弛豫时间，如果实际每一次压缩所用的时间都大于弛豫时间，那么压缩过程中就几乎随时接近平衡态。

对于一个准静态过程，压强 $p$ 和体积 $V$ 都是确定的值，在 $p-V$ 图上为实线；对于非静态过程，在 $p-V$ 图上为虚线。


### 9.1.2 功、内能和热量
#### 准静态过程做功
<center>![活塞](img/piston.png)</center>

规定$\delta A>0$为系统对外做功，$\delta A<0$为外界对系统做功。

那么图中：

$$
\delta A = -F dl = -psdl = pdV
$$
那么
$$
\delta A = pdV
$$
$$
A=\int_{V_1}^{V_2}pdV
$$

系统所做的功在数值上等于$p-V$图上过程曲线以下的面积。

<center>![pV积分](img/pV_int.png)</center>

### 内能、热量

焦耳发现，使得系统从一个状态转移到另一个状态，不管通过什么方式，所做的功是相等的。

因此，利用功可以定义**内能**：$E_2-E_1=A_s$。微观上，热力学系统的内能是所有分子热运动动能和分子间势能的总和。系统的内能是状态量。

还可以通过内能定义**热量**。热力学系统 **从外界吸收的热量** 定义为在不做功过程中系统内能的增量。$Q=E_2-E_1$.

对于理想气体，内能为：

$$
E=\frac{i}{2} \nu R T
$$

因为 $ \overline{\varepsilon _t} = \frac{i}{2} k_B T $，所以$E=\nu N_A \overline{\varepsilon _t} = \frac{i}{2} \nu R T$

#### 热容量

**摩尔热容量** 当 $1\mathrm{~mol}$ 物体温度升高1K时所吸收的热量。
$$
C_m=\frac{\Delta Q}{\Delta T}
$$
**定容热容**
$$
C_V=\left.\lim_{\Delta T\to 0}\frac{\Delta Q}{\Delta T}\right|_V=\left.\frac{\delta Q}{\mathrm{d} T}\right|_V
$$
**定压热容**
$$
C_p=\left.\lim_{\Delta T\to 0}\frac{\Delta Q}{\Delta T}\right|_p=\left.\frac{\delta Q}{\mathrm{d} T}\right|_p
$$
**定容摩尔热容**
$$
C_{V,m}=C_V/\nu
$$
**定压摩尔热容**
$$
C_{p,m}=C_p/\nu
$$

### 9.1.3 热力学第一定律

某一过程，系统从外界吸热 $Q$，对外界做功 $W$，系统内能从初始态 $E_1$ 变为 $E_2$，则由**能量守恒**：

对于准静态过程：
$$
Q=E_2-E_1+W=\Delta E+\int_{V_1}^{V_2}p \mathrm{d} V
$$

对于无限小过程：
$$
\delta Q=\mathrm{d} E+\delta A=\mathrm{d} E+p\mathrm{d} V
$$

### 9.1.4 热力学第一定律的应用

#### 等容过程

$$dV = 0$$

因为$dV=0$，所以$pdV=0$；由热力学第一定律，有$dQ=dE$

对于1mol理想气体，由于$E=\frac{i}{2} RT$，所以$dE = \frac{i}{2} R dT$

$$
C_{V,m}=\left.\frac{\delta Q}{\mathrm{d} T}\right|_V
= \frac{dQ}{dT} = \frac{i}{2} R$$

#### 等压过程

$$dp = 0$$

$$C_{p,m}=(\frac{i}{2} + 1)R$$

#### 等温过程

#### 绝热过程

<img src="https://notes.sjtu.edu.cn/uploads/upload_906c8c27b92cf2cbabdd0bbb5d695f73.png" alt="image-20230610225713601" style="zoom:33%;" />

#### 多方过程

### 9.1.5 循环过程和热机的效率



## 9.2 热力学第二定律

### 9.2.1 热力学第二定律
pass
### 9.2.2 可逆过程和不可逆过程
pass
### 9.2.3 卡诺定理
pass
### 9.2.4 熵
pass
### 9.2.5 熵增加原理
pass
### 9.2.6 玻尔兹曼熵
pass