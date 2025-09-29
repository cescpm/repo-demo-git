def sum(a,b):
    return a+b


if __name__ == "__main__":
    print("Hello World")

    import numpy as np

    data = np.loadtxt('data/data.txt')
    print(f"NumPy detected shape: {data.shape}")

    import PIL.Image
    import ast

    img = PIL.Image.open('data/JoeBarTeam.jpg')

    users_choice = ''

    while users_choice != 'Yes':

        cropping_tuple = ast.literal_eval(input('Enter the coordinates where you want the image to be cut' \
                                'Must fbe a 4-tuple: (left, upper, right, lower)'))

        cropped_img = img.crop(cropping_tuple)
        cropped_img.show()

        users_choice = input('Do you wish cropping the image this way? (Yes/No)')

    cropped_img.save(f'outputs/cropped_image_{cropping_tuple}.jpg')



