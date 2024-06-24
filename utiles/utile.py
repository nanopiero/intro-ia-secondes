import numpy as np
from PIL import Image
import torch
import matplotlib.pyplot as plt


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


import torch
from torchvision import datasets, transforms

def preleve_image_MNIST(n):
  transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
  dataset_Lecun = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
  return np.array(jeu_de_donnees[n][0]).squeeze(), jeu_de_donnees[n][1]


def afficher(image, width_cm=0):
  try:
    dpi = 96  # Default DPI for matplotlib
    width_inches = width_cm / 2.54
    height_inches = (image.height / image.width) * width_inches
    fig, ax = plt.subplots(figsize=(width_inches, height_inches), dpi=dpi)
    ax.imshow(image)
    ax.axis('off')
    plt.show()
  except:
    plt.imshow(image, cmap='gray')


def ouvrir(image):
    return np.array(Image.open(image))

