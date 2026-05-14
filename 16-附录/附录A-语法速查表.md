<!--
  本节最后更新：2026-05-11
  验证环境：无（语法速查——参考章节）
-->

## 附录 A 常用语言与语法速查表

> 本节是快速参考，不是教程。如果你完全没接触过这些语言，建议先通过 Vibe Coding 实际体验，遇到语法问题时回来查阅。

---

### A.1 JavaScript / TypeScript 核心语法

#### A.1.1 变量声明与作用域

```javascript
// var —— 函数作用域，存在变量提升问题，不再推荐使用
var name = "Alice";
function example() {
  console.log(name); // undefined（变量提升）
  var name = "Bob";
}

// let —— 块级作用域，可重新赋值
let count = 0;
count = 1;
if (true) {
  let x = 10;
}
// console.log(x); // ❌ x is not defined

// const —— 块级作用域，不可重新赋值（推荐默认使用）
const pi = 3.14;
// pi = 3.1415; // ❌ 不可重新赋值

const user = { name: "Alice" };
user.name = "Bob"; // ✅ 对象内容可以修改（引用不变）

// 暂时性死区（TDZ）
// console.log(a); // ❌ Cannot access 'a' before initialization
let a = 10;

// 解构赋值中的 TDZ
function test({ a = 1, b = 2 } = {}) {
  console.log(a, b);
}
test(); // 1, 2
```

#### A.1.2 函数定义

```javascript
// 传统函数声明（存在函数提升）
function add(a, b) {
  return a + b;
}

// 函数表达式
const multiply = function(a, b) {
  return a * b;
};

// 箭头函数（现代JS最常用）
const divide = (a, b) => a / b;
const square = x => x * x;

// 带返回值的箭头函数（多行）
const greet = (name) => {
  const message = `Hello, ${name}!`;
  return message;
};

// 默认参数
const introduce = (name, age = 18) => {
  return `${name} is ${age} years old`;
};

// 可选参数
const sayHello = (name) => {
  return `Hello, ${name || "Guest"}!`;
};

// 剩余参数
const sumAll = (...numbers) => {
  return numbers.reduce((sum, num) => sum + num, 0);
};

// 异步函数
async function fetchUser(id) {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}

// 立即执行函数表达式（IIFE）
(function() {
  console.log("立即执行");
})();

// 箭头函数IIFE
(() => {
  console.log("箭头函数IIFE");
})();
```

#### A.1.3 解构赋值与展开运算符

```javascript
// 对象解构
const user = { name: "Alice", age: 30, city: "Beijing" };
const { name, age } = user;
const { name: userName, age: userAge } = user; // 重命名

// 默认值
const { name, age = 18, country = "China" } = user;

// 嵌套解构
const nested = { user: { name: "Alice", address: { city: "Beijing" } } };
const { user: { name, address: { city } } } = nested;

// 数组解构
const colors = ["red", "green", "blue", "yellow"];
const [first, second, third] = colors;
const [, , thirdColor] = colors; // 跳过前两个

// 剩余运算符（收集剩余元素）
const [head, ...rest] = colors; // head="red", rest=["green", "blue", "yellow"]

// 展开运算符（展开数组/对象）
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5]; // [1, 2, 3, 4, 5]

const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 }; // { a: 1, b: 2, c: 3 }

// 合并对象（后面对象覆盖前面）
const merged = { ...obj1, ...obj2 };

// 函数参数展开
const nums = [1, 2, 3];
Math.max(...nums); // 3

// 解构配合展开
const { name, ...rest } = user; // rest = { age: 30, city: "Beijing" }

// 函数参数解构
function printUser({ name, age }) {
  console.log(`${name} is ${age}`);
}
printUser(user);
```

#### A.1.4 数组方法速查

| 方法 | 作用 | 返回值 | 是否修改原数组 |
|------|------|--------|--------------|
| `map()` | 转换每个元素 | 新数组 | 否 |
| `filter()` | 过滤元素 | 新数组 | 否 |
| `reduce()` | 累积计算 | 任意值 | 否 |
| `find()` | 查找第一个匹配元素 | 元素/undefined | 否 |
| `findIndex()` | 查找第一个匹配索引 | 索引/-1 | 否 |
| `some()` | 是否有元素满足条件 | boolean | 否 |
| `every()` | 是否所有元素满足条件 | boolean | 否 |
| `includes()` | 是否包含指定元素 | boolean | 否 |
| `concat()` | 合并数组 | 新数组 | 否 |
| `slice()` | 截取子数组 | 新数组 | 否 |
| `push()` | 末尾添加元素 | 新长度 | 是 |
| `pop()` | 末尾删除元素 | 被删元素 | 是 |
| `shift()` | 开头删除元素 | 被删元素 | 是 |
| `unshift()` | 开头添加元素 | 新长度 | 是 |
| `splice()` | 插入/删除元素 | 被删元素数组 | 是 |
| `sort()` | 排序 | 原数组引用 | 是 |
| `reverse()` | 反转数组 | 原数组引用 | 是 |
| `flat()` | 扁平化数组 | 新数组 | 否 |
| `flatMap()` | 映射后扁平化 | 新数组 | 否 |
| `fill()` | 填充数组 | 原数组 | 是 |
| `indexOf()` | 查找元素索引 | 索引/-1 | 否 |
| `lastIndexOf()` | 从后查找元素索引 | 索引/-1 | 否 |
| `join()` | 数组转字符串 | 字符串 | 否 |
| `toString()` | 数组转字符串 | 字符串 | 否 |

```javascript
// 常用数组操作示例
const numbers = [1, 2, 3, 4, 5];

// map - 转换
const doubled = numbers.map(x => x * 2); // [2, 4, 6, 8, 10]

// filter - 过滤
const evens = numbers.filter(x => x % 2 === 0); // [2, 4]

// reduce - 累积
const sum = numbers.reduce((acc, x) => acc + x, 0); // 15

// find - 查找
const found = numbers.find(x => x > 3); // 4

// flat - 扁平化
const nested = [1, [2, [3, [4]]]];
const flattened = nested.flat(2); // [1, 2, 3, [4]]

// flatMap - 映射并扁平化
const sentences = ["Hello world", "Goodbye world"];
const words = sentences.flatMap(s => s.split(" ")); // ["Hello", "world", "Goodbye", "world"]

// fill - 填充
const filled = new Array(5).fill(0); // [0, 0, 0, 0, 0]
```

#### A.1.5 Promise 和异步编程

```javascript
// Promise 基础
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("success");
    // 或 reject(new Error("failed"));
  }, 1000);
});

promise.then(result => console.log(result))
       .catch(error => console.error(error));

// Promise.all（全部完成）
const promises = [fetch('/api/users'), fetch('/api/posts')];
Promise.all(promises)
  .then(responses => Promise.all(responses.map(r => r.json())))
  .then(data => console.log(data));

// Promise.allSettled（全部完成或失败）
Promise.allSettled(promises)
  .then(results => results.forEach(r => console.log(r.status)));

// Promise.race（第一个完成）
Promise.race([
  fetch('/api/data'),
  new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), 5000))
])
.then(data => console.log(data))
.catch(err => console.error(err));

// Promise.any（第一个成功）
Promise.any([
  Promise.reject('error1'),
  Promise.resolve('success'),
  Promise.reject('error2')
])
.then(result => console.log(result)); // "success"

// async/await（现代异步写法）
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Fetch failed:', error);
    throw error;
  }
}

// 并行执行多个异步操作
async function fetchMultiple() {
  const [users, posts] = await Promise.all([
    fetch('/api/users').then(r => r.json()),
    fetch('/api/posts').then(r => r.json())
  ]);
  return { users, posts };
}

// 串行执行
async function fetchSequentially() {
  const users = await fetch('/api/users').then(r => r.json());
  const posts = await fetch('/api/posts').then(r => r.json());
  return { users, posts };
}

// 异步迭代
async function processItems(items) {
  for await (const item of items) {
    await process(item);
  }
}
```

#### A.1.6 TypeScript 类型系统

```typescript
// 基础类型
const name: string = "Alice";
const age: number = 30;
const isActive: boolean = true;
const list: string[] = ["a", "b", "c"];
const tuple: [string, number] = ["Alice", 30]; // 元组

// 接口定义
interface User {
  id: string;           // 必填字段
  name: string;
  email: string;
  age?: number;         // 可选字段（?标记）
  readonly createdAt: Date;  // 只读字段
}

// 接口继承
interface Admin extends User {
  permissions: string[];
}

// 接口声明合并
interface User {
  avatar?: string;  // 可以添加新属性
}

// 类型别名
type Status = "active" | "inactive" | "pending";
type Point = { x: number; y: number };
type ID = string | number;

// 联合类型与交叉类型
type Result<T, E> = { success: true; data: T } | { success: false; error: E };
type ReadonlyUser = Readonly<User>;  // 内置工具类型
type PartialUser = Partial<User>;    // 全部可选
type PickUser = Pick<User, "name" | "email">; // 挑选字段
type OmitUser = Omit<User, "password">; // 排除字段

// 泛型
interface ApiResponse<T> {
  data: T;
  success: boolean;
  message?: string;
}

// 泛型函数
function identity<T>(arg: T): T {
  return arg;
}

// 泛型类
class Container<T> {
  private items: T[] = [];
  add(item: T): void {
    this.items.push(item);
  }
  get(index: number): T | undefined {
    return this.items[index];
  }
}

// 泛型约束
interface Lengthwise {
  length: number;
}

function logLength<T extends Lengthwise>(arg: T): T {
  console.log(arg.length);
  return arg;
}

// 条件类型
type NonNullable<T> = T extends null | undefined ? never : T;
type ExtractArray<T> = T extends (infer U)[] ? U : never;
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

// 模板字面量类型
type EventName<T extends string> = `${T}Changed`;
type UserEvents = EventName<"name" | "email">; // "nameChanged" | "emailChanged"

// 类型守卫
function isString(value: unknown): value is string {
  return typeof value === "string";
}

// 断言函数
function assertIsNumber(value: unknown): asserts value is number {
  if (typeof value !== "number") {
    throw new Error("Not a number");
  }
}

// 索引类型
type Keys = keyof User; // "id" | "name" | "email" | "age" | "createdAt"
type Values = User[keyof User]; // string | number | Date | undefined

// 映射类型
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};

type Partial<T> = {
  [P in keyof T]?: T[P];
};
```

#### A.1.7 类与面向对象

```typescript
// 类定义
class Person {
  // 私有属性
  private _name: string;
  
  // 构造函数
  constructor(name: string) {
    this._name = name;
  }
  
  // Getter
  get name(): string {
    return this._name;
  }
  
  // Setter
  set name(newName: string) {
    if (newName.length > 0) {
      this._name = newName;
    }
  }
  
  // 方法
  greet(): string {
    return `Hello, ${this._name}!`;
  }
}

// 继承
class Student extends Person {
  constructor(name: string, public studentId: string) {
    super(name);
  }
  
  study(subject: string): string {
    return `${this.name} is studying ${subject}`;
  }
}

// 抽象类
abstract class Shape {
  abstract getArea(): number;
  
  getDescription(): string {
    return `This shape has area: ${this.getArea()}`;
  }
}

class Circle extends Shape {
  constructor(private radius: number) {
    super();
  }
  
  getArea(): number {
    return Math.PI * this.radius ** 2;
  }
}

// 接口实现
interface Printable {
  print(): void;
}

class Document implements Printable {
  print(): void {
    console.log("Printing document...");
  }
}

// 静态成员
class MathUtils {
  static PI = 3.14159;
  
  static calculateArea(radius: number): number {
    return this.PI * radius ** 2;
  }
}

// 私有字段（#语法）
class Counter {
  #count = 0;
  
  increment(): void {
    this.#count++;
  }
  
  get count(): number {
    return this.#count;
  }
}

// 方法重载
class Calculator {
  add(a: number, b: number): number;
  add(a: string, b: string): string;
  add(a: number | string, b: number | string): number | string {
    if (typeof a === "number" && typeof b === "number") {
      return a + b;
    }
    return `${a}${b}`;
  }
}
```

#### A.1.8 模块化与ESM

```typescript
// 导出
export const PI = 3.14;
export function add(a: number, b: number): number {
  return a + b;
}
export class Calculator {}
export type Status = "active" | "inactive";

// 默认导出
export default function greet(name: string): string {
  return `Hello, ${name}!`;
}

// 导入
import { PI, add, Calculator } from "./math";
import Greet from "./greet";
import * as math from "./math";

// 动态导入
async function loadModule() {
  const module = await import("./lazy");
  module.doSomething();
}

// 命名空间导入
import { default as Greet, PI as MathPI } from "./math";

// 重新导出
export { add as sum } from "./math";
export * from "./utils";

// 导入类型（仅类型导入）
import type { User } from "./types";

// 导出类型
export type { Status };
```

#### A.1.9 装饰器（Decorators）

```typescript
// 类装饰器
function sealed(constructor: Function) {
  Object.seal(constructor);
  Object.seal(constructor.prototype);
}

@sealed
class Greeter {
  greeting: string;
  constructor(message: string) {
    this.greeting = message;
  }
  greet() {
    return `Hello, ${this.greeting}`;
  }
}

// 方法装饰器
function enumerable(value: boolean) {
  return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    descriptor.enumerable = value;
  };
}

class Greeter {
  greeting: string;
  constructor(message: string) {
    this.greeting = message;
  }
  
  @enumerable(false)
  greet() {
    return `Hello, ${this.greeting}`;
  }
}

// 属性装饰器
function format(formatString: string) {
  return function (target: any, propertyKey: string) {
    let value = target[propertyKey];
    
    const getter = function () {
      return formatString.replace("%s", value);
    };
    
    const setter = function (newVal: string) {
      value = newVal;
    };
    
    Object.defineProperty(target, propertyKey, {
      get: getter,
      set: setter,
      enumerable: true,
      configurable: true
    });
  };
}

class Greeter {
  @format("Hello, %s!")
  greeting: string;
  
  constructor(message: string) {
    this.greeting = message;
  }
}

// 参数装饰器
function validate(target: any, propertyKey: string, parameterIndex: number) {
  console.log(`Validating parameter at index ${parameterIndex}`);
}

class UserService {
  createUser(@validate name: string, @validate age: number) {
    // ...
  }
}
```

---

### A.2 Python 常用模式

#### A.2.1 变量与数据结构

```python
# 基本类型
name = "Alice"
age = 30
is_active = True
pi = 3.14
big_num = 10**18  # 任意精度整数

# 列表（list）- 可变数组
items = [1, 2, 3]
items.append(4)      # 添加元素
items.insert(0, 0)   # 插入元素
items.remove(2)      # 删除元素
items.pop()          # 弹出最后一个元素
items.extend([5, 6]) # 扩展列表

# 字典（dict）- 键值对
user = {"name": "Alice", "age": 30}
user["city"] = "Beijing"  # 添加键值对
del user["age"]          # 删除键值对
print(user.get("name", "Unknown"))  # 安全获取
keys = user.keys()       # 获取所有键
values = user.values()   # 获取所有值
items = user.items()     # 获取所有键值对

# 元组（tuple）- 不可变序列
point = (10, 20)
single = (5,)  # 单元素元组必须加逗号

# 集合（set）- 无序不重复
unique = {1, 2, 3, 3, 3}  # {1, 2, 3}
unique.add(4)
unique.remove(2)
union = unique | {3, 4, 5}  # 并集
intersection = unique & {2, 3}  # 交集
difference = unique - {3}  # 差集

# 冻结集合（frozenset）- 不可变集合
fs = frozenset([1, 2, 3])

# 字符串操作
s = "Hello, World!"
s.upper()           # "HELLO, WORLD!"
s.lower()           # "hello, world!"
s.strip()           # 去除首尾空白
s.replace("World", "Python")  # "Hello, Python!"
s.split(",")        # ["Hello", " World!"]
", ".join(["a", "b", "c"])  # "a, b, c"
s.startswith("Hello")  # True
s.endswith("!")        # True
s.find("World")        # 7
```

