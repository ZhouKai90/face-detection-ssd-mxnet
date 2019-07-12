#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OPTIMIZER=rmsprop
TENSORBOARD=True
LR_STEPS=20,40,60
REC_DATA_PATH=$DIR/data/widerface_pascal_rec

python $DIR/train.py \
--num-class 1 \
--class-names "face" \
--train-path $REC_DATA_PATH/train.rec \
--train-list $REC_DATA_PATH/train.lst \
--val-path $REC_DATA_PATH/val.rec \
--val-list $REC_DATA_PATH/val.lst \
--prefix $DIR/output/widerface_pascal_300/ssd_vgg16 \
--pretrained $DIR/model/vgg16_reduced \
--epoch 1 \
--gpus 0,1 \
--data-shape 300 \
--label-width 390 \
--batch-size 64 \
--lr-steps ${LR_STEPS} \
--lr 0.001 \
--freeze ''
#--optimizer ${OPTIMIZER}
#--tensorboard True \
