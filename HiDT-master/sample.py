import torch # pip3 install torch
from PIL import Image #  pip3 install pillow
import matplotlib.pyplot as plt # pip3 install matplotlib

from hidt.networks.enhancement.RRDBNet_arch import RRDBNet #pip3 install torchvision
from hidt.style_transformer import StyleTransformer #pip3 install pyyaml
from hidt.utils.preprocessing import GridCrop, enhancement_preprocessing


config_path = 'configs/daytime.yaml'
gen_weights_path = 'trained_models/generator/daytime.pt'
device = 'cpu:0'

style_transformer = StyleTransformer( 
    config_path,
    gen_weights_path,
    inference_size=256, # output image size
    device=device
)

# 테스트 이미지 로드
img_path = 'images/daytime/content/1.jpg'

img = Image.open(img_path)

print(img.size)

plt.figure(figsize=(16, 10))
#plt.imshow(img) 
#img.save('test.png') # 변환전 출력


# 이미지를 변환할 스타일 list 로드
from pprint import pprint

with open('styles.txt') as f:
    styles = f.read()

styles = {style.split(',')[0]: torch.tensor([float(el) for el in style.split(',')[1][1:-1].split(' ')]) for style in styles.split('\n')[:-1]}
#pprint(styles)


# 이미지 변환하는 함수
def transfer(img, style):
    style_to_transfer = styles[style] # 변환할 스타일을 지정한다.
    style_to_transfer = style_to_transfer.view(1, 1, 3, 1).to(device)

    with torch.no_grad(): #해상도 증가
        content_decomposition = style_transformer.get_content(img)[0]

        decoder_input = {
            'content': content_decomposition['content'],
            'intermediate_outputs': content_decomposition['intermediate_outputs'],
            'style': style_to_transfer
        }

        transferred = style_transformer.trainer.gen.decode(decoder_input)['images']

    return (transferred[0].cpu().clamp(-1, 1).numpy().transpose(1, 2, 0) + 1.) / 2.
    
test_img = Image.open('images/test/01.jpg')

fig, axes = plt.subplots(1, 2, figsize=(20, 10))
#axes[0].imshow(test_img)
#axes[1].imshow(transfer(test_img, style='night'))

plt.figure(figsize=(16, 10))
plt.axis('off') # 막대그래프 제거
plt.imshow(test_img)
plt.savefig("origin.png")

plt.figure(figsize=(16, 10))
plt.axis('off')
plt.imshow(transfer(test_img, style='night'))
plt.savefig("result.png")


#axes[0].figure.savefig("test1.png")
#axes[1].figure.savefig("test2.png")

#axes[0].savefig("orig.png")
#axes[1].savefig("return.png")

#test_img.save('origin.png')
#resultimg = transfer(test_img, style='night')
#resultimg.savefig('result.png')





'''
test_img = Image.open('images/test/02.jpg')

fig, axes = plt.subplots(1, 2, figsize=(20, 10))
axes[0].imshow(test_img)
axes[1].imshow(transfer(test_img, style='day2'))

test_img = Image.open('images/test/02.jpg')

fig, axes = plt.subplots(1, 2, figsize=(20, 10))
axes[0].imshow(test_img)
axes[1].imshow(transfer(test_img, style='sunset_hard_harder'))

test_img = Image.open('images/test/03.jpg')

fig, axes = plt.subplots(1, 2, figsize=(20, 10))
axes[0].imshow(test_img)
axes[1].imshow(transfer(test_img, style='sunset_hard_harder'))

test_img = Image.open('images/test/03.jpg')

fig, axes = plt.subplots(1, 2, figsize=(20, 10))
axes[0].imshow(test_img)
axes[1].imshow(transfer(test_img, style='semihard_day'))

test_img = Image.open('images/test/04.jpg')

fig, axes = plt.subplots(1, 2, figsize=(20, 10))
axes[0].imshow(test_img)
axes[1].imshow(transfer(test_img, style='darknight'))

'''