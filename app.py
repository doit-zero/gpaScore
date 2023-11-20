import numpy as np
import tensorflow as tf
import pandas as pd


# 구조호된 데이터를 읽겠다는 것! 엑셀파일 같은 것
data = pd.read_csv("gpascore.csv")

# 데이터 중 빈칸 지우기
data = data.dropna()
# 데이터 중 빈칸에 평균값 넣음 data.fillna(100)


x데이터 = []
for i, rows in data.iterrows():
    x데이터.append([rows["gre"], rows["gpa"], rows["rank"]])


y데이터 = data["admit"].values


model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Dense(64, activation="tanh"),
        tf.keras.layers.Dense(128, activation="tanh"),
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ]
)

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(np.array(x데이터), np.array(y데이터), epochs=2000)


# 예측
예측값 = model.predict([[750, 3.70, 3], [400, 2.2, 1]])
print(예측값)
