import sys
import numpy as np
import cv2
from scipy import stats

def amostragem_reducao (img,percent,tech):

	width, height = img.shape

	n= 100/percent
	new_img=img[0:(width/n),0:(height/n)]

	l=0
	for row in range(0,width-1,n):
		c=0
		for column in range(0,height-1,n):
			if tech=='media':		
				new_value= np.mean (img[row:row+n,column:column+n])
			elif tech=='mediana':
				new_value= np.median (img[row:row+n,column:column+n])
			elif tech== 'moda':
				aux= stats.mode(img[row:row+n,column:column+n],axis=None)
				new_value=aux[0]
			else:
				print('tecnica invalida')

			new_img[l,c]=int(new_value)
			c=c+1	
		l=l+1	
	return new_img

def amostragem_aumento (img,percent,tech):

	print('ERRO! Digite um porcentual menor igual a 100%')

def quantizacao(new_img, qtd_ngray):

	step= 255/qtd_ngray 
	intervalo=range(0,256,step)

	width,height= new_img.shape
	img_quant=new_img
	for row in range(0,width):
		for column in range(0,height):
			for cont in range(1,len(intervalo)):
				if img_quant[row,column] <= intervalo[cont] :
					if cont==(len(intervalo)-1):
						img_quant[row,column]=intervalo[cont]
						break
					else:
						img_quant[row,column]=intervalo[cont-1]
						break

        return img_quant

name=str(sys.argv[1])
percent=int(sys.argv[2])
qtd_ngray=int(sys.argv[3])
tech=str(sys.argv[4])

img_original= cv2.imread('Imagens/'+name,0)
cv2.imshow('Imagem original',img_original)

#Amostragem
if percent <= 100:
	img_amostrada=amostragem_reducao(img_original,percent,tech)
	cv2.imshow('Imagem amostrada',img_amostrada)
else:
	img_amostrada=amostragem_aumento(img_original,percent,tech)

#Quantizacao
if percent <= 100:
	img_quantizada=quantizacao(img_amostrada, qtd_ngray)
	cv2.imshow('Imagem amostrada quantizada',img_quantizada)

cv2.waitKey(0)
cv2.destroyAllWindows()





