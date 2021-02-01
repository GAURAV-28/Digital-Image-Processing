# name: File path of the pgm image file
# Output is a 2D list of integers
import math
def readpgm(name):
	image = []
	with open(name) as f:
		lines = list(f.readlines())
		if len(lines) < 3:
			print("Wrong Image Format\n")
			exit(0)

		count = 0
		width = 0
		height = 0
		for line in lines:
			if line[0] == '#':
				continue

			if count == 0:
				if line.strip() != 'P2':
					print("Wrong Image Type\n")
					exit(0)
				count += 1
				continue

			if count == 1:
				dimensions = line.strip().split(' ')
				print(dimensions)
				width = dimensions[0]
				height = dimensions[1]
				count += 1
				continue

			if count == 2:	
				allowable_max = int(line.strip())
				if allowable_max != 255:
					print("Wrong max allowable value in the image\n")
					exit(0)
				count += 1
				continue

			data = line.strip().split()
			data = [int(d) for d in data]
			image.append(data)
	return image	

# img is the 2D list of integers
# file is the output file path
def writepgm(img, file):
	with open(file, 'w') as fout:
		if len(img) == 0:
			pgmHeader = 'p2\n0 0\n255\n'
		else:
			pgmHeader = 'P2\n' + str(len(img[0])) + ' ' + str(len(img)) + '\n255\n'
			fout.write(pgmHeader)
			line = ''
			for i in img:
				for j in i:
					line += str(j) + ' '
				line += '\n'
			fout.write(line)
image = readpgm('test.pgm')
W=len(image[0])
H=len(image)		
l=[[0 for x in range(W)]for y in range(H)]
for p in range(W):
	l[0][p]=image[0][p]
for q in range(H):
	l[q][0]=image[q][0]	

for i in range(1,H-1):
	for j in range(1,W-1):
		l[i][j]=(image[i-1][j-1]+image[i-1][j]+image[i-1][j+1]+image[i][j-
1]+image[i][j]+image[i][j+1]+image[i+1][j-1]+ image[i+1][j]+image[i+1][j+1])//9
#print(image)		
print(l)
writepgm(l, 'average.pgm')

hdif=[[0 for x in range(W)]for y in range(H)]
for j in range(1,W-1):
	hdif[0][j] = (image[H-1][j-1]-image[H-1][j+1]) + 2*(image[0][j-1]-image[0][j+1]) + (image[1][j-1]-image[1][j+1])
	hdif[H-1][j] = (image[H-2][j-1]-image[H-2][j+1]) + 2*(image[H-1][j-1]-image[H-1][j+1]) + (image[0][j-1]-image[0][j+1])
for i in range(1,H-1):
	hdif[i][0] = (image[i-1][W-1]-image[i-1][1]) + 2*(image[i][W-1]-image[i][1]) + (image[i+1][W-1]-image[i+1][1])
	hdif[i][W-1] = (image[i-1][W-2]-image[i-1][0]) + 2*(image[i][W-2]-image[i][0]) + (image[i+1][W-2]-image[i+1][0])


hdif[0][0] = (image[H-1][W-1]-image[H-1][1]) + 2*(image[0][W-1]-image[0][1]) + (image[1][W-1]-image[1][1])
hdif[0][W-1] = (image[H-1][W-2]-image[H-1][0]) + 2*(image[0][W-2]-image[0][0]) + (image[1][W-2]-image[1][0])
hdif[H-1][0] = (image[H-2][W-1]-image[H-2][1]) + 2*(image[H-1][W-1]-image[H-1][1]) + (image[0][W-1]-image[0][1])
hdif[H-1][W-1] = (image[H-2][W-2]-image[H-2][0]) + 2*(image[H-1][W-2]-image[H-1][0]) + (image[0][W-2]-image[0][0])

vdif=[[0 for x in range(W)]for y in range(H)]

for j in range(1,W-1):
	vdif[0][j] = (image[H-1][j-1]-image[1][j-1]) + 2*(image[H-1][j]-image[1][j]) + (image[H-1][j+1]-image[1][j+1])
	vdif[H-1][j] = (image[H-2][j-1]-image[0][j-1]) + 2*(image[H-2][j]-image[0][j]) + (image[H-2][j+1]-image[0][j+1])
for i in range(1,H-1):
	vdif[i][0] = (image[i-1][W-1]-image[i+1][W-1]) + 2*(image[i-1][0]-image[i+1][0]) + (image[i-1][1]-image[i+1][1])
	vdif[i][W-1] = (image[i-1][W-2]-image[i+1][W-2]) + 2*(image[i-1][W-1]-image[i+1][W-1]) + (image[i-1][0]-image[i+1][0])

vdif[0][0] = (image[H-1][W-1]-image[1][W-1]) + 2*(image[H-1][0]-image[1][0]) + (image[H-1][1]-image[1][1])
vdif[0][W-1] = (image[H-1][W-2]-image[1][W-2]) + 2*(image[H-1][W-1]-image[1][W-1]) + (image[H-1][0]-image[1][0])
vdif[H-1][0] = (image[H-2][W-1]-image[0][W-1]) + 2*(image[H-2][0]-image[0][0]) + (image[H-2][1]-image[0][1])
vdif[H-1][W-1] = (image[H-2][W-2]-image[0][W-2]) + 2*(image[H-2][W-1]-image[0][W-1]) + (image[H-2][0]-image[0][0])	


