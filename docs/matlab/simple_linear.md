# Matlab 简单线性回归（最小二乘法）

## $y=kx$

**注意！X，Y必须是*****同维度列向量***

```matlab
X=[1,2,3,4,5]';
Y=[3.9,8.1,12.0,15.9,20.2]';
k=X\Y
```

其中`X`和`Y`分别对应$y=kx$中的$x$和$y$，`k`对应$k$。

`\`为左除

## $y=kx+b$

```matlab
X=[1,2,3,4,5]';
Y=[3.9,8.1,12.0,15.9,20.2]';
res=[ones(length(X),1) X]\Y;
k=res(2)
b=res(1)
```

`k`对应$k$，`b`对应$b$

## 计算$R^2$

$$R^2=1-\frac{\sum_{i=1}^n(y_i-\hat{y}_i)^2}{\sum_{i=1}^n(y_i-\bar{y})^2}$$

其中$\hat y$为$y$的计算值，即

$$\hat{y}_i=kx_i+b$$

$\bar y$为$y$的平均值，即

$$\bar y=\frac{1}{n}\sum_{i=1}^n y_i$$

**以$y=kx+b$为例**

```matlab
YCalc=k*X+b;
Rsq = 1 - sum((Y - YCalc).^2)/sum((Y - mean(Y)).^2)
```

`Rsq`即为$R^2$

## 参考

[线性回归 Matlab](https://ww2.mathworks.cn/help/matlab/data_analysis/linear-regression.html)

[一元线性回归计算器](https://overflowcat.github.io/simple-linear-regression-calc/)