#### A.2.2 列表推导式与生成器

```python
# 基础列表推导
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带条件过滤
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# 嵌套推导（矩阵转置）
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 集合推导
unique_squares = {x**2 for x in [-1, 0, 1, 2]}
# {0, 1, 4}

# 字典推导
squared_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 生成器表达式（内存高效）
gen = (x**2 for x in range(1000000))  # 不立即计算

# 生成器函数
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# 无限生成器
def infinite_counter(start=0):
    while True:
        yield start
        start += 1

# 迭代器协议
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        raise StopIteration
```

#### A.2.3 函数与参数

```python
def add(a: int, b: int) -> int:
    """返回两个数的和"""
    return a + b

# 默认参数
def greet(name: str = "World") -> str:
    return f"Hello, {name}!"

# 可变位置参数（*args）
def sum_all(*args: int) -> int:
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

# 可变关键字参数（**kwargs）
def create_user(**kwargs):
    return kwargs

create_user(name="Alice", age=30)  # {"name": "Alice", "age": 30}

# 解包参数
nums = [1, 2, 3]
sum_all(*nums)  # 相当于 sum_all(1, 2, 3)

config = {"host": "localhost", "port": 5432}
# connect(**config)  # 相当于 connect(host="localhost", port=5432)

# Lambda 函数
square = lambda x: x ** 2

# 高阶函数
def apply(func, value):
    return func(value)

apply(lambda x: x * 2, 5)  # 10

# 匿名函数作为参数
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# 函数注解
def calculate(
    x: int,
    y: int,
    operation: str = "add"
) -> int:
    """
    计算两个数的运算结果
    
    Args:
        x: 第一个数字
        y: 第二个数字
        operation: 运算类型，可选值: "add", "subtract", "multiply", "divide"
    
    Returns:
        运算结果
    """
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        return x / y
    else:
        raise ValueError(f"Unknown operation: {operation}")
```

#### A.2.4 类与面向对象

```python
class Person:
    # 类属性（所有实例共享）
    species = "Homo sapiens"
    
    # 初始化方法
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    # 实例方法
    def greet(self) -> str:
        return f"Hello, my name is {self.name}"
    
    # 类方法
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        current_year = 2024
        return cls(name, current_year - birth_year)
    
    # 静态方法
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

# 创建实例
person = Person("Alice", 30)
person.greet()  # "Hello, my name is Alice"

# 继承
class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self, subject: str) -> str:
        return f"{self.name} is studying {subject}"

# 特殊方法（魔术方法）
class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v1 + v2  # Vector(4, 6)
v1 * 2   # Vector(2, 4)

# 属性装饰器
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

# 抽象基类
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass
    
    @abstractmethod
    def get_perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def get_area(self) -> float:
        return 3.14159 * self.radius ** 2
    
    def get_perimeter(self) -> float:
        return 2 * 3.14159 * self.radius
```

#### A.2.5 装饰器

```python
# 基础装饰器
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

add(2, 3)
# Output:
# Calling add with args=(2, 3), kwargs={}
# add returned 5

# 带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    return f"Hello, {name}!"

greet("Alice")  # ["Hello, Alice!", "Hello, Alice!", "Hello, Alice!"]

# 保留元数据的装饰器
import functools

def log_decorator(func):
    @functools.wraps(func)  # 保留原函数元数据
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    """Return sum of two numbers"""
    return a + b

# 装饰器类
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 多个装饰器叠加
@log_decorator
@repeat(times=2)
def say_hello():
    return "Hello!"

# 装饰器用于类型检查
def type_check(*arg_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            for arg, expected_type in zip(args, arg_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Expected {expected_type}, got {type(arg)}")
            return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def multiply(a, b):
    return a * b
```

#### A.2.6 上下文管理器

```python
# 使用 with 语句
with open("file.txt", "r") as f:
    content = f.read()
# 文件自动关闭

# 自定义上下文管理器（类方式）
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"Elapsed time: {elapsed:.2f}s")
        return False

with Timer():
    for _ in range(1000000):
        pass

# 自定义上下文管理器（装饰器方式）
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"Elapsed: {elapsed:.2f}s")

with timer():
    pass

# 嵌套上下文管理器
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content)

# 自定义资源管理
class DatabaseConnection:
    def __init__(self, db_url):
        self.db_url = db_url
        self.connection = None
    
    def __enter__(self):
        self.connection = self.connect()
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
        return False  # 不抑制异常
    
    def connect(self):
        print(f"Connecting to {self.db_url}")
        return {"connection": "active"}

# 使用
with DatabaseConnection("postgresql://localhost/mydb") as conn:
    print("Using connection:", conn)

# 使用 contextmanager 装饰器创建临时文件
from contextlib import contextmanager
import tempfile
import os

@contextmanager
def temp_file():
    fd, path = tempfile.mkstemp()
    try:
        yield path
    finally:
        os.close(fd)
        os.remove(path)

with temp_file() as filepath:
    print(f"Working with temp file: {filepath}")
```

#### A.2.7 常用标准库

| 模块 | 用途 | 常用功能 |
|------|------|---------|
| `os` | 操作系统接口 | 文件/目录操作、环境变量 |
| `sys` | 系统参数与函数 | 命令行参数、退出码 |
| `json` | JSON 序列化 | dump/load, dumps/loads |
| `datetime` | 日期时间处理 | datetime, date, time |
| `re` | 正则表达式 | 匹配、替换、分割 |
| `collections` | 数据结构 | defaultdict, OrderedDict, Counter |
| `itertools` | 迭代工具 | 循环、组合、排列 |
| `functools` | 函数工具 | partial, lru_cache, reduce |
| `asyncio` | 异步编程 | 协程、事件循环 |
| `unittest` | 测试框架 | TestCase, mock |
| `logging` | 日志记录 | 日志级别、格式、处理器 |
| `argparse` | 命令行参数解析 | 参数定义、帮助信息 |
| `pathlib` | 文件路径操作 | 面向对象的路径处理 |
| `urllib` | URL 处理 | 解析、请求 |
| `hashlib` | 哈希函数 | md5, sha256 |

#### A.2.8 Python 异步编程

```python
import asyncio

# 基础协程
async def fetch_data(url):
    print(f"Fetching {url}")
    await asyncio.sleep(1)  # 模拟IO操作
    return {"url": url, "data": "sample"}

# 并发执行多个协程
async def main():
    # 方式1: asyncio.gather
    results = await asyncio.gather(
        fetch_data("https://api.example.com/users"),
        fetch_data("https://api.example.com/posts"),
        fetch_data("https://api.example.com/comments")
    )
    print(results)
    
    # 方式2: 创建任务
    task1 = asyncio.create_task(fetch_data("https://api.example.com/a"))
    task2 = asyncio.create_task(fetch_data("https://api.example.com/b"))
    
    await task1
    await task2

# 运行事件循环
asyncio.run(main())

# 带超时的等待
async def fetch_with_timeout(url, timeout=5):
    try:
        return await asyncio.wait_for(fetch_data(url), timeout=timeout)
    except asyncio.TimeoutError:
        print(f"Timeout fetching {url}")
        return None

# 并发限制（Semaphore）
async def limited_fetch(url, semaphore):
    async with semaphore:
        return await fetch_data(url)

async def fetch_all(urls):
    semaphore = asyncio.Semaphore(10)  # 最多10个并发
    tasks = [limited_fetch(url, semaphore) for url in urls]
    return await asyncio.gather(*tasks)

# 异步迭代器
async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def iterate():
    async for num in async_range(5):
        print(num)

# 异步生成器
async def async_generator():
    for i in range(10):
        await asyncio.sleep(0.1)
        yield i * 2

# 任务取消
async def long_running_task():
    try:
        for i in range(10):
            await asyncio.sleep(1)
            print(f"Task running: {i}")
    except asyncio.CancelledError:
        print("Task was cancelled")
        raise

async def cancel_task():
    task = asyncio.create_task(long_running_task())
    await asyncio.sleep(3)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task cancellation confirmed")
```

---

### A.3 HTML / CSS 关键布局速览

#### A.3.1 HTML 文档基础结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="页面描述">
  <meta name="keywords" content="关键词1, 关键词2">
  <meta name="author" content="作者名">
  <title>页面标题</title>
  <link rel="stylesheet" href="style.css">
  <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
  <header>页眉</header>
  <nav>导航</nav>
  <main>
    <article>主要内容</article>
    <aside>侧边栏</aside>
  </main>
  <footer>页脚</footer>
  <script src="app.js" defer></script>
</body>
</html>
```

#### A.3.2 常用语义标签

| 标签 | 语义 | 常用属性 |
|------|------|---------|
| `<header>` | 页面/区块头部 | 无 |
| `<nav>` | 导航链接 | 无 |
| `<main>` | 主要内容（唯一） | 无 |
| `<article>` | 独立内容区块 | 无 |
| `<section>` | 内容分区 | 无 |
| `<aside>` | 侧边内容 | 无 |
| `<footer>` | 页面/区块底部 | 无 |
| `<a>` | 链接 | href, target, rel |
| `<img>` | 图片 | src, alt, width, height |
| `<input>` | 输入框 | type, name, value, placeholder |
| `<button>` | 按钮 | type, disabled |
| `<form>` | 表单 | action, method, enctype |
| `<label>` | 标签 | for |
| `<textarea>` | 多行文本输入 | rows, cols |
| `<select>` | 下拉选择 | name |
| `<option>` | 选项 | value, selected |
| `<table>` | 表格 | border |
| `<thead>` | 表格头部 | 无 |
| `<tbody>` | 表格主体 | 无 |
| `<tr>` | 表格行 | 无 |
| `<th>` | 表头单元格 | scope |
| `<td>` | 表格单元格 | 无 |

#### A.3.3 HTML5 表单输入类型

| type 值 | 用途 | 特点 |
|---------|------|------|
| `text` | 普通文本 | 单行文本输入 |
| `email` | 邮箱地址 | 自动验证格式 |
| `password` | 密码 | 输入内容隐藏 |
| `number` | 数字输入 | 显示数字键盘 |
| `tel` | 电话号码 | 显示电话键盘 |
| `url` | 网址 | 自动验证格式 |
| `date` | 日期选择 | 显示日期选择器 |
| `time` | 时间选择 | 显示时间选择器 |
| `datetime-local` | 日期时间 | 本地日期时间选择器 |
| `range` | 滑块 | 范围选择 |
| `checkbox` | 复选框 | 可多选 |
| `radio` | 单选按钮 | 同组互斥 |
| `file` | 文件上传 | 支持 multiple 属性 |
| `color` | 颜色选择 | 显示颜色选择器 |
| `search` | 搜索框 | 样式优化 |
| `hidden` | 隐藏字段 | 不显示但提交 |

#### A.3.4 Flexbox 布局（最常用）

```css
/* 容器属性 */
.container {
  display: flex;              /* 启用 Flexbox */
  flex-direction: row;        /* row | row-reverse | column | column-reverse */
  justify-content: flex-start;/* flex-start | center | flex-end | space-between | space-around | space-evenly */
  align-items: stretch;       /* stretch | flex-start | center | flex-end | baseline */
  flex-wrap: nowrap;          /* nowrap | wrap | wrap-reverse */
  gap: 16px;                 /* 项目间距 */
  align-content: stretch;     /* flex-start | center | flex-end | space-between | space-around | stretch */
}

/* 项目属性 */
.item {
  flex-grow: 0;              /* 放大比例 */
  flex-shrink: 1;            /* 缩小比例 */
  flex-basis: auto;          /* 基础大小 */
  flex: 1;                   /* 简写: flex-grow flex-shrink flex-basis */
  align-self: auto;          /* 单独对齐方式 */
  order: 0;                  /* 排列顺序 */
}

/* 常用布局示例 */
/* 水平居中 */
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 两栏布局 */
.two-columns {
  display: flex;
  gap: 16px;
}
.sidebar { width: 250px; flex-shrink: 0; }
.main { flex: 1; }

/* 响应式换行 */
.wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

/* 等分布局 */
.equal-width {
  display: flex;
}
.equal-width > * {
  flex: 1;
}

/* 固定侧边栏，内容自适应 */
.layout {
  display: flex;
}
.aside {
  width: 200px;
  flex-shrink: 0;
}
.content {
  flex: 1;
  min-width: 0; /* 防止内容溢出 */
}
```

#### A.3.5 Grid 布局

```css
/* 容器属性 */
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* 三列等宽 */
  grid-template-rows: auto;               /* 行高自动 */
  gap: 16px;                              /* 间距 */
  
  /* 区域命名 */
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
}

/* 项目定位 */
.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }

/* 响应式列数 */
@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;  /* 单列 */
    grid-template-areas:
      "header"
      "sidebar"
      "main"
      "footer";
  }
}

/* 跨越多个单元格 */
.span-two {
  grid-column: span 2;  /* 跨越2列 */
  grid-row: span 2;     /* 跨越2行 */
}

/* 精确位置 */
.item {
  grid-column: 2 / 4;   /* 从第2列到第4列 */
  grid-row: 1 / 3;      /* 从第1行到第3行 */
}

/* 命名网格线 */
.grid-lines {
  display: grid;
  grid-template-columns: [sidebar-start] 200px [sidebar-end content-start] 1fr [content-end];
  grid-template-rows: [header-start] 100px [header-end content-start] 1fr [content-end];
}

/* 自动填充 */
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
}
```

#### A.3.6 CSS 选择器优先级

| 优先级 | 选择器类型 | 示例 | 权重值 |
|--------|------------|------|--------|
| 1（最高） | !important | `color: red !important` | 无限 |
| 2 | 内联样式 | `<div style="color: red">` | 1000 |
| 3 | ID 选择器 | `#header` | 100 |
| 4 | 类选择器 | `.btn` | 10 |
| 4 | 伪类 | `:hover`, `:nth-child(2)` | 10 |
| 4 | 属性选择器 | `[type="text"]` | 10 |
| 5（最低） | 元素选择器 | `div`, `p` | 1 |
| 5 | 伪元素 | `::before`, `::after` | 1 |

```css
/* 选择器组合示例 */
/* 权重: 100 + 10 = 110 */
#header .logo { }

/* 权重: 10 + 1 = 11 */
.container p { }

/* 权重: 10 + 10 + 1 = 21 */
.btn.primary:hover { }
```

#### A.3.7 CSS 常用属性速查

| 属性类别 | 属性 | 常用值 |
|----------|------|--------|
| 布局 | `display` | block, inline, inline-block, flex, grid, none |
| 布局 | `position` | static, relative, absolute, fixed, sticky |
| 布局 | `float` | left, right, none |
| 布局 | `clear` | left, right, both |
| 盒模型 | `margin` | length, auto |
| 盒模型 | `padding` | length |
| 盒模型 | `border` | width style color |
| 盒模型 | `box-sizing` | content-box, border-box |
| 文本 | `font-size` | px, em, rem, % |
| 文本 | `font-weight` | normal, bold, 100-900 |
| 文本 | `text-align` | left, right, center, justify |
| 文本 | `text-decoration` | none, underline, line-through |
| 文本 | `line-height` | number, length, % |
| 颜色 | `color` | color name, #hex, rgb(), rgba() |
| 背景 | `background` | color, image, gradient |
| 尺寸 | `width/height` | length, %, auto |
| 尺寸 | `min-width/min-height` | length, % |
| 尺寸 | `max-width/max-height` | length, % |
| 圆角 | `border-radius` | length, % |
| 阴影 | `box-shadow` | offset-x offset-y blur spread color |
| 阴影 | `text-shadow` | offset-x offset-y blur color |
| 动画 | `transition` | property duration timing |
| 动画 | `animation` | name duration timing iteration |
| 变换 | `transform` | translate, rotate, scale, skew |
| 溢出 | `overflow` | visible, hidden, scroll, auto |
| 光标 | `cursor` | pointer, default, text, move |
| 不透明度 | `opacity` | 0-1 |

