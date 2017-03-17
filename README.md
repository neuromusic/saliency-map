saliency-map (Python)
============
Saliency Map. Laurent Itti, Christof Koch (2000)

## Install

Clone the repository, then

``` bash
python setup.py install
```

or

``` bash
pip install ./
```

## How to Use

``` Python
from saliency_map import SaliencyMap
from saliency_map.utils import OpencvIo

oi = OpencvIo()
src = oi.imread(IMAGE_PATH)
sm = SaliencyMap(src)
oi.imshow_array([sm.map])
```

## Example

### Visual Search Task
![Bar](./images/bar.png "Bar")
![Saliency map Bar](./images/s_bar.png "Saliency map Bar")

### Wall
![Wall](./images/wall.png "Wall")
![Saliency map Wall](./images/s_wall.png "Saliency map Wall")
