# DragView

`DragView` aims to help with the visualisation of DRAGON/DONJON output using the ParaView software. While it currently only works for the SN type calculation for 2D and 3D Cartesian or hexagonal geometries, it is hoped that this is flexible enough that other types of geometries and calculations can be added. 

## Examples 

Below are examples of the sort of visualisation possible with ParaView. 

[<img src="images/2DAIC2.svg?raw=true&sanitize=true" width="300" alt="Gallery" />](usage-view/2DCAR) [<img src="images/3DTAK2.svg?raw=true&sanitize=true" width="300" alt="Gallery" />](usage-view/3DCAR) 
[<img src="images/2DSNA.svg?raw=true&sanitize=true" width="300" alt="Gallery" />](usage-view/2DHEX)  [<img src="images/3DT4AX.svg?raw=true&sanitize=true" width="300" alt="Gallery" />](usage-view/2DHEX)  

_From left to right, top to bottom: AIC benchmark (2D Cartesian model), Takeda Model 2 (3D Cartesian model), simple 2D hexagonal model, Takeda Model 4 (3D hexagonal model)_

## Installation

There are two libraries needed apart from the default python ones: `vtk` and `pygan`. Once these are installed, you need to ensure that the paths to these installations are added to your `PYTHONPATH` environment variable.
  - `vtk` can be easily installed using `pip` ([link](https://pypi.org/project/vtk/)) in your conda environment or otherwise. If using `pip`, there is generally no need to update the `PYTHONPATH` for `vtk`.
    - _For Polytechnique Montreal users_, this is already installed on the **Bateman** and **Planck** servers. The installation is path `/usr/localp/vtk/build`.
  - `pygan` is available with the latest DRAGON5 distribution [(link](http://merlin.polymtl.ca)). Make sure to run the following command in the `Pygan` directory:
```sh
make hdf5=1 pip=1
```
`pip=1` will ensure that the required libraries will be installed using `pip` and will not require using the `PYTHONPATH`.

If needed, to your `.bashrc` or `.zshrc` or `.profile`, add:
```sh
export PYTHONPATH=$PYTHONPATH:/usr/localp/vtk/build
```

Finally, clone this repository somewhere and check your environment variables are correctly set:
```sh
echo $PYTHONPATH
```


## Basic Usage

To create the vtu files for visualisation in Paraview, you need the LCM objects created by DRAGON5. There are two ways of using `DragView`:
  1. `view`: the LCM object files are already available, and just need to process them.
  2. `dragon_view`: only the `.c2m` procedure file is available and DRAGON5 needs to execute this to produce the LCM object files, which are then processed.

You can run the following to see the available options
```sh
python /path_to_cloned_repo/rDragView.py --help
```

The material index can be visualised as well as the flux. If there is more than one energy group, the flux for each energy group is saved to a different file. 

### 1A. `view`

This assumes that the geometry, macrolib, tracking and flux LCM objects are available in the current working directory and named as `_GEOM`, `_MACR`, `_TRCK` and `_FLUX` respectively. You can then run
```sh
python /path_to_cloned_repo/rDragView.py -c 'view' -n 'testrun'
```
where 
- `c` specifies the calculation type.
- `n` specifies the test run name, _optional_ in this case.

The vtu files are then generated in the working directory. Examples can be found in the [Usage-view](usage-view) gallery.

### 1B. `dragon_view`

The `.c2m` procedure is assumed to be in the current working directory. Care should be taken that the `PARAMETER`s and `LINKED_LIST`s are properly defined. The command for execution is then 
```sh
python /path_to_cloned_repo/rDragView.py -c 'dragon_view' -n 'name_of_c2m_procedure'
```
where 
- `c` specifies the calculation type.
- `n` specifies the name of the `.c2m` procedure _*without*_ the extension, _*REQUIRED*_ in this case.

The vtu files are then generated in the working directory. Examples can be found in the [Usage-dragon_view](usage-dragon_view) gallery.

### 2. Visualisation with ParaView

ParaView can be downloaded at the following [link](https://www.paraview.org/download/). Once installed, click on 
```
File -> Open
```
and navigate to the folder containing the vtu files. Select the desired file and _*click on 'Apply'*_ (usually found in the left panel in the 'Properties' tab). 

There are countless visualisation (e.g. clip, slice, extract) and data manipulation options available natively in ParaView, and the [wiki](https://www.paraview.org/Wiki/ParaView) is a good place to start. 

## Contributing

If you make improvements to this code or have suggestions, please do not hesitate to fork the repository or submit bug reports on github. The repository's URL is:
```
https://github.com/atyab191/DragView
```

## License 

Copyright (C) 2025 Polytechnique Montreal

This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

## Acknowledgement

This work was completed during a PhD and postdoc fellowship funded by NSERC. 