#### A.3.8 CSS 响应式设计

```css
/* 媒体查询基础 */
@media (max-width: 768px) {
  .container {
    padding: 0 16px;
  }
}

/* 多个断点 */
@media (min-width: 768px) and (max-width: 1024px) {
  .sidebar {
    width: 200px;
  }
}

/* 移动端优先 */
.container {
  padding: 0 12px;
}

@media (min-width: 640px) {
  .container {
    padding: 0 24px;
  }
}

@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
}

/* 响应式网格 */
.responsive-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 640px) {
  .responsive-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .responsive-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* 隐藏元素 */
@media (max-width: 640px) {
  .desktop-only {
    display: none;
  }
}

@media (min-width: 641px) {
  .mobile-only {
    display: none;
  }
}

/* 弹性图片 */
img {
  max-width: 100%;
  height: auto;
}

/* 响应式字体大小 */
html {
  font-size: 16px;
}

@media (min-width: 768px) {
  html {
    font-size: 18px;
  }
}

@media (min-width: 1024px) {
  html {
    font-size: 20px;
  }
}
```

#### A.3.9 CSS 动画与过渡

```css
/* 过渡动画 */
.button {
  transition: background-color 0.3s ease, transform 0.2s;
}

.button:hover {
  background-color: #007bff;
  transform: translateY(-2px);
}

.button:active {
  transform: translateY(0);
}

/* 关键帧动画 */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}

@keyframes slideIn {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* 使用动画 */
.card {
  animation: fadeIn 0.5s ease-out forwards;
}

.loader {
  animation: pulse 1.5s ease-in-out infinite;
}

.sidebar {
  animation: slideIn 0.3s ease-out;
}

.bouncing-ball {
  animation: bounce 0.5s ease-in-out infinite;
}

.spinner {
  animation: rotate 2s linear infinite;
}

/* 动画延迟 */
.card:nth-child(2) {
  animation-delay: 0.1s;
}

.card:nth-child(3) {
  animation-delay: 0.2s;
}

.card:nth-child(4) {
  animation-delay: 0.3s;
}

/* 性能优化 */
.animated-element {
  will-change: transform, opacity;
  backface-visibility: hidden;
  transform-style: preserve-3d;
}
```

#### A.3.10 CSS 高级选择器

```css
/* 属性选择器 */
input[type="text"] {
  border: 1px solid #ccc;
}

a[href^="https://"] {
  color: #007bff;
}

img[src$=".png"] {
  border-radius: 8px;
}

a[href*="example"] {
  font-weight: bold;
}

/* 伪类选择器 */
li:nth-child(odd) {
  background-color: #f8f9fa;
}

li:nth-child(3n) {
  border-right: 2px solid #007bff;
}

input:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25);
}

button:not(:disabled):hover {
  background-color: #0056b3;
}

p:first-of-type {
  margin-top: 0;
}

p:last-of-type {
  margin-bottom: 0;
}

/* 伪元素选择器 */
p::first-line {
  font-weight: bold;
}

p::first-letter {
  font-size: 2em;
  float: left;
  margin-right: 0.5em;
}

.clearfix::after {
  content: "";
  display: table;
  clear: both;
}

.tooltip::before {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  padding: 4px 8px;
  background-color: #333;
  color: white;
  border-radius: 4px;
  font-size: 12px;
  white-space: nowrap;
  opacity: 0;
  transition: opacity 0.2s;
}

.tooltip:hover::before {
  opacity: 1;
}

/* 组合选择器 */
header > nav > ul > li {
  display: inline-block;
}

article + article {
  margin-top: 24px;
  padding-top: 24px;
  border-top: 1px solid #eee;
}

section ~ footer {
  margin-top: 48px;
}

/* :is() 选择器（简化选择器列表） */
:is(header, footer, aside) {
  background-color: #f8f9fa;
}

/* :where() 选择器（权重为0） */
:where(.btn, .link) {
  color: #007bff;
}

/* :has() 选择器（父选择器） */
.card:has(.featured) {
  border-color: #007bff;
}

/* :not() 否定选择器 */
div:not(.special) {
  opacity: 0.5;
}
```

---

### A.4 SQL 基础查询

#### A.4.1 基础语句

```sql
-- 查询指定列
SELECT column1, column2 FROM table_name;

-- 查询所有列（生产环境慎用）
SELECT * FROM users;

-- 条件过滤
SELECT * FROM users WHERE age > 18;

-- 排序
SELECT * FROM users ORDER BY created_at DESC;

-- 限制数量
SELECT * FROM users LIMIT 10;

-- 分页
SELECT * FROM users LIMIT 10 OFFSET 20;

-- 去重
SELECT DISTINCT category FROM products;

-- 计数
SELECT COUNT(*) FROM users;

-- 别名
SELECT name AS username, age AS user_age FROM users;

-- 计算列
SELECT name, price * quantity AS total FROM orders;

-- 字符串拼接（PostgreSQL）
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users;

-- 字符串拼接（MySQL）
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users;

-- 字符串拼接（SQL Server）
SELECT first_name + ' ' + last_name AS full_name FROM users;
```

#### A.4.2 WHERE 子句条件运算符

| 运算符 | 描述 | 示例 |
|--------|------|------|
| `=` | 等于 | `WHERE name = 'Alice'` |
| `<>` / `!=` | 不等于 | `WHERE status <> 'deleted'` |
| `>` | 大于 | `WHERE price > 100` |
| `<` | 小于 | `WHERE age < 18` |
| `>=` | 大于等于 | `WHERE score >= 60` |
| `<=` | 小于等于 | `WHERE created_at <= '2024-01-01'` |
| `BETWEEN` | 在范围内 | `WHERE price BETWEEN 100 AND 200` |
| `IN` | 在列表中 | `WHERE status IN ('active', 'pending')` |
| `LIKE` | 模糊匹配 | `WHERE name LIKE '%Alice%'` |
| `ILIKE` | 大小写不敏感模糊匹配（PostgreSQL） | `WHERE name ILIKE '%alice%'` |
| `IS NULL` | 为空 | `WHERE deleted_at IS NULL` |
| `IS NOT NULL` | 不为空 | `WHERE deleted_at IS NOT NULL` |
| `AND` | 逻辑与 | `WHERE age > 18 AND status = 'active'` |
| `OR` | 逻辑或 | `WHERE category = 'book' OR price < 50` |
| `NOT` | 逻辑非 | `WHERE NOT status = 'deleted'` |

#### A.4.3 数据操作语句（DML）

```sql
-- 插入单条数据
INSERT INTO users (name, email, age) 
VALUES ('Alice', 'alice@example.com', 30);

-- 返回插入的行（PostgreSQL）
INSERT INTO users (name, email) 
VALUES ('Bob', 'bob@example.com')
RETURNING *;

-- 批量插入
INSERT INTO users (name, email) 
VALUES ('Bob', 'bob@example.com'),
       ('Charlie', 'charlie@example.com');

-- 更新数据
UPDATE users 
SET name = 'Alice Smith', age = 31 
WHERE id = 1;

-- 更新多个表（PostgreSQL）
UPDATE users u
SET last_login = CURRENT_TIMESTAMP
FROM sessions s
WHERE u.id = s.user_id
  AND s.expires_at > CURRENT_TIMESTAMP;

-- 删除数据
DELETE FROM users 
WHERE id = 1;

-- 删除并返回（PostgreSQL）
DELETE FROM users 
WHERE status = 'inactive'
RETURNING *;

-- 截断表（清空所有数据）
TRUNCATE TABLE users;

-- 截断表并重置序列（PostgreSQL）
TRUNCATE TABLE users RESTART IDENTITY;

-- 合并（Upsert，PostgreSQL）
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com')
ON CONFLICT (id) DO UPDATE SET
  name = EXCLUDED.name,
  email = EXCLUDED.email;

-- 合并（MySQL）
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'alice@example.com')
ON DUPLICATE KEY UPDATE
  name = VALUES(name),
  email = VALUES(email);
```

#### A.4.4 JOIN 关联查询

| JOIN 类型 | 说明 | 语法示例 |
|-----------|------|---------|
| INNER JOIN | 只返回两表匹配的行 | `SELECT * FROM a INNER JOIN b ON a.id = b.a_id` |
| LEFT JOIN | 返回左表所有行，右表匹配的行 | `SELECT * FROM a LEFT JOIN b ON a.id = b.a_id` |
| RIGHT JOIN | 返回右表所有行，左表匹配的行 | `SELECT * FROM a RIGHT JOIN b ON a.id = b.a_id` |
| FULL JOIN | 返回两表所有行 | `SELECT * FROM a FULL JOIN b ON a.id = b.a_id` |
| CROSS JOIN | 笛卡尔积 | `SELECT * FROM a CROSS JOIN b` |
| NATURAL JOIN | 自动按同名列匹配 | `SELECT * FROM a NATURAL JOIN b` |

```sql
-- JOIN 示例
SELECT orders.id, users.name, orders.total
FROM orders
JOIN users ON orders.user_id = users.id
WHERE orders.status = 'completed';

-- 多表 JOIN
SELECT o.id, u.name, p.name AS product_name, o.total
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.created_at >= '2024-01-01';

-- 自 JOIN
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- LEFT JOIN 查找不存在的记录
SELECT u.id, u.name
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

#### A.4.5 聚合函数

| 函数 | 作用 | 示例 |
|------|------|------|
| `COUNT()` | 计数 | `COUNT(*)` |
| `SUM()` | 求和 | `SUM(price)` |
| `AVG()` | 平均值 | `AVG(score)` |
| `MAX()` | 最大值 | `MAX(created_at)` |
| `MIN()` | 最小值 | `MIN(price)` |
| `GROUP_CONCAT()` | 字符串拼接（MySQL） | `GROUP_CONCAT(name)` |
| `STRING_AGG()` | 字符串拼接（PostgreSQL） | `STRING_AGG(name, ', ')` |
| `ARRAY_AGG()` | 数组聚合（PostgreSQL） | `ARRAY_AGG(name)` |
| `STDDEV()` | 标准差 | `STDDEV(score)` |
| `VARIANCE()` | 方差 | `VARIANCE(score)` |

```sql
-- GROUP BY 分组聚合
SELECT category, COUNT(*) as count, AVG(price) as avg_price
FROM products
GROUP BY category
HAVING COUNT(*) > 10;

-- ROLLUP（小计和总计）
SELECT category, brand, SUM(quantity) as total
FROM products
GROUP BY ROLLUP(category, brand);

-- CUBE（所有组合）
SELECT category, brand, SUM(quantity) as total
FROM products
GROUP BY CUBE(category, brand);
```

#### A.4.6 子查询与CTE

```sql
-- 子查询
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- 相关子查询
SELECT name, 
       (SELECT COUNT(*) FROM orders WHERE orders.product_id = products.id) as order_count
FROM products;

-- EXISTS 子查询
SELECT name
FROM products p
WHERE EXISTS (
  SELECT 1 FROM orders o 
  WHERE o.product_id = p.id 
    AND o.order_date >= '2024-01-01'
);

-- NOT EXISTS 子查询
SELECT name
FROM users u
WHERE NOT EXISTS (
  SELECT 1 FROM orders o 
  WHERE o.user_id = u.id
);

-- IN 子查询
SELECT *
FROM products
WHERE category IN (
  SELECT category FROM categories WHERE is_active = true
);

-- CTE（公共表表达式）
WITH monthly_sales AS (
  SELECT 
    DATE_TRUNC('month', order_date) as month,
    SUM(total) as total_sales
  FROM orders
  GROUP BY DATE_TRUNC('month', order_date)
)
SELECT 
  month,
  total_sales,
  LAG(total_sales) OVER (ORDER BY month) as previous_month,
  ROUND((total_sales - LAG(total_sales) OVER (ORDER BY month)) * 100.0 / LAG(total_sales) OVER (ORDER BY month), 2) as growth_rate
FROM monthly_sales;

-- 多CTE
WITH 
  active_users AS (
    SELECT id, name FROM users WHERE status = 'active'
  ),
  user_orders AS (
    SELECT user_id, COUNT(*) as order_count 
    FROM orders 
    WHERE created_at >= '2024-01-01'
    GROUP BY user_id
  )
SELECT au.name, COALESCE(uo.order_count, 0) as orders
FROM active_users au
LEFT JOIN user_orders uo ON au.id = uo.user_id
ORDER BY orders DESC;

