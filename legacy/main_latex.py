import os

import matplotlib.pyplot as plt


def main():
    pic_name = "test.svg"
    tex = '$\\frac{1}{\\sqrt{2\\sqrt{2\\pi}}} \\exp\\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right)$'

    # Создание области отрисовки
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()

    # Отрисовка формулы
    t = ax.text(0.5, 0.5, tex,
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=40, color='black')

    # Определение размеров формулы
    ax.figure.canvas.draw()
    bbox = t.get_window_extent()
    print(bbox.width, bbox.height)

    # Установка размеров области отрисовки
    fig.set_size_inches(bbox.width / 80, bbox.height / 80)  # dpi=80

    # Отрисовка или сохранение формулы в файл
    # plt.show()
    plt.savefig(os.path.join("../resources", pic_name))
    # plt.savefig(pic_name, dpi=300)


if __name__ == "__main__":
    main()
