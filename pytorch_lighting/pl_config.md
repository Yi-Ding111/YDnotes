```json
config = {“max_epochs”:30,
          “val_check_interval”:0.2, # how many times we want to validate during an epoch
          “check_val_every_n_epoch”:1,
          “gradient_clip_val”:1.0,
          “num_training_samples_per_epoch”: 800,
          “lr”:3e-5,
          “train_batch_sizes”: [8],
          “val_batch_sizes”: [1],
          # “seed”:2022,
          “num_nodes”: 1,
          “warmup_steps”: 300, # 800/8*30/10, 10%
          “result_path”: “./result”,
          “verbose”: True,
          }
```

这个config字典定义了训练一个PyTorch Lightning模型所需要的各种超参数和设置。其中,result_path指定了模型结果(检查点、日志等)的保存路径。在本例中,结果将保存到当前目录下的./result文件夹中。PyTorch Lightning会在此文件夹下自动创建以下结构:

```
result/
├── checkpoints/    # 检查点文件夹
│   ├── epoch=29-step=719.ckpt
│   └── ...
├── ...
├── version_0/     # 第0次运行的结果
│   ├── events.out.tfevents...      # tensorboard事件日志
│   ├── hparams.yaml                # 训练超参数 
│   ├── ...
└── version_1/     # 第1次运行的结果
```

所以,该配置指定了:

\- result_path: ./result
\- checkpoints: ./result/checkpoints/  # 检查点
\- events.out.tfevents...: ./result/version_0/events.out.tfevents... # tensorboard日志
\- hparams.yaml: ./result/version_0/hparams.yaml  # 训练超参数







.ckpt是什么文件?



.ckpt文件是PyTorch保存的模型检查点(checkpoint)文件。检查点文件通过在训练期间定期保存模型权重的快照,可以实现:1. 模型断点续训:如果训练意外中断,可以从最后一个检查点恢复训练。2. 选择最优模型:训练结束后,可以从val_loss最低的检查点加载模型权重。3. 调优模型超参数:可以从某个检查点恢复训练,调整学习率、批次大小等超参数。PyTorch Lightning会自动保存检查点文件,其路径由Trainer的dirpath参数指定。

检查点文件名的格式为:

```
epoch{epoch}_step{train_step}.ckpt
```

其中,{epoch}和{train_step}会被实际的epoch数和train_step数替换。

```
epoch=29-step=719.ckpt
```

表示第29轮第719步的检查点。