-- 递归CTE（树形结构）
WITH RECURSIVE category_tree AS (
  SELECT id, name, parent_id, 1 as level
  FROM categories
  WHERE parent_id IS NULL
  UNION ALL
  SELECT c.id, c.name, c.parent_id, ct.level + 1
  FROM categories c
  JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree ORDER BY level, name;
```

#### A.4.7 窗口函数

```sql
-- 基本窗口函数
SELECT 
  name,
  department,
  salary,
  AVG(salary) OVER (PARTITION BY department) as avg_dept_salary,
  ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank
FROM employees;

-- 排名函数
SELECT 
  name,
  score,
  ROW_NUMBER() OVER (ORDER BY score DESC) as row_num,
  RANK() OVER (ORDER BY score DESC) as rank,
  DENSE_RANK() OVER (ORDER BY score DESC) as dense_rank
FROM students;

-- LAG 和 LEAD
SELECT 
  date,
  sales,
  LAG(sales) OVER (ORDER BY date) as previous_day,
  LEAD(sales) OVER (ORDER BY date) as next_day,
  sales - LAG(sales) OVER (ORDER BY date) as daily_change
FROM daily_sales;

-- 累计求和
SELECT 
  date,
  sales,
  SUM(sales) OVER (ORDER BY date) as cumulative_sales,
  SUM(sales) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as weekly_avg
FROM daily_sales;

-- 窗口帧
SELECT 
  id,
  value,
  AVG(value) OVER (ORDER BY id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) as moving_avg
FROM metrics;

-- NTILE（分桶）
SELECT 
  name,
  salary,
  NTILE(4) OVER (ORDER BY salary DESC) as quartile
FROM employees;

-- FIRST_VALUE 和 LAST_VALUE
SELECT 
  department,
  name,
  salary,
  FIRST_VALUE(salary) OVER (PARTITION BY department ORDER BY salary DESC) as highest_salary,
  LAST_VALUE(salary) OVER (PARTITION BY department ORDER BY salary DESC ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) as lowest_salary
FROM employees;

#### A.4.8 数据库设计基础

```sql
-- 创建表
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(100) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 添加外键约束
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  total NUMERIC(10, 2) NOT NULL,
  status VARCHAR(20) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建索引
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_created_at ON orders(created_at);

-- 复合索引
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- 唯一索引
CREATE UNIQUE INDEX idx_users_username ON users(username);

-- 视图
CREATE VIEW active_users AS
SELECT id, username, email
FROM users
WHERE created_at >= NOW() - INTERVAL '30 days';

-- 触发器（自动更新时间戳）
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_users_modtime
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

-- 存储过程
CREATE OR REPLACE FUNCTION get_user_orders(user_id INT)
RETURNS TABLE(order_id INT, total NUMERIC, status VARCHAR) AS $$
BEGIN
  RETURN QUERY
  SELECT id, total, status
  FROM orders
  WHERE orders.user_id = get_user_orders.user_id
  ORDER BY created_at DESC;
END;
$$ LANGUAGE plpgsql;

-- 序列
CREATE SEQUENCE order_id_seq START WITH 1 INCREMENT BY 1;

-- 检查约束
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price NUMERIC(10, 2) NOT NULL CHECK (price > 0),
  stock INT NOT NULL CHECK (stock >= 0)
);

-- 枚举类型（PostgreSQL）
CREATE TYPE order_status AS ENUM ('pending', 'processing', 'completed', 'cancelled');

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  status order_status DEFAULT 'pending'
);
```

#### A.4.9 SQL 性能优化

```sql
-- 避免 SELECT *
-- 坏
SELECT * FROM users;
-- 好
SELECT id, name, email FROM users;

-- 使用索引
-- 确保 WHERE 条件和 JOIN 条件上有索引
SELECT * FROM orders WHERE user_id = 123; -- 需要 idx_orders_user_id

-- 避免在索引列上使用函数
-- 坏（无法使用索引）
SELECT * FROM users WHERE UPPER(email) = 'ALICE@EXAMPLE.COM';
-- 好
SELECT * FROM users WHERE email = 'alice@example.com';

-- 使用 LIMIT 限制结果
SELECT * FROM logs ORDER BY created_at DESC LIMIT 100;

-- 避免 N+1 查询
-- 坏（N+1 查询）
SELECT * FROM users;
-- 然后对每个用户执行 SELECT * FROM orders WHERE user_id = ?

-- 好（JOIN 或预加载）
SELECT u.*, o.*
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.id = 123;

-- 使用 EXISTS 替代 IN
-- 当子查询结果很大时，EXISTS 更高效
SELECT name
FROM products p
WHERE EXISTS (
  SELECT 1 FROM orders o 
  WHERE o.product_id = p.id
);

-- 使用 UNION ALL 替代 UNION
-- UNION 会去重，UNION ALL 不会，更快
SELECT name FROM users
UNION ALL
SELECT name FROM admins;

-- 分析查询计划
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123;
```

---

### A.5 终端命令速查

#### A.5.1 文件系统操作

| 命令 | 作用 | 常用示例 |
|------|------|---------|
| `ls` | 列出目录内容 | `ls -la`（显示所有文件） |
| `cd` | 切换目录 | `cd projects/my-app` |
| `pwd` | 显示当前路径 | `pwd` |
| `mkdir` | 创建目录 | `mkdir -p a/b/c`（递归创建） |
| `rm` | 删除文件/目录 | `rm -rf dir`（⚠️ 慎用） |
| `cp` | 复制 | `cp file.txt backup/` |
| `mv` | 移动/重命名 | `mv old.txt new.txt` |
| `touch` | 创建空文件 | `touch app.js` |
| `cat` | 查看文件内容 | `cat file.txt` |
| `less` | 分页查看 | `less file.txt` |
| `head` | 查看文件开头 | `head -20 file.txt` |
| `tail` | 查看文件末尾 | `tail -f log.txt`（实时监控） |
| `find` | 查找文件 | `find . -name "*.py"` |
| `grep` | 搜索文本 | `grep "error" log.txt` |
| `ln` | 创建链接 | `ln -s target linkname`（软链接） |
| `chmod` | 修改权限 | `chmod 755 script.sh` |
| `chown` | 修改所有者 | `chown user:group file.txt` |
| `du` | 查看目录大小 | `du -sh .`（人类可读） |
| `df` | 查看磁盘空间 | `df -h`（人类可读） |

#### A.5.2 搜索与文本处理

| 命令 | 作用 | 常用示例 |
|------|------|---------|
| `grep` | 搜索文本 | `grep "error" log.txt` |
| `grep -r` | 递归搜索 | `grep -r "TODO" .` |
| `grep -i` | 忽略大小写 | `grep -i "Error" log.txt` |
| `grep -v` | 反向匹配 | `grep -v "DEBUG" log.txt` |
| `find` | 查找文件 | `find . -name "*.py"` |
| `find -type f` | 查找文件（非目录） | `find . -type f -name "*.js"` |
| `sed` | 文本替换 | `sed 's/old/new/g' file.txt` |
| `sed -i` | 原地替换 | `sed -i 's/old/new/g' file.txt` |
| `awk` | 文本处理 | `awk '{print $1}' file.txt` |
| `cut` | 提取字段 | `cut -d',' -f1 file.csv` |
| `sort` | 排序 | `sort file.txt` |
| `sort -r` | 反向排序 | `sort -r file.txt` |
| `uniq` | 去重 | `sort file.txt \| uniq` |
| `wc` | 统计 | `wc -l file.txt`（行数） |
| `tr` | 字符替换 | `tr '[:lower:]' '[:upper:]'` |
| `cut` | 截取 | `cut -c 1-10 file.txt` |

#### A.5.3 网络与进程

| 命令 | 作用 | 常用示例 |
|------|------|---------|
| `curl` | HTTP 请求 | `curl https://api.example.com` |
| `curl -X POST` | POST 请求 | `curl -X POST -d '{"name":"Alice"}' https://api.example.com` |
| `curl -H` | 添加请求头 | `curl -H "Authorization: Bearer token" https://api.example.com` |
| `wget` | 下载文件 | `wget https://example.com/file.zip` |
| `ps` | 查看进程 | `ps aux` |
| `ps aux \| grep` | 查找进程 | `ps aux \| grep node` |
| `kill` | 终止进程 | `kill -9 PID` |
| `killall` | 终止所有同名进程 | `killall node` |
| `netstat` | 网络状态 | `netstat -tlnp` |
| `ss` | 网络连接 | `ss -tlnp`（比 netstat 更快） |
| `ping` | 网络连通性 | `ping google.com` |
| `dig` | DNS 查询 | `dig example.com` |
| `nslookup` | DNS 查询 | `nslookup example.com` |
| `traceroute` | 路由追踪 | `traceroute google.com` |
| `mtr` | 网络诊断 | `mtr google.com` |

#### A.5.4 文件内容操作

```bash
# 查看文件内容
cat file.txt          # 显示全部内容
less file.txt         # 分页查看（按 q 退出）
head -20 file.txt     # 查看前20行
tail -20 file.txt     # 查看后20行
tail -f log.txt       # 实时监控文件

# 编辑文件
nano file.txt         # 简单编辑器
vim file.txt          # 强大编辑器

# 比较文件
diff file1.txt file2.txt    # 显示差异
diff -u file1.txt file2.txt # 统一格式
comm file1.txt file2.txt    # 逐行比较

# 文件压缩
tar -czvf archive.tar.gz dir/   # 创建压缩包
tar -xzvf archive.tar.gz       # 解压压缩包
zip archive.zip file1.txt file2.txt  # 创建 zip
unzip archive.zip              # 解压 zip

# 文件权限
chmod 755 script.sh   # rwxr-xr-x
chmod +x script.sh    # 添加执行权限
chmod -w file.txt     # 移除写权限
```

#### A.5.5 系统信息

| 命令 | 作用 | 常用示例 |
|------|------|---------|
| `uname` | 系统信息 | `uname -a` |
| `whoami` | 当前用户 | `whoami` |
| `date` | 当前时间 | `date` |
| `uptime` | 系统运行时间 | `uptime` |
| `free` | 内存使用 | `free -h` |
| `top` | 进程监控 | `top` |
| `htop` | 进程监控（更友好） | `htop` |
| `df` | 磁盘空间 | `df -h` |
| `du` | 目录大小 | `du -sh .` |

---

### A.6 Git 常用命令

#### A.6.1 基础命令

| 命令 | 作用 | 示例 |
|------|------|------|
| `git init` | 初始化仓库 | `git init my-project` |
| `git clone` | 克隆仓库 | `git clone https://github.com/user/repo.git` |
| `git add` | 暂存文件 | `git add .` 或 `git add file.txt` |
| `git commit` | 提交变更 | `git commit -m "feat: add new feature"` |
| `git push` | 推送到远程 | `git push origin main` |
| `git pull` | 拉取更新 | `git pull origin main` |
| `git branch` | 分支管理 | `git branch -a`（查看所有分支） |
| `git checkout` | 切换分支 | `git checkout feature-branch` |
| `git merge` | 合并分支 | `git merge feature-branch` |
| `git status` | 查看状态 | `git status` |
| `git log` | 查看提交历史 | `git log --oneline` |
| `git diff` | 查看变更 | `git diff` |
| `git reset` | 撤销暂存 | `git reset HEAD file.txt` |
| `git revert` | 撤销提交 | `git revert <commit-hash>` |

#### A.6.2 Git 工作流示例

```bash
# 创建新功能分支
git checkout -b feature/login

# 修改文件后暂存
git add .

# 提交（遵循 Conventional Commits）
git commit -m "feat(auth): add login page with OAuth"

# 推送分支到远程
git push -u origin feature/login

# 拉取最新主分支
git checkout main
git pull origin main

# 合并分支（或创建 Pull Request）
git checkout feature/login
git merge main

# 解决冲突后提交
git add .
git commit -m "fix: resolve merge conflicts"

# 删除本地分支
git checkout main
git branch -d feature/login

# 删除远程分支
git push origin --delete feature/login
```

#### A.6.3 Git 配置

```bash
# 配置用户信息
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# 设置默认分支名
git config --global init.defaultBranch main

# 设置编辑器
git config --global core.editor "code --wait"

# 设置别名
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"

# 查看配置
git config --list --global

# 配置行尾符
git config --global core.autocrlf true  # Windows
git config --global core.autocrlf input  # macOS/Linux

# 配置缓存时间
git config --global credential.helper cache --timeout=3600
```

#### A.6.4 Git 高级操作

```bash
# 交互式暂存
git add -i

# 撤销工作区修改
git checkout -- file.txt

# 修改最后一次提交
git add .
git commit --amend

# 合并多个提交
git rebase -i HEAD~3

# 创建标签
git tag -v1.0.0
git push origin v1.0.0

# 查看远程仓库
git remote -v

# 添加远程仓库
git remote add upstream https://github.com/original/repo.git

# 拉取上游更新
git fetch upstream
git merge upstream/main

# 清理未跟踪文件
git clean -f

# 强制推送（谨慎使用）
git push origin main --force

# 查看文件历史
git log --oneline --follow -- file.txt

# 显示分支图
git log --oneline --graph --all

# 暂存当前工作
git stash
git stash list
git stash apply
git stash drop
git stash pop

# 恢复删除的文件
git checkout <commit-hash> -- file.txt

# 清理本地过期分支
git fetch --prune
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d
```

#### A.6.5 .gitignore 模板

```
# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.DS_Store

# 环境变量
.env
.env.local
.env.*.local

# 构建输出
dist/
build/
.next/
out/
.vite/

# 编辑器
.vscode/
.idea/
*.swp
*.swo
*~

# 测试覆盖
coverage/
.nyc_output/

# 日志
*.log
logs/

# 数据库
*.sqlite
*.db

# OS
Thumbs.db
ehthumbs.db
Icon?
._*

# 包管理
pnpm-lock.yaml
package-lock.json
yarn.lock
```

---

### A.7 Docker 常用命令

#### A.7.1 镜像操作

| 命令 | 作用 | 示例 |
|------|------|------|
| `docker pull` | 拉取镜像 | `docker pull nginx:latest` |
| `docker build` | 构建镜像 | `docker build -t myapp .` |
| `docker images` | 列出镜像 | `docker images` |
| `docker rmi` | 删除镜像 | `docker rmi nginx:latest` |
| `docker tag` | 打标签 | `docker tag myapp:latest myapp:v1.0` |
| `docker push` | 推送镜像 | `docker push myapp:latest` |

#### A.7.2 容器操作

| 命令 | 作用 | 示例 |
|------|------|------|
| `docker run` | 运行容器 | `docker run -d -p 80:80 nginx` |
| `docker ps` | 列出运行中容器 | `docker ps` |
| `docker ps -a` | 列出所有容器 | `docker ps -a` |
| `docker stop` | 停止容器 | `docker stop <container-id>` |
| `docker start` | 启动容器 | `docker start <container-id>` |
| `docker rm` | 删除容器 | `docker rm <container-id>` |
| `docker exec` | 进入容器 | `docker exec -it <container-id> bash` |
| `docker logs` | 查看日志 | `docker logs -f <container-id>` |
| `docker inspect` | 查看容器详情 | `docker inspect <container-id>` |

#### A.7.3 Docker Compose

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgres://db:5432/mydb
    depends_on:
      - db
    volumes:
      - .:/app

  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=mydb
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=secret

volumes:
  postgres_data:
```

```bash
# 启动服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down

# 重建服务
docker-compose up -d --build

# 进入容器
docker-compose exec web bash

# 查看服务状态
docker-compose ps
```

---

### A.8 JavaScript/TypeScript 高级特性

#### A.8.1 异步编程进阶

```typescript
// Promise.allSettled 处理多个可能失败的操作
async function fetchMultipleUrls(urls: string[]) {
  const results = await Promise.allSettled(
    urls.map(url => fetch(url).then(r => r.json()))
  );
  
  const successes = results
    .filter(r => r.status === 'fulfilled')
    .map(r => (r as PromiseFulfilledResult<any>).value);
  
  const failures = results
    .filter(r => r.status === 'rejected')
    .map(r => (r as PromiseRejectedResult).reason);
  
  return { successes, failures };
}

// 使用 AbortController 取消请求
async function fetchWithCancel(url: string, signal: AbortSignal) {
  const response = await fetch(url, { signal });
  return response.json();
}

const controller = new AbortController();
fetchWithCancel('/api/data', controller.signal);
controller.abort(); // 取消请求

// 异步生成器
async function* paginatedFetch(url: string) {
  let nextUrl = url;
  
  while (nextUrl) {
    const response = await fetch(nextUrl);
    const data = await response.json();
    yield data.results;
    nextUrl = data.next;
  }
}

// 并发任务限制
async function limitedConcurrency<T>(
  tasks: (() => Promise<T>)[],
  limit: number
): Promise<T[]> {
  const results: T[] = [];
  const executing = new Set<Promise<T>>();
  
  for (const task of tasks) {
    const promise = task().then(result => {
      executing.delete(promise);
      return result;
    });
    
    executing.add(promise);
    results.push(promise);
    
    if (executing.size >= limit) {
      await Promise.race(executing);
    }
  }
  
  return Promise.all(results);
}
```

#### A.8.2 元编程与反射

```typescript
// Proxy 拦截对象操作
const validator = {
  get(target: object, prop: string) {
    if (!(prop in target)) {
      throw new Error(`Property "${prop}" does not exist`);
    }
    return target[prop as keyof typeof target];
  },
  
  set(target: object, prop: string, value: any) {
    if (prop === 'age' && (typeof value !== 'number' || value < 0)) {
      throw new Error('Age must be a positive number');
    }
    target[prop as keyof typeof target] = value;
    return true;
  }
};

const person = new Proxy({ name: 'Alice', age: 30 }, validator);

// Reflect API
const obj = { a: 1, b: 2 };

Reflect.get(obj, 'a');           // 1
Reflect.set(obj, 'c', 3);       // true
Reflect.has(obj, 'b');          // true
Reflect.deleteProperty(obj, 'c'); // true
Reflect.ownKeys(obj);           // ['a', 'b']

// 动态属性访问
const propertyName = 'age';
Reflect.get(person, propertyName); // 30

// 类装饰器工厂
function configurable(value: boolean) {
  return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    descriptor.configurable = value;
  };
}

