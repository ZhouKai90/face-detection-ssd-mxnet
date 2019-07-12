#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REC_DATA_PATH=$DIR/../data/widerface_pascal_rec

python $DIR/prepare_dataset.py \
    --dataset pascal \
    --year 2019 \
    --set train \
    --target $REC_DATA_PATH/train.lst \
    --root $DIR/../data/widerface \
    --class-names "face" \
    --true-negative False


python $DIR/prepare_dataset.py \
    --dataset pascal \
    --year 2019 \
    --set val \
    --target $REC_DATA_PATH/val.lst \
    --root $DIR/../data/widerface \
    --class-names "face" \
    --true-negative False