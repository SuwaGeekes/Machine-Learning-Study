import numpy as np

# 活性化関数
def activation(x):
  return (x > 0).astype('int')

def NOR(x1, x2):
  # バイアスを含む重みベクトル
  w1 = np.array([-0.5, -0.5, 0.7])
  w2 = np.array([0.5, 0.5, -0.2])
  w3 = np.array([0.5, 0.5, -0.7])

  # レイヤごとに重みをまとめる
  layer1_w = np.array([w1, w2])
  layer2_w = np.array(w3)

  # 第一層での処理
  layer1_x = np.array([x1, x2, 1])
  layer2_x = activation(np.dot(layer1_w, layer1_x))

  # 第二層での処理
  layer2_x = np.append(layer2_x, 1)
  output = activation(np.dot(layer2_w, layer2_x))
  return output
  

if __name__=='__main__':
  for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
    y = NOR(xs[0], xs[1])
    print(str(xs) + " -> " + str(y))