// Mixin 模式
type Constructor<T = {}> = new (...args: any[]) => T;

function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    createdAt = new Date();
    updatedAt = new Date();
    
    save() {
      this.updatedAt = new Date();
      // 保存逻辑
    }
  };
}

class User {
  constructor(public name: string) {}
}

const TimestampedUser = Timestamped(User);
```

#### A.8.3 错误处理与调试

```typescript
// 自定义错误类
class AppError extends Error {
  constructor(
    public message: string,
    public code: string,
    public statusCode: number = 500
  ) {
    super(message);
    this.name = 'AppError';
    Error.captureStackTrace(this, this.constructor);
  }
}

// 使用 try-catch-finally
async function safeOperation() {
  let resource;
  
  try {
    resource = await acquireResource();
    return await resource.process();
  } catch (error) {
    console.error('Operation failed:', error);
    throw new AppError('Operation failed', 'OPERATION_FAILED');
  } finally {
    if (resource) {
      await resource.release();
    }
  }
}

// 错误边界（React）
class ErrorBoundary extends React.Component {
  state = { hasError: false, error: null };
  
  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }
  
  componentDidCatch(error: Error, info: React.ErrorInfo) {
    console.error('Error caught:', error, info);
  }
  
  render() {
    if (this.state.hasError) {
      return <FallbackComponent error={this.state.error} />;
    }
    return this.props.children;
  }
}

// 调试技巧
function debugLog(...args: any[]) {
  if (process.env.NODE_ENV === 'development') {
    console.log('[DEBUG]', ...args);
  }
}

// 性能监控
function measurePerformance(label: string) {
  const start = performance.now();
  return {
    end: () => {
      const duration = performance.now() - start;
      console.log(`${label} took ${duration.toFixed(2)}ms`);
      return duration;
    }
  };
}
```

---

### A.9 Python 高级特性

#### A.9.1 元类编程

```python
# 简单元类
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = None

# 元类验证
class ValidateMeta(type):
    def __new__(cls, name, bases, attrs):
        # 验证类属性
        if 'required' in attrs:
            if not isinstance(attrs['required'], list):
                raise TypeError("required must be a list")
        return super().__new__(cls, name, bases, attrs)

class Model(metaclass=ValidateMeta):
    required = ['name', 'id']
```

#### A.9.2 上下文管理器进阶

```python
from contextlib import contextmanager, ExitStack

# 嵌套上下文管理器
@contextmanager
def nested_contexts():
    with open('file1.txt') as f1, open('file2.txt') as f2:
        yield (f1, f2)

# 使用 ExitStack 管理动态数量的上下文
def process_files(file_paths):
    with ExitStack() as stack:
        files = [stack.enter_context(open(path)) for path in file_paths]
        return [f.read() for f in files]

# 抑制异常
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('non_existent_file.txt')
```

#### A.9.3 并发编程

```python
# 线程池
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fetch_url(url):
    import requests
    return requests.get(url).text

# 线程池（IO密集型任务）
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_url, urls))

# 进程池（CPU密集型任务）
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(compute_intensive_task, data))

# 异步线程池
async def async_fetch(urls):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        tasks = [loop.run_in_executor(pool, fetch_url, url) for url in urls]
        return await asyncio.gather(*tasks)
```

#### A.9.4 装饰器进阶

```python
# 类装饰器
class timer_decorator:
    def __init__(self, func):
        self.func = func
        self.call_count = 0
    
    def __call__(self, *args, **kwargs):
        self.call_count += 1
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{self.func.__name__} called {self.call_count} times, took {elapsed:.2f}s")
        return result

