#!/usr/bin/env bash

# this is a training script
# defining global parameters
GPUS='0,1'
TRAIN_REC_PATH=./data/pascal/train.rec
VAL_REC_PATH=./data/pascal/val.rec
NETWORK=vgg16_reduced
BATCH_SIZE=128
DATA_SHAPE=300
PRETRAINED=./model/vgg16_reduced
OPTIMIZER=rmsprop
TENSORBOARD=False
LR_STEPS=20,40,60

python ./train.py \
    --train-path ${TRAIN_REC_PATH} \
    --val-path ${VAL_REC_PATH} \
    --network ${NETWORK} \
    --batch-size ${BATCH_SIZE} \
    --data-shape ${DATA_SHAPE} \
    --gpus ${GPUS} \
    --pretrained ${PRETRAINED} \
    --optimizer ${OPTIMIZER} \
#    --tensorboard ${TENSORBOARD} \
    --lr-steps ${LR_STEPS} \
    --freeze '' \
    --lr 0.04 \
    --voc07 Ture