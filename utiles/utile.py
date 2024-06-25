import numpy as np
from PIL import Image
import torch
import matplotlib.pyplot as plt
import torch
from torchvision import datasets, transforms

def table(a):
  return np.array(a)

def repete(a,n):
  l = [a for i in range(n)]
  if len(a.shape) == 1:
    return np.stack(l)
  else:
    return np.concatenate(l, axis=len(a.shape) - 2)

def empile(L):
  return np.stack(L)


def transpose(a):
  return a.transpose()


def suite_arithmetique(n):
  return np.arange(0,n + 1)




def preleve_image_MNIST(n):
  transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
  jeu_de_donnees = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
  return np.array(jeu_de_donnees[n][0]).squeeze(), jeu_de_donnees[n][1]


def ouvrir(chemin_image):
    image = np.array(Image.open(chemin_image))
    print(image.shape)
    return np.transpose(image, axes=(2,1,0))


def afficher(image, width_cm=15):
  try:
    image2 = np.transpose(image, axes=(1,2,0))
    image2 = Image.fromarray(image2)
    dpi = 96  # Default DPI for matplotlib
    width_inches = width_cm / 2.54
    height_inches = (image2.height / image2.width) * width_inches
    fig, ax = plt.subplots(figsize=(width_inches, height_inches), dpi=dpi)
    ax.imshow(image2)
    ax.axis('off')
    plt.show()
  except:
    plt.imshow(image, cmap='gray')

