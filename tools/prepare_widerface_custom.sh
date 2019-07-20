#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python $DIR/prepare_dataset.py \
    --dataset widerface \
    --annotations wider_face_train_bbx_gt.txt \
    --set trainval \
    --target $DIR/../data/widerface_rec/train.lst  \
    --root $DIR/../data/widerface

python $DIR/prepare_dataset.py \
    --dataset widerface \
    --annotations wider_face_train_bbx_gt.txt \
    --set test \
    --target $DIR/../data/widerface_rec/val.lst \
    --shuffle False \
    --root $DIR/../data/widerface
