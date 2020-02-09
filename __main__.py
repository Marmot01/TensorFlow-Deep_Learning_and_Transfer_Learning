import matplotlib.image as mpimg

from rsidea.models import *
from rsidea.preprocess import read_data, read_label, split_data
from rsidea.util.draw import *
from rsidea.util.history import *
from tensorflow.keras import backend as K
import numpy
from rsidea.util.losses import loss_ddc

save = False

'''ddc demo'''
# 读取数据
x, y = read_data.read_SIRI_WHU()
# 分割数据
x_train, y_train, x_test, y_test = split_data.split(x, y, rate=0.5)
# 获取原训练模型
model, mmd = ddc.DDC(input_shape=x_train[0].shape, output_shape=12)
# 配置模型
model.compile(optimizer='adam',
              loss=loss_ddc(mmd),
              metrics=['accuracy'],
              experimental_run_tf_function=False)
# # 模型评测
# model.evaluate(x_test, y_test, verbose=2)
# # 填入数据进行训练
# history = model.fit([x_train, x_test], y_train, epochs=5)
# history = history.history
# # 模型保存
# if save:
#     model.save(".\\model_data\\model\\ddc_SIRI_WHU.h5")
#     model.save_weights(".\\model_data\\weight\\ddc_SIRI_WHU.h5")
#     save_history(history, ".\\model_data\\history\\ddc_SIRI_WHU.json")
#     print("Saved!")
# # 模型评测
# model.evaluate(x_test, y_test, verbose=2)
# # 画折线图
# draw_accuracy(history)
# draw_loss(history)
# # 画单张预测展示图
# label_name = read_label.read_SIRI_WHU()
# x = mpimg.imread(".\\data\\demo.jpg") / 255.0
# draw_predict_demo(model, x, label_name)
