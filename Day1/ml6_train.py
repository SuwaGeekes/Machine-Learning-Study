from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import matplotlib.pyplot as plt

# ノイズの入った　y = 3x を生成
x_train = np.random.rand(100, 1).astype('float32')
y_train = 3 * x_train + np.random.randn(100, 1)

#  z = WX のモデルを生成
model = Sequential()
model.add(Dense(1, use_bias=False))     # WX
model.add(Activation('linear'))     # そのまま伝播
model.compile(optimizer='SGD', loss='mse')  # 確率的勾配降下法で平均二乗誤差の損失関数を最小化

# 64回学習させる
model.fit(x_train, y_train, epochs=64)

# 学習によって得られた傾きを用いて描画
w = model.layers[0].get_weights()[0][0][0]
x = p = np.linspace( 0, 1, 100)
y = w*x
plt.scatter(x_train, y_train)
plt.plot(x, y, c='orange')
plt.show()