# 参数化装饰器
def repeat(times: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

# 装饰器组合
@timer_decorator
@repeat(times=3)
def expensive_operation():
    # ...
    pass

# 装饰器用于缓存
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

### A.10 SQL 高级查询

#### A.10.1 递归查询

```sql
-- 树形结构遍历
WITH RECURSIVE category_hierarchy AS (
  SELECT 
    id, 
    name, 
    parent_id, 
    1 as level,
    ARRAY[id] as path
  FROM categories
  WHERE parent_id IS NULL
  
  UNION ALL
  
  SELECT 
    c.id, 
    c.name, 
    c.parent_id,
    ch.level + 1,
    ch.path || c.id
  FROM categories c
  JOIN category_hierarchy ch ON c.parent_id = ch.id
)
SELECT * FROM category_hierarchy ORDER BY path;

-- 层级路径
WITH RECURSIVE path_builder AS (
  SELECT 
    id,
    name,
    parent_id,
    name as full_path
  FROM categories
  WHERE parent_id IS NULL
  
  UNION ALL
  
  SELECT 
    c.id,
    c.name,
    c.parent_id,
    pb.full_path || ' > ' || c.name
  FROM categories c
  JOIN path_builder pb ON c.parent_id = pb.id
)
SELECT * FROM path_builder;
```

#### A.10.2 窗口函数进阶

```sql
-- 累计求和与移动平均
SELECT
  date,
  sales,
  SUM(sales) OVER (ORDER BY date) as cumulative_sales,
  AVG(sales) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as weekly_avg,
  AVG(sales) OVER (ORDER BY date RANGE BETWEEN INTERVAL '7 days' PRECEDING AND CURRENT ROW) as rolling_7d_avg
FROM daily_sales;

-- 同比分析
WITH monthly_sales AS (
  SELECT
    DATE_TRUNC('month', sale_date) as month,
    SUM(amount) as total_sales
  FROM sales
  GROUP BY DATE_TRUNC('month', sale_date)
)
SELECT
  month,
  total_sales,
  LAG(total_sales, 12) OVER (ORDER BY month) as sales_last_year,
  ROUND((total_sales - LAG(total_sales, 12) OVER (ORDER BY month)) * 100.0 / NULLIF(LAG(total_sales, 12) OVER (ORDER BY month), 0), 2) as yoy_growth_pct
FROM monthly_sales;

-- 百分位数
SELECT
  id,
  value,
  PERCENT_RANK() OVER (ORDER BY value) as percent_rank,
  CUME_DIST() OVER (ORDER BY value) as cumulative_distribution,
  NTILE(100) OVER (ORDER BY value) as percentile
FROM metrics;
```

#### A.10.3 性能优化进阶

```sql
-- 覆盖索引（包含所有查询字段）
CREATE INDEX idx_users_name_email ON users(name) INCLUDE (email, created_at);

-- 部分索引
CREATE INDEX idx_active_users ON users(id) WHERE status = 'active';

-- 表达式索引
CREATE INDEX idx_users_email_lower ON users(LOWER(email));

-- 物化视图
CREATE MATERIALIZED VIEW daily_sales_summary AS
SELECT
  DATE_TRUNC('day', sale_date) as day,
  SUM(amount) as total_sales,
  COUNT(DISTINCT customer_id) as unique_customers
FROM sales
GROUP BY DATE_TRUNC('day', sale_date);

-- 刷新物化视图
REFRESH MATERIALIZED VIEW daily_sales_summary;

-- 并行查询
SET max_parallel_workers_per_gather = 4;

-- 查询重写优化
-- 原查询
SELECT * FROM orders WHERE EXTRACT(YEAR FROM created_at) = 2024;

-- 优化后（可以使用索引）
SELECT * FROM orders 
WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01';

-- 使用 CTE 优化复杂查询
WITH recent_users AS (
  SELECT id FROM users WHERE created_at >= NOW() - INTERVAL '30 days'
),
user_orders AS (
  SELECT user_id, COUNT(*) as order_count FROM orders GROUP BY user_id
)
SELECT ru.id, COALESCE(uo.order_count, 0) as orders
FROM recent_users ru
LEFT JOIN user_orders uo ON ru.id = uo.user_id;
```

---

### A.11 终端命令进阶

#### A.11.1 高级搜索与过滤

```bash
# 查找包含特定模式的文件
grep -r "TODO" --include="*.ts" .

# 查找大文件
find . -type f -size +100M -exec ls -lh {} \;

# 查找最近修改的文件
find . -type f -mtime -7 -exec ls -la {} \;

# 搜索并替换多个文件
grep -l "old-text" --include="*.md" . | xargs sed -i 's/old-text/new-text/g'

# 统计代码行数
find . -name "*.ts" -o -name "*.tsx" | xargs wc -l

# 排除目录搜索
grep -r "pattern" . --exclude-dir=node_modules --exclude-dir=.git

# 正则表达式搜索
grep -E "^[A-Z].*[.!?]$" file.txt

# 显示匹配上下文
grep -A 5 -B 5 "error" log.txt
```

#### A.11.2 进程管理

```bash
# 查看进程树
pstree -p

# 查找端口占用
lsof -i :3000
ss -tlnp | grep 3000

# 终止端口占用进程
kill -9 $(lsof -t -i :3000)

# 后台运行命令
nohup node server.js &

# 查看后台任务
jobs

# 前台/后台切换
fg %1
bg %1

# 进程资源监控
top -p <PID>
htop
```

#### A.11.3 文件操作进阶

```bash
# 批量重命名
for f in *.txt; do mv "$f" "${f%.txt}.md"; done

# 创建符号链接
ln -s /path/to/original /path/to/link

# 比较目录差异
diff -r dir1 dir2

# 批量修改文件权限
find . -type f -name "*.sh" -exec chmod +x {} \;

# 查找重复文件
fdupes -r .

# 安全删除（移到回收站）
trash-put file.txt

# 创建时间戳文件
touch -d "2024-01-15 10:30:00" file.txt

# 文件内容排序去重
sort file.txt | uniq -c | sort -rn

# 统计词频
cat file.txt | tr '[:upper:]' '[:lower:]' | grep -oE '\w+' | sort | uniq -c | sort -rn | head -20
```

#### A.11.4 网络操作

```bash
# 测试端口连通性
nc -zv localhost 3000

# 下载整个网站
wget -r -p -np https://example.com/docs/

# HTTP 请求详细信息
curl -v https://api.example.com

# 发送 JSON 请求
curl -X POST https://api.example.com/data \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","age":30}'

# 保存响应到文件
curl -o output.json https://api.example.com/data

# 使用代理
curl -x http://proxy:8080 https://example.com

# 测试网站性能
curl -s -w "Time: %{time_total}s\nSize: %{size_download} bytes\n" -o /dev/null https://example.com
```

---

### A.12 Git 工作流进阶

#### A.12.1 Git Flow

```bash
# 初始化 Git Flow
git flow init

# 创建功能分支
git flow feature start login-feature

# 完成功能分支
git flow feature finish login-feature

# 创建发布分支
git flow release start 1.0.0

# 完成发布分支
git flow release finish 1.0.0

# 创建热修复分支
git flow hotfix start critical-bug

# 完成热修复
git flow hotfix finish critical-bug
```

#### A.12.2 高级合并策略

```bash
# 合并时保留分支历史
git merge --no-ff feature-branch

# 仅获取特定提交
git cherry-pick <commit-hash>

# 交互式变基（重新排序/合并提交）
git rebase -i HEAD~5

# 从另一个分支获取特定提交
git rebase --onto main feature-branch start-commit..end-commit

# 解决合并冲突
git merge feature-branch
# 编辑冲突文件后
git add .
git commit

# 使用 mergetool 解决冲突
git mergetool
```

#### A.12.3 分支管理

```bash
# 清理已合并的本地分支
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d

# 清理远程已删除的分支
git fetch --prune

# 创建带说明的标签
git tag -a v1.0.0 -m "Version 1.0.0 release"

# 推送所有标签
git push --tags

# 查看标签详情
git show v1.0.0

# 创建轻量级标签（无说明）
git tag v1.0.0-lightweight
```

#### A.12.4 数据恢复

```bash
# 恢复已删除的提交
git reflog
git checkout <commit-hash>

# 恢复已删除的分支
git reflog | grep "branch-name"
git checkout -b branch-name <commit-hash>

# 从远程仓库恢复
git fetch origin
git reset --hard origin/main

# 撤销本地所有修改
git checkout .
git clean -fd

# 恢复特定文件到特定版本
git checkout <commit-hash> -- path/to/file.txt
```

---

### A.13 正则表达式速查

#### A.13.1 基本字符匹配

| 模式 | 描述 | 示例 | 匹配结果 |
|------|------|------|---------|
| `.` | 匹配任意单个字符（除换行） | `a.c` | `abc`, `a1c`, `a_c` |
| `\w` | 匹配单词字符（字母、数字、下划线） | `\w+` | `hello`, `test_1` |
| `\W` | 匹配非单词字符 | `\W` | `@`, `#`, ` ` |
| `\d` | 匹配数字 | `\d{3}` | `123`, `456` |
| `\D` | 匹配非数字 | `\D+` | `abc`, `hello` |
| `\s` | 匹配空白字符（空格、Tab、换行） | `\s` | ` `, `\t`, `\n` |
| `\S` | 匹配非空白字符 | `\S+` | `hello`, `world` |
| `\b` | 匹配单词边界 | `\bword\b` | 独立单词 `word` |
| `\B` | 匹配非单词边界 | `\Bword` | `sword` 中的 `word` |

#### A.13.2 量词与重复

| 量词 | 描述 | 示例 | 含义 |
|------|------|------|------|
| `*` | 零次或多次 | `a*` | `""`, `a`, `aa`, `aaa` |
| `+` | 一次或多次 | `a+` | `a`, `aa`, `aaa` |
| `?` | 零次或一次 | `a?` | `""`, `a` |
| `{n}` | 恰好 n 次 | `\d{3}` | 三位数字 |
| `{n,}` | 至少 n 次 | `\d{2,}` | 两位及以上数字 |
| `{n,m}` | n 到 m 次 | `\d{2,4}` | 两位到四位数字 |
| `*?` | 非贪婪匹配（零次或多次） | `a.*?b` | 最短匹配 |
| `+?` | 非贪婪匹配（一次或多次） | `a.+?b` | 最短匹配 |

#### A.13.3 字符类与分组

```regex
# 字符类
[abc]      # 匹配 a, b, c 中的任意一个
[a-z]      # 匹配小写字母
[A-Z]      # 匹配大写字母
[0-9]      # 匹配数字
[a-zA-Z]   # 匹配任意字母
[^abc]     # 匹配除 a, b, c 外的任意字符

# 预定义字符类
[0-9]      # 等价于 \d
[^0-9]     # 等价于 \D
[a-zA-Z0-9_]  # 等价于 \w

# 分组
(abc)      # 捕获分组 - 捕获匹配的文本
(?:abc)    # 非捕获分组 - 仅分组不捕获
(?<name>...)  # 命名分组（Python/JS 支持）

# 引用分组（反向引用）
\1         # 引用第一个捕获组
\2         # 引用第二个捕获组
$1         # 在替换中引用第一个捕获组（JS）
```

#### A.13.4 锚点与边界

| 锚点 | 描述 | 示例 |
|------|------|------|
| `^` | 字符串开头 | `^Hello` |
| `$` | 字符串结尾 | `world$` |
| `\A` | 字符串绝对开头 | `\AHello` |
| `\Z` | 字符串绝对结尾 | `world\Z` |
| `^...$` | 精确匹配整行 | `^\d{3}-\d{4}$` |

#### A.13.5 常用正则模式

```regex
# 邮箱地址
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

# URL
https?://[^\s/$.?#].[^\s]*

# 手机号（中国大陆）
^1[3-9]\d{9}$

# IP 地址（IPv4）
^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$

# 日期（YYYY-MM-DD）
^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$

# HTML 标签
<[^>]+>

# 中文汉字
^[\u4e00-\u9fa5]+$

# 密码强度（至少8位，包含大小写字母和数字）
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$

# 颜色十六进制
^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$

# 用户名（字母开头，允许字母数字下划线，4-16位）
^[a-zA-Z]\w{3,15}$
```

#### A.13.6 正则表达式在各语言中的使用

```javascript
// JavaScript
const email = "user@example.com";
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
console.log(emailRegex.test(email)); // true

// 提取匹配
const text = "Phone: 138-1234-5678";
const phoneRegex = /(\d{3})-(\d{4})-(\d{4})/;
const match = text.match(phoneRegex);
console.log(match[0]); // "138-1234-5678"
console.log(match[1]); // "138"

// 替换
const sentence = "Hello, World!";
const replaced = sentence.replace(/World/g, "JavaScript");
console.log(replaced); // "Hello, JavaScript!"

// 全局匹配
const colors = "red green blue";
const allColors = colors.match(/\w+/g); // ["red", "green", "blue"]

// 命名捕获组
const dateStr = "2024-01-15";
const dateRegex = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/;
const { year, month, day } = dateStr.match(dateRegex).groups;
```

```python
# Python
import re

# 匹配
pattern = r'^\d{3}-\d{4}-\d{4}$'
phone = "138-1234-5678"
if re.match(pattern, phone):
    print("Valid phone")

# 搜索
text = "Contact: 138-1234-5678 or 139-8765-4321"
phones = re.findall(r'\d{3}-\d{4}-\d{4}', text)
print(phones)  # ['138-1234-5678', '139-8765-4321']

# 替换
clean = re.sub(r'\d', '*', "Phone: 12345")
print(clean)  # "Phone: *****"

# 编译正则（提高性能）
phone_pattern = re.compile(r'^\d{3}-\d{4}-\d{4}$')
result = phone_pattern.match("138-1234-5678")

# 命名分组
pattern = re.compile(r'(?P<area>\d{3})-(?P<exchange>\d{4})-(?P<number>\d{4})')
match = pattern.match("138-1234-5678")
print(match.group('area'))  # "138"

# 分割
parts = re.split(r'[,;\s]+', "a,b;c d")
print(parts)  # ['a', 'b', 'c', 'd']
```

#### A.13.7 正则表达式性能优化

```javascript
// 避免灾难性回溯
// 坏模式（可能导致回溯灾难）
const badPattern = /(a+)+b/;
// 好模式
const goodPattern = /a+b/;

// 使用非捕获组提高性能
// 慢（不需要捕获时使用捕获组）
const slow = /(?:abc|def)+/;
// 快
const fast = /(?:abc|def)+/;

// 锚定匹配
// 慢（没有锚点，需要扫描整个字符串）
const unanchored = /pattern/;
// 快（明确开头）
const anchored = /^pattern/;

// 使用字符类替代选择分支
const slowAlt = /a|b|c|d|e/;
const fastClass = /[a-e]/;

// 避免贪婪匹配与通配符的组合
// 慢
const slowGreedy = /<.*>/;
// 快（使用非贪婪）
const nonGreedy = /<.*?>/;
```

#### A.13.8 正则表达式调试技巧

```bash
# 在线测试工具
# https://regex101.com - 实时匹配、解释
# https://regexr.com - 交互式学习
# https://regex-visual.com - 可视化正则

# 命令行测试
echo "test123" | grep -E "^[a-z]+\d+$"
echo "hello@world.com" | grep -P "^[\w.]+@[\w.]+\.\w+$"
```

---

### A.14 Shell 脚本基础

#### A.14.1 脚本结构

```bash
#!/bin/bash
# shebang: 指定解释器路径

# 注释以 # 开头

# 严格模式
set -e      # 遇到错误立即退出
set -u      # 使用未定义变量时报错
set -o pipefail  # 管道中任一命令失败则整体失败

# 常用组合
set -euo pipefail
```

#### A.14.2 变量与参数

```bash
# 变量赋值（等号两侧不能有空格）
name="Alice"
count=42
readonly PI=3.14159  # 只读变量

# 变量使用
echo $name
echo "Hello, ${name}!"  # 推荐带花括号

# 默认值
echo ${name:-"Guest"}   # 变量未设置时使用默认值
echo ${name:="Guest"}   # 变量未设置时赋默认值
echo ${name:?"Error: name not set"}  # 未设置时报错

# 命令行参数
echo $0    # 脚本名
echo $1    # 第一个参数
echo $#    # 参数个数
echo $@    # 所有参数
echo $*    # 所有参数（作为单个字符串）

# 特殊变量
echo $?    # 上一条命令的退出码
echo $$    # 当前进程 PID
echo $!    # 后台进程 PID
```

#### A.14.3 字符串操作

```bash
str="Hello, World!"

# 字符串长度
echo ${#str}  # 13

# 截取
echo ${str:7}     # "World!"
echo ${str:7:5}   # "World"
echo ${str:0:5}   # "Hello"

# 替换
echo ${str/World/Bash}  # "Hello, Bash!"
echo ${str//o/O}        # "HellO, WOrld!"（全局替换）

# 删除匹配前缀
echo ${str#Hello}  # ", World!"
echo ${str##*o}    # "rld!"（最长匹配）

# 删除匹配后缀
echo ${str%!}      # "Hello, World"
echo ${str%%.*}    # 删除第一个 . 之后内容

# 大小写转换
echo ${str,,}  # "hello, world!"（转小写）
echo ${str^^}  # "HELLO, WORLD!"（转大写）
```

#### A.14.4 条件判断

```bash
# if 语句
if [ "$name" = "Alice" ]; then
    echo "Hello Alice"
elif [ "$name" = "Bob" ]; then
    echo "Hello Bob"
else
    echo "Hello stranger"
fi

# 文件测试
if [ -f "$file" ]; then      # 是否是普通文件
    echo "$file exists"
fi
if [ -d "$dir" ]; then       # 是否是目录
    echo "$dir is a directory"
fi
if [ -e "$path" ]; then      # 是否存在
    echo "$path exists"
fi
if [ -r "$file" ]; then      # 是否可读
    echo "readable"
fi
if [ -w "$file" ]; then      # 是否可写
    echo "writable"
fi
if [ -x "$file" ]; then      # 是否可执行
    echo "executable"
fi
if [ -s "$file" ]; then      # 文件是否非空
    echo "not empty"
fi

# 数值比较
if [ "$count" -eq 10 ]; then  # 等于
    echo "count is 10"
fi
if [ "$count" -ne 10 ]; then  # 不等于
    echo "count is not 10"
fi
if [ "$count" -gt 10 ]; then  # 大于
if [ "$count" -ge 10 ]; then  # 大于等于
if [ "$count" -lt 10 ]; then  # 小于
if [ "$count" -le 10 ]; then  # 小于等于

# 字符串比较
if [ "$str" = "hello" ]; then     # 等于
    echo "match"
fi
if [ "$str" != "hello" ]; then    # 不等于
    echo "no match"
fi
if [ -z "$str" ]; then            # 是否为空
    echo "empty string"
fi
if [ -n "$str" ]; then            # 是否非空
    echo "non-empty string"
fi

# 逻辑运算
if [ "$a" = "x" ] && [ "$b" = "y" ]; then  # and
    echo "both match"
fi
if [ "$a" = "x" ] || [ "$b" = "y" ]; then  # or
    echo "one matches"
fi
if ! [ -f "$file" ]; then                  # not
    echo "file does not exist"
fi

# 双括号（高级）
if [[ "$name" == A* ]]; then    # 通配符匹配
    echo "name starts with A"
fi
if [[ "$str" =~ ^[0-9]+$ ]]; then  # 正则匹配
    echo "str is all digits"
fi
```

#### A.14.5 循环

```bash
# for 循环（列表）
for fruit in apple banana cherry; do
    echo "I like $fruit"
done

# for 循环（数字范围）
for i in {1..10}; do
    echo "Number: $i"
done

# for 循环（C 风格）
for ((i=0; i<10; i++)); do
    echo "Count: $i"
done

# for 循环（命令输出）
for file in *.txt; do
    echo "Processing $file"
done

# while 循环
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    ((count++))
done

# until 循环（条件为假时执行）
count=0
until [ $count -ge 5 ]; do
    echo "Count: $count"
    ((count++))
done

# 读取文件
while IFS= read -r line; do
    echo "Line: $line"
done < "input.txt"

# 循环控制
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break      # 跳出循环
    fi
    if [ $i -eq 3 ]; then
        continue   # 跳过当前迭代
    fi
    echo "Number: $i"
done
```

#### A.14.6 函数

```bash
# 函数定义
function greet() {
    echo "Hello, $1!"
}

# 简化定义
greet() {
    local name=$1   # local: 局部变量
    echo "Hello, $name!"
}

# 调用函数
greet "Alice"

# 返回值
add() {
    local sum=$(( $1 + $2 ))
    echo $sum      # 通过标准输出返回
}

result=$(add 3 5)
echo "Result: $result"  # 8

# 返回退出码
is_even() {
    local num=$1
    if [ $((num % 2)) -eq 0 ]; then
        return 0   # 成功（偶数）
    else
        return 1   # 失败（奇数）
    fi
}

if is_even 4; then
    echo "4 is even"
fi
```

#### A.14.7 输入输出重定向

```bash
# 标准输出重定向
command > output.txt     # 覆盖写入
command >> output.txt    # 追加写入

# 标准错误重定向
command 2> error.log
command 2>> error.log

# 同时重定向
command > output.log 2>&1    # stdout 和 stderr 合并
command &> output.log        # bash 简写
command > output.log 2> error.log  # 分别重定向

# 输入重定向
command < input.txt
command <<< "inline string"  # 字符串作为输入

# Here Document
cat << EOF
This is a
multi-line
text
EOF

# 丢弃输出
command > /dev/null 2>&1

# 管道
command1 | command2          # 标准输出管道
command1 2>&1 | command2     # 标准错误也通过管道
```

#### A.14.8 数组

```bash
# 定义数组
fruits=("apple" "banana" "cherry")
numbers=(1 2 3 4 5)

# 访问元素
echo ${fruits[0]}      # "apple"
echo ${fruits[1]}      # "banana"

# 所有元素
echo ${fruits[@]}      # "apple banana cherry"
echo ${fruits[*]}      # "apple banana cherry"

# 数组长度
echo ${#fruits[@]}     # 3

# 添加元素
fruits+=("orange")
fruits[5]="grape"

# 删除元素
unset fruits[1]

# 遍历数组
for fruit in "${fruits[@]}"; do
    echo "Fruit: $fruit"
done

# 关联数组（bash 4+）
declare -A user
user["name"]="Alice"
user["age"]=30
echo ${user["name"]}  # "Alice"
```

#### A.14.9 实用脚本模式

```bash
#!/bin/bash
set -euo pipefail

# 日志函数
log_info() {
    echo "[INFO] $(date '+%Y-%m-%d %H:%M:%S') - $1"
}

log_error() {
    echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') - $1" >&2
}

# 错误处理
cleanup() {
    log_info "Cleaning up..."
    # 清理临时文件
    rm -f /tmp/temp_*
}

trap cleanup EXIT  # 脚本退出时执行清理

# 参数解析
usage() {
    echo "Usage: $0 [-n name] [-v] [-h]"
    echo "  -n name    Set name"
    echo "  -v         Verbose mode"
    echo "  -h         Show help"
    exit 1
}

verbose=false
while getopts "n:vh" opt; do
    case $opt in
        n)
            name="$OPTARG"
            ;;
        v)
            verbose=true
            ;;
        h)
            usage
            ;;
        \?)
            usage
            ;;
    esac
done

# 进度条
progress() {
    local current=$1
    local total=$2
    local width=50
    local percent=$((current * 100 / total))
    local filled=$((current * width / total))
    local empty=$((width - filled))
    
    printf "\r["
    printf "%${filled}s" | tr ' ' '#'
    printf "%${empty}s" | tr ' ' '-'
    printf "] %d%%" $percent
}

# 使用示例
for i in {1..10}; do
    progress $i 10
    sleep 0.1
done
echo ""
```

#### A.14.10 常见脚本任务

```bash
# 备份目录
backup_dir() {
    local src=$1
    local dest=${2:-./backup}
    local timestamp=$(date +%Y%m%d_%H%M%S)
    local backup_file="${dest}/backup_${timestamp}.tar.gz"
    
    mkdir -p "$dest"
    tar -czf "$backup_file" "$src"
    echo "Backup created: $backup_file"
}

# 批量文件重命名
batch_rename() {
    local pattern=$1
    local replacement=$2
    
    for file in *"$pattern"*; do
        if [ -f "$file" ]; then
            local new_name="${file//$pattern/$replacement}"
            mv "$file" "$new_name"
            echo "Renamed: $file -> $new_name"
        fi
    done
}

# 系统健康检查
health_check() {
    echo "=== System Health Check ==="
    echo "Uptime: $(uptime -p)"
    echo "Memory:"
    free -h
    echo "Disk:"
    df -h /
    echo "CPU Load:"
    top -bn1 | head -5
}
```

---

### A.15 GraphQL 查询语言

#### A.15.1 基本查询

```graphql
# 查询（Query）- 读取数据
query GetUser {
  user(id: "1") {
    id
    name
    email
    posts {
      title
      content
    }
  }
}

# 带变量的查询
query GetUser($userId: ID!) {
  user(id: $userId) {
    id
    name
    email
    posts(limit: 10) {
      title
      createdAt
    }
  }
}

# 查询变量定义
# {
#   "userId": "1"
# }
```

#### A.15.2 变更（Mutation）

```graphql
# 变更（Mutation）- 写入数据
mutation CreatePost {
  createPost(input: {
    title: "Hello GraphQL"
    content: "This is my first post"
    authorId: "1"
  }) {
    id
    title
    createdAt
  }
}

# 带变量的变更
mutation CreateUser($input: CreateUserInput!) {
  createUser(input: $input) {
    id
    name
    email
    token
  }
}

# 变量
# {
#   "input": {
#     "name": "Alice",
#     "email": "alice@example.com",
#     "password": "secure123"
#   }
# }
```

#### A.15.3 订阅（Subscription）

```graphql
# 订阅（Subscription）- 实时更新
subscription OnNewMessage {
  newMessage(roomId: "general") {
    id
    content
    sender {
      name
      avatar
    }
    createdAt
  }
}

subscription OnUserStatusChanged {
  userStatusChanged {
    userId
    status
    lastSeen
  }
}
```

#### A.15.4 Schema 定义

```graphql
# 类型定义
type User {
  id: ID!
  name: String!
  email: String!
  age: Int
  posts: [Post!]!
  createdAt: DateTime!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
  comments: [Comment!]!
  createdAt: DateTime!
}

type Comment {
  id: ID!
  content: String!
  author: User!
  createdAt: DateTime!
}

# 枚举
enum Role {
  ADMIN
  USER
  GUEST
}

# 接口
interface Node {
  id: ID!
  createdAt: DateTime!
}

type Article implements Node {
  id: ID!
  createdAt: DateTime!
  title: String!
  body: String!
}

# 联合类型
union SearchResult = User | Post | Comment

# 输入类型（用于变更）
input CreateUserInput {
  name: String!
  email: String!
  password: String!
  role: Role = USER
}

input UpdatePostInput {
  title: String
  content: String
}
```

#### A.15.5 高级查询模式

```graphql
# 分片（Fragment）- 复用字段
fragment UserFields on User {
  id
  name
  email
  avatar
}

query GetUsers {
  users {
    ...UserFields
    posts {
      ...PostFields
    }
  }
}

fragment PostFields on Post {
  id
  title
  excerpt
  createdAt
}

# 内联分片
query GetNode($id: ID!) {
  node(id: $id) {
    ... on User {
      name
      email
    }
    ... on Post {
      title
      content
    }
  }
}

# 指令
query GetUsers($includeEmail: Boolean!) {
  users {
    id
    name
    email @include(if: $includeEmail)
    age @skip(if: $includeEmail)
  }
}

# 别名
query GetUserData {
  alice: user(id: "1") {
    name
    email
  }
  bob: user(id: "2") {
    name
    email
  }
}
```

#### A.15.6 Apollo Client 使用示例

```typescript
// Apollo Client 配置
import { ApolloClient, InMemoryCache, gql } from '@apollo/client';

const client = new ApolloClient({
  uri: 'https://api.example.com/graphql',
  cache: new InMemoryCache(),
});

// 查询
const GET_USERS = gql`
  query GetUsers {
    users {
      id
      name
      email
    }
  }
`;

const { data, loading, error } = await client.query({
  query: GET_USERS,
});

// 带变量的查询
const GET_USER = gql`
  query GetUser($id: ID!) {
    user(id: $id) {
      id
      name
      posts {
        title
      }
    }
  }
`;

const { data } = await client.query({
  query: GET_USER,
  variables: { id: "1" },
});

// 变更
const CREATE_POST = gql`
  mutation CreatePost($input: CreatePostInput!) {
    createPost(input: $input) {
      id
      title
    }
  }
`;

const { data } = await client.mutate({
  mutation: CREATE_POST,
  variables: {
    input: {
      title: "New Post",
      content: "Content here",
      authorId: "1",
    },
  },
});
```

#### A.15.7 GraphQL vs REST 对比

| 特性 | GraphQL | REST |
|------|---------|------|
| 数据获取 | 客户端指定所需字段 | 服务器返回固定结构 |
| 请求数量 | 单请求获取多资源 | 可能需要多个请求 |
| 过度获取 | 避免 | 常见 |
| 版本管理 | 无需版本号 | 通常需要版本号 |
| 缓存 | 需要客户端处理 | 原生 HTTP 缓存 |
| 学习曲线 | 较陡峭 | 较平缓 |
| 工具生态 | Apollo、Relay | Swagger、Postman |
| 文档 | 自省机制 | Swagger/OpenAPI |
| 文件上传 | 需额外处理 | 原生支持 |

#### A.15.8 最佳实践

```graphql
# 分页规范（Relay 连接规范）
type Query {
  users(first: Int, after: String): UserConnection!
  posts(first: Int, after: String, orderBy: PostOrder): PostConnection!
}

type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
}

type UserEdge {
  node: User!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

# 错误处理
type Mutation {
  createUser(input: CreateUserInput!): CreateUserPayload!
}

type CreateUserPayload {
  user: User
  errors: [Error!]
}

type Error {
  field: String!
  message: String!
}
```

---

### A.16 配置格式深入：TOML

#### A.16.1 TOML 基础语法

```toml
# TOML - 极简配置格式，常用于 Rust/Cargo、Python/pyproject.toml

# 键值对
title = "My Application"
port = 3000
debug = true

# 字符串
name = "Alice"
description = """
Multi-line
string
"""
path = "C:\\Users\\Alice"  # 转义
raw = 'C:\Users\Alice'     # 原始字符串，不转义

# 整数
count = 42
hex = 0xDEADBEEF
octal = 0o755
binary = 0b11010110

# 浮点数
pi = 3.14
negative = -0.01
sci = 5e+22

# 布尔值
enabled = true
disabled = false

# 日期时间
date = 2024-01-15
time = 10:30:00
datetime = 2024-01-15T10:30:00Z
datetime_local = 2024-01-15T10:30:00+08:00

# 表格（Table）
[server]
host = "0.0.0.0"
port = 8080

[server.logging]
level = "info"
file = "server.log"

# 数组
ports = [3000, 3001, 3002]
names = ["Alice", "Bob", "Charlie"]

# 表格数组
[[products]]
name = "Laptop"
price = 999.99
tags = ["electronics", "computers"]

[[products]]
name = "Phone"
price = 699.99
tags = ["electronics", "mobile"]

# 内联表格
point = { x = 10, y = 20 }
```

#### A.16.2 格式对比总结

| 特性 | JSON | YAML | TOML | INI |
|------|------|------|------|-----|
| 可读性 | 一般 | 好 | 很好 | 好 |
| 注释支持 | 否 | 是 | 是 | 是 |
| 复杂度 | 低 | 高 | 低 | 很低 |
| 类型系统 | 较丰富 | 丰富 | 明确 | 仅字符串 |
| 循环引用 | 否 | 可 | 否 | 否 |
| 多文档 | 否 | 是（---） | 否 | 否 |
| 流行领域 | Web API | 配置/K8s | 项目配置 | 旧式配置 |
| 解析速度 | 快 | 慢 | 快 | 很快 |

---

### A.17 Web API 设计模式

#### A.17.1 RESTful API 设计规范

```javascript
// 基础路由设计
// GET    /api/users          - 获取用户列表
// POST   /api/users          - 创建用户
// GET    /api/users/:id      - 获取单个用户
// PUT    /api/users/:id      - 更新用户（全量）
// PATCH  /api/users/:id      - 更新用户（部分）
// DELETE /api/users/:id      - 删除用户

// 查询参数
// GET /api/users?page=1&limit=20
// GET /api/users?sort=created_at&order=desc
// GET /api/users?search=alice&status=active

// 关联资源
// GET /api/users/:id/posts      - 用户的帖子
// GET /api/posts/:id/comments   - 帖子的评论
```

```typescript
// Express.js REST API 示例
import express from 'express';

const app = express();
app.use(express.json());

// 列表查询
app.get('/api/users', async (req, res) => {
  const { page = 1, limit = 20, sort = 'created_at', order = 'desc' } = req.query;
  
  const users = await db.users.findMany({
    skip: (Number(page) - 1) * Number(limit),
    take: Number(limit),
    orderBy: { [sort as string]: order },
  });
  
  const total = await db.users.count();
  
  res.json({
    data: users,
    pagination: {
      page: Number(page),
      limit: Number(limit),
      total,
      totalPages: Math.ceil(total / Number(limit)),
    },
  });
});

// 创建资源
app.post('/api/users', async (req, res) => {
  const { name, email, age } = req.body;
  
  // 输入验证
  if (!name || !email) {
    return res.status(400).json({ error: 'Name and email are required' });
  }
  
  const user = await db.users.create({
    data: { name, email, age },
  });
  
  res.status(201).json({ data: user });
});

// 错误处理中间件
app.use((err: Error, req: express.Request, res: express.Response, next: express.NextFunction) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Internal Server Error',
    message: process.env.NODE_ENV === 'development' ? err.message : undefined,
  });
});
```

#### A.17.2 API 响应格式规范

```typescript
// 成功响应
interface SuccessResponse<T> {
  success: true;
  data: T;
  metadata?: {
    page?: number;
    limit?: number;
    total?: number;
    timestamp: string;
  };
}

// 错误响应
interface ErrorResponse {
  success: false;
  error: {
    code: string;
    message: string;
    details?: Record<string, string[]>;
  };
}

// 使用示例
// 成功: { "success": true, "data": { "id": 1, "name": "Alice" } }
// 列表: { "success": true, "data": [...], "metadata": { "page": 1, "total": 50 } }
// 错误: { "success": false, "error": { "code": "VALIDATION_ERROR", "message": "Invalid input" } }
```

#### A.17.3 API 认证模式

```typescript
// JWT 认证中间件
import jwt from 'jsonwebtoken';

interface AuthRequest extends express.Request {
  user?: { id: string; role: string };
}

const authenticate = (req: AuthRequest, res: express.Response, next: express.NextFunction) => {
  const authHeader = req.headers.authorization;
  
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Authorization header required' });
  }
  
  const token = authHeader.split(' ')[1];
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET!) as { id: string; role: string };
    req.user = decoded;
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid or expired token' });
  }
};

// 角色验证
const authorize = (...roles: string[]) => {
  return (req: AuthRequest, res: express.Response, next: express.NextFunction) => {
    if (!req.user || !roles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }
    next();
  };
};

// 使用
app.get('/api/admin/users', authenticate, authorize('admin'), async (req, res) => {
  const users = await db.users.findMany();
  res.json({ data: users });
});
```

#### A.17.4 API 版本管理

```javascript
// URL 版本
// /api/v1/users
// /api/v2/users

// 请求头版本
// Accept: application/vnd.myapp.v1+json

// Express URL 版本
const v1Router = express.Router();
const v2Router = express.Router();

v1Router.get('/users', (req, res) => {
  res.json({ version: 'v1', users: [] });
});

v2Router.get('/users', (req, res) => {
  res.json({ version: 'v2', users: [], metadata: {} });
});

app.use('/api/v1', v1Router);
app.use('/api/v2', v2Router);
```

---

### A.18 React 常用模式速查

#### A.18.1 组件基础

```tsx
// 函数组件
function Welcome({ name }: { name: string }) {
  return <h1>Hello, {name}!</h1>;
}

// 箭头函数组件
const Welcome: React.FC<{ name: string }> = ({ name }) => {
  return <h1>Hello, {name}!</h1>;
};

// 带状态组件
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
    </div>
  );
}
```

#### A.18.2 Hooks 常用模式

```tsx
import { useState, useEffect, useCallback, useMemo, useRef, useContext } from 'react';

// useEffect - 副作用
function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    let cancelled = false;
    
    const fetchUser = async () => {
      setLoading(true);
      const response = await fetch(`/api/users/${userId}`);
      const data = await response.json();
      
      if (!cancelled) {
        setUser(data);
        setLoading(false);
      }
    };
    
    fetchUser();
    
    return () => {
      cancelled = true;  // 清理函数
    };
  }, [userId]);  // 依赖项
  
  if (loading) return <div>Loading...</div>;
  return <div>{user?.name}</div>;
}

// useCallback - 避免函数重创建
const handleSubmit = useCallback(async (data: FormData) => {
  const response = await fetch('/api/submit', {
    method: 'POST',
    body: JSON.stringify(data),
  });
  return response.json();
}, []);  // 空依赖表示函数不会改变

// useMemo - 避免重复计算
const sortedItems = useMemo(() => {
  return items.sort((a, b) => a.name.localeCompare(b.name));
}, [items]);

// useRef - 引用 DOM
function AutoFocus() {
  const inputRef = useRef<HTMLInputElement>(null);
  
  useEffect(() => {
    inputRef.current?.focus();
  }, []);
  
  return <input ref={inputRef} type="text" />;
}

// useRef - 保存可变值
function Timer() {
  const intervalRef = useRef<number | null>(null);
  
  const startTimer = useCallback(() => {
    intervalRef.current = setInterval(() => {
      console.log('Tick');
    }, 1000);
  }, []);
  
  const stopTimer = useCallback(() => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
    }
  }, []);
  
  return <div>
    <button onClick={startTimer}>Start</button>
    <button onClick={stopTimer}>Stop</button>
  </div>;
}
```

#### A.18.3 自定义 Hooks

```tsx
// useLocalStorage
function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });
  
  const setValue = useCallback((value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error('Error saving to localStorage:', error);
    }
  }, [key, storedValue]);
  
  return [storedValue, setValue] as const;
}

// useDebounce
function useDebounce<T>(value: T, delay: number = 300): T {
  const [debouncedValue, setDebouncedValue] = useState(value);
  
  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    
    return () => clearTimeout(timer);
  }, [value, delay]);
  
  return debouncedValue;
}

// useFetch
function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  
  useEffect(() => {
    let cancelled = false;
    
    const fetchData = async () => {
      setLoading(true);
      setError(null);
      
      try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
        const result = await response.json();
        
        if (!cancelled) {
          setData(result);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err instanceof Error ? err : new Error('Unknown error'));
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    };
    
    fetchData();
    
    return () => { cancelled = true; };
  }, [url]);
  
  return { data, loading, error };
}

// 使用自定义 Hook
function SearchComponent() {
  const [searchTerm, setSearchTerm] = useState('');
  const debouncedSearch = useDebounce(searchTerm, 500);
  const { data, loading } = useFetch<User[]>(`/api/users?search=${debouncedSearch}`);
  
  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        placeholder="Search users..."
      />
      {loading ? <p>Loading...</p> : (
        <ul>
          {data?.map(user => <li key={user.id}>{user.name}</li>)}
        </ul>
      )}
    </div>
  );
}
```

#### A.18.4 React 性能优化

```tsx
// React.memo - 避免不必要重渲染
const ExpensiveComponent = React.memo(({ data }: { data: User }) => {
  return <div>{/* 复杂渲染 */}</div>;
});

// useMemo 防止 props 重新创建
function Parent() {
  const config = useMemo(() => ({
    theme: 'dark',
    size: 'large',
  }), []);
  
  return <Child config={config} />;
}

// useCallback 防止回调函数重新创建
function Parent() {
  const [count, setCount] = useState(0);
  
  const increment = useCallback(() => {
    setCount(prev => prev + 1);
  }, []);
  
  return <Child onClick={increment} />;
}

// 虚拟列表（react-window）
import { FixedSizeList } from 'react-window';

function VirtualList({ items }: { items: string[] }) {
  const Row = ({ index, style }: { index: number; style: React.CSSProperties }) => (
    <div style={style}>Item {items[index]}</div>
  );
  
  return (
    <FixedSizeList
      height={400}
      itemCount={items.length}
      itemSize={35}
      width={300}
    >
      {Row}
    </FixedSizeList>
  );
}

// 代码分割（React.lazy + Suspense）
const LazyComponent = React.lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

#### A.18.5 React Router 常用模式

```tsx
import { BrowserRouter, Routes, Route, Link, useParams, useNavigate } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/users">Users</Link>
        <Link to="/about">About</Link>
      </nav>
      
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/users" element={<UserList />} />
        <Route path="/users/:id" element={<UserDetail />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

// 动态路由参数
function UserDetail() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  
  return (
    <div>
      <h1>User: {id}</h1>
      <button onClick={() => navigate('/users')}>Back</button>
    </div>
  );
}

// 嵌套路由
function Layout() {
  return (
    <div>
      <header>
        <h1>My App</h1>
      </header>
      <Outlet />  {/* 子路由在此渲染 */}
    </div>
  );
}

<Routes>
  <Route path="/" element={<Layout />}>
    <Route index element={<Home />} />
    <Route path="dashboard" element={<Dashboard />} />
    <Route path="settings" element={<Settings />} />
  </Route>
</Routes>
```

#### A.18.6 状态管理模式

```tsx
// Context + useReducer 模式
import { createContext, useContext, useReducer, ReactNode } from 'react';

// 定义状态和动作
interface AuthState {
  user: User | null;
  loading: boolean;
  error: string | null;
}

type AuthAction =
  | { type: 'LOGIN_START' }
  | { type: 'LOGIN_SUCCESS'; payload: User }
  | { type: 'LOGIN_FAILURE'; payload: string }
  | { type: 'LOGOUT' };

// Reducer
function authReducer(state: AuthState, action: AuthAction): AuthState {
  switch (action.type) {
    case 'LOGIN_START':
      return { ...state, loading: true, error: null };
    case 'LOGIN_SUCCESS':
      return { user: action.payload, loading: false, error: null };
    case 'LOGIN_FAILURE':
      return { ...state, loading: false, error: action.payload };
    case 'LOGOUT':
      return { user: null, loading: false, error: null };
    default:
      return state;
  }
}

// Context
const AuthContext = createContext<{
  state: AuthState;
  dispatch: React.Dispatch<AuthAction>;
} | null>(null);

// Provider
function AuthProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(authReducer, {
    user: null,
    loading: false,
    error: null,
  });
  
  return (
    <AuthContext.Provider value={{ state, dispatch }}>
      {children}
    </AuthContext.Provider>
  );
}

