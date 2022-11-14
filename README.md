# Segmentation of medical images (detection of cancer cells)
the work done in the image segmentation of a brain tumor Custom Dataset
contained 250 images of a mini-project from the lecture `advanced signal processing`.
This project concerns Brain tumor segmentation seeks to separate healthy tissue from tumorous
regions.
This is an essential step in diagnosis and treatment planning to maximize the likelihood of successful
treatment. Magnetic resonance imaging (MRI) provides detailed information about brain tumor anatomy,
making it an important tool for effective diagnosis which is requisite to replace the existing manual
detection system where patients rely on the skills and expertise of a human.


## algorithme of Local segmentation approach
<p >
<img src="https://github.com/misarb/BrainCancer/blob/main/img/8.png" style=" width:600px ; height:400px "  >
</p>

Here is an illustration showing this principle of growing regions:
<p >
<img src="https://github.com/misarb/BrainCancer/blob/main/img/9.png" style=" width:900px ; height:400px "  >
</p>
There are two types of region growing methods, namely:

1-The primer method.

2-The linear method.

## src code of this approche in matlab

```bash
  git clone https://github.com/misarb/BrainCancer/tree/main/matlapDetectionTumor
```

## Result
<p >
<img src="https://github.com/misarb/BrainCancer/blob/main/img/2.PNG" style=" width:600px ; height:400px "  >
<img src="https://github.com/misarb/BrainCancer/blob/main/img/3.PNG" style=" width:600px ; height:400px "  >
<img src="https://github.com/misarb/BrainCancer/blob/main/img/4.PNG" style=" width:600px ; height:400px "  >
</p>





## MASK RCNN algorithme
The architecture of the Convolutional Neural Network has a convolutional part upstream and therefore has two very distinct parts:

```bash
 ` A convolutional part `: Its final objective is to extract characteristics specific to each
image by compressing them to reduce their initial size. In summary, the image provided in
input passes through a succession of filters, creating at the same time new images
called convolution maps. Finally, the resulting convolution maps are concatenated
in a feature vector called CNN code.
` A classification part `: The CNN code obtained at the output of the convolutional part is provided in
entering a second part, consisting of fully connected layers called
multilayer perceptron (MLP for Multi Layers Perceptron). The role of this part is to
combine the characteristics of the CNN code in order to classify the image.
```
<p >
<img src="https://github.com/misarb/BrainCancer/blob/main/img/10.png" style=" width:600px ; height:400px "  >
</p>

##

## src code of MASK-RCNN

```bash
  
  git clone  https://github.com/misarb/BrainCancer/tree/main/pythonModulle
  `data to train the module :` 
  git clone https://github.com/misarb/BrainCancer/tree/main/BrainTumor_Data
```
## Result of MASK-RCNN

<p >
<img src="https://github.com/misarb/BrainCancer/blob/main/img/5.PNG" style=" width:600px ; height:500px "  >
<img src="https://github.com/misarb/BrainCancer/blob/main/img/6.PNG" style=" width:600px ; height:600px "  >
</p>

## Contributing

Contributions are always welcome!

<p >
<img src="https://github.com/misarb/BrainCancer/blob/main/img/1.PNG" style=" width:600px ; height:600px "  >
<img src="https://github.com/misarb/BrainCancer/blob/main/img/7.PNG" style=" width:600px ; height:600px "  >
</p>



## Clone this project

```
  git clone git@github.com:misarb/BrainCancer.git
```

CD into the project

```bash
  cd BrainCancer
```

## Authors

- [@misarb](https://github.com/misarb)

