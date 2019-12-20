import os, sys
import tensorflow as tf
import numpy as np


def create_save_model(model_dir):
    # tflite変換
    save_model_dir = os.path.join(model_dir, "SavedModel")
    converter = tf.lite.TFLiteConverter.from_saved_model(
        save_model_dir
        )
    # converter.allow_custom_ops=True
    # converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
    tflite_model = converter.convert()
    with open(model_dir + "/tf2_mobile_unet.tflite", 'wb') as f:
        f.write(tflite_model)
    print("finish save tflite_model")

    tf_converter.convert(tf_model_path=os.path.join(model_dir, "original_98_frozen.pb"),
                        mlmodel_path=os.path.join(model_dir, 'pfld.mlmodel'),
                        input_name_shape_dict={'image_batch:0':[1,args.image_size,args.image_size,3]},
                        output_feature_names=['pfld_inference/fc/BiasAdd:0']
                        )
    print("finish save savedmodel")


if __name__ == '__main__':
    create_save_model("")
