import matplotlib.pyplot as plt
import numpy as np

def compare_plot(imgs, labels, cmaps=None):
    """
    複数画像を比較して出力する際に使用
    
    imgs : 複数画像を含んだリスト
    labels : 画像のラベルを含んだリスト
    cmaps : 画像の出力形式を含んだリスト(チャンネルが1の際に使用)
    """
    fig, ax = plt.subplots(1, len(labels), figsize=(6*len(labels),6))

    for i, im in enumerate(imgs):
        if len(im.shape) == 3:
            ax[i].imshow(im)
        else:
            ax[i].imshow(im, cmap=cmaps[i])
        ax[i].set_title(labels[i])
    plt.show()
