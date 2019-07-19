#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

python $DIR/demo.py \
	--network "vgg16_reduced" \
	--images  $DIR/test/images \
	--epoch 0 \
	--data-shape 512 \
	--class-names "faces" \
	--gpu 0 \
	--deploy \
	--prefix ./model/deploy_ssd_ \
    --dir $DIR/test/images \
    --output $DIR/test/output \
    --ext .jpg

