# Cramér-Rao不等式

$$
D(\hat{\theta}) \geq \frac{1}{n E \left[ \left( \frac{\partial}{\partial \theta} \ln p(X, \theta) \right)^2 \right]}
$$

这个公式称为**Cramér-Rao不等式**（Cramér-Rao Inequality）或**Cramér-Rao下界**（Cramér-Rao Lower Bound, CRLB）。它是数理统计中估计理论的一部分，提供了估计参数的方差的一个下界。具体来说，对于任何**无偏**估计量\(\hat{\theta}\)，它的方差不能小于该下界。

公式中各符号的含义如下：

- $D(\hat{\theta})$是估计量$\hat{\theta}$的方差。
- $n$是样本量。
- $\frac{\partial}{\partial \theta} \ln p(X, \theta)$是对数似然函数（分布律/概率密度）关于参数$\theta$的偏导数。

Cramér-Rao下界对于估计量的效率以及构建最优估计量具有重要意义。