#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#python $DIR/prepare_dataset.py --dataset coco --set train2014,valminusminival2014 --target $DIR/../data/train.lst  --root $DIR/../data/coco
python $DIR/prepare_dataset.py --dataset coco --set train2017 --target $DIR/../data/coco_rec/train.lst  --root $DIR/../data/coco
python $DIR/prepare_dataset.py --dataset coco --set val2017 --target $DIR/../data/coco_rec/val.lst --shuffle False --root $DIR/../data/coco
