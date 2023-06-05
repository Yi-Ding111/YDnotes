# TORCH.UTILS.DATA

https://pytorch.org/docs/stable/data.html

## Dataset

torch.utils.data.Dataset 是一个 PyTorch 的抽象类,代表一个数据集。

当你想要构建一个自定义的数据集用于训练神经网络时,你需要继承这个 Dataset 类,并实现以下两个方法:

- `__len__()` - 返回数据集的大小.
- `__getitem__()` - 根据索引返回样本和对应标签然后你可以将这个Dataset类的实例传递给 PyTorch 的 DataLoader,从而获得一个batch的样本,用于训练。

one simple example:

```python
from torch.utils.data import Dataset
```

```python
class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        X = self.data[index]
        y = self.labels[index]
        return X, y

data = [1, 2, 3, 4, 5]
labels = [0, 0, 1, 1, 0]

dataset = CustomDataset(data, labels)
loader = DataLoader(dataset, batch_size=2)

for X, y in loader:
    # X is a batch of data, y is a batch of labels
```

PyTorch 的 Dataset 是一个非常有用的工具,它允许你构建自定义数据集,并轻松构建 DataLoader 来 iterate 这个数据集。



## from torch.utils.data import Dataset && from datasets import Dataset

这两个Dataset类有以下区别:torch.utils.data.Dataset:- 是 PyTorch 内置的 Dataset 类,用于构建自定义数据集
\- 需要你实现 __len__ 和 __getitem__ 方法
\- 通常用于训练神经网络,与 DataLoader 结合使用datasets.Dataset:- 是 Hugging Face 数据集库 (datasets) 中的 Dataset 类
\- 实现了许多便利方法,如 .map(), .filter(), .shuffle() 等
\- 可以直接从许多数据源(CSV, JSON, Parquet 等)构建 Dataset
\- 除了用于训练,也常用于评估和预测
\- 可以与 torch.utils.data.DataLoader 结合使用,也可以独立使用所以,总体来说:- torch.utils.data.Dataset 更加底层和灵活,用于构建PyTorch训练所需的自定义数据集- datasets.Dataset 提供了更高级的接口,可以更轻松地从各种数据源构建数据集,不仅用于训练,也常用于评估和推理举个简单的例子:使用 torch.utils.data.Dataset:

```python
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        X = self.data[index]
        y = self.labels[index]
        return X, y
```

 使用 datasets.Dataset:

```python
from datasets import Dataset

dataset = Dataset.from_dict({
    'data': [1, 2, 3, 4, 5],
    'labels': [0, 0, 1, 1, 0] 
})
```

所以总的来说,可以根据你的具体使用场景选择适当的Dataset类。两者也可以结合使用,例如从datasets构建Dataset,然后从该Dataset构建torch.utils.data.DataLoader用于训练。



## Dataloader

https://pytorch.org/tutorials/beginner/basics/data_tutorial.html#preparing-your-data-for-training-with-dataloaders



PyTorch DataLoader是PyTorch中用于加载和预处理数据集的工具。

它可以帮助你:

1. 从各种数据集中批量加载数据。
2. 预处理数据,如归一化、随机增强等。

3. 为模型提供训练和验证数据。



一个基本的DataLoader可以这样定义:

```python
from torch.utils.data import DataLoader
from torchvision import datasets

train_loader = DataLoader(datasets.MNIST('./mnist_data', train=True, download=True), 
                          batch_size=64, 
                          shuffle=True)
```

这个DataLoader会:

1. 从mnist_data文件夹中下载MNIST数据集并加载训练数据。
2. 批量读取数据,每个batch包含64个样本。
3. 在每个epoch前打乱数据顺序
4. 为模型的训练提供数据。



```python
batch = next(iter(train_dataloader))
pixel_values, labels, target_sequences = batch
```

这行代码从`train_dataloader`的迭代器中取出下一批数据,赋值给`batch`。



那么,一个典型的PyTorch模型训练会这样使用Dataloader:

```python
model.train()
for batch_idx, (data, target) in enumerate(train_loader):
    # 加载一批数据和标签
    # data 的shape 为 [64, 1, 28, 28]
    # target 的shape 为 [64]
    
    # 清零梯度
    optimizer.zero_grad()  
    
    # 前向传播
    output = model(data)
    
    # 计算损失
    loss = loss_fn(output, target)
    
    # 反向传播
    loss.backward()
    
    # 更新参数
    optimizer.step()
```



所以,总的来说,PyTorch DataLoader的主要作用是:

1. 加载数据集并预处理数据.
2. 以batch的形式为模型提供训练、验证和测试数据.
3. 加速模型的训练过程.