// 自定义 Hook
function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
}

// 使用
function LoginForm() {
  const { dispatch } = useAuth();
  
  const handleLogin = async (email: string, password: string) => {
    dispatch({ type: 'LOGIN_START' });
    try {
      const response = await fetch('/api/login', { method: 'POST', body: JSON.stringify({ email, password }) });
      const user = await response.json();
      dispatch({ type: 'LOGIN_SUCCESS', payload: user });
    } catch (err) {
      dispatch({ type: 'LOGIN_FAILURE', payload: 'Login failed' });
    }
  };
  
  return <form>{/* ... */}</form>;
}
```

---

### A.19 数据结构与算法速查

#### A.19.1 时间复杂度速查

| 数据结构 | 访问 | 搜索 | 插入 | 删除 |
|----------|------|------|------|------|
| 数组 | O(1) | O(n) | O(n) | O(n) |
| 栈 | O(n) | O(n) | O(1) | O(1) |
| 队列 | O(n) | O(n) | O(1) | O(1) |
| 链表 | O(n) | O(n) | O(1) | O(1) |
| 哈希表 | O(1)* | O(1)* | O(1)* | O(1)* |
| 二叉搜索树 | O(log n) | O(log n) | O(log n) | O(log n) |
| 平衡树 | O(log n) | O(log n) | O(log n) | O(log n) |
| 堆 | O(n) | O(n) | O(log n) | O(log n) |

*注：哈希表平均时间复杂度为 O(1)，最坏情况为 O(n)

#### A.19.2 排序算法速查

| 算法 | 最好 | 平均 | 最坏 | 空间 | 稳定 |
|------|------|------|------|------|------|
| 冒泡排序 | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| 选择排序 | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| 插入排序 | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| 快速排序 | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |
| 归并排序 | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| 堆排序 | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ |
| 计数排序 | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ |
| 基数排序 | O(nk) | O(nk) | O(nk) | O(n+k) | ✅ |

#### A.19.3 常用算法模式

```javascript
// 双指针 - 有序数组两数之和
function twoSum(nums, target) {
  let left = 0, right = nums.length - 1;
  
  while (left < right) {
    const sum = nums[left] + nums[right];
    if (sum === target) return [left, right];
    if (sum < target) left++;
    else right--;
  }
  
  return [-1, -1];
}

