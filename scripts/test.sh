#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

python $DIR/demo.py \
	--network "vgg16_reduced" \
	--images "image (1),image (2),image (3),image (4),image (5),image (6),image (7)" \
	--epoch 0 \
	--data-shape 512 \
	--class-names "faces" \
	--gpu 0 \
	--deploy \
	--prefix ./model/deploy_ssd_ \
    --dir test/images \
    --ext .jpg

