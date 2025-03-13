import threading
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

# 1. 下载和加载 MNIST 数据集
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

trainloader = DataLoader(trainset, batch_size=64, shuffle=True)
testloader = DataLoader(testset, batch_size=64, shuffle=False)

# 2. 定义神经网络模型
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28 * 28, 128)  # 输入层 28x28=784，隐藏层 128 个神经元
        self.fc2 = nn.Linear(128, 10)  # 输出层，10 个神经元表示 10 个类别（数字 0 到 9）
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)
        
    def forward(self, x):
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        x = self.softmax(x)
        return x

# 3. 创建模型实例
model = SimpleNN()
#model.load_state_dict(torch.load('model_weights.pth', weights_only=True))
#model.eval()
# 4. 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.002)

# 5. 训练模型
def train():
    epochs = 1
    # 3. 创建模型实例
    model = SimpleNN()
    model.load_state_dict(torch.load('model_weightss.pth', weights_only=True))
    model.eval()
    # 4. 定义损失函数和优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.002)
    for epoch in range(epochs):
        running_loss = 0.0
        for inputs, labels in trainloader:
            # 清空梯度
            optimizer.zero_grad()

            # 向前传播
            outputs = model(inputs)

            # 计算损失
            loss = criterion(outputs, labels)

            # 反向传播
            loss.backward()

            # 更新权重
            optimizer.step()

            running_loss += loss.item()
        torch.save(model.state_dict(), 'model_weightss.pth')
        print(f"Epoch {epoch+1}, Loss: {running_loss/len(trainloader)}")
a=threading.Thread(target=train)
b=threading.Thread(target=train)
c=threading.Thread(target=train)

a.start()
b.start()
c.start()

# 6. 测试模型
correct = 0
total = 0
with torch.no_grad():
    for inputs, labels in testloader:
        outputs = model(inputs)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
print(correct,"/",total)
print(f"Accuracy on test set: {100 * correct / total}%")


sample_image, _ = testset[0]
model.eval()
with torch.no_grad():
    output = model(sample_image.unsqueeze(0))
    predicted_label = torch.argmax(output, 1).item()

print(f"Predicted label for the first image: {predicted_label}")
