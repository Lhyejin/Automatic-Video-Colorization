import numpy
import math
import cv2
import pandas as pd
import glob
import argparse
def psnr (original, colorized) :
    mse = numpy.mean((original-colorized)**2)
    if mse == 0 :
        return 100
    else :
        return 20*math.log10(255.0/math.sqrt(mse))

#원본 이미지(ground truth)들이 모여있는 폴더 path 지정(해당 path에는 이미지만 있어야함)
# 끝에 /* 꼭 붙이기


parser = argparse.ArgumentParser()
parser.add_argument("--original", default='./data/test/', type=str)
parser.add_argument("--color", default='./model/0100/001/prediction0', type=str, help="Test dir path")
parser.add_argument("--output", default='result', type=str)
args = parser.parse_args()
print(args)
original_path = args.original

#모듈을 통과한 이미지들이 모여있는 폴더 path 지정(해당 path에는 이미지만 있어야함)
# 끝에 /* 꼭 붙이기
colorized_path = args.color

#original 이미지가 모여 있는 폴더에서 사진들 이름 다 불러오기
original_list = glob.glob(original_path)
#colorized 이미지가 모여 있는 폴더에서 사진들 이름 다 불러오기
colorized_list = glob.glob(colorized_path)

#psnr 결과 저장 리스트
psnr_list = []

#psnr 계산
index = 0
while index < len(original_list) :
    original_img = cv2.imread(original_list[index])
    colorized_img = cv2.imread(colorized_list[index])
    original_img = cv2.resize(original_img, dsize=(colorized_img.shape[1], colorized_img.shape[0]))
    psnr_list.append(psnr(original_img, colorized_img))
    index += 1

#DataFrame 생성
data = {'original' : original_list,
        'colorized' : colorized_list,
        'psnr' : psnr_list
       }
df = pd.DataFrame(data)

#csv에 저장
df.to_csv("%s.csv"%(args.output), mode='w')