for i in range(1,H-1):
	for j in range(1,W-1):
		hdif[i][j] = (image[i-1][j-1]-image[i-1][j+1]) + 2*(image[i][j-1]-image[i][j+1]) + (image[i+1][j-1]-image[i+1][j+1])
		vdif[i][j] = (image[i-1][j-1]-image[i+1][j-1]) + 2*(image[i-1][j]-image[i+1][j]) + (image[i-1][j+1]-image[i+1][j+1])




grad=[[0 for x in range(W)]for y in range(H)]
grad1=[[0 for x in range(W)]for y in range(H)]
for i in range(0,H):
	for j in range(0,W):
		grad[i][j]=int((hdif[i][j]**2+vdif[i][j]**2)**(0.5))
def findmax(grad,H,W):
	l=[]
	for i in range(0,H):
		l.append(max(grad[i]))
	return max(l)
M=findmax(grad,H,W)		
for i in range(0,H):
	for j in range(0,W):
		grad1[i][j]=(grad[i][j]*255)//M
#print(image)
#print(grad1)

writepgm(grad1, 'edge.pgm')



def minEnergy(i,j,MinEnergy):
	#print(i,j)
	if i==0:
		MinEnergy[i][j]=grad1[i][j]
	elif j==0:
		#print(min(MinEnergy[i-1][j],MinEnergy[i-1][j+1]),2)
		#print(grad1[i][j],1)
		MinEnergy[i][j]=grad1[i][j]+min(MinEnergy[i-1][j],MinEnergy[i-1][j+1])

	elif j==W-1:
		
		MinEnergy[i][j]=grad1[i][j]+min(MinEnergy[i-1][j-1],MinEnergy[i-1][j])	 	
	else:

		MinEnergy[i][j]=grad1[i][j]+min(MinEnergy[i-1][j-1],MinEnergy[i-1][j],MinEnergy[i-1][j+1])	
	return MinEnergy[i][j]

ener=[[0 for x in range(W)]for y in range(H)]
for i in range(0,H):
	for j in range(0,W):
		ener[i][j]=minEnergy(i,j,ener)


def dowhite(i,j,save,ener):
	image[i][j]=255
	
	save.append((i,j))
	if i>0:
		if j-1<0:
			if ener[i-1][j]<ener[i-1][j+1]:
				if (i-1,j) not in save:
					dowhite(i-1,j,save,ener)
			elif ener[i-1][j]==ener[i-1][j+1]:
				if (i-1,j) not in save:
					dowhite(i-1,j,save,ener)
				if (i-1,j+1) not in save:
					dowhite(i-1,j+1,save,ener)
			else:
				if (i-1,j+1) not in save:
					dowhite(i-1,j+1,save,ener)
		elif j+1==W:
			if ener[i-1][j]<ener[i-1][j-1]:
				if (i-1,j) not in save:
					dowhite(i-1,j,save,ener)
			elif ener[i-1][j]==ener[i-1][j-1]:
				if (i-1,j) not in save:
					dowhite(i-1,j,save,ener)
				if (i-1,j-1) not in save:
					dowhite(i-1,j-1,save,ener)
			else:
				if (i-1,j-1) not in save:
					dowhite(i-1,j-1,save,ener)
		else:
			if ener[i-1][j-1]==min(ener[i-1][j-1],ener[i-1][j],ener[i-1][j+1]) and ener[i-1][j]==ener[i-1][j-1]==ener[i-1][j+1]:
				if (i-1,j) not in save:

					dowhite(i-1,j,save,ener)
				if (i-1,j+1) not in save:

					dowhite(i-1,j+1,save,ener)
				if (i-1,j-1) not in save:
					dowhite(i-1,j-1,save,ener)
			elif ener[i-1][j-1]==min(ener[i-1][j-1],ener[i-1][j],ener[i-1][j+1]) and ener[i-1][j-1]==ener[i-1][j]:
				if (i-1,j) not in save:
					dowhite(i-1,j,save,ener)
				if (i-1,j-1) not in save:
					dowhite(i-1,j-1,save,ener)
			elif ener[i-1][j+1]==min(ener[i-1][j-1],ener[i-1][j],ener[i-1][j+1]) and ener[i-1][j-1]==ener[i-1][j+1]:
				if (i-1,j+1) not in save:
					dowhite(i-1,j+1,save,ener)
				if (i-1,j-1) not in save:
					dowhite(i-1,j-1,save,ener)
			elif ener[i-1][j]==min(ener[i-1][j-1],ener[i-1][j],ener[i-1][j+1])and ener[i-1][j+1]==ener[i-1][j]:
				if (i-1,j) not in save:
					dowhite(i-1,j,save,ener)
				if (i-1,j+1) not in save:
					dowhite(i-1,j+1,save,ener)
			elif ener[i-1][j+1]==min(ener[i-1][j-1],ener[i-1][j],ener[i-1][j+1]):
				if (i-1,j+1) not in save:
					dowhite(i-1,j+1,save,ener)
			elif ener[i-1][j]==min(ener[i-1][j-1],ener[i-1][j],ener[i-1][j+1]):
				if (i-1,j) not in save:
					dowhite(i-1,j,save,ener)
			elif ener[i-1][j-1]==min(ener[i-1][j-1],ener[i-1][j],ener[i-1][j+1]):
				if (i-1,j-1) not in save:
					dowhite(i-1,j-1,save,ener)

m=min(ener[H-1])
save=[]
for j in range(W):
	if ener[H-1][j]==m:
		dowhite(H-1,j,save,ener)							

print(image)
writepgm(image, 'fimage.pgm')

	






		
