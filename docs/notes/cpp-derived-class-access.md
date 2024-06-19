# C++ 继承访问说明符

<table>
 <tr>
    <th></th>
    <th>继承方式为public</th>
    <th>继承方式为protected</th>
    <th>继承方式为private</th>
  </tr>
  <tr>
    <td>基类成员为public</td>
    <td>public</td>
    <td>protected</td>
    <td>private</td>
  </tr>
  <tr>
    <td>基类成员为protected</td>
    <td>protected</td>
    <td>protected</td>
    <td>private</td>
  </tr>
  <tr>
    <td>基类成员为private</td>
    <td>不可访问</td>
    <td>不可访问</td>
    <td>不可访问</td>
  </tr>
</table>

定义一个类`A`：
```cpp
class A {
public:
    int a;
protected:
    int b;
private:
    int c;
};
```

使用不同的继承方式，对应的成员访问性如下：
```cpp
class B : public A {
    // A::a -> public
    // A::b -> protected
    // A::c 不可访问
};
 
class C : protected A
{
    // A::a -> protected
    // A::b -> protected
    // A::c 不可访问
};
 
class D : private A
{
    // A::a -> private
    // A::b -> private
    // A::c 不可访问
};
```

## References
[https://blog.csdn.net/u010608296/article/details/86632533](https://blog.csdn.net/u010608296/article/details/86632533)遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/)

[cppreference.com 派生类](https://zh.cppreference.com/w/cpp/language/derived_class)