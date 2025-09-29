def sum(a,b):
    return a+b


if __name__ == "__main__":
    print("Hello World")

    import numpy as np

    data = np.loadtxt('data/data.txt')
    print(f"NumPy detected shape: {data.shape}")

    import PIL.Image

    img = PIL.Image.open('data/JoeBarTeam.jpg')
    img.show()