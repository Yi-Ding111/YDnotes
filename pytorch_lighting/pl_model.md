# Pytorch Lightning Model





## Model define

https://lightning.ai/docs/pytorch/stable/common/lightning_module.html



定义一个 LightningModule 模型, 主要有这些sections:



1. Initialization (`__init__` and `setup()`).
2. Train Loop (`training_step()`)
3. Validation Loop (`validation_step()`)
4. Test Loop (`test_step()`)
5. Prediction Loop (`predict_step()`)
6. Optimizers and LR Schedulers (`configure_optimizers()`)





### training_step()

训练步骤,计算loss并记录





### validation_step()

验证步骤,通过计算编辑距离来评估模型的性能 





### configure_optimizers()

定义优化器