// 滑动窗口 - 最长无重复子串
function lengthOfLongestSubstring(s) {
  const charSet = new Set();
  let left = 0, maxLength = 0;
  
  for (let right = 0; right < s.length; right++) {
    while (charSet.has(s[right])) {
      charSet.delete(s[left]);
      left++;
    }
    charSet.add(s[right]);
    maxLength = Math.max(maxLength, right - left + 1);
  }
  
  return maxLength;
}

// 二分查找
function binarySearch(nums, target) {
  let left = 0, right = nums.length - 1;
  
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    
    if (nums[mid] === target) return mid;
    if (nums[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  
  return -1;
}

// 深度优先搜索（DFS）
function dfs(graph, start, visited = new Set()) {
  visited.add(start);
  console.log(start);
  
  for (const neighbor of graph[start]) {
    if (!visited.has(neighbor)) {
      dfs(graph, neighbor, visited);
    }
  }
}

// 广度优先搜索（BFS）
function bfs(graph, start) {
  const visited = new Set([start]);
  const queue = [start];
  
  while (queue.length > 0) {
    const node = queue.shift();
    console.log(node);
    
    for (const neighbor of graph[node]) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push(neighbor);
      }
    }
  }
}

// 动态规划 - 斐波那契数列
function fibonacci(n) {
  if (n <= 1) return n;
  
  const dp = [0, 1];
  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i-1] + dp[i-2];
  }
  
  return dp[n];
}

// 动态规划 - 背包问题
function knapsack(weights, values, capacity) {
  const n = weights.length;
  const dp = Array.from({ length: n + 1 }, () => Array(capacity + 1).fill(0));
  
  for (let i = 1; i <= n; i++) {
    for (let w = 1; w <= capacity; w++) {
      if (weights[i-1] <= w) {
        dp[i][w] = Math.max(
          values[i-1] + dp[i-1][w - weights[i-1]],
          dp[i-1][w]
        );
      } else {
        dp[i][w] = dp[i-1][w];
      }
    }
  }
  
  return dp[n][capacity];
}

// 回溯算法 - 全排列
function permute(nums) {
  const result = [];
  
  function backtrack(path, remaining) {
    if (remaining.length === 0) {
      result.push([...path]);
      return;
    }
    
    for (let i = 0; i < remaining.length; i++) {
      path.push(remaining[i]);
      backtrack(path, [...remaining.slice(0, i), ...remaining.slice(i + 1)]);
      path.pop();
    }
  }
  
  backtrack([], nums);
  return result;
}
```

---

### A.20 Node.js 常用 API 速查

#### A.20.1 文件系统（fs）

```javascript
import fs from 'fs/promises';
import fsSync from 'fs';

// 异步读取文件
async function readFile() {
  const content = await fs.readFile('file.txt', 'utf-8');
  console.log(content);
}

// 异步写入文件
async function writeFile() {
  await fs.writeFile('output.txt', 'Hello, World!', 'utf-8');
}

// 追加内容
async function appendFile() {
  await fs.appendFile('log.txt', `${new Date().toISOString()} - Log entry\n`);
}

// 检查文件是否存在
async function fileExists(path) {
  try {
    await fs.access(path);
    return true;
  } catch {
    return false;
  }
}

// 目录操作
async function dirOperations() {
  await fs.mkdir('new-dir', { recursive: true });  // 创建目录
  const files = await fs.readdir('.');               // 读取目录
  await fs.rmdir('old-dir', { recursive: true });    // 删除目录
}

// 文件信息
async function fileInfo() {
  const stats = await fs.stat('file.txt');
  console.log({
    size: stats.size,
    isFile: stats.isFile(),
    isDirectory: stats.isDirectory(),
    created: stats.birthtime,
    modified: stats.mtime,
  });
}

// 流式读取（大文件）
function streamRead() {
  const readStream = fsSync.createReadStream('large-file.txt', { encoding: 'utf-8' });
  
  readStream.on('data', (chunk) => {
    console.log(`Received ${chunk.length} bytes`);
  });
  
  readStream.on('end', () => {
    console.log('Finished reading');
  });
}
```

#### A.20.2 路径处理（path）

```javascript
import path from 'path';

// 路径操作
const fullPath = '/home/user/projects/app/src/index.js';

console.log(path.dirname(fullPath));      // '/home/user/projects/app/src'
console.log(path.basename(fullPath));     // 'index.js'
console.log(path.extname(fullPath));      // '.js'
console.log(path.parse(fullPath));
// { root: '/', dir: '/home/user/projects/app/src', base: 'index.js', ext: '.js', name: 'index' }

// 路径拼接
const configPath = path.join(__dirname, 'config', 'app.json');
console.log(configPath);  // 使用当前平台的路径分隔符

// 路径规范化
console.log(path.normalize('/home/../home/user/./project'));  // '/home/user/project'

// 相对路径
console.log(path.relative('/home/user/projects/app', '/home/user/projects/lib'));
// '../lib'

// 绝对路径判断
console.log(path.isAbsolute('/home/user'));  // true
console.log(path.isAbsolute('relative/path'));  // false
```

#### A.20.3 事件（EventEmitter）

```javascript
import EventEmitter from 'events';

// 创建事件发射器
class MyEmitter extends EventEmitter {
  constructor() {
    super();
  }
}

const emitter = new MyEmitter();

// 监听事件
emitter.on('data', (data) => {
  console.log('Data received:', data);
});

emitter.once('once', () => {
  console.log('This will only fire once');
});

// 发射事件
emitter.emit('data', { id: 1, value: 'test' });
emitter.emit('once');
emitter.emit('once');  // 不会触发

// 错误处理
emitter.on('error', (err) => {
  console.error('Error:', err.message);
});

// 移除监听器
const handler = (data) => console.log('Handler', data);
emitter.on('event', handler);
emitter.off('event', handler);  // 移除特定监听器
emitter.removeAllListeners();   // 移除所有监听器

// 检查监听器
console.log(emitter.listenerCount('data'));  // 1
console.log(emitter.listeners('data'));       // [Function]
```

#### A.20.4 子进程（child_process）

```javascript
import { exec, spawn, execSync } from 'child_process';

// 执行命令（捕获输出）
async function runCommand() {
  return new Promise((resolve, reject) => {
    exec('ls -la', (error, stdout, stderr) => {
      if (error) {
        reject(error);
        return;
      }
      resolve(stdout);
    });
  });
}

// spawn - 流式输出（适合长时间运行的命令）
function streamCommand() {
  const child = spawn('node', ['server.js'], {
    stdio: 'inherit',  // 继承父进程的标准输入输出
    env: { ...process.env, NODE_ENV: 'development' },
  });
  
  child.on('error', (err) => {
    console.error('Failed to start:', err);
  });
  
  child.on('exit', (code, signal) => {
    console.log(`Process exited with code ${code}`);
  });
}

// 同步执行
try {
  const result = execSync('git rev-parse HEAD', { encoding: 'utf-8' });
  console.log('Current commit:', result.trim());
} catch (error) {
  console.error('Git command failed:', error.message);
}
```

#### A.20.5 网络（http/https）

```javascript
import http from 'http';
import https from 'https';

// 创建 HTTP 服务器
const server = http.createServer((req, res) => {
  // 设置响应头
  res.writeHead(200, {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  });
  
  // 请求处理
  const { method, url } = req;
  
  if (method === 'GET' && url === '/api/health') {
    res.end(JSON.stringify({ status: 'ok' }));
  } else {
    res.writeHead(404);
    res.end(JSON.stringify({ error: 'Not found' }));
  }
});

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});

// 发送 HTTP 请求
function httpRequest(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (response) => {
      let data = '';
      
      response.on('data', (chunk) => {
        data += chunk;
      });
      
      response.on('end', () => {
        try {
          resolve(JSON.parse(data));
        } catch {
          resolve(data);
        }
      });
    }).on('error', reject);
  });
}
```

---

### A.21 调试与错误处理模式

#### A.21.1 JavaScript 调试技巧

```javascript
// console 高级用法
console.log('Simple log');
console.error('Error message');  // 红色输出
console.warn('Warning');          // 黄色输出
console.info('Info message');
console.debug('Debug info');

// 格式化输出
console.log('User: %s, Age: %d', 'Alice', 30);
console.log('Object: %o', { name: 'Alice', age: 30 });

// 表格输出
console.table([
  { name: 'Alice', age: 30 },
  { name: 'Bob', age: 25 },
]);

// 分组
console.group('User Details');
console.log('Name: Alice');
console.log('Age: 30');
console.groupEnd();

// 计时
console.time('fetch-data');
// ... 耗时操作 ...
console.timeEnd('fetch-data');  // "fetch-data: 123.45ms"

// 堆栈跟踪
console.trace('Trace point');

// 计数
console.count('click');  // click: 1
console.count('click');  // click: 2

// 性能监控
performance.mark('start');
// ... 操作 ...
performance.mark('end');
performance.measure('operation', 'start', 'end');
const measurements = performance.getEntriesByType('measure');
```

#### A.21.2 Python 调试技巧

```python
import pdb
import logging
from time import perf_counter

# 设置断点
def buggy_function(x):
    breakpoint()  # Python 3.7+ 进入 pdb 调试器
    return x / 0

# pdb 命令
# n - next (下一行)
# s - step into (进入函数)
# c - continue (继续执行)
# p variable - print variable (打印变量)
# l - list (显示源代码)
# q - quit (退出调试器)

# logging 模块
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def process_data(data):
    logger.debug(f"Processing data: {data[:100]}...")
    try:
        result = complex_operation(data)
        logger.info(f"Successfully processed data, result: {result}")
        return result
    except ValueError as e:
        logger.error(f"Value error processing data: {e}", exc_info=True)
        raise
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        raise

# 性能分析
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@measure_time
def slow_function():
    import time
    time.sleep(1)
```

#### A.21.3 错误处理最佳实践

```typescript
// TypeScript 错误处理

// 自定义错误类层次
class AppError extends Error {
  constructor(
    message: string,
    public code: string,
    public statusCode: number = 500,
    public details?: Record<string, unknown>
  ) {
    super(message);
    this.name = 'AppError';
  }
}

class ValidationError extends AppError {
  constructor(message: string, details?: Record<string, string[]>) {
    super(message, 'VALIDATION_ERROR', 400, details);
    this.name = 'ValidationError';
  }
}

class AuthenticationError extends AppError {
  constructor(message: string = 'Authentication required') {
    super(message, 'AUTH_ERROR', 401);
    this.name = 'AuthenticationError';
  }
}

class NotFoundError extends AppError {
  constructor(resource: string, id: string) {
    super(`${resource} with id ${id} not found`, 'NOT_FOUND', 404);
    this.name = 'NotFoundError';
  }
}

// 全局错误处理
async function handleApiCall<T>(fn: () => Promise<T>): Promise<T> {
  try {
    return await fn();
  } catch (error) {
    if (error instanceof AppError) {
      throw error;  // 已知错误，继续抛出
    }
    
    if (error instanceof TypeError) {
      throw new ValidationError('Invalid data type');
    }
    
    // 未知错误，记录日志
    console.error('Unexpected error:', error);
    throw new AppError('An unexpected error occurred', 'INTERNAL_ERROR', 500);
  }
}

// 重试模式
async function withRetry<T>(
  fn: () => Promise<T>,
  options: { maxRetries?: number; delay?: number; backoff?: number } = {}
): Promise<T> {
  const { maxRetries = 3, delay = 1000, backoff = 2 } = options;
  
  let lastError: Error | null = null;
  
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error instanceof Error ? error : new Error(String(error));
      
      if (attempt < maxRetries) {
        const waitTime = delay * Math.pow(backoff, attempt - 1);
        console.warn(`Attempt ${attempt} failed, retrying in ${waitTime}ms...`);
        await new Promise(resolve => setTimeout(resolve, waitTime));
      }
    }
  }
  
  throw lastError || new Error('Retry failed');
}

// 使用示例
const data = await withRetry(
  () => fetch('/api/data').then(r => r.json()),
  { maxRetries: 3, delay: 500 }
);
```

---

### Vibe 练习

对 Claude Code 说：

> "我的代码中出现了这个语法：[复制你遇到的语法片段]，帮我解释它是什么意思，并用更简单的代码重写（如果你认为必要的话）。"

> "帮我检查这段 SQL 查询的性能问题，并提供优化建议。"

> "帮我设计一个高效的数据库索引策略，用于以下查询模式..."

> "帮我实现一个正则表达式来匹配 [描述你的匹配需求]，并解释它的各个部分。"

> "帮我写一个 Shell 脚本来自动化 [描述你的任务]，包含错误处理和日志功能。"

> "帮我检查这个 React 组件的性能问题，并提供优化建议。"

> "帮我实现一个 GraphQL 查询来获取 [描述你的数据需求]。"

> "帮我分析这段代码的时间复杂度，并提供优化方案。"

> "帮我用 DSA 模式实现 [描述算法需求]，并解释工作原理。"