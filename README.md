<a target="_blank" href="https://colab.research.google.com/github/devkhullar/LetsFindStars/blob/main/FindStars.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

# Data Visualization with DS9 + Find Stars with Photutils

This workshop is divided into two parts:
1. In part 1, we will be learning how to use DS9, a widely used imaging tool for astronomers to visualize all kinds of astronomical data, from pesky FITS files that have your science data to region files for your supplementary science. We will learn to make an RGB image of a galaxy on DS9, use some of the tools available in DS9 (creating regions, tiled images with locked coordinates, scaling parameters, etc). 
2. The second part of the workshop will cover contents on using the `DAOStarFinder` algorithm for point source detection (which could be black holes, neutron stars, Active Galactic Nuclei, Nebulae, you name it!) and then performing aperture photometry on those point sources. 

## DS9
You can install DS9 from this [link](https://sites.google.com/cfa.harvard.edu/saoimageds9).

### for Mac users
If you are using a mac, please download the Aqua version of DS9.

**Note**: You may stumble upon an error something along the lines of 'damaged application'. To counter that, please run the following code in a terminal:

<code>xattr -c /Applications/SAOImageDS9.app </code>

### for Windows users
If you are using a Windows machine, please click the `Windows 64 bit` tab and DS9 should star downloading. Further, you will need to unpack it in your computer, where if you select the DS9 in the folder where you downloaded it, it will ask you to select a directory to store the contents of DS9 and then `unzip` it. 

## Photutils

The easiest way to access this code is through google colab. There is a link for google colab provided at the top of the README.md file that you can select to run code out of your computer.

Otherwise, you can also fork this repository by running the following code in your terminal:
```
git clone https://github.com/devkhullar/LetsFindStars.git 
cd LetsFindStars
```

## Data Access
For the purpose this presentation, we are going to look at the data of M66 (NGC 3627), an intermediate star forming galaxy about 10.1 Mpc away from us. You can download the JWST science images from the PHANGS collaboration data access [page](https://archive.stsci.edu/hlsp/phangs.html#hst_image_products_table). Even though I am going to work with NGC 3627, you are free to download any images you want (I recommend downloading the JWST science images of IC 5332!).
