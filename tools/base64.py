import base64
import io
from imageio import imread

filename = "example.jpg"
with open(filename, "rb") as fid:
    data = fid.read()

b64_bytes = base64.b64encode(data)
b64_string = b64_bytes.decode()
image_data = b64_string

print(image_data)

a = base64.b64decode(image_data)
b = io.BytesIO(a)
img = imread(b)

# import matplotlib.pyplot as plt
# plt.imshow(img)
# plt